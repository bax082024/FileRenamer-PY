# File Renamer & Undo Script

This project is a Python script that allows users to rename multiple files, 
in a folder while also providing an undo feature to restore the original filenames. 
The script is useful for bulk renaming operations and ensuring that changes can be reverted if needed.

---

## Features

- Rename multiple files based on user-defined patterns.
- Filter by file type (example: `.txt`, `.jpg`, etc.).
- Stores a backup of original filenames before renaming.
- Undo functionality to restore previous filenames.
- Error handling for missing files and permission issues.

---

## Requirements

- Python 3.x
- Works on Windows, Linux, macOS

---

## How to use 

**Step 1:**

1. Run `FileRenamer.py`
2. Enter the file extension to rename (ex: `.txt`, `.jpg` etc) 
3. Enter the naming pattern (ex: `file_{num}`)
4. The script renames files and creates a `backup.txt` to store original names.

**Step 2:**

1. Run `UndoRenamer.py`
2. it reads backup.txt and restores the original filenames.
3. The backup file is deleted after restoration.

---

## Contact

For questions or feedback, please contact :

- **bax082024@gmail.com**

