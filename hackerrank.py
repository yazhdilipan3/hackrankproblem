
n = int(input("enter the number:"))

if n%2!=0:
    print("weird")
elif n%2==0 and 2<=n<=5:
    print("not weird")
elif n%2==0 and 6<=n<=20:
    print("weird")
else :
    print("not weird")
    
n = int(input("Enter the number:"))
arr = list(map(int,input().strip().split(",")))

arr.sort()

n = int(input("Enter the students:"))
m = [] 
for s in range(0,n+1):
    name = input()
    score =float(input())
    name.append(m)
    score.append(m)

print(m)
