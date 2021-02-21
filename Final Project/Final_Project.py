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

    def hash(self):
        print("chop the chicken meat")

    def prepare_vegetables(self):
        print("Chop the tomato, pepper and onion")

    def pry(self):
        print("Fry the chicken on low heat, stirring occasionally.")

    def add_onion(self):
        print("Add the onions and the finely cut garlic after a little water.")

    def add_spices(self):
        print("After frying for 1-2 minutes, add the peppers.")

    def add_vegetables(self):
        print("When the peppers are sautéed, add the tomato, tomato paste, spices and salt and continue to cook.")

    def last_step(self):
        print("Finally, add 1 glass of water and cook with the lid closed until the meats are cooked.")

    def start(self):
        self.lets_start()
        self.hash()
        self.prepare_vegetables()
        self.open_the_cooker()
        self.put_the_cooker()
        self.pry()
        self.add_onion()
        self.add_spices()
        self.add_vegetables()
        self.last_step()
        self.finish()


class ChickenSoup(Recipes):
    def __init(self, recipe_name):
        super().__init__(recipe_name)

    def boiling(self):
        print("Let's take the chicken into the pot, add salt and boil it")

    def prepare_saucepan(self):
        print("When the avuk juice is ready, let's take oil, butter and flour in the pot and roast it.")

    def mixing(self):
        print("When the smell of flour comes out, let's add chicken broth little by little and mix it quickly.")

    def add_chicken(self):
        print("When it starts to boil, let's throw away the noodle and chicken pieces.")

    def ready_after_cooking(self):
        print("When the vermicelli is cooked, our soup is ready. Let's serve with lemon.")

    def start(self):
        self.lets_start()
        self.boiling()
        self.open_the_cooker()
        self.put_the_cooker()
        self.prepare_saucepan()
        self.mixing()
        self.add_chicken()
        self.ready_after_cooking()
        self.finish()


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
