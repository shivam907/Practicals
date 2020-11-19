file=open("/home/shivam/Desktop/practicals/code5/file.txt","r")
f1=open("/home/shivam/Desktop/practicals/code5/file_without_A.txt","w")
while True:
    line=file.readline()
    if line=='':
        break
    if 'a' not in line:
        f1.write(line)
file.close()
f1.close()