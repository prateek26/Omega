#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")

import pandas as pd
import cgi
import base64

form= cgi.FieldStorage()

mail=form.getvalue("mail")
v=form.getvalue("value")

h=bytes(v,'utf-8')
k= base64.b64decode (h)
k = k.decode('utf-8')

print(k)

df = pd.read_csv("Book1.csv",index_col=0)
i = df.index
i = i.values[-1] + 1


f = open("Book1.csv","r")
lines= f.readlines()
f.close()

a = lines[-1].split(',')
s = a[-1].replace('x',k)

a[-1]=s
s = ",".join(a)
lines[-1]=s

f = open("Book1.csv","w")
f.writelines(lines)
f.close
print("""<script>window.location='http://localhost/cgi-bin/check2.py?value={0}&mail={1}'</script>""".format(k,mail))
print("done")
