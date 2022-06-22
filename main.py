
file_name = "Reciepts"
def catalog_reader(file_name):
    cook_book = {}
    dish_ingridient = []
    with open(file_name, 'r', encoding='cp1251') as file:
        for dish in file:
            dish = dish.strip()
            list_ingridients = []
            number_ingridiets = file.readline()
            for item in range(int(number_ingridiets)):
                line_ingridient = file.readline()
                list_ingridient_dish = (line_ingridient.strip()).split(" | ")
                dec_ingridient = {}
                dec_ingridient = {'ingredient_name': list_ingridient_dish[0], 'quantity': list_ingridient_dish[1], 'measure': list_ingridient_dish[2]}
                list_ingridients.append(dec_ingridient)
            file.readline()
            cook_book[dish] = list_ingridients
    return cook_book
cook_book = catalog_reader(file_name)

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        list_ingridients = cook_book[dish]
        for dec_ingridient in list_ingridients:
            ingridient = dec_ingridient['ingredient_name']
            if ingridient in  list_by_dishes:
                dec_ingridient_by_shop = list_by_dishes[ingridient]
                new_ammont_ingridient = 0
                old_ammount_ingridient = 0
                old_ammount_ingridient = dec_ingridient_by_shop['quantity']
                new_ammont_ingridient = str(int(old_ammount_ingridient) + int(dec_ingridient['quantity'])* person_count)
                list_by_dishes[ingridient]={'quantity':new_ammont_ingridient, 'measure' : dec_ingridient['measure']}
            else:
                list_by_dishes[ingridient] = {'quantity':dec_ingridient['quantity'], 'measure' : dec_ingridient['measure']}
    return  list_by_dishes

dishes = ["Омлет", "Омлет", "Фахитос"]
list_by_dishes = get_shop_list_by_dishes(dishes, 2)
print(list_by_dishes)
