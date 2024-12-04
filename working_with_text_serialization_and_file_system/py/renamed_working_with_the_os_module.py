"""
1. Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями. 
Программа должна:
"""

import os
import shutil

def sort_files_by_extension(folder_path):
    os_name = os.name
    print(f"Операционная система: {os_name}")

    current_dir = os.path.abspath(folder_path)
    print(f"Путь до папки: {current_dir}")

    extensions_info = {}

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        file_extension = os.path.splitext(file_name)[-1].lower()
        if file_extension == "":
            file_extension = "no_extension"

        ext_folder_path = os.path.join(folder_path, file_extension.strip('.'))
        os.makedirs(ext_folder_path, exist_ok=True)

        new_file_path = os.path.join(ext_folder_path, file_name)
        shutil.move(file_path, new_file_path)

        file_size = os.path.getsize(new_file_path)
        if file_extension not in extensions_info:
            extensions_info[file_extension] = {"count": 0, "size": 0}
        extensions_info[file_extension]["count"] += 1
        extensions_info[file_extension]["size"] += file_size

    for ext, info in extensions_info.items():
        print
        (f"В папке с расширением .{ext} перемещено {info['count']} файлов, их суммарный размер - {info['size'] / (1024 ** 3):.2f} гигабайт")

    for ext in extensions_info.keys():
        ext_folder_path = os.path.join(folder_path, ext.strip('.'))
        renamed = False

        for file_name in os.listdir(ext_folder_path):
            old_file_path = os.path.join(ext_folder_path, file_name)

            new_file_name = f"renamed_{file_name}"
            new_file_path = os.path.join(ext_folder_path, new_file_name)

            os.rename(old_file_path, new_file_path)
            print(f"Файл {file_name} был переименован в {new_file_name}")
            renamed = True
            break 

if __name__ == "__main__":
    folder_to_process = "test_folder"
    sort_files_by_extension(folder_to_process)
