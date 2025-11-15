import sys

def check_valid_command(command):
    return False

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        
        if not check_valid_command(command):
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
