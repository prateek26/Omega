#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe


print("content-type:text/html")
print("\n")


import cgi
import pybase64
import base64

data = []
l = ['a','b','c','d','e','f','g','h']
enc_l= []

form=cgi.FieldStorage()
email=form.getvalue("value")


for i in l:
    q=bytes(i,'utf-8')
    value=base64.b64encode(q)
    h=value.decode('utf-8')
    enc_l.append(h)


    
for i in range(8):
    image = pybase64.b64encode(open('/Apache24/htdocs/cartoon/'+l[i]+'.png', 'rb').read()).decode('utf-8').replace('\n', '')
    img_tag = '<img name={0} src="data:image/png;base64,{1}" >'.format(l[i],image)
    data.append(img_tag)

print("""
<html>
<head>
<style>
.image{
width:100px
height:100px

}
</style>
<title>Security Page</title>
<style>

</style>
</head>
<body>
<form action>
<h1 style="background-color:#ccc">Select An Image</h1>
<table>
""")
for i in range(4):
    print("""
	<tr><td><a href="http://localhost/cgi-bin/imagestore.py?value={2}&mail={4}">{0}</a></td>
	<td><a href="http://localhost/cgi-bin/imagestore.py?value={3}&mail={4}">{1}</a></td>
	</tr>
	""".format(data[i],data[i+4],enc_l[i],enc_l[i+4],email))
print("""
</table>
</form>
</body>
</html>
""")


