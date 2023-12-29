import os
import shutil

def organize_downloads_folder(download_path):
    # Define folders for different file types
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Compressed": [".zip", ".rar", ".7z"],
        "Others": []  # Default folder for other file types
    }

    # Ensure folders exist, create if not
    for folder in folders.keys():
        folder_path = os.path.join(download_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # List all files in the downloads folder
    files = [f for f in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, f))]

    # Organize files into respective folders
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in folders.items():
            if file_extension in extensions:
                source_path = os.path.join(download_path, file)
                destination_path = os.path.join(download_path, folder, file)

                shutil.move(source_path, destination_path)
                print(f"Moved {file} to {folder}")
                moved = True
                break

        # If the file type is not recognized, move it to the 'Others' folder
        if not moved:
            source_path = os.path.join(download_path, file)
            destination_path = os.path.join(download_path, "Others", file)

            shutil.move(source_path, destination_path)
            print(f"Moved {file} to Others")

if __name__ == "__main__":
    # Replace 'YOUR_DOWNLOADS_PATH' with the actual path to your downloads folder
    downloads_path = r'D:\full stack development\pythonProject\d98Customautomation\downloadhere'
    organize_downloads_folder(downloads_path)
