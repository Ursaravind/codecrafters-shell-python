import os

from .utils import constants as cs

BUILTINS = {cs.ECHO, cs.EXIT, cs.TYPE}


def find_executable(command: str) -> str | None:
    path = os.environ.get("PATH", "")
    # here we are using os.pathsep because in windows the directory separator is ; and in linux it is :
    # so irrespective of the operating system , we use the safe parse  .
    file_path = None
    for directory in path.split(os.pathsep):
        _file_path = os.path.join(directory, command)
        if os.path.isfile(_file_path) and os.access(_file_path, os.X_OK):
            file_path = _file_path
    return file_path


def handle_echo(args):
    print(" ".join(args))


def handle_exit(args):
    return True


def handle_type(args):
    if args:
        for name in args:
            if name in BUILTINS:
                print(f"{name} is a shell builtin")
                continue
            executable = find_executable(command=name)
            if executable:
                print(f"{name} is {executable}")
            else:
                print(f"{name}: not found")
    else:
        print("type: missing operand")


def get_command_handler(command: str):
    registry = {
        cs.ECHO: handle_echo,
        cs.TYPE: handle_type,
        cs.EXIT: handle_exit,
    }
    return registry.get(command)
