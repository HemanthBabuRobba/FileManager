import os

def newfile():
    try:
        name = input("\n\t Enter File Name : ")+".txt"
        if os.path.isfile(name):
            print("\nThis file already exists")
        else:
            f = open(name,"w")
            f.write("Empty File...")
            print("File is Successfully Created")
            f.close()
    except:
        print("File is Failed to Created")

def openfile():
    for j,i in enumerate(record):
        print("\n\t ",j+1,". ",i)
    try:
        select = int(input("\n\t Enter S.no of File to be Open : "))
        insidefile(record[select-1])
    except:
        print("\n     Invalid Number...")

def insidefile(name):
    print("\n     File Name : ",name)
    option = ["1. Add Point","2. Clear All","3. Clear All and Add Point ","4. Rename the File","5. Show File"]
    print("\n----------------------------------------------------")
    for i in option:
        print("\n\t",i)
    print("\n----------------------------------------------------")
    choice = input("\n     Enter above Option : ")
    if choice == '1':
        print("\n   Enter the Line : ",end=" ")
        line = ""
        while True:
             x = input()
             line = line+" "+x
             if "." not in x:
                 break
        f = open(name,"a")
        f.write(line)
        print("\n     Points Added...")
        f.close()
    elif choice == '2':
        f = open(name,"w")
        f.write("Empty File...")
        print("\n     All Cleared...")
        f.close()
    elif choice == '3':
        print("\n    Enter the Line : ",end = ' ')
        line = ""
        while True:
            x = input()
            line = line+" "+x
            if "." not in x:
                break
        f = open(name,'w')
        f.write(line)
        print("\n     Points Added...")
        f.close()
    elif choice == '4':
        name1 = input("\n\t Enter New Name : ")+".txt"
        if name1 not in record:
            try:
                os.rename(name,name1)
                index = record.index(name)
                record[index] = name1
                print("\n     File Renamed Successfully")
            except:
                print("\n     File Renaming is Failed...")
        else:
            print("\n     This Filename is already exists...")
    elif choice == '5':
        try:
            f = open(name,'r')
            contents = f.read()
            print("\n\t\t ----------     X      ------------      X     --------------")
            contents = contents.split('.')
            for i in range(len(contents)-1):
                print("\n\t   ",contents[i],".")
            print("\n\t\t ----------     X      ------------      X     --------------")
            f.close()
        except:
            print("\n     Unable to Reade the File...")
    else:
        print("\n     Invalid Option")
    
def delfile():
    print("\n\tFiles : ")
    for j,i in enumerate(record):
        print("\n\t",j+1,". ",i)

    select = int(input("\n\t Enter S.no to Delete the File : "))
    name = record[select-1]
    try:
        os.remove(name)
        print("\n     File Deleted Successfully...")
    except:
        print("\n     File Deleted Unsuccessfully...")
record = []
files = os.listdir(os.getcwd())
for i in files:
    if ".txt" in i:
        record.append(i)
options = ["1. New File","2. Open File","3. Delete File","4. Quit"]
print("\n----------------------------------------------------")
for i in options:
    print("\n\t",i)
print("\n----------------------------------------------------")
while True:
    choice = input("\n Choose Option : ")
    if choice == '1':
        newfile()
    elif choice == '2':
        openfile()
    elif choice == '3':
        delfile()
    elif choice == '4':
        quit()
    else:
        print("\n\t Invalid Option")
