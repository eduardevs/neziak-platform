from Models.models import Algorithm, algorithms_dict
new_algo = {
    "name":"Etc2",
    "description": "this is dumb",
    "complexity": "linear_search"
}



print(new_algo['complexity'])

test = algorithms_dict[new_algo['complexity']
                    ]

print(test)