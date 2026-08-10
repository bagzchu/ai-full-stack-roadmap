from pathlib import Path
import shutil

my_folder = Path("C:/Users/Test")
#print(my_folder.exists())

for item in my_folder.iterdir():
    if item.is_file():
        print(f"File: {item.name} | Extension: {item.suffix}")

# Define the paths for our new folders
images_folder = my_folder / "Images"
docs_folder = my_folder / "Documents"

images_folder.mkdir(exist_ok=True)
docs_folder.mkdir(exist_ok=True)

for item in my_folder.iterdir():
    if item.is_file():
        # Get the extension in lowercase (e.g., .JPG becomes .jpg)
        ext = item.suffix.lower()

        # Check if it's an image
        if ext in [".jpg", ".jpeg", ".png", ".gif"]:
            destination = images_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"🚚 Moved Image: {item.name}")

        # Check if it's a document
        elif ext in [".pdf", ".docx", ".txt", ".xlsx"]:
            destination = docs_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"🚚 Moved Document: {item.name}")