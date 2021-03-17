#prime no
n=int(input("enter number"))
for k in range(2,n):
      if n%k==0:
            print("not prime")
            break
else:
      print("prime")
