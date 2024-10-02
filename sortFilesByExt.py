import os
import shutil
import datetime

#list files from Dir and get extension
def filesInDir(my_dir:str):
    onlyFiles = [f for f in os.listdir(my_dir) if os.path.isfile(os.path.join(my_dir,f))]
    return(onlyFiles)

def getExt(my_dir:str):
    fileExt = []
    for i in filesInDir(my_dir):
        ext = os.path.splitext(i)
        fileExt.append(ext[1])
        print(ext[1])
    return(fileExt)

def scheduleTask():
    file = open(r'd:\Users\Murilo\Documents\MURILO\sortFiles\schedule.txt', 'a')
    file.write(f'The script ran at {datetime.datetime.now()} \n')
    
#sort files and move for respective folders
def moveFiles(my_dir:str):
    extensions = getExt(my_dir)
    files = filesInDir(my_dir)
    for c in files: 
        oldPath = os.path.join(my_dir,c)
        print(oldPath)
        for x in extensions:
            if x != '.part' and not os.path.exists(os.path.join(my_dir,x)): #check if folder already exists
                os.makedirs(os.path.join(my_dir,x))
                print(f"The folder {x} has been created succesfully")
            newPath = os.path.join(my_dir,x,c)
            if x != '.part' and x in c and not os.path.exists(os.path.join(newPath)): #check if files not in folder
                print(newPath)
                shutil.move(oldPath, newPath)
                print("Files has been moved succesfuly!")


    
    
scheduleTask()
moveFiles("D:/Users/Murilo/Downloads")