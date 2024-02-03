from typing import NamedTuple as _NamedTuple


class ShellOutput(_NamedTuple):
    cmd: str
    out: str | bytes | None = None
    err: str | bytes | None = None
    code: int | None = None

    @property
    def executed(self) -> bool:
        return self.code is not None

    @property
    def success(self) -> bool:
        return self.code == 0

    @property
    def details(self) -> tuple[str, ...]:
        details = (
            f"Command: {self.cmd}",
            f"Executed: {self.executed}",
            f"Exit Code: {self.code}",
            f"Output: {self.out or None}",
            f"Error: {self.err or None}",
        )
        return details

    @property
    def summary(self) -> str:
        if not self.executed:
            return f"Command could not be executed."
        if not self.success:
            return f"Command failed with exit code {self.code}."
        return f"Command executed successfully."
