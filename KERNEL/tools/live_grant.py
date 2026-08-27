"""Live-shadow capability grant minted only by a validated pilot activation.

A ``LiveShadowGrant`` is proof that one strict activation document — carrying
the operator's exact half-open UTC window, command identities and hashes, and
repository binding — validated completely at a captured instant. Handing the
grant to a result store or acceptance lock replaces their default
live-repository refusal with an exact equality requirement against the granted
roots. Every path without a grant keeps the existing fixture-only refusals.

Minting is restricted to ``live_shadow.authorize_live_activation``; the mint
key is module-private and importing it anywhere else is a boundary violation
under the approved cooperative-actor threat model (spec section 2.2 / design
decision 20). Direct construction fails closed.
"""

from __future__ import annotations

from pathlib import Path


_MINT_KEY = object()


class LiveShadowGrant:
    __slots__ = (
        "repository_root",
        "kernel_root",
        "views_root",
        "activation_id",
        "writer_id",
        "recorded_at",
        "window_enforced",
    )

    def __init__(
        self,
        key: object,
        *,
        repository_root: str | Path,
        activation_id: str,
        writer_id: str,
        recorded_at: str,
        window_enforced: bool = False,
    ):
        if key is not _MINT_KEY:
            raise ValueError("live shadow grants are minted only by a validated activation")
        self.repository_root = Path(repository_root).resolve()
        self.kernel_root = self.repository_root / "KERNEL"
        self.views_root = self.kernel_root / "views"
        self.activation_id = activation_id
        self.writer_id = writer_id
        self.recorded_at = recorded_at
        # Records whether the operator window was actually checked at mint time.
        # Defaults False (fail-closed): a grant that cannot prove window
        # enforcement is refused at every durable-write path (adversarial
        # review 2026-08-27, finding 1 — read-onlyness must not rest on the
        # call path alone).
        self.window_enforced = bool(window_enforced)


def require_live_grant(grant: object) -> LiveShadowGrant:
    if not isinstance(grant, LiveShadowGrant):
        raise ValueError("live_grant must be a minted LiveShadowGrant")
    return grant
