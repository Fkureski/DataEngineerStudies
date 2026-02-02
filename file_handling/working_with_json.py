import json

""" with open ('anscombe.json', mode = "r") as file:
    data = json.load(file)
    print(data) """

data = {'Name': 'Alice',
        'Age': 22,
        'City': 'New York'}

with open ('output2.json', mode = "w") as file:
    json.dump(data, file)
    