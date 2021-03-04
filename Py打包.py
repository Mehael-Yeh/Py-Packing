import os
import shutil
import tkinter
from tkinter import filedialog
def main():
    def Deletefolder(Foldername):
        shutil.rmtree(Folderpath + f'/{Foldername}')
    Installer = os.popen('pip install PyInstaller')
    p=Installer.read()
    if p.find('completed successfully.',-30,-1)\
      or p.find('Requirement already satisfied',0,50):
        root = tkinter.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename(
            title='选择您想打包的Py文件',
            filetypes=[('Python文件','.py')])
        (Folderpath,Filename) = os.path.split(Filepath)
        os.system('cd '+ Folderpath + '&& pyinstaller -F ' + Filename)
        Savefilepath = str(filedialog.asksaveasfilename(
            title='请选择exe文件存储路径',
            filetypes=[('可执行程序','.exe')],
            initialfile=Filename.replace('py','exe')))
        (Savepath,Savename) = os.path.split(Savefilepath)
        Filepath_new = Folderpath + '/dist/' + Filename.replace('py','exe')
        shutil.move(Filepath_new,Savepath + Filename.replace('py','exe'))
        os.rename(Savepath + Filename.replace('py','exe'),Savefilepath)
        os.remove(Filepath.replace('py','spec'))
        Deletefolder('dist')
        Deletefolder('build')
        Deletefolder('__pycache__')
if __name__ == '__main__':
    main()