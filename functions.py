from os import path, listdir


class MyDir():
    def __init__(self, diretorio):
        self.diretorio = diretorio
    
    def listing(self):
        try:
            flist = listdir(self.diretorio)
            return flist
        except FileNotFoundError:
            print(f"[ERROR] This directory doesn't exist! Check again")
            
class Files(MyDir):
    def __init__(self, diretorio):
        super().__init__(diretorio)
    
    def check_files(self):
        try:
            files = MyDir(self.diretorio).listing()
            myFiles = [f for f in files if path.isfile(path.join(self.diretorio,f))]
            return myFiles                
        except FileNotFoundError:
            print(f"[ERROR] {files} is not valid! Try again!")
            
    def check_dir(self):
        try:
            dirs = MyDir(self.diretorio).listing()
            subDir = [d for d in dirs if path.isdir(path.join(self.diretorio,d))]
            return subDir
        except FileNotFoundError:
            print(f"[ERROR]{dirs} is not valid!Try Again!")



print(Files(".").check_dir())