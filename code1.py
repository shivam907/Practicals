file=open('/home/shivam/Desktop/practicals/test.txt',"r")

doc=file.readlines()
# print(type(doc),"   ", doc)

for i in doc:
    words=i.split()
    for a in words:
        print(a+"#",end='')
file.close()