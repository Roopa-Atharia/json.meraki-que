# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

a='[{1:2,3:4,5:6,6:7,8:"2+0j","5+0j":9}]'

import json
b=json.loads(a)
print(b)