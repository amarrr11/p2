import pickle
def write():
    f=open("myfile.dat","wb")
    record=[]
    while True:
        roll=int(input("enter roll"))
        name=input("enter name")
        marks=int(input("enter marks"))
        list1=[roll,name,marks]
        record.append(list1)
        choice=input("enter more records(y/n)?")
        if choice=='n':
            break
    pickle.dump(record,f)
    print("data saved successfully")
def read():
    f=open("myfile.dat","rb")
    r=pickle.load(f)
    for i in r:
        print (i)
def search():
    f=open("myfile.dat","rb")
    rollno=int(input("enter roll to find"))
    flag=0
    r=pickle.load(f)
    for i in r:
        if i[0]==rollno:
            print(i)
            flag=1
            break
    if flag==0:
        print("element not found")
write()
read()
search()
