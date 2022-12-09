# create json file--
import json

a={"name":"Roopa","class":11,"marks":56}
with open("file1.json","w") as b:
    json.dump(a,b)

# import json

# a={"name":"roopa","class":11,"favorite subject":"scien"}
# with open("Roopa_data.json","w") as b:
#     json.dump(a,b)