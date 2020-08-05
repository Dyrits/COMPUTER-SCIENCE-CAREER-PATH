from datetime import time


class Menu():
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} | Available from {self.start_time.isoformat('minutes')} to {self.end_time.isoformat('minutes')}!"

    def calculate_bill(self, purchased_items):
        return sum(self.items[purchased_item] for purchased_item in purchased_items)


brunch = Menu("Brunch", {'pancakes': 7.50,
                         'waffles': 9.00,
                         'burger': 11.00,
                         'home fries': 4.50,
                         'coffee': 1.50,
                         'espresso': 3.00,
                         'tea': 1.00,
                         'mimosa': 10.50,
                         'orange juice': 3.50
                         }, time(11), time(16))

early_bird = Menu("Early Bird", {'salumeria plate': 8.00,
                                 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00,
                                 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50,
                                 'coffee': 1.50,
                                 'espresso': 3.00, }, time(15), time(18))

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00,
                         'ceaser salad': 16.00,
                         'pizza with quattro formaggi': 11.00,
                         'duck ragu': 19.50,
                         'mushroom ravioli (vegan)': 13.50,
                         'coffee': 2.00, 'espresso': 3.00, }, time(17), time(23))

kids = Menu("Kids", {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00,
                     'apple juice': 3.00}, time(11), time(21))

# print(kids)
# print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
# print(early_bird.calculate_bill(
#     ["salumeria plate", "mushroom ravioli (vegan)"]))


class Franchise():
    def __init__(self, adress, menus):
        self.adress = adress
        self.menus = menus

    def __repr__(self):
        return self.adress

    def available_menus(self, time):
        return [menu for menu in self.menus if menu.start_time < time < menu.end_time]


flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [
                            brunch, early_bird, dinner, kids])

# print(flagship_store.available_menus(time(12)))
# print(flagship_store.available_menus(time(17)))


class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


basta_fazoolin_wmh = Business("Basta Fazoolin' with my Heart", [
                              flagship_store, new_installment])

arepas_menu = Menu("Take a'Areapa", {'arepa pabellon': 7.00,
                                     'pernil arepa': 8.50,
                                     'guayanes arepa': 8.00,
                                     'jamon arepa': 7.50
                                     }, time(10), time(20))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

take_a_arepa = Business("Take a' Arepa", [arepas_place])