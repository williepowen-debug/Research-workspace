"""Fixture-only exclusive locking for the local acceptance critical section."""

from __future__ import annotations

import fcntl
import os
import stat
from pathlib import Path
from types import TracebackType

from live_grant import LiveShadowGrant, require_live_grant


LIVE_KERNEL_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LIVE_KERNEL_ROOT.parent


class FixtureAcceptanceLock:
    """Exclusive advisory lock beneath an injected, non-repository workspace.

    The lock serializes local custody mechanics only. Acquiring it does not grant
    an actor capability, validate a command, or authorize a result disposition.
    Without a minted live grant the lock refuses every repository-related root;
    with one it requires exactly the granted repository root and nothing else.
    """

    def __init__(
        self,
        workspace_root: str | Path,
        *,
        forbidden_repository_root: str | Path | None = None,
        live_grant: LiveShadowGrant | None = None,
    ):
        self.workspace_root = Path(workspace_root).resolve()
        if live_grant is not None:
            if forbidden_repository_root is not None:
                raise ValueError("live_grant and forbidden_repository_root are mutually exclusive")
            self.live_grant: LiveShadowGrant | None = require_live_grant(live_grant)
            self.forbidden_repository_root: Path | None = None
            if self.workspace_root != self.live_grant.repository_root:
                raise ValueError("live acceptance lock must target exactly the granted repository root")
        else:
            self.live_grant = None
            repository_root = Path(forbidden_repository_root or REPOSITORY_ROOT).resolve()
            self.forbidden_repository_root = repository_root
            if (
                self.workspace_root == repository_root
                or repository_root in self.workspace_root.parents
                or self.workspace_root in repository_root.parents
            ):
                raise ValueError("fixture acceptance lock cannot target the live repository tree")
        self.path = self.workspace_root / ".rw" / "locks" / "command.lock"
        self._descriptor: int | None = None

    @property
    def held(self) -> bool:
        return self._descriptor is not None

    def __enter__(self) -> "FixtureAcceptanceLock":
        if self.held:
            raise RuntimeError("fixture acceptance lock instance is already held")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        resolved_lock_directory = self.path.parent.resolve()
        if self.live_grant is not None:
            expected = (self.live_grant.repository_root / ".rw" / "locks").resolve()
            if resolved_lock_directory != expected:
                raise ValueError("live acceptance lock directory must resolve exactly inside the granted root")
        else:
            repository_root = self.forbidden_repository_root
            assert repository_root is not None
            if resolved_lock_directory == repository_root or repository_root in resolved_lock_directory.parents:
                raise ValueError("fixture acceptance lock cannot resolve into the live repository tree")
        flags = os.O_CREAT | os.O_RDWR
        if hasattr(os, "O_CLOEXEC"):
            flags |= os.O_CLOEXEC
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(self.path, flags, 0o600)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise ValueError("fixture acceptance lock path must be a regular file")
            fcntl.flock(descriptor, fcntl.LOCK_EX)
        except BaseException:
            os.close(descriptor)
            raise
        self._descriptor = descriptor
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        descriptor = self._descriptor
        self._descriptor = None
        if descriptor is None:
            return
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)
