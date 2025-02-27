import os

folder_path = r"C:\Users\busch\OneDrive\Documents\aagergaergaerg\PYYYTest"

files = os.listdir(folder_path)


for index, file in enumerate(files):
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path) and file.endswith(".txt"):
        new_name = f"file_{index+1}.txt"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

print("✅ All .txt files renamed successfully (other files ignored)!")
