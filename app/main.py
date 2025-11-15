import sys

BUILTINS = {"exit"}

def run_builtin(args):
    cmd = args[0]
    if cmd == "exit":
        if len(args) > 1:
            code = int(args[1])
        else:
            code = 0
        sys.exit(code)

def main():
    while True:
        try:
            sys.stdout.write("$ ")
            line = input()
            args = line.split()

            if args[0] not in BUILTINS:
                print(f"{args[0]}: command not found")

            run_builtin(args)
        except KeyboardInterrupt:  # Ctrl-C
            print()
            continue


if __name__ == "__main__":
    main()
