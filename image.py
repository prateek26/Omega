#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

import sys
import os

src =  "a1.png"

print("Content-Type: image/png")
print("Content-Length: " + str(os.stat(src).st_size))
print("\n")
sys.stdout.flush()
sys.stdout.buffer.write(open(src, "rb").read())
