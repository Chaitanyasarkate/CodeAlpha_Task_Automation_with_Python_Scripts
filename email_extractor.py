import os
import re

# Define file paths
input_file = "input.txt"
output_file = "output_emails.txt"

# Check if input file exists
if not os.path.exists(input_file):
    print(f"❌ Input file '{input_file}' not found. Please create it first.")
    exit()

# Read content from the input file
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Regular expression pattern for email extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract all email addresses
emails = re.findall(email_pattern, content)

# Remove duplicates (optional)
emails = list(set(emails))

# Save extracted emails to output file
with open(output_file, "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

# Show success message
print("✅ Email extraction completed successfully!")
print(f"📄 Total Emails Found: {len(emails)}")
print(f"💾 Saved in: {os.path.abspath(output_file)}")
