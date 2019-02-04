#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")

import os
import pandas as pd
import cgi
from flask import Flask,redirect

form=cgi.FieldStorage()

df = pd.read_csv("Book1.csv",index_col=0)

d=dict(df)
for i in d.keys():
    d[i]=list(d[i])

if ("mail" and "pas") in form:
        firstname=form.getvalue("firstname")
        lastname=form.getvalue("lastname")
        email=form.getvalue("mail")
        password=form.getvalue("pas")
        #firstname = "amba"
        #lastname = "aljdf"
        #email = "af@gmail.com"
        #password = "af"
        d = []
        k = df.index
        k = 6+1
        d.append(str(k))
        d.append(firstname)
        d.append(lastname)
        d.append(email)
        d.append(password)
        d.append('x')

        s = ','.join(d)
        s = '\n'+s
        with open("Book1.csv","a") as f:
            f.writelines(s)
            
        print(d)
        
        print(""" wait redirecting you!!!
               """)
       
        print("""<script>window.location='http://localhost/cgi-bin/imageprivacy.py'</script>""")
        
elif ("email" and "pass")  in form:

        email = form.getvalue("email")
        password = form.getvalue("pass")

        if(email in d['email']):
            if(password in d['password']):
                
                print(""" wait redirecting you!!!
                   """)
                print("""<script>window.location='http://localhost/cgi-bin/imageprivacy.py?value={}'</script>""".format(email))
            else:
                print("Retype Password")
                print("""<script>window.location='http://localhost/homepage.html'</script>""")
        else:
            print("Accoutn not found")
            print("""<script>window.location='http://localhost/homepage.html'</script>""")
      


else:
        print("hi")
       
        print("""<script>window.location='http://localhost/homepage.html'</script>""")




