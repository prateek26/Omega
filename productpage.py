#!C:\Users\LUcifer\AppData\Local\Programs\Python\Python37-32\python.exe


print("content-type:text/html")
print("\n")


print("""

<html>
<head><title>Products</title>
<style>
h1{background-color:lightblue;
   padding:15px;}

img{width:120px;
	height:120px;
	border-radius:30%;
	padding:3px;
	border:4px solid lightblue;}

p{color:green;
	font-style:italic;}
	
a{color:Black;}
	
ul{list-style-type:square;
	   color:purple;}
h3{width:20%;}

.gallery{
	font-size:25px;
	text-align:left;
	width:180px;
	float:left;
	margin:15px;}	   

background-color:#f4e292	
</style>
</head>
<body>
<h1>Products</h1>
<div class="gallery">
  <a target="_blank" href="watch.html"><img src="watch.jpg"/></a>
  <div class="desc">Watch</div>
</div>

<div class="gallery">
  <a target="_blank" href="shoes.html"><img src="shoes.png"/></a>
  <div class="desc">Shoes</div>
</div>

<div class="gallery">
  <a target="_blank" href="earphones.html"><img src="earphones.jpg"/></a>
  <div class="desc">Earphones</div>
</div>

<div class="gallery">
  <a target="_blank" href="pendrive.html"><img src="pendrive.png"/></a>
  <div class="desc">Pendrive</div>
</div>

<div class="gallery">
  <a target="_blank" href="mobile.html"><img src="mobile.jpg"/></a>
  <div class="desc">Mobile</div>
</div>

<div class="gallery">
  <a target="_blank" href="laptop.html"><img src="laptop.jpg"/></a>
  <div class="desc">Laptop</div>
</div>
</body>
</html>





""")
