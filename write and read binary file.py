import pickle
def write():
    f=open('myfile.dat','wb')
    lst=['Ram','Shyam','sita','Gita']
    #dict={'Roll':1,'Namr':'Anup'}
    pickle.dump(lst,f)
    f.close()
def readfile():
    f=open('myfile.dat','rb')
    list1=pickle.load(f)
    print(list1)
    f.close()
write()
readfile()
