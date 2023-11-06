start=int(input("Enter starting range for finding factorial:"))
end=int(input("Enter ending range for factorial seq:"))
fact=1
for i in range(start,end+1):
    fact=fact*i
    print(fact,end=",")