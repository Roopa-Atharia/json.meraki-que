# Q.3 Python object ko json string mai convert karne ka program likho?

a={
    "name": "David", 
    "class": "I", 
    "age": 6
}

import json
b=json.dumps(a)
print(b)
print(type(b))