import os

decivename=os.system("adb devices -l")
print(str(decivename).replace('',','))