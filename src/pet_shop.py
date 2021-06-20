# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop ["admin"]["total_cash"]

# def add_or_remove_cash(pet_shop, number):
#     amount = pet_shop["admin"]["total_cash"]
#     sum_amount = amount + number
#     pet_shop["admin"]["total_cash"] = sum_amount
#     return pet_shop ["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop 

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, extra_pets):
    pet_shop["admin"]["pets_sold"] =+ extra_pets
    return pet_shop["admin"]["pets_sold"] 

def get_stock_count(pet_shop):
    return len(pet_shop ["pets"])

def get_pets_by_breed(var_input, breed):
    breed_count = []
    for pet in var_input["pets"]:
        if pet ["breed"] == breed:
            breed_count.append(breed)
    return breed_count

def get_pets_by_breed(var_input, breed):
    breed_count = []
    for pet in var_input["pets"]:
        if pet ["breed"] == breed:
            breed_count.append(breed)
    return breed_count

def find_pet_by_name( pet_shop_stock, name):
    list_of_pets = pet_shop_stock["pets"]
    result = None
    for pet in list_of_pets:
        if pet["name"] == name:
            result = pet
    return result





        



