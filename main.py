file_name = "Recieps"
def catalog_reader(file_name):
    cook_book = {}
    dish_ingridient = []
    with open(file_name) as file:
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
            fake = file.readline()
            cook_book[dish] = list_ingridients
    return cook_book
cook_book = catalog_reader(file_name)
dishes = ["Омлет", "Утка по-пекински", "Фахитос"]
def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        list_ingridients = cook_book[dish]
        for dec_ingridient in list_ingridients:
            if dec_ingridient['ingredient_name'] in  list_by_dishes :
                list_by_dishes[dec_ingridient['ingredient_name']] =


        input()



#         for list_ingridient in cook_book[dish]:
#             # Список словарей ингридиентов
#             for ingridient in list_ingridient:
#                 # словарь ингридиента
#                 print(ingridient)
#                 list_by_ingridients = {name_ingridient: }
#
get_shop_list_by_dishes(dishes, 2)

    # {
    #     'Картофель': {'measure': 'кг', 'quantity': 2},
    #     'Молоко': {'measure': 'мл', 'quantity': 200},
    #     'Помидор': {'measure': 'шт', 'quantity': 4},
    #     'Сыр гауда': {'measure': 'г', 'quantity': 200},
    #     'Яйцо': {'measure': 'шт', 'quantity': 4},
    #     'Чеснок': {'measure': 'зубч', 'quantity': 6}
    # }