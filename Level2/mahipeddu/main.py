import os
import subprocess

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {path}")
    except Exception as e:
        print(f"Error changing directory: {e}")

def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def create_file(path):
    try:
        with open(path, 'a'):
            os.utime(path, None)
        print(f"File created: {path}")
    except Exception as e:
        print(f"Error creating file: {e}")

def open_in_editor(path):
    editor = 'nano' 
    try:
        subprocess.run([editor, path])
    except Exception as e:
        print(f"Error opening file in editor: {e}")

def main():
    while True:
        command = input("my_shell> ").strip().split()
        
        if not command:
            continue
        
        cmd = command[0]
        args = command[1:]
        
        if cmd == 'cd':
            if args:
                change_directory(args[0])
            else:
                print("Usage: cd <path>")
        
        elif cmd == 'mkdir':
            if args:
                make_directory(args[0])
            else:
                print("Usage: mkdir <path>")
        
        elif cmd == 'touch':
            if args:
                create_file(args[0])
            else:
                print("Usage: touch <file>")
        
        elif cmd == 'open':
            if args:
                open_in_editor(args[0])
            else:
                print("Usage: open <file>")
        
        elif cmd == 'exit':
            print("Exiting shell.")
            break
        
        else:
            print(f"Command not found: {cmd}")

if __name__ == "__main__":
    main()
