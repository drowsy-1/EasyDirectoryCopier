# version where you specify which files to skip in comma seperated list

import os
import datetime

def gather_files_skip_by_name():
    directory = input("Enter the directory path: ").strip()

    # Get comma-separated skip names
    skip_input = input("Enter comma-separated names of files/folders to skip (or leave blank): ").strip()
    skip_list = {item.strip() for item in skip_input.split(",")} if skip_input else set()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.normpath(directory))
    output_filename = f"{base_name}_{timestamp}.txt"

    with open(output_filename, "w", encoding="utf-8", errors="replace") as outfile:
        for root, dirs, files in os.walk(directory):
            # Filter out directories we want to skip
            dirs[:] = [d for d in dirs if d not in skip_list]

            for file in files:
                if file in skip_list:
                    continue  # skip the file by name

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

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

    print(f"All files have been combined into {output_filename}")

if __name__ == "__main__":
    gather_files_skip_by_name()
