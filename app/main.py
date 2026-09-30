import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        usr_input = input().strip().lower()
        parts = usr_input.split()
        if usr_input == "exit":
            break
        command = parts[0]
        args = parts[1]
        if parts:
            if command == "echo":
                print(" ".join(parts[1:]))
            elif command == "type" and args in builtins:
                print(f"{parts[1]} is a shell builtin")
            elif command == "type" and args not in builtins:
                print(f"{args}: not found")
            else:
                print(f"{usr_input}: command not found")
        else:
            print("No user input provided")


if __name__ == "__main__":
    main()
