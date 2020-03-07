#qrc_build.py

import glob
import os, sys

# current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
last_char = dir_path[len(dir_path)-1:len(dir_path)]
if last_char != "\\":
   dir_path = dir_path + "\\"
print ( "current path added \:", dir_path )

# enum file in folder which contains *.qml file
dirs = os.listdir( dir_path )
print( dirs )

# generate qrc file from file list
current_path = os.path.dirname(sys.argv[0])
join_path = os.path.join( current_path,"skin.qrc" )
print( "os.path.dirName:",current_path )
print( "open this join_path to write:",join_path )
fo = open( join_path, "w+") # w+ to overwrite old file while running

fo.write( "<RCC>\n")
fo.write( "\t" + "<qresource prefix=\"/\">\n")
for file in dirs:
   if -1 != file.find(".conf"):
      fo.write( "\t" + "<file>" + file + "</file>" + "\n" )
for file in dirs:
   if -1 != file.find(".qml"):
      fo.write( "\t" + "<file>" + file + "</file>" + "\n" )
fo.write( "\t" + "</qresource>\n")   
fo.write( "</RCC>\n")

fo.close()
