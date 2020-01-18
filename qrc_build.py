#qrc_build.py

import glob
import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
print ( "current path:", dir_path )
print ( "current path length:", len(dir_path) )
print ( "char at end:", dir_path[len(dir_path)-1:len(dir_path)])
last_char = dir_path[len(dir_path)-1:len(dir_path)]
if last_char != "\\":
   dir_path = dir_path + "\\"
print ( "current path added \:", dir_path )

# planA
# print(glob.glob("c:\*.txt"))

# planB
# 打开文件
path = "C:/"
dirs = os.listdir( dir_path )
print( dirs )

# 输出所有文件和文件夹
for file in dirs:
   print ( file )

# 打开一个文件
fo = open("main.qrc", "w+")
print ( "文件名: ", fo.name )
print ( "是否已关闭 : ", fo.closed )
print ( "访问模式 : ", fo.mode )
# print ( "末尾是否强制加空格 : ", fo.softspace )

fo.write( "<RCC>\n")
fo.write( "\t" + "<qresource prefix=\"/\">\n")
for file in dirs:
   if -1 != file.find(".qrc"):
      fo.write( "\t" + "<file>" + file + "</file>" + "\n" )
fo.write( "\t" + "</qresource>\n")   
fo.write( "</RCC>\n")


# 关闭打开的文件
fo.close()
