import random

class Deck:
  cards = [1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8]
  
  def __init__(self):
    random.shuffle(self.cards)
  
  def draw(self):
    if len(self.cards) == 0:
      raise ValueError("山札がありません。")
    return self.cards.pop()
  
  def remaining_cards(self):
    return len(self.cards)