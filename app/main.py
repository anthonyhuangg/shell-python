import sys

def check_valid_command(command):
    return False

def main():
    sys.stdout.write("$ ")
    command = input()
    
    if not check_valid_command(command):
        print(f"{command}: command not found")

    pass

if __name__ == "__main__":
    main()
