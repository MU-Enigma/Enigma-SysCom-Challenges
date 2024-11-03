import os                        # interaction with os and manipulate directories etc
import sys                       # to make script interact with command line
import datetime                  # for working with dates and time
from pathlib import Path         # for oriented way to interact with file paths
import hashlib                   # for hashin algo to generate secure identifires for commits
import shutil                    # high level file ops including copying and moving files and directories.

class VCS:
    def __init__(self, path = '.vcs'):                   # Setting up the paths and loading active branch if repo exists
        self.repo_path = Path(path)
        self.snapshots_path = self.repo_path / "snapshots"
        self.branches_path = self.repo_path / "branches"
        self.active_branch_file = self.repo_path / "active_branch"

        self.active_branch = "main"

        if not self.repo_path.exists():
            self.init_repo()
        else:
            self.active_branch = self.load_active_branch() or "main"

    def init_repo(self):                              # creation of initial stucture for repo if it doesn't exist.
        os.makedirs(self.snapshots_path, exist_ok = True)
        os.makedirs(self.branches_path, exist_ok = True)

        self.create_branch("main")
        self.switch_branch("main")

        print("Repository initialised with 'main' branch.")

    def load_active_branch(self):                     # loads current active branch from active branch file
        if self.active_branch_file.exists():
            with open(self.active_branch_file, "r") as file:
                return file.read().strip()
        return None
    
    def save_active_branch(self, branch_name):        # saves the specified branch as active branch by writing it in active branch file
        with open(self.active_branch_file, "w") as file:
            file.write(branch_name)

    def commit(self, filename, message):              # creates a save copy of specified file with identifier and logging it in branch history.
        if not Path(filename).exists():
            print(f"File '{filename}' does not exist.")
            return
        
        commit_hash = hashlib.sha1(datetime.datetime.now().isoformat().encode()).hexdigest()
        commit_dir = self.snapshots_path / commit_hash
        os.makedirs(commit_dir, exist_ok= True)

        shutil.copy(filename, commit_dir / Path(filename).name)

        branch_log = self.branches_path / f"{self.active_branch}.log"
        parent_commit = self.get_last_commit()
        with open(branch_log, "a") as log_file:
            log_file.write(f"{commit_hash[:7]} - {message} (parent: {parent_commit})\n")

        print(f"Committed '{filename}' to {self.active_branch} as {commit_hash[:7]} - {message}")


    def get_last_commit(self):                      # gets last commit hash from active branch log file
        branch_log = self.branches_path / f"{self.active_branch}.log"
        if branch_log.exists():
            with open(branch_log, "r") as log_file:
                lines = log_file.readlines()
                if lines:
                    return lines[-1].split()[0]
        return None
    
    def create_branch(self, branch_name):           # creates new branch from current commit in active branch
        branch_log = self.branches_path / f"{branch_name}.log"
        if branch_log.exists():
            print(f"Branch '{branch_name}' already exists.")
            return
        
        with open(branch_log,"w") as log_file:
            last_commit = self.get_last_commit()
            if last_commit:
                log_file.write(f"{last_commit} - Initial branch point \n")

        print(f"Created branch '{branch_name}'.")


    def switch_branch(self, branch_name):           # switches active branch
        branch_log = self.branches_path / f"{branch_name}.log"
        if not branch_log.exists():
            print(f"Branch '{branch_name}' does not exist.")
            return
        
        self.active_branch = branch_name
        self.save_active_branch(branch_name)
        print(f"Switched to branch '{branch_name}'.")


    def log(self):                                  # shows commit hitory of active branch
        branch_log = self.branches_path / f"{self.active_branch}.log"
        if branch_log.exists():
            with open(branch_log, "r") as log_files:
                print(f"Commit history for branch '{self.active_branch}':\n" + log_files.read())
        else:
            print(f"No commits found for branch '{self.active_branch}'.")

        
    def checkout(self, commit_hash):               # restore file from commit by copying from snapshot dir to working dir
        commit_dir = self.snapshots_path / commit_hash
        if not commit_dir.exists():
            print("Commit not found.")
            return
        for file_path in commit_dir.iterdir():
            shutil.copy(file_path, Path(file_path.name))
        print(f"Checked out {commit_hash[:7]} on branch '{self.active_branch}'.")


def main():                                     # for command in line interface for interacting with vcs class
    _vcs_ = VCS()
        
    if len(sys.argv) < 2:
        print("Usage: python vcs.py <command> [arguments]")
        return

    cmd = sys.argv[1]
    
    if cmd == "commit":
        if len(sys.argv) < 4:
            print("Usage: python vcs.py commit <filename> <message>")
            return
        filename = sys.argv[2]
        message = sys.argv[3]
        _vcs_.commit(filename, message)
    
    elif cmd == "create-branch":
        if len(sys.argv) < 3:
            print("Usage: python vcs.py create-branch <branch_name>")
            return
            
        branch_name = sys.argv[2]
        _vcs_.create_branch(branch_name)
    
    elif cmd == "switch-branch":
        if len(sys.argv) < 3:
            print("Usage: python vcs.py switch-branch <branch_name>")
            return
        branch_name = sys.argv[2]
        _vcs_.switch_branch(branch_name)
    
    elif cmd == "log":
        _vcs_.log()
    
    elif cmd == "checkout":
        if len(sys.argv) < 3:
            print("Usage: python vcs.py checkout <commit_hash>")
            return
        commit_hash = sys.argv[2]
        _vcs_.checkout(commit_hash)
    
    else:
        print("Unknown command.")

if __name__ == "__main__":
        main()