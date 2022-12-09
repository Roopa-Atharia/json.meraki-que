# L,R=map(int, input().split())
# while L<=R:
#     if L%2!=0:
#         print(L,end=" ")
#     L+=1

# Find maximum no--
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a<c:
#     print(a)
# elif b<c and b>a:
#     print(b)
# else:
#     print(c)

# Natural sum--
# n=int(input())
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# a=int(input())
# b=int(input())
# c=int(input())
# if (a>b and a<c) or (a<b and a>c):
#     print(a)
# elif (b>a and b<c) or (b<a and b>c):
#     print(b)
# elif (c>b and c<a) or (c<b and c>a):
#     print(c)
# else:
#     print("not")

# Fcatorial--
# n=int(input())
# i=0
# while i<=n:
#     if n%i==0:
#         ptint(i)
#     else:
#         print("not")
#     i=i+1

# N=int(input())
# i=1
# while i<=N:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     i+=1


# N=int(input())
# for i in range(1,N+1):
#     print("*"*i,end=" ")
    

# N=int(input())
# i=1
# c=0
# while i<=N:
#     if N%i==0:
#         print(i)
#     i=i+1

# a=int(input())
# b=[]
# i=0
# while i<a:
#     n=int(input())
#     j=0
#     while j<=n:
#         if n[i]<n[j]:
#             n[i],n[j]=n[j],n[i]
#             b.append(n[i])
#         j+=1
#     i+=1
# print(b)

# N=int(input("enter the number"))
# sum_e=0
# sum_o=0
# i=1
# while i<=N*2:
#     if i%2!=0:
#         sum_o+=i
#     else:
#         sum_e+=i
#     i+=1
# print(sum_o)
# print(sum_e)
    
# a,b,c=map(int, input().split())
# a=int(input())
# b=int(input())
# c=int(input())
# if a+b>c and b+c>a and c+a>b:
#     print("YES")
# else:
#     print("NO")



# N=int(input())
# i=1
# c=0
# for i in range(1,N+1):
#     if N%i==0:
#         c+=1 
# print(c,end=" ")
# for i in range(1,N+1):
#     if N%i==0:
#         print(i,end=" ")
    

# a="my name is tanu"
# # ['my','name','is','tanu']
# b= []
# c=''
# for d in a:
#     if d== ' ':
#         b.append(c)
#         c=''
#     else:
#         c+=d
# if c:
#     b.append(c)

# print(b)

# N=int(input())
# i=1
# while i<=N:
#     print(i)
#     i+=1

# a,b,c=map(int, input().split())
# if a==b and b==c:
#     print("Equilateral")
# elif (a==b and b!=c) or (b==c and b!=a) or (a==c and a!=b):
#     print("Isosceles")
# else:
#     print("Scalene")


# a=int(input("enter the num"))
# b=int(input("enter the num"))
# c=int(input("enter the num"))
# if (a>b and a<c) or (a<b and a>c):
#     print(a)
# elif (b>a and b<c) or (b<a and b>c):
#     print(b)
# elif (c>b and c<a) or (c<b and c>a):
#     print(c)
# else:
#     print("not")
# 
# N=int(input())
# i=1
# b=[]
# while i<=N:
#     k=int(input())
#     b.append(k)
#     i=i+1
# print(b)



# N=int(input())
# i=1
# b=[]
# while i<=N:
#     k=int(input())
#     b.append(k)
#     i=i+1
# j=1
# z=[]
# while j<=len(b):
#     z.append(b[-j])
#     j+=1
# print(z)

# a=[]
# b=int(input())
# for i in range(0,b):
#     n=int(input())
#     a.append(n)
# r=a[::-1]
# print(r)
