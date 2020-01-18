#rcc_build.py
import os
import sys

source_path = "skin"
source_name = "skin"
target_path = "bin/"
target_name = "skin"
exe_path = "../bin/"
index = 0

command = "mkdir bin"
ret = os.system( command )
print("mkdir ret:",ret)

# if 1

for index in range(1,3):
    print("index:",index)    
    folder_name = source_path + str(index)
    # qrc part
    python_path = source_path + str(index) + "/" + "qrc_build.py"
    print("python_path:",python_path)
    current_path = os.path.dirname(sys.argv[0])
    print( "os.path.dirName:",os.path.dirname(sys.argv[0]) )
    joinStr = os.path.join( current_path , folder_name ,"qrc_build.py" )
    joinStr = "\"" + joinStr + "\""
    print( "joinStr:",joinStr )
    command = "python3 " + joinStr
    print("command:",command)
    joinStr = joinStr.replace( "\\","\\\\" )
    print( "joinStr with \\\\:",joinStr )
    # unicoe / raw string
#    joinStr.encode('unicode_escape')
    # exec() hard to use even when I put a hand write path exec(r"D:\Test\qrc_build.py"), so choose os.system instead
#    ret = exec(joinStr)
    ret = os.system( command )
    print("exec ret:",ret)    
    # rcc part
    info = "src_path" + str(index) + ":"
    src_path = folder_name + "/" + source_name + ".qrc"    
    print(info,src_path)
    tar_path = target_path + target_name + str(index) + ".rcc"
    print("tar_path",str(index), ":",tar_path)
    command = "rcc -binary " + src_path + " -o " + tar_path
    print("command:",command)
    ret = os.system( command )
    print("rcc ret:",ret)
    command2  = "cp " + tar_path + " " + exe_path + target_name + str(index) + ".rcc"
    print("command:",command2)
    ret = os.system( command2 )
    print("cp ret:",ret)


# else 

#index += 1
#print("index:",index)
#src1 = source_path + str(index) + "/" + source_name + str(index) + ".qrc"
#index += 1
#src2 = source_path + str(index) + "/" + source_name + str(index) + ".qrc"
#tar2 = target_path + "skin1.rcc"
#command = "rcc -binary " + src1 + " -o bin/skin1.rcc"
#ret = os.system( command )
#print( "build skin1.qrc ret:",ret )
#command = "rcc -binary ./skin2/skin2.qrc -o bin/skin2.rcc"
#ret = os.system( command )
#print( "build skin2.qrc ret:",ret )

# endif
