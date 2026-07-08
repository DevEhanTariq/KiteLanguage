import sys
from .commands import *

args = sys.argv[1:]
command = args[0]

def main() -> None:
    if not args:
        print("Usage: mycli <command>")
        exit()

    if command == "init":
        kinit(args)

    elif command == "remove":
        kremove(args)

    elif command == "parse":
        kparse(args)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()