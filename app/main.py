import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = {"echo", "exit", "type"}
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
        if command == "exit":
            break
        elif command == "echo":
            print(" ".join(parts[1:]))
        elif command == "type":
            if not args:
                print("type: missing operand")
            else:
                for name in args:
                    if name in builtins:
                        print(f"{name} is a shell builtin")
                    else:
                        print(f"{name}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
