# print(2+3);
# print(4-3);
# print(2*3);
# print(5/3);
# print(3**2);
# print(5//2);
# a="we are starting python";

# print(a[0:7]);
# b=input("enter the value")
# print(type(b));
# name="arslan","ans";
# print(name);
# num1 = input("enter the number 1:")
# num2 = input("enter the number 2:")
# num1=int(num1);
# num2=int(num2);

# print(num1+num2);
# numbers=[];
# for i in range(6):
#      print("enter the number",(i+1));
#      num=input();
#      numbers.append(num);
# print(numbers);   
print("enter the 6 numbers one by one");
numbers=[];
for i in range(6):
    print("enter the number",i+1,":")
    num=int(input());
    numbers.append(num);
print(numbers);
def sum_fun(numbers):
    sums=sum(numbers);
    print("sum of numbers is:",sums);
def avrage_fun(numbers):
    avrage=sum(numbers)/len(numbers);
    print("avrage of number is:",avrage);
    
sum_fun(numbers);
avrage_fun(numbers);