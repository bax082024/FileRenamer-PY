import os

folder_path = r"C:\Users\busch\OneDrive\Documents\aagergaergaerg\PYYYTest"
backup_file = os.path.join(folder_path, "backup.txt")

if os.path.exists(backup_file):
    try:
        with open(backup_file, "r") as backup:
            for line in backup:
                new_name, old_name = line.strip().split(" -> ")
                new_path = os.path.join(folder_path, new_name)
                old_path = os.path.join(folder_path, old_name)

                os.rename(new_path, old_path)
                print(f"Restored: {new_name} -> {old_name}")

        print("Undo completed! All file names restored.")

        os.remove(backup_file)

    except Exception as e:
        print(f"Error restoring files: {e}")

else:
    print("No backup file found. Cannot undo renaming.")

