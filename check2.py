#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe


print("content-type:text/html")
#print("Content-Type: image/png")
print("\n")

import cgi
import pandas as pd

form =  cgi.FieldStorage()

i = form.getvalue("value")
mail=form.getvalue("mail")

df = pd.read_csv("Book1.csv",index_col=0)
k = df[df['email']==mail]
k = k['image']
t = k.values
t=t[-1]
#print(k['image'],type(k['image']))
if(t==i):
   print("""<script>window.location='http://localhost/cgi-bin/home.py?mail={0}'</script>""".format(mail))
else:
    print("""<script>window.location='http://localhost/homepage.html'</script>""")


