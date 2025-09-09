import os
import shutil
source_folder = r"C:\Users\Admin\Pictures\Camera Roll"
destination_folder = r"C:\Users\Admin\Pictures\JPG_Files"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
moved_files = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        try:
            shutil.move(
                os.path.join(source_folder, filename),
                os.path.join(destination_folder, filename)
            )
            print(f"✅ Moved: {filename}")
            moved_files += 1
        except Exception as e:
            print(f"⚠️ Error moving {filename}: {e}")
print(f"\nTotal files moved: {moved_files}")
