class Recipes:
    def __init__(self, recipe_name):
        self.recipe_name = recipe_name

    def lets_start(self):
        print("\nRecipe Name:", self.recipe_name)

    def open_the_cooker(self):
        print("Open the cooker.")

    def salt(self):
        print("Sprinkle Salt.")

    def put_the_cooker(self):
        print("Put It on the Cooker.")

    def add_water(self):
        print("Add Water in the Saucepan.")

    def heat_balance(self):
        print("Lower The Heat.")

    def finish(self):
        print("Enjoy Your Meal.")

    def start(self):
        pass


class RiceRecipe(Recipes):
    def __init(self, recipe_name):
        super().__init__(recipe_name)

    def prepare_rices(self):
        print("Put Your Rices in Water and Wait 30 Minutes.")

    def filter_rices(self):
        print("Filter Your Rice.")

    def blight(self):
        print("Blight the Rice.")

    def rest(self):
        print("Rest Your Rice.")

    def start(self):
        self.lets_start()
        self.prepare_rices()
        self.filter_rices()
        self.open_the_cooker()
        self.put_the_cooker()
        self.add_water()
        self.blight()
        self.heat_balance()
        self.rest()
        self.finish()


class ChickenSauteRecipe(Recipes):
    def __init(self, recipe_name):
        super().__init__(recipe_name)

    def start(self):
        pass


class ChickenSoup(Recipes):
    def __init(self, recipe_name):
        super().__init__(recipe_name)

    def start(self):
        pass


choice = '0'
while choice != '4':
    print("\nMain Choice: Choose 1 of 3 choices")
    print("Choose 1 for RiceRecipe")
    print("Choose 2 for ChickenSauteRecipe")
    print("Choose 3 for ChickenSoup")
    print("Choose 4 for Exit")

    choice = input("Please make a choice: ")

    if choice == "1":
        rice_recipe = RiceRecipe("Pilav \n")
        rice_recipe.start()
    elif choice == "2":
        chicken_saute_recipe = ChickenSauteRecipe("Chicken Saute \n")
        chicken_saute_recipe.start()
    elif choice == "3":
        chicken_soup_recipe = ChickenSoup("Chicken Soup \n ")
        chicken_soup_recipe.start()
    elif choice == "4":
        exit()
    else:
        print("I don't understand your choice.\n")
