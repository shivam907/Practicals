import pickle 
def creating_file():
    student_data = {}
    list_of_student = []
    n = int(input("Enter Number of Students "))
    for i in range(0,n):
        student_data['roll']=int(input('Roll no of {} '.format(i+1)))
        student_data['name']=input("Name of {} ".format(i+1))
        list_of_student.append(student_data)
        student_data={}
    file = open("/home/shivam/Desktop/practicals/code3/stud_data.c","wb")
    pickle.dump(list_of_student, file)
    file.close()
def Search_roll():
    file = open("/home/shivam/Desktop/practicals/code3/stud_data.c", "rb")
    list_of_students = pickle.load(file)
    roll_no = int(input("Enter roll no of student to be searched "))
    for i in list_of_students:
        if i['roll'] == roll_no:
            b=True
            break
        else:
            b=False
    if b:
        print('Roll no  {}  is of  {}'.format(roll_no, i['name']))
    else:
        print("Roll no {} is Not Present ".format(roll_no))
creating_file()
Search_roll()