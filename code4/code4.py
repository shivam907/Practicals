import pickle
file=open("stud_data.dat","wb")
dic={}
n=int(input("Enter No of Students "))
for k in range(n):
    roll_no=int(input("Enter Roll no "))
    name=input("Enter Name ")
    mark=int(input("Enter Marks "))
    dic[roll_no]={}
    dic[roll_no]["Name"]=name
    dic[roll_no]["Marks"]=mark
pickle.dump(dic, file)
file.close()
file=open("stud_data.dat","rb+")
d=pickle.load(file)
rollno=int(input("Enter Roll To Update Marks  "))
for k in d:
    if k==rollno:
        m=int(input("Enter Marks "))
        d[k]["Marks"]=m
        print(d)
pickle.dump(d, file)
file.close()