import json
Users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(Users)
print(Users["name"])
print(Users["address"])
print(Users["address"]["street"])
print(Users["address"]["geo"]["lng"])

print("\nConvert python dictionary to JSON")
result = json.dumps(Users)
print(result)

print("\nWrite the code and turn into file")
with open("result.json", "w") as file:
    json.dump(Users, file)  # Dump support object such a file
