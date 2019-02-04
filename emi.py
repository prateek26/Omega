#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")



import pandas
import cgi


form=cgi.FieldStorage()
mail=form.getvalue("mail")


data = pandas.read_csv("")



print("""<html>
        <head>
        <style>
        div{text-align:center}
        </style>
        </head>
        <body>
        <div>
        emi-Status: {0}<br />
        Maximum emi value: {1}<br/>
        Intrest rate: {2} <br/>
        </div>
        </body>
        </html>""".format(status,amt-emi,rate))




