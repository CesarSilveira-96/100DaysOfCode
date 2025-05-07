# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print (travel_log["France"][1])

# Lista dentro de lista (Nested)
nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1]) #D


travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },

    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}

print(travel_log["Germany"]["cities_visited"][0])

