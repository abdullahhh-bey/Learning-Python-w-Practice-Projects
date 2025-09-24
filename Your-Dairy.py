import datetime
import os

def takeInput():
    print("1. Write New Entry")
    print("2. Add an Entry")
    print("3. Read All Entries")
    print("4. Delete Entries")
    print("5. Exit")
    option = int(input("Enter Option Number: "))
    
    match option:
        case 1:
            WriteEntry()
        case 2:
            AddEntry()
        case 3:
            ReadEntry()
        case 4:
            DeleteFile()
        case 5:
            print("Goodbye ...")
            return 
            
            
    

def WriteEntry():
    fileName = input("Enter new Diary name: ")
    if os.path.exists(f"{fileName}.txt"):
        print("file already created")
    else:
        print(f"{fileName} Created")
        
        content = str(input("Write an Entry: "))
        f = open(f"./{fileName}.txt", "wt")
        date = datetime.datetime.now()
        f.write(f"[{date}]  {content}\n")
        
        print("New Entry Created!")
    
    
    
def AddEntry():
    content = str(input("Add an Entry: "))
    
    f = open("./localEntry.txt", "at")
    date = datetime.datetime.now()
    f.write(f"[{date}]  {content}\n")
    
    print("Entry Added!")



def ReadEntry():
    fileName = str(input("Enter filename you want to read: "))
    
    if os.path.exists(f"{fileName}.txt"):
        f = open(f"./{fileName}.txt" , "rt")
        content = f.read()
        print(content)
    else:
        print("No such file in directory")
        
        
        
def DeleteFile():
    file = str(input("Enter file you want to delete: "))
    
    if os.path.exists(f"{file}.txt"):
        os.remove(f"{file}.txt")
        print(f"{file}.txt DELETED")
    else:
        print("No such file in directory")
        
        
        
print("WELCOME TO THE DAILYDO")
takeInput()