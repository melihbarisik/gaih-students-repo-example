import sys

class Hangman:
    searching_word=""
    correct_character_list=list()

    def __init__(self):
      pass

    def get_word_from_user(self):
        self.searching_word = input("Write your word to find \n")
        self.correct_character_list = ['_' for i in range(len(self.searching_word))]


    def compare_character(self,guess):
        counter=0
        for character in self.searching_word:
            if guess == character:
                self.correct_character_list[counter]= character

            counter+=1

    def write_words(self,word_list):
        for character in self.correct_character_list:
            print(character, end=" ")
        print()

    def start_the_game(self):

       for ch in range(len(self.searching_word)):
           self.if_game_over()
           print("Retries:", len(self.searching_word)-ch)
           guess_character = input("Your guess:")
           self.compare_character(guess_character)
           self.write_words(self.correct_character_list)

       else:
           print("Your Retries is Overke")
           sys.exit()

    def if_game_over(self):
        if "_" not in self.correct_character_list:
            print("Game Overke, Thx for Playing")
            sys.exit()

player = Hangman()
player.get_word_from_user()
player.start_the_game()


