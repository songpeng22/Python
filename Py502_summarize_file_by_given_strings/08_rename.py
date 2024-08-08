
import os

def rename_files_in_folder(folder_path, match_in_old_name, string_of_replace_with):
    is_replace_all = False
    # 遍历指定文件夹内的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        old_file_path = os.path.join(folder_path, filename)
        # 检查文件名是否包含匹配字符串
        if os.path.isfile(old_file_path) and match_in_old_name in filename:
            # 生成新文件名
            new_name = filename.replace(match_in_old_name, string_of_replace_with)
            new_file_path = os.path.join(folder_path, new_name)
            
            if not is_replace_all:
                # 提示用户确认重命名
                confirm = input(f"确认将 '{filename}' 重命名为 '{new_name}'? (y/n/a): ")
                
                if confirm.lower() == 'y':
                    os.rename(old_file_path, new_file_path)
                    print(f"文件 '{filename}' 已重命名为 '{new_name}'")
                elif confirm.lower() == 'n':
                    print(f"跳过 '{filename}'")
                elif confirm.lower() == 'a':
                    os.rename(old_file_path, new_file_path)
                    print(f"文件 '{filename}' 已重命名为 '{new_name}'")
                    is_replace_all = True  # 启用自动重命名
                else:
                    print("无效输入，跳过该文件")
            else:
                # 如果已经选择了 'a'，直接重命名
                os.rename(old_file_path, new_file_path)
                print(f"文件 '{filename}' 已重命名为 '{new_name}'")
        else:
            print(f"'{filename}' 不包含 '{match_in_old_name}'，跳过")

if __name__ == '__main__':
    print(f"rename")
    # 使用示例
    folder_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\"
    match_in_old_name = input("请输入要匹配的字符串: ")
    string_of_replace_with = input("请输入替换字符串: ")
    rename_files_in_folder(folder_path, match_in_old_name, string_of_replace_with)
