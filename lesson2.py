# set collection
# sets = set()
# print(type(sets))
# proffesion = {"backend", "backend", 12, (1, 2)}

# for i in proffesion:
#     print(i)
# print(proffesion)
# list_set = tuple(proffesion)
# print(list_set)

# list_setcities = {"Tokyo", "Bishkek", "Baku", "Karakol"}
# towns = {"Naryn", "Jalal-Abad", "Balukchy", "Batken"}
# towns.update(("nazgul",))
# print(towns)
# # # union, update
# v = cities.add("Tokyoo")
# cities.clear()
# a = cities.copy()
# cities.discard("Tokyoo")
# cities.remove("Bakuo")
# print(cities)

# cities = {"Tokyo", "Bishkek", "Baku", "Karakol"}
# towns = {"Naryn", "Jalal-Abad", "Balukchy", "Batken"}
# union, update
# a = cities.union(towns)
# cities.update({1: 5, 8: 9, }.items())
# print(city_town)
# print(cities)
# print(towns)

# cities = {"Tokyo", "Bishkek", "Baku", "Karakol"}
# towns = {"Tokyo", "Naryn", "Jalal-Abad", "Balukchy", "Batken"}
# # pop_element = cities.pop()
# inter = cities.intersection(towns)
# print(inter)
# cities.update(("fnkjehkjekre",[]))
# print(cities)
# print(cities.symmetric_difference(towns))
# towns.symmetric_difference_update(cities)
# print(towns.symmetric_difference_update(cities))
# print(cities)
# print(pop_element)

# cities = {"Tokyo", "Naryn",  "Bishkek", "Baku", "Karakol", "Batken"}
# towns = {"Naryna", "Batkena"}
# print(cities.issubset(towns))
# print(cities.issuperset(towns))
# print(cities.isdisjoint(towns))
# collections

student = {
    "name": "Nazgul",
    "age": 18,
    "year": None,
    "subjects": {
        "math": (80, 47, 68, 100),
        "python": (67, 88, 97, 82),
        "html": (67, 80, 97, 88),
        "css": (67, 88, 91, 88),
    },
    "total": None
}
student = {
    "name": "Nazgul",
    "age": 18,
    "year": 2004,
    "subjects": {
        "math": 80,
        "python": 76,
        "html": 88,
        "css": 90,
    },
    "total": 87
}