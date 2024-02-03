import subprocess as _subprocess
from pathlib import Path as _Path

from pyshellman.output import ShellOutput as _ShellOutput


def run(
    command: list[str],
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput:
    cmd_str = " ".join(command)
    try:
        process = _subprocess.run(command, text=text_output, cwd=cwd, capture_output=True)
    except FileNotFoundError:
        return _ShellOutput(cmd=cmd_str)
    out = process.stdout.strip() if text_output else process.stdout
    err = process.stderr.strip() if text_output else process.stderr
    code = process.returncode
    return _ShellOutput(cmd=cmd_str, out=out or None, err=err or None, code=code)
