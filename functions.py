from os import path, listdir


class MyDir():
    def __init__(self, diretorio):
        self.diretorio = diretorio
    
    def listing(self):
        try:
            flist = listdir(self.diretorio)
            return flist
        except FileNotFoundError:
            print(f"This directory doesn't exist! Check again")
            
class Files(MyDir):
    def __init__(self, diretorio):
        super().__init__(diretorio)
    
    def check_files(diretorio,flist):
        try:
            myFiles = [f for f in flist if path.isfile(path.join(diretorio,f))]
            return myFiles                
        except:
            pass

