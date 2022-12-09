# Q4.Python dictionary(sort by key) object ko json data mai convert karne ka program likho?

a={1:5,5:4,8:3,7:2}

import json
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)