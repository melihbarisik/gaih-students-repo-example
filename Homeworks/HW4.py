import sys

class Hangman:
    searching_word=""
    correct_character_list=list()
    character_you_tried = list()

    def __init__(self):
      pass

    def get_word_from_user(self):
        self.searching_word = input("Write your word to find \n")
        self.correct_character_list = ['_' for i in range(len(self.searching_word))]
        self.character_you_tried = ['_' for i in range(len(self.searching_word)+2)]


    def compare_character(self,guess):
        counter=0
        for character in self.searching_word:
            if guess == character:
                self.correct_character_list[counter]= character


            counter+=1

    def write_words(self):
        for character in self.correct_character_list:
            print(character, end=" ")
        print()

    def write_used_word(self):
        print("Word you tried -->", end=" ")
        for character in self.character_you_tried:
            print(character, end=" ")
        print()

    def start_the_game(self):
       counter = 0
       for ch in range(len(self.searching_word)+2):
           self.if_game_over()
           print("Retries:", len(self.searching_word)+3 - ch)
           guess_character = input("Your guess:")
           self.character_you_tried[counter] = guess_character
           self.compare_character(guess_character)
           self.write_words()
           self.write_used_word()
           counter +=1
           print()

       else:
           print("Your Retries is Overke")
           sys.exit()

    def if_game_over(self):
        if "_" not in self.correct_character_list:
            print("Game Overke, You Win!! Thnx for Playing")
            sys.exit()

player = Hangman()
player.get_word_from_user()
player.start_the_game()


