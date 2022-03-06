vehicles = {
    'Dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bmbardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

vehicles["starfighter"] = "lockheed F-104"
vehicles["learjet"] = "Bombadier Learjet 75"
vehicles["toy"] = "glider"

vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
#del vehicles["f1"]
result = vehicles.pop("f1", "whatever...")
print(result)

# my_car = vehicles['fiesta']
# print(my_car)
#
# learner = vehicles.get("er5")
# print(learner)

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")

