#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe

print("content-type:text/html")
print("\n")


import pandas as pd
import cgi

form=cgi.FieldStorage()
mail=form.getvalue("mail")

data=pd.read_csv("result.csv")

d = data[data['customer_email']==mail]
credit_score=d['total_score'].values
credit_score= credit_score[-1]

kyc = d['kyc'].values
kyc = kyc[-1]

print("""<html>
        <head>

        </head>
        <body>
        <head><br>Score Card</head>
        <div>
        User credit score:  {0}<br/>
        """.format(credit_score))
if(kyc==1):
    print("""
        KYC COMPLETED!<br>
        Benefits:<br />
        <a href="credit.py?mail={0}">APPLY FOR LOAN</a>
        """.format(mail))
else:
    print("""KYC NOT COMPLETED""")
    
print("""</div>
        </body>
        </html>
        """)
if(credit_score>=75):
    print("You can make all type of Payments")
elif(credit_score>=50):
    print("You can make Payment Only By Debit/Credit and EMI Mode")
else:
    print("You can make only Debit/Credit Payment.")


        



