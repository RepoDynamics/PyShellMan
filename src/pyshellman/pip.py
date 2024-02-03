from pathlib import Path as _Path

from pyshellman.output import ShellOutput as _ShellOutput
from pyshellman.python import module as _python_module


_list = list


def run(
    command: list[str],
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return _python_module(command=["pip", *command], cwd=cwd, text_output=text_output)


def list(
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return run(command=["list"], cwd=cwd, text_output=text_output)


def install(
    command: _list[str],
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return run(command=["install", *command], cwd=cwd, text_output=text_output)


def install_requirements(
    path: str | _Path,
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    return install(command=["-r", str(path)], cwd=cwd, text_output=text_output)


def install_package(
    name: str,
    requirement_specifier: str | None = None,
    upgrade: bool = False,
    install_dependencies: bool = True,
    index: str | None = None,
    cwd: str | _Path | None = None,
    text_output: bool = True,
) -> _ShellOutput | None:
    index_name_url = {
        "testpypi": "https://test.pypi.org/simple/",
    }
    command = []
    if upgrade:
        command.append("--upgrade")
    command.append(f"{name}{requirement_specifier or ''}")
    if not install_dependencies:
        command.append("--no-deps")
    if index:
        index_url = index_name_url.get(index) or index
        command.extend(["--index-url", index_url])
    return install(command=command, cwd=cwd, text_output=text_output)
