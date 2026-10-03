import os
import shutil

from .utils import constants as cs

BUILTINS = {cs.ECHO, cs.EXIT, cs.TYPE, cs.PWD, cs.CD}


def find_executable(command: str) -> str | None:
    """This function finds the executable on your machine based on the command .
    using python `shutil` lib to find the executable .
     Args:
         command : given input user command . ex: pwd , git , status .
     Returns: Executable or None .
    """
    # LEGACY
    # path = os.environ.get("PATH", "")
    # here we are using os.pathsep because in windows the directory separator is ; and in linux it is :
    # so irrespective of the operating system , we use the safe parse  .
    # for directory in path.split(os.pathsep):
    #     _file_path = os.path.join(directory, command)
    #     if os.path.isfile(_file_path) and os.access(_file_path, os.X_OK):
    #         return _file_path
    # commented above manual code because the limitation
    # where the shell is not recognizing the commands like git ,python , it needs exact names of executables , git.exe , python.exe etc
    # using shutil , its does the searching like shell does , if command founds it returns executable else it returns None
    return shutil.which(command)


def handle_echo(args):
    print(" ".join(args))


def handle_exit(args):
    return True


def handle_pwd(args):
    print(os.getcwd())


def handle_cd(args):
    try:
        os.chdir(args[0])
    except Exception as e:
        print(f"cd: {args[0]}: No such file or directory")


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
        cs.PWD: handle_pwd,
        cs.CD: handle_cd,
    }
    return registry.get(command)
