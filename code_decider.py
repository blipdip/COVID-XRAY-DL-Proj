import os

def decider_function():
     decider = input('Which model do you want to run(main, AlexNet, Lenet5)\n')

     if decider == "main":
          os.system("CODE.py")
     elif decider == "AlexNet":
          os.system("code_alex.py")
     elif decider == "Lenet5":
          os.system("code_lenet5")
     else:
          print("Input error")
          decider_function()

#print("Installing pre-requisites...\n")
#os.system("pre-req.bat")

decider_function()