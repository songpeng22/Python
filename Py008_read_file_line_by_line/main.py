# with statement to write file - do not need file close
with open('E:\\PaddleOCR_Data\\test.txt', 'w') as file:
    file.write('line 1\n')
    file.write('line 2\n')
    file.write('line 3\n')


# read file line by line
with open("E:\\PaddleOCR_Data\\test.txt") as file_in:
    lines = []
    for line in file_in:
        print(line)
        lines.append(line)

"""
# test code - Label.txt - Cache.cach
with open("E:\\PaddleOCR_Data\\train_data\\Cache.cach","r",encoding="utf-8") as file_in:
    lines = []
    for line in file_in:
        if(line.find("med012") != -1):
            print(line)
        lines.append(line)
"""