import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        parts = command.split()
        print(parts)

        if command == "exit":
            break
        if parts and parts[0] == "echo":
            print(" ".join(parts[1:]))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
