#!/usr/bin/env python3
"""nisaba_pull.py — read NISABA's memory store and session transcripts from the Console API.

PROME-owned (2026-10-17). Reads only; never writes to the store or a session.
Output goes OUTSIDE the fleet repo by default (~/nisaba-pulls/<stamp>/) — NISABA's
memory is Will's personal material and the plan forbids it in fleet files.

Auth: ANTHROPIC_API_KEY from the environment, else from PROME/.env (gitignored by the
root `.env` rule) as a line `ANTHROPIC_API_KEY=sk-ant-...`. A user key also needs
ANTHROPIC_WORKSPACE_ID=wrkspc_... (same two places) — the workspace NISABA lives in.

Usage:
  python3 PROME/tools/nisaba_pull.py                      # memory + every session of the agent
  python3 PROME/tools/nisaba_pull.py --memory-only
  python3 PROME/tools/nisaba_pull.py --session sesn_...   # one transcript
  python3 PROME/tools/nisaba_pull.py --out DIR
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

AGENT_ID = "agent_01BWvWQjj2JLXAGfgyinE7uf"            # NISABA (plan header, 2026-10-17)
STORE_ID = "memstore_01N83EazosQ9GTmzaUwTQF88"         # Nisaba-memory
REPO = Path(__file__).resolve().parents[2]


def _env(name: str) -> str | None:
    val = os.environ.get(name)
    if val:
        return val
    env = REPO / "PROME" / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def load_key() -> str:
    key = _env("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("no ANTHROPIC_API_KEY in the environment or PROME/.env — "
                 "Console → Settings → API keys (the org holding the credits); "
                 "write it as ANTHROPIC_API_KEY=... into PROME/.env (gitignored).")
    return key


def make_client():
    """A user key (sk-ant-usr-) is not workspace-scoped: every Managed Agents call then
    needs the anthropic-workspace-id header (observed 400, 2026-10-17 21:0x ET)."""
    from anthropic import Anthropic
    headers = {}
    ws = _env("ANTHROPIC_WORKSPACE_ID")
    if ws:
        headers["anthropic-workspace-id"] = ws
    return Anthropic(api_key=load_key(), default_headers=headers)


def dump(obj):
    return obj.model_dump() if hasattr(obj, "model_dump") else obj


def text_of(content) -> str:
    """Flatten a content list (text blocks) to a string; keep non-text blocks as JSON."""
    if isinstance(content, str):
        return content
    out = []
    for b in content or []:
        b = dump(b)
        if isinstance(b, dict) and b.get("type") == "text":
            out.append(b.get("text", ""))
        else:
            out.append("```json\n" + json.dumps(b, indent=1, default=str)[:4000] + "\n```")
    return "\n".join(out)


def pull_memory(client, out: Path) -> int:
    mdir = out / "memory"
    mdir.mkdir(parents=True, exist_ok=True)
    index = []
    n = 0
    for m in client.beta.memory_stores.memories.list(STORE_ID, path_prefix="/", view="full"):
        d = dump(m)
        if d.get("type") != "memory":
            continue
        path = d["path"].lstrip("/")
        target = mdir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        content = d.get("content")
        if content is None:  # view=full not honoured — fetch one by one
            content = client.beta.memory_stores.memories.retrieve(d["id"], memory_store_id=STORE_ID).content
        target.write_text(content or "")
        index.append({"path": d["path"], "id": d.get("id"), "bytes": d.get("content_size_bytes"),
                      "sha256": d.get("content_sha256"), "updated_at": str(d.get("updated_at"))})
        n += 1
    (mdir / "_index.json").write_text(json.dumps(index, indent=1))
    return n


def render_session(client, sid: str, out: Path) -> Path:
    sdir = out / "sessions"
    sdir.mkdir(parents=True, exist_ok=True)
    sess = dump(client.beta.sessions.retrieve(session_id=sid))
    lines = [f"# Session {sid}", "",
             f"- status: {sess.get('status')} · created: {sess.get('created_at')} · "
             f"agent: {json.dumps(sess.get('agent'), default=str)}",
             f"- usage: {json.dumps(sess.get('usage'), default=str)}", ""]
    raw = []
    page = client.beta.sessions.events.list(session_id=sid)
    events = list(page) if hasattr(page, "__iter__") and not hasattr(page, "data") else list(page.data)
    # paginate if the SDK page exposes next pages
    while hasattr(page, "has_next_page") and page.has_next_page():
        page = page.get_next_page()
        events.extend(page.data)
    for ev in events:
        d = dump(ev)
        raw.append(d)
        t = d.get("type", "?")
        ts = d.get("processed_at") or d.get("created_at") or ""
        if t == "user.message":
            lines += [f"## WILL  `{ts}`", "", text_of(d.get("content")), ""]
        elif t == "agent.message":
            lines += [f"## NISABA  `{ts}`", "", text_of(d.get("content")), ""]
        elif t in ("agent.tool_use", "agent.mcp_tool_use", "agent.custom_tool_use"):
            name = d.get("name") or d.get("tool_name")
            inp = json.dumps(d.get("input"), default=str)
            lines += [f"- tool `{name}` `{ts}`: {inp[:600]}"]
        elif t in ("agent.tool_result", "agent.mcp_tool_result"):
            body = text_of(d.get("content"))
            lines += [f"  - result: {body[:600].replace(chr(10), ' ')}"]
        elif t == "session.status_idle":
            lines += [f"- _idle_ `{ts}` {json.dumps(d.get('stop_reason'), default=str)}"]
        elif t in ("session.status_terminated", "session.error", "agent.thread_context_compacted"):
            lines += [f"- _{t}_ `{ts}`"]
    md = sdir / f"{sid}.md"
    md.write_text("\n".join(lines))
    (sdir / f"{sid}.events.json").write_text(json.dumps(raw, indent=1, default=str))
    return md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--memory-only", action="store_true")
    ap.add_argument("--session", action="append", default=[])
    a = ap.parse_args()
    client = make_client()
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    out = Path(a.out) if a.out else Path.home() / "nisaba-pulls" / stamp
    out.mkdir(parents=True, exist_ok=True)
    n = pull_memory(client, out)
    print(f"memory: {n} file(s) → {out/'memory'}")
    if a.memory_only:
        return
    sids = a.session
    if not sids:
        for s in client.beta.sessions.list():
            d = dump(s)
            ag = d.get("agent") or {}
            ag_id = ag.get("id") if isinstance(ag, dict) else ag
            if ag_id == AGENT_ID:
                sids.append(d["id"])
        print(f"sessions on {AGENT_ID}: {len(sids)}")
    for sid in sids:
        print("transcript →", render_session(client, sid, out))


if __name__ == "__main__":
    main()
