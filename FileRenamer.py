import os

folder_path = input("Enter the folder path where the files are located: ").strip()

if not os.path.exists(folder_path):
    print("Error: The specified folder does not exist. Please check the path and try again.")
    exit()

file_extension = input("Enter the file type to rename (e.g., .txt): ").strip()
name_pattern = input("Enter the naming pattern (use {num} for numbers): ").strip()

files = os.listdir(folder_path)

backup_file = os.path.join(folder_path, "backup.txt")

try:
    with open(backup_file, "w") as backup:
        for index, file in enumerate(files):
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path) and file.endswith(file_extension):
                new_name = name_pattern.format(num=index+1) + file_extension
                new_path = os.path.join(folder_path, new_name)

                backup.write(f"{new_name} -> {file}\n")

                os.rename(old_path, new_path)
                print(f"Renamed: {file} -> {new_name}")

    print("All files renamed successfully! (Backup created)")

except Exception as e:
    print(f"Error: {e}")
