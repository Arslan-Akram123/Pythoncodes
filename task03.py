print("**********************check the person is child young or senior*****************************");

age=int(input("enter the age of person:"));

if(age<18):
    print(age);
    print("person is child");
elif age>=18 and age<=45:
     print(age);
     print("person is young");
else:
    print(age);
    print("person is senior");
   

