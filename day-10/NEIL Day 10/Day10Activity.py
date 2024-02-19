import json


name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_food = input("Enter your favorite food: ")


user_data = {
    "name": name,
    "age": age,
    "favorite_food": favorite_food
}


json_data = json.dumps(user_data, indent=4)


with open("output.json", "w") as file:
    file.write(json_data)

print("Data has been saved to 'output.json'.")