print("please enter the 6 numbers one by one") ;

number=[];

for i in range(1,7):
    num=int(input(f"enter the number {i} :"));
    number.append(num);
        
def sum_numbers(number):
    sums=sum(number);
    print("sum of number is:",sums);
    
def avrage_numbers(number):
    avrages=sum(number)/len(number);
    print("avrage of number is:",avrages);

sum_numbers(number);
avrage_numbers(number);

