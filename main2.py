# Interactive Y/N Prompt
# The script will ask you (Y/N) for each file before adding it to the final text file.
# You can simply press y to include it or n to skip it.

import os
import datetime


def gather_files_interactive():
    directory = input("Enter the directory path: ").strip()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.normpath(directory))
    output_filename = f"{base_name}_{timestamp}.txt"

    with open(output_filename, "w", encoding="utf-8", errors="replace") as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

                # Ask user if they want to include the file
                answer = input(f"Include '{relative_path}'? (y/n): ").strip().lower()
                if answer != 'y':
                    continue  # skip this file if the user chooses

                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
                        contents = infile.read()
                except Exception as e:
                    contents = f"Error reading file: {e}"

                outfile.write(f"Filename: {file}\n")
                outfile.write(f"Relative Path: {relative_path}\n")
                outfile.write("'''\n")
                outfile.write(contents)
                outfile.write("\n'''\n\n")

    print(f"All selected files have been combined into {output_filename}")


if __name__ == "__main__":
    gather_files_interactive()
