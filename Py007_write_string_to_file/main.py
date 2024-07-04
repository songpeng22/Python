# normal file write
file = open("E:\\PaddleOCR_Data\\train_data_04_capture\\requirements.txt","w")  
file.write("Hello") 
file.write(" World\n") 
file.write("This is our new text file\n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.\n")
file.close() 

# with statement to write file - do not need file close
with open('E:\\PaddleOCR_Data\\train_data_04_capture\\requirements.txt', 'a') as file:
    file.write('hello world again !\n')