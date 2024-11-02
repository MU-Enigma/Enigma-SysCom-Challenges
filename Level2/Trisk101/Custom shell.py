import os # for interacting with the operating system + directory and file manipulation
import subprocess #for oening files in external directories
import sys
def cd(path):  # changes directory
    try:
        os.chdir(path)
        print(f"Changed directory -> {os.getcwd()}")
    except FileNotFoundError:  # incase directory doesn't exist.
        print(f"Directory '{path} doesn't exist.") 
    except NotADirectoryError:   # incase path is not a directory.
        print(f"{path} Not a directory.")
    except Exception as e:  #  in case of any other general errors adn displays them.
        print(f"Error: {e}")


def mkdir(dir_name):  #creates directory
    try:
        os.makedirs(dir_name, exist_ok=True) # to prevent error incase directory already exists.
        print(f"Directory '{dir_name}' created.")
    except Exception as e: # gets any errors during the creation of the directory and prints them.
        print(f"Error: {e}") 


def touch(f_name):  #creates a file
    try:
        open(f_name, 'a').close() #'a' opens the file in append mode, ifx file exists, it opens and closes it unchanged, if it doesnt exist, it creates a new one.
        print(f"File'{f_name}' created.")
    except Exception as e: #  in case of any other general errors adn displays them.
        print(f"Error: {e}")


def open_file(file_name, editor = 'None'): # opens file based on the operating system with dual compatibility for windows, linux and MacOS
    if editor is None:
        editor = 'nano' if sys.platform.startswith('linux') else 'notepad' # Checking whether the os is windows or linux
    try:
        subprocess.run([editor,file_name]) # opens the file in the editor based on os
    except FileNotFoundError:
        print(f"Editor '{editor}' not found.")
    except Exception as e: #  in case of any other general errors adn displays them.
        print(f"Error: {e}")



def command_h(command): # Handling of all the commands (cd, mkdir, touch, open, exit)
    cmd, *args = command

    if cmd == "cd" and args: # for changing directory
        cd(args[0])
    elif cmd == "mkdir" and args: # for making a new directory
        mkdir(args[0])
    elif cmd == "touch" and args: # for creating a new file
        touch(args[0])
    elif cmd == "open" and args: # for opening the file in editor
        editor = args[1] if len(args) > 1 else None
        open_file(args[0], editor)
    elif cmd == "exit": # for exiting the shell
        print("Exiting Shell.")
        return False
    else:
        print("Unknown command") # unknown command handle
    return True


def main():
    print("Custom Shell - Enter 'exit' to quit : ")
    while True:
        command = input("Enter command : ").strip().split() # takes whitespaces ,tabs out of consideration and makes the commands separated for easier parsing
        if command:
            if not command_h(command):
                break

if __name__ == "__main__":
    main()