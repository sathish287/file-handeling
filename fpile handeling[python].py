print("*********************************")
print("*  file handling  *")
print("*********************************")
import os
import sys
def fi():
  print("1.create file")
  print("2.list file")
  print("3.edit file")
  print("4.delete file")
  print("5.read file")
  print("6.program stoped")
  a=input("enter your choice:")
    match a:
   case"1":
      print("_________________________________________________")
      print("creating file")
      print("_________________________________________________")
      print("enter your file name\n")
      print("_________________________________________________")
      print("enter your file name\n")
      f=input("")
      h=f+".txt"
      with open(h,'x')as file:
      print(f,"files is created sucessfully")
   case"2":
      print("_________________________________________________")
      print("listing file")
      print("_________________________________________________")
      path="D:\python sql connector"
      file=os.listdir(path)
      for file in file:
      print(file)
   case"3":
      print("_________________________________________________")
      print("editing file")
      print("_________________________________________________")
      name+input("enter the file name that you want to edit\n:")
      name=name+".txt"
      file=open(name,"a")
      print(file.write("word"))
      print("edited the file")
   case"4":
      print("_________________________________________________")
      print("deliting file")
      print("_________________________________________________")
      name=input("enter the file name that you want to delete\n:")
      name=name+'.txt"
      os.remove(name)
      print("file",name,"deleted successfully")
   case"5":
      print("_________________________________________________")
      print("reading file")
      print("_________________________________________________")
      print("reading file\n")
      print("...........................")
      print("enter the file name that you want to read\n")
   case"6":
      print("_________________________________________________")
      print("program stopped")
      sys.exit(0)
      print("_________________________________________________")
      while true:
      fi()
      print("**************************************************")
      
