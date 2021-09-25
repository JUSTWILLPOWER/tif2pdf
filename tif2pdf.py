#!python
from posixpath import dirname
import tkinter
from tkinter import filedialog
from tkinter.constants import FALSE, NO
import img2pdf
import os
'''
@description  :将文件夹内的所有图片合起来转为pdf
---------
@param  :需要转换的图片tuble， 以及合并后的文件名
-------
@Returns  :无
-------
'''
def Img_To_Pdf(allFile:tuple, fileName:str):
    dirName = os.path.dirname(allFile[0])
    path = os.path.join(dirName, fileName) + '.pdf'
    with open(path, "wb") as f:
        f.write(img2pdf.convert(allFile))
root = tkinter.Tk()  # 创建实例
root.withdraw()  # 隐藏
selectPic_Name = filedialog.askopenfilenames()
print(selectPic_Name)
Img_To_Pdf(selectPic_Name, "Coverted_File")

