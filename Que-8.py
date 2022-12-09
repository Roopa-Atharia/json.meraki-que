a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
f=["name","designation","age","salary"]
empdetail={}
emp1={}
i=0
while i<len(a):
    emp1.update({f[i]:a[i]})
    i=i+1
emp2={}
i=0
while i<len(b):
    emp2.update({f[i]:b[i]})
    i=i+1
emp3={}
i=0
while i<len(c):
    emp3.update({f[i]:c[i]})
    i=i+1
emp4={}
i=0
while i<len(d):
    emp4.update({f[i]:d[i]})
    i=i+1
empdetail.update({"emp1":emp1})
empdetail.update({"emp2":emp2})
empdetail.update({"emp3":emp3})
empdetail.update({"emp4":emp4})
print(empdetail)

import json

n=open('emp_details.json',"w")
json.dump(empdetail,n,indent=4)
n.close

