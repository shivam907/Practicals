import pickle
file = open("/home/shivam/Desktop/practicals/code3/stud_data.dat", "rb")
list_of_students = pickle.load(file)
roll_no = int(input("Enter roll no of student to be searched "))
for i in list_of_students:
    if int(i['roll']) == roll_no:
        b=True
        break
    else:
        b=False

if b:
    print('Roll no  {}  is of  {}'.format(roll_no, i['name']))
else:
    print("Roll no {} is Not Present ".format(roll_no))