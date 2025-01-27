import pickle

import os

def idcard():
    
    name=input("enter name")
    admissionnumber=int(input("enter admission number"))
    Class=int(input("enter class"))
    section=input("enter secton")
    blood_group=input("enter blood group")
    dob=input("enter date of birth (DD/MM/YYYY)")
    father_name=input("enter father name")
    mother_name=input("enter mother name")
    contact_number=int(input("enter contact number"))
    idcard=[name,admissionnumber,Class,section,blood_group,dob,father_name,mother_name,contact_number]
    
    f=open("identitycard.dat",'ab') #opening a binary file in append mode
    pickle.dump(idcard,f)
    f.close()





def displaydetails():
    with open("identitycard.dat",'rb') as f:
        while True:
            try:
                rec=pickle.load(f)
                print("Name",rec[0])
                print("Admission number",rec[1])
                print("Class",rec[2])
                print("section",rec[3])
                print("blood group",rec[4])
                print("dob",rec[5])
                print("father name",rec[6])
                print("mother name",rec[7])
                print("contact number",rec[8])
                print("")
               
            except EOFError:
                break

def searchdetails(admissionnumber):
    f=open("identitycard.dat",'rb')
    flag=False
    while True:
     try:
         rec=pickle.load(f)
         if admissionnumber==rec[1]:
                print("Name",rec[0])
                print("Class",rec[2])
                print("section",rec[3])
                print("blood group",rec[4])
                print("dob",rec[5])
                print("father name",rec[6])
                print("mother name",rec[7])
                print("contact number",rec[8])
            
                flag=True
     except EOFError:
         break
    
    if flag==False:
        print("No Records found")
    f.close()


def deletedetails(admissionnumber):#adharno  should be entered by the user
    f=open("identitycard.dat",'rb')
    f1=open("temp.dat",'wb')
    found=False
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==admissionnumber:
                found=True
            else:
                pickle.dump(rec,f1)
        except EOFError:
            break
    f.close()
    f1.close()
    print("record deleted successfully")
    os.remove("identitycard.dat")
    os.rename("Temp.dat","identitycard.dat")



#main function
            
ch=0

while (ch!=4):

   print("")
   print("1.To add records ")
   print("2.To view records ")
   print("3.To delete records")
   print("4.To display all records")
   print("5.Exit")
   print("")
   choice=int(input("enter choice (1/2/3/4/5)"))
   if choice==1:
       idcard()
       print("")
       
   elif choice==2:
        admissionnumber=int(input("enter admission number"))
        searchdetails(admissionnumber)
        print("")

   elif choice==3:
       admissionnumber=int(input("enter admission number"))
       deletedetails(admissionnumber)
       print("")
       
   elif choice==4:
       displaydetails()

   elif choice==5:
       break
    
    
        
   else:
        print("Enter valid choice:")
        print("")
    

   

    




    


