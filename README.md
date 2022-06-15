# Duplicate File Handler

This Python script is designed to search for duplicate files within a specified directory based on size and hash values. It provides users with options to display the file tree, identify duplicates, and delete selected duplicates to free up disk space.

## Features

- **Directory Tree Listing**: List all files in specified directory and subdirectories with a particular file format.
- **Sorting Options**: Display files in ascending or descending order of their size.
- **Duplicate Identification**: Identify duplicate files based on file size and MD5 hash.
- **Selective File Deletion**: Option to delete selected duplicate files to free up space.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/duplicate-file-handler.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

You will be prompted to:
- Enter the file format you are interested in (e.g., `.txt`, `.jpg`). Leave empty and press enter if you want to consider all files.
- Choose a size sorting option (`1` for Descending or `2` for Ascending order).
- Decide whether to check for duplicates.
- Choose to delete files, if duplicates are found.

### Note
When running the deletion option, ensure you have the necessary permissions to delete files in the chosen directory.

## Example

```bash
$ python file_organizer.py /path/to/directory
Enter file format:
.txt
Enter a sorting option:
1. Descending
2. Ascending
1

[...Output...]
```

## Warning

Use the deletion feature with caution. Deleted files are not recoverable through this script.

## License

This project is licensed under the [MIT License](LICENSE.txt).
