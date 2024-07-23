import shutil

# back file before operation
def backup_file(file_path):
    backup_file_path = file_path + '.bak'
    shutil.copy2(file_path, backup_file_path)
    print(f"文件已备份为 {backup_file_path}")

# read file line by line
def sort_file_lines(file_path):
    lines = set()
    with open(file_path, "r", encoding="utf-8") as _file:
        lines = _file.readlines()
    #print(lines)
    
    sorted_lines = sorted(lines, key=str.casefold)
    length = len(sorted_lines)
    print(f"len:{length}")

    with open(file_path, 'w', encoding="utf-8") as _file:
        _file.writelines(sorted_lines)

    print(f"文件 {file_path} 已按行排序")

# defines
filter_src = ["Cache.cach","fileState.txt","Label.txt"]
target_file = filter_src[2]
file_path = "E:\\PaddleOCR_Data\\train_data\\" + target_file
backup_file(file_path)
sort_file_lines(file_path)