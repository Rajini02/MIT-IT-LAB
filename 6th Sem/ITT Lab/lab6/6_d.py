body = open("/Users/PRANAV/Desktop/VI sem/ITT lab/lab6/body.txt", "r+")
name = open("/Users/PRANAV/Desktop/VI sem/ITT lab/lab6/names.txt", "r+")
bdy = body.read()
#print(bdy)
for nam in name:
  #print(nam)
  mail  = "Hello " + nam.strip() + "\n" + bdy
  print(mail)
  wri = open("/Users/PRANAV/Desktop/VI sem/ITT lab/lab6/"+ nam.strip()+".txt", "w")
  wri.write(mail)