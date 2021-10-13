#using loop to transfer to list or tuple /
real_password = []
password = "iampeter"

for letter in password:
    real_password += letter
print(real_password)

#change the position of text
def encrypt(password, shift):
    new_password = ""
    for letter in password:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_password += new_letter

#add text to dict
def add_country(country_visited, times_visited, cities_visited):
    country = {}
    country["country"] = country_visited
    country["visits"] = times_visited
    country["cities"] = cities_visited
    travel_log.append(country)

add_country("Russia", 2, ["Moscow","St. peter"])
print(travel_log)