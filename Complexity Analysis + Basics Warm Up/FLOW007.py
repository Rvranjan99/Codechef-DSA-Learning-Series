def renum(n):
          rev=0
          while(n>0):
                    rev=(rev*10)+(n%10)
                    n=n//10
          return rev
t=int(input())
for _ in range(t):
          n=int(input())
          a=renum(n)
          print(a)
