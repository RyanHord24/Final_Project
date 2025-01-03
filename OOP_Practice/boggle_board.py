import random
import string

class BoggleBoard:
    total_dice = []
    
    def __init__(self):
        pass

    def make_boggle(self):  
        print("____\n____\n____\n____")

    def shake(self):
        self.make_dice()
        board = "____\n____\n____\n____"
        board_list = list(board)
        for index, space in enumerate(board_list):
            if space == "_":
                count = 0
                board_list[index] = random.choice(BoggleBoard.total_dice[count])
                count += 1
        print("".join(board_list))


    def make_dice(self):
        count = 1
        while count < 17:
            dice_number = [1, 2, 3, 4, 5, 6]
            for index, space in enumerate(dice_number):
                dice_number[index] = random.choice(string.ascii_uppercase)
                BoggleBoard.total_dice.append(dice_number)
                count += 1
            


first_boggle = BoggleBoard()

first_boggle.shake()