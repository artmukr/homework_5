cities = ['Kyiv', 'Lviv', "Dnipro", 'London', 'Bila Tserkva']
city = input('Enter your town :')
if not city in cities:
    print("not found")

for index, town in enumerate(cities):
    if town == city and index % 2 == 0:
        print("It`s all good")
        break
    elif town == city and index % 2 != 0:
        del cities[index]
        print(cities)
        break





