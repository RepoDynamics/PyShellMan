from pathlib import Path as _Path

from pyshellman.output import ShellOutput as _ShellOutput
from pyshellman.shell import run as _run


def run(
    command: list[str],
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return _run(command=["python", *command], cwd=cwd, text_output=text_output)


def module(
    command: list[str],
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return run(command=["-m", *command], cwd=cwd, text_output=text_output)
