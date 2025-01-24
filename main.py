import os
import datetime


def gather_files_into_single_text():
    # Prompt for the directory path
    directory = input("Enter the directory path: ").strip()

    # Generate a timestamp for the output file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Use the base folder name plus the timestamp to name the output file
    base_name = os.path.basename(os.path.normpath(directory))
    output_filename = f"{base_name}_{timestamp}.txt"

    # Open the output file in write mode
    with open(output_filename, "w", encoding="utf-8", errors="replace") as outfile:
        # Walk through all subdirectories and files
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Create a relative path from the main directory to the file
                relative_path = os.path.relpath(file_path, directory)

                # Attempt to read the file contents
                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
                        contents = infile.read()
                except Exception as e:
                    # If there's an error reading a file (e.g., it's binary), skip or log an error
                    contents = f"Error reading file: {e}"

                # Write file info and contents to the output
                outfile.write(f"Filename: {file}\n")
                outfile.write(f"Relative Path: {relative_path}\n")
                outfile.write("'''\n")
                outfile.write(contents)
                outfile.write("\n'''\n\n")

    print(f"All files have been combined into {output_filename}")


# Run the function if this script is executed directly
if __name__ == "__main__":
    gather_files_into_single_text()
