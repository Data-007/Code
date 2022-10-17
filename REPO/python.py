import os
from re import I, X
import string
import subprocess
from traceback import print_list
from typing_extensions import Self
from xml.dom.pulldom import END_ELEMENT

def GetWin():
    #generates text file "windows.txt" current dir
    list=[os.system("wmctrl -p -G -l >windows.txt")]
    


def jls_extract_def():
    
    return 


def ReadWin():
    f= open("windows.txt", "r")
    for lines in f:
        #list[lines]=print(f.readline(lines))
        
        WinNum=lines = jls_extract_def()
    f.close
    return  list[linenum] #was list[lines]
   


__name__ == '__main__'
GetWin()
ReadWin()
