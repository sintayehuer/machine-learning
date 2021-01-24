Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> def write_to_file(filename, data)
op.open(filename, 'a')
op.write(data+"\t")
op.close()
op=open("multiplication.txt",'a')
for num in range(0,11):
    text=str(num)+"\t" + str(pow(num,2))+"\t" + str(pow(num,3))+"\t" + str (pow(num,4))
    write_to_file("mult.txt", text)
    read=open("mult.txt",'r')
   # print(rd.read())