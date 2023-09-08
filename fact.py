num=int(input("Enter the number n: "))
factorial=1
if num<0:
    print("enter valid digit")
elif num==0 :
    print("okay")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print(factorial)