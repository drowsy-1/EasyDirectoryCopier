import os
import datetime


def gather_files_interactive_skip_modules():
    # Prompt for the directory path
    directory = input("Enter the directory path: ").strip()

    # Create an output file name using the folder name + date/time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.normpath(directory))
    output_filename = f"{base_name}_{timestamp}.txt"

    # Directories to skip automatically (e.g., dependencies, version control)
    skip_dirs = {'node_modules', '.git', 'next', '.next'}

    with open(output_filename, "w", encoding="utf-8", errors="replace") as outfile:
        for root, dirs, files in os.walk(directory):
            # Remove any directories in the skip list so they're not even traversed
            dirs[:] = [d for d in dirs if d not in skip_dirs]

            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

                # Ask user if they want to include the file
                answer = input(f"Include '{relative_path}'? (y/n): ").strip().lower()
                if answer != 'y':
                    continue  # skip this file if the user says no

                # Attempt to read the file
                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
                        contents = infile.read()
                except Exception as e:
                    contents = f"Error reading file: {e}"

                # Write file information and contents to the output
                outfile.write(f"Filename: {file}\n")
                outfile.write(f"Relative Path: {relative_path}\n")
                outfile.write("'''\n")
                outfile.write(contents)
                outfile.write("\n'''\n\n")

    print(f"All selected files have been combined into {output_filename}")


if __name__ == "__main__":
    gather_files_interactive_skip_modules()
