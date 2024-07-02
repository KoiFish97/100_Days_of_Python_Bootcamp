# Nesting

# Look at it like a folder in a folder

# Normal Dictionary
# {Key: Value}

# List Inside Dictionary
# {Key: [List]}

# Dictionary Inside Dictionary
# {Key: {Dictionary}}

# Both Dictionary and List
# {
    # Key1: [List],
    # Key2: {Dictionary},
# }

# Nesting Dictionaries Inside Lists
# [{
    # Key1: [List],
    # Key2: {Dictionary},
# }, End Index 1
# {  Start Index 2
    # Key1: Value,
    # Key2: Value,
# }]

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List Inside a Dictionary in a Dictionary
# travel_log = {
    # "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    # "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
# }

# Nesting Dictionary Inside a List
travel_log = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 12
    },
]
