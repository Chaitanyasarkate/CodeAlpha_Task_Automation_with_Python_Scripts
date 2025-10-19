import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Regular expression pattern for email extraction
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def extract_emails():
    # Ask user to select an input text file
    input_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text Files", "*.txt")]
    )

    if not input_path:
        messagebox.showwarning("No File Selected", "Please select a text file.")
        return

    # Read the file content
    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract all email addresses
    emails = re.findall(EMAIL_PATTERN, content)
    emails = list(set(emails))  # Remove duplicates

    if not emails:
        messagebox.showinfo("No Emails Found", "No valid email addresses found in the file.")
        return

    # Define output file path in same folder as input file
    output_path = os.path.join(os.path.dirname(input_path), "output_emails.txt")

    # Save emails to output file
    with open(output_path, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    # Show success message
    messagebox.showinfo(
        "Success",
        f"✅ Email extraction completed!\n\n"
        f"📄 Total Emails Found: {len(emails)}\n"
        f"💾 Saved to:\n{output_path}"
    )

# GUI Setup
root = tk.Tk()
root.title("Email Extractor Automation")
root.geometry("400x250")
root.resizable(False, False)

# Title Label
tk.Label(root, text="📧 Email Extractor Automation", font=("Arial", 16, "bold"), fg="#0078D7").pack(pady=20)

# Instructions
tk.Label(root, text="Select a .txt file to extract all email addresses from it.", font=("Arial", 10)).pack(pady=5)

# Extract Button
extract_button = tk.Button(
    root,
    text="Select File & Extract Emails",
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    padx=20,
    pady=10,
    command=extract_emails
)
extract_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 10),
    bg="#f44336",
    fg="white",
    width=10,
    command=root.destroy
)
exit_button.pack(pady=10)

# Run the App
root.mainloop()
