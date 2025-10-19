# Email Extractor Automation (GUI)

## Overview

This is a Python-based GUI application that automatically extracts all valid email addresses from a text file and saves them to a new file. The application uses Tkinter for the graphical interface and regular expressions to detect email addresses.

---

## Features

- Select any `.txt` file using a file picker.
- Automatically extract all valid email addresses.
- Removes duplicate emails.
- Saves results to `output_emails.txt` in the same folder as the input file.
- Shows a success popup with total emails found and file path.
- Simple and user-friendly GUI.

---

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- `re` and `os` (built-in Python modules)

Optional:

- PyInstaller (to create a standalone `.exe` file)

---

## How to Run

1. Clone or download the repository.
2. Make sure you have Python 3 installed.
3. Open terminal/command prompt and navigate to the project folder.
4. Run the script:
   ```bash
   python email_extractor_gui.py
Click the "Select File & Extract Emails" button.

Choose a .txt file containing text with email addresses.

The emails will be extracted and saved to output_emails.txt.

Creating a Standalone Executable
To create a standalone Windows .exe file:

Install PyInstaller:

pip install pyinstaller
Run the following command in your project folder:


pyinstaller --onefile --noconsole email_extractor_gui.py
The .exe file will be created in the dist folder.

Optional: Add a custom icon:

pyinstaller --onefile --noconsole --icon=mail.ico email_extractor_gui.py

Folder Structure

graphql

EmailExtractor/

│

├── email_extractor_gui.py     # Main Python script

├── input.txt                  # Sample text file (optional)

├── output_emails.txt          # Generated after running the app

└── mail.ico                   # Optional icon for exe
