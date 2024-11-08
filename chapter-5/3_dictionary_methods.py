
a ={
    "name":"harry",
    "from":"india",
    "marks":[92,98,96]
}

# *items method
print(a.items())

# *keys method
print(a.keys())

# *values method
print(a.values())

# *update method
a.update({"name": "Abu Bokor", "from": "Bangladesh"})

print(a)

# *get method
print(a.get('name'))

# ! differences between a["name"] and a.get("name");

# if there is no data :
# a["name"] : return error;
# a.get("name") : return None;
