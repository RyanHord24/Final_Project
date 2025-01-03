class GuessingGame:
    def __init__(self, number):
        self.number = number
        self.guess_num = None
    def guess(self, num):
        self.guess_num = num
        number = self.number
        if num < number:
            return 'low'
        if num > number:
            return 'high'  
        if num == number:
            return 'correct'
    def solved(self):     
        if self.number == self.guess_num:
            return True
        else:
            return False
