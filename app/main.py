import shlex
import subprocess
import sys

from .commands import find_executable, get_command_handler


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        try:
            parts = shlex.split(input())
        except EOFError:
            break
        if not parts:
            continue

        command = parts[0]
        args = parts[1:]
        handler = get_command_handler(command=command)
        if handler:
            is_exit = handler(args=args)
            if is_exit:
                break
        else:
            executable = find_executable(command=command)
            if executable:
                subprocess.run([command, *args], executable=executable)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
