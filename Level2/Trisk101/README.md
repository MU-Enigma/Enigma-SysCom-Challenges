
# Simple Custom Shell (PS 2.1)

**By:** Parv Dubey  
**ID:** SE23UMEC021

---

## Software Requirements
- **OS:** Windows/MacOS/Linux
- **Python**
- **VS Code**

---

## Introduction

We will import our required libraries. No additional libraries are required to be downloaded as all are pre-downloaded Python libraries.

```
import os
import subprocess
import sys
```

Other than the top two libraries, the third library (`sys`) is used to make the custom shell functional across 3 operating systems (i.e., Windows, Linux, and MacOS).

The code is mostly self-explanatory. Wherever I have used commands other than normal Python commands, I have given comments to explain their roles in that particular code block.

The code is very basic and straightforward, with mostly condition-based operations for all of the required commands to work (i.e., `cd`, `mkdir`, `touch`, `open`, `exit`). I have included one or two extra lines of code in each defined function to handle any errors and prevent the code from crashing.

For the functions `cd` and `mkdir`, I used help from ChatGPT to understand what commands I needed to use and how and where I should implement them in the code.

The entire shell has been coded in Python and on VS Code with a manual install of the Python extension for it and Python 3.11 from the Microsoft Store.

---

## Important Note

When the shell is started for the first time, you won't have any directories to access, so run the `mkdir` command and create a few directories. After that, you can use the `cd` command to switch between them. The `touch` and `open` commands will open Notepad on Windows and MacOS, and Nano on Linux distros.
