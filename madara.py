import os
import shutil
path = "C:\\Users\\Pulkit\\Downloads\\C111\\badminton.gif"
name,extension = os.path.splitext(path)
print(name)
print(extension)
source = "C:\\Users\\Pulkit\\Downloads\\C111\\badminton.gif"
desination = "C:\\Users\\Pulkit\\Downloads\\C111\\badminton_copy.gif"
shutil.copy(source,desination)
print(os.listdir("C:\\Users\\Pulkit\\Downloads\\C111"))

