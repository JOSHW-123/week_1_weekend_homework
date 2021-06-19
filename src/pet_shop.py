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