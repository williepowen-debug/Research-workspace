#!/usr/bin/env python3
"""Render console-panel-keeper.yaml (the Console "Agent config" paste) from agents/keeper/agent.md.

agent.md is the single source; run this after every edit to it. Verifies the round trip and exits 1 on mismatch.
"""
import pathlib, sys, yaml

HERE = pathlib.Path(__file__).resolve().parent
SRC, OUT = HERE / "agents/keeper/agent.md", HERE / "console-panel-keeper.yaml"

class Block(str):
    pass

yaml.add_representer(Block, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|"))

_, fm, body = SRC.read_text().split("---", 2)
cfg = yaml.safe_load(fm)
panel = {"name": cfg["name"], "description": cfg["description"], "model": cfg["model"],
         "system": Block(body.strip() + "\n"), "mcp_servers": [], "tools": cfg["tools"], "skills": []}
header = ("# GENERATED from agents/keeper/agent.md by render_console_panel.py: do not hand-edit.\n"
          "# Paste into the Console 'Agent config' panel. After a Console edit, 'Export as code' and fold it back into agent.md.\n")
OUT.write_text(header + yaml.dump(panel, sort_keys=False, allow_unicode=True, width=10000))

back = yaml.safe_load(OUT.read_text())
ok = back["system"].strip() == body.strip() and back["tools"] == cfg["tools"] and back["model"] == cfg["model"]
print(f"{'OK' if ok else 'MISMATCH'}: {OUT.name} rendered from {SRC.name} ({len(body.strip().splitlines())} prompt lines)")
sys.exit(0 if ok else 1)
