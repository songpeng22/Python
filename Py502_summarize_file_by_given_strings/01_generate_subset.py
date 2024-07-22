import os

# defines
filter_src = ["Cache.cach","fileState.txt","Label.txt"]
target_file = filter_src[1]

file_dir = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
dir_of_subset = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
dir_of_mainset = 'E:\\PaddleOCR_Data\\train_data\\'
dir_of_excludeset = 'E:\\PaddleOCR_Data\\train_data_00_excluded\\'

def list_file(src_dir):
    files = os.listdir(file_dir)
    print('list files:')
    print(files)
    return files
files = list_file(file_dir)

# write file lists to file
file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
filelist_path_of_subset = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
filelist_path_of_mainset = "E:\\PaddleOCR_Data\\train_data\\filelists.txt"
filelist_path_of_excludeset = "E:\\PaddleOCR_Data\\train_data_00_excluded\\filelists.txt"
def generate_file_path_list_file(tar_file):
    print('\nwrite file lists to file:')
    file = open(tar_file, "w") 
    for f in files:
        if f.endswith(".png"):
            print(f)
            file.write(f + "\n")
        elif f.endswith(".jpg"):
            print(f)
            file.write(f + "\n")
        elif f.endswith(".jpeg"):
            print(f)
            file.write(f + "\n")
        else:
            extension = f.split('.')
            #print(extension)
            #print(extension[-1] + "is excluded.")
            print(f + " is excluded.")
    file.close()
generate_file_path_list_file(file_path)

# read file line by line
#file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
def read_file_line_by_line_with_strip(file_path):
    print('\nread file line by line:')
    # write lines to array
    lines_key = []
    with open(file_path, "r", encoding="utf-8") as file_in:
        for line in file_in:
            print(line.strip())
            lines_key.append(line.strip())
    return lines_key
#lines_keys = read_file_line_by_line_with_strip(filelist_path_of_subset)
# write lines to array
file_path_of_mainset = dir_of_mainset + target_file
def read_file_line_by_line(file_path):
    print('\nread file line by line:')
    lines_full = []
    with open(file_path, "r", encoding="utf-8") as file_full:
        for line_full in file_full:
            #print(line_full)
            lines_full.append(line_full)
    return lines_full
#lines_full = read_file_line_by_line(file_path_of_mainset)

# found keys is contained in Label.txt, and write into new path
file_path_of_subset = dir_of_subset + target_file
file_path_of_excludeset = dir_of_excludeset + target_file
def filter_lines_with_keys(keys_file,lines_file,file_new):
    bFoundAll = True
    countOfFound = 0
    lines_keys = read_file_line_by_line_with_strip(keys_file)
    lines_full = read_file_line_by_line(lines_file)
    lines_excluded = lines_full[:]
    countOfMainSet = len(lines_full)
    with open(file_new, "w", encoding="utf-8") as _file_new:
        for key in lines_keys:
            #print(key)
            bFound = False
            for line in lines_excluded[:]:
                if line.find(key) != -1:
                    #print(line)
                    lines_excluded.remove(line)
                    _file_new.write(line)
                    bFound = True
                    countOfFound+=1
                    break
            if(bFound != True):
                print(key + " not found!!!")
                bFoundAll = False
    """
    # generate excludeset file
    with open(file_path_of_excludeset, "w", encoding="utf-8") as _file_new:
        for line in lines_excluded:
            _file_new.write(line)
    """            
    print(f"main set count:{countOfMainSet},found:{countOfFound},exclude count:{countOfMainSet - countOfFound}")
    return bFoundAll

bFoundAll = filter_lines_with_keys(filelist_path_of_subset,file_path_of_mainset,file_path_of_subset)
if(bFoundAll == True):
    print("found all keys.")



