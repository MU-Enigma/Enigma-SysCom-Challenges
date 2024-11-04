# Version Control System

**By**: Parv Dubey  
**ID**: SE23UMEC021

This was genuinely a challenge…had to depend heavily on ChatGPT and YouTube to understand how GitHub works (a VERY small part of it tbh).

I have tried to make a version control system based on what I understood, and it is a very basic barebone copy of GitHub.

## Features

- **Snapshots**: Contains directories for each commit, named by their hash.
- **Branches**: Contains log files for each branch.
- **Active Branch**: A file that stores the name of the currently active branch.

I made the code include basic error handling, such as checking if files exist before committing, preventing the creation of a branch if it already exists, and verifying that branches exist before switching to them.

## Libraries Imported

- `os`: Interaction with OS and manipulation of directories, etc.
- `sys`: To make the script interact with the command line.
- `datetime`: For working with dates and time.
- `pathlib`: For an oriented way to interact with file paths.
- `hashlib`: For hashing algorithms to generate secure identifiers for commits.
- `shutil`: High-level file operations, including copying and moving files and directories.

The source code has been attached, so enjoy! I have commented in it to tell what is doing what in it.

The biggest problems I hit were first trying to figure out what I'm trying to do and what I'm actually doing. I had to refer to ChatGPT a lot for the endless number of errors I kept running into (debugging is like a mini built-in ChatGPT lite). I mostly was getting attribute errors regarding my `active_branch`, so I had to fix that.

To implement the code

Follow these steps :

    1. commit a file : python vcs.py commit myfile.txt "Initial commit"
    2. create a new branch : python vcs.py create-branch feature-xyz
    3. switch branches : python vcs.py switch-branch feature-xyz
    4. log commits : python vcs.py log
    5. checkout a commit : python vcs.py checkout <commit_hash>



In the end, I had a lot of fun doing these levels for Hacktoberfest. I definitely learnt a lot thanks to it though…Thanks a lot, guys.
