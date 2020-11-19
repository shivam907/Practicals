f=open('/home/shivam/Desktop/practicals/test.txt',"r")
cont=f.read()
print(cont)
v=c=l=u=0
for ch in cont:
    if (ch.islower()):
        l+=1
    elif(ch.isupper()):
        u+=1
    ch=ch.lower()
    if( ch in ['a','e','i','o','u']):
        v+=1
    elif (ch in ['b','c','d','f','g',
                    'h','j','k','l','m',
                    'n','p','q','r','s',
                    't','v','w','x','y','z']):
        c+=1
f.close()
print("Vowels are : ",v)
print("consonants are : ",c)
print("Lower case letters are : ",l)
print("Upper case letters are : ",u)