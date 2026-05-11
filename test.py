def details(name : str, weight : float, age : int, married : bool, allergies : list, contact : dict, email : str):
    print(name)
    print(weight)
    print(age)
    print(type(married))
    print(allergies)
    print(contact)
    print(email)


d = {"name" : "Rounak", 'weight' : 74.2, 'age' : 52,'married' : True, 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "rounak@example.com"}

details(**d)