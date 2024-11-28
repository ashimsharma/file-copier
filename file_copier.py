import os

def generate_file_name(f):
    x = f.rstrip(".txt")
    y = f"{x}-Copy.txt"
    if os.path.exists(y) == False:
        z = y
    else:
        i = 1
        while True:
            c = f"{x}-Copy{str(i)}.txt"
            if os.path.exists(c) == False:
                z = c
                break
            else:
                i += 1

    return z
    
def copy_file(fn):
    a = generate_file_name(fn)
    b = open(fn,"r")
    c = b.read()
    d = open(a,"w")
    d.write(c)

    b.close()
    d.close()

    return "File Copied."

def main():
    while(True):
        filen = input("Enter name of the file to be copied: ")
        if(os.path.exists(filen) == True):
            print(copy_file(filen))
        else: 
            print("File does not exist, Try Again.")

if(__name__ == "__main__"):
    main()
