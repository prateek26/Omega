#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")



import pandas
import cgi


form=cgi.FieldStorage()
mail=form.getvalue("mail")

data=pandas.read_csv("result.csv")
d = data[data['customer_email']==mail]
amount = d['loan_amount'].values
amount = amount[-1]
interest = d['interest'].values
interest = interest[-1]


print("""<html>
        <body>
        <div>
        Maximum amount of Credit: {0}<br/>
        Interest: {1}%<br />
        </div>
        </body>
        </html>
        """.format(amount,interest))


