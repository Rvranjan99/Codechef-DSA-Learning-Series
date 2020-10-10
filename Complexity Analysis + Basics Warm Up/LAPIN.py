# cook your dish here
t=int(input())
for _ in range(t):
          x=input()
          n=len(x)
          m=n//2
          if(n%2==0):
                    
                    if sorted(x[:m])==sorted(x[m:]):
                              print('YES')
                    else:
                              print('NO')
          else:
                    
                    if sorted(x[:m])==sorted(x[m+1:]):
                              print('YES')
                    else:
                              print('NO')
          
