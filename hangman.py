class Word():
  def __init__(self, chosen_word):
    self.chosen_word = chosen_word
    self.char_dicts = []
    self.board = ''

  def game_init(self):
    for char in self.chosen_word:
      Dict = {}
      Dict[0] = char
      Dict[1] = False
      self.char_dicts.append(Dict) 
    for i in self.char_dicts:
      self.board += '_ '
    print(self.char_dicts)
    print(self.board)

  def guess_letter(self):
    board_list = list(self.board)
    # print(self.char_dicts[0][0])
    guess = input('Guess a letter: ')
    # print('You guessed:', guess)
    for i, char in enumerate(self.char_dicts):
      if guess == char[0]:
        # self.board += guess + ' '
        print('True: ', guess)
        board_list[i] = guess
      # else:
      #   # self.board += '_ '
      #   print('False: ', char[0])
    self.board = "".join(board_list)
    if '_' in self.board:
      return self.guess_letter()




game_word = Word('establishment')

game_word.game_init()
game_word.guess_letter()