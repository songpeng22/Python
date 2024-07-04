import os

# defines
filter_src = ["Cache.cach","fileState.txt","Label.txt"]
target_file = filter_src[1]

file_dir = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
def list_file(src_dir):
    files = os.listdir(file_dir)
    print('list files:')
    print(files)
    return files
files = list_file(file_dir)

# write file lists to file
file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
def generate_file_path_list_file(tar_file):
    print('\nwrite file lists to file:')
    file = open(file_path, "w") 
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
lines_key = []
lines_full = []
file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
def read_file_line_by_line_with_strip(file_path):
    print('\nread file line by line:')
    # write lines to array
    with open(file_path, "r", encoding="utf-8") as file_in:
        for line in file_in:
            print(line.strip())
            lines_key.append(line.strip())
    return lines_key
lines_key = read_file_line_by_line_with_strip(file_path)
# write lines to array
file_path = "E:\\PaddleOCR_Data\\train_data\\" + target_file
def read_file_line_by_line(file_path):
    print('\nread file line by line:')
    with open(file_path, "r", encoding="utf-8") as file_full:
        for line_full in file_full:
            #print(line_full)
            lines_full.append(line_full)
    return lines_full
lines_full = read_file_line_by_line(file_path)

# found keys is contained in Label.txt, and write into new path
file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\" + target_file
def filter_lines_with_keys(lines_keys,lines_full,file_new):
    bFoundAll = True
    with open(file_path, "w", encoding="utf-8") as file_new:
        for key in lines_key:
            #print(key)
            bFound = False
            for line in lines_full:
                if line.find(key) != -1:
                    #print(line)
                    file_new.write(line)
                    bFound = True
                    break
            if(bFound != True):
                print(key + " not found!!!")
                bFoundAll = False
    return bFoundAll

bFoundAll = filter_lines_with_keys(lines_key,lines_full,file_path)
if(bFoundAll == True):
    print("found all keys.")



