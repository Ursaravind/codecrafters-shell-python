import sys

from .commands import get_command_handler


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        try:
            parts = input().strip().split()
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
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
