# cook your dish here
t=int(input())
for _ in range(t):
          n=int(input())
          s=list(map(int,input().split()))
          c=1 
          i=1
          j=0
          while(i<n):
                    if s[j]>s[i]:
                              c+=1
                              
                    else:
                              s[i]=s[j]
                    i+=1
                    j+=1 
                    
                              
                    
          print(c) 
          
