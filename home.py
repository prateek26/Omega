#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")


import cgi
import pandas


form=cgi.FieldStorage()
mail=form.getvalue("mail")

print("Proceed to : ")
print("""<html>
        
        <body>
        <div>
        <a href="http://localhost/productpage.html?">product page</a><br/>
        <a href="scorecard.py?mail={0}">score profile</a><br/>
        </div>
        </body>
        </html>
        """.format(mail))

        
