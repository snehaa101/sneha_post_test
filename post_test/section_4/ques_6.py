# CREATE A LIST OF 8 CITY NAMES
cities = ["mumbai", "paris", "london", "tokyo", "seoul", "la", "bhopal", "busan"]

# PRINT FIRST 4 CITIES
print("First 4 cities : ", cities[:4])

# PRINT LAST 4 CITIES
print("First 4 cities : ", cities[-4:])

# ADD NEW CITY
cities.append("ney york")

# REMOVE A CITY
cities.pop(0)

# CONVERT LIST TO TUPLE
city_tuple = tuple(cities)
print("tuple : ", city_tuple)
