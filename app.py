import os
import shutil
from pathlib import Path

# 檔案分類規則
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf", ".md"],
    "Music": [".m4a", ".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".sh", ".json"],
    "Others": []
}

# 取得使用者下載資料夾路徑（Windows）
def get_download_folder():
    return Path.home() / "Downloads"

# 分類檔案
def organize_files(download_folder):
    for item in os.listdir(download_folder):
        item_path = os.path.join(download_folder, item)

        # 跳過資料夾（避免重複分類）
        if os.path.isdir(item_path):
            continue

        file_ext = os.path.splitext(item)[1].lower()
        moved = False

        for category, extensions in file_types.items():
            if file_ext in extensions:
                category_folder = os.path.join(download_folder, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(category_folder, item))
                print(f"✅ 移動「{item}」到「{category}/」")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(download_folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(others_folder, item))
            print(f"📦 移動「{item}」到「Others/」")

    print("\n🎉 所有檔案已分類完成！")

# 主程式入口
if __name__ == "__main__":
    download_folder = get_download_folder()
    print(f"📂 開始分類下載資料夾：{download_folder}")
    organize_files(download_folder)
