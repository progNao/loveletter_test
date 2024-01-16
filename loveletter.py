from deck import Deck
from com.card_number_1 import Soldier_com
from com.card_number_2 import Clown_com
from com.card_number_3 import Knight_com
from com.card_number_4 import Monk_com
from com.card_number_5 import Magician_com
from com.card_number_6 import General_com
from com.card_number_7 import Minister_com
from player.card_number_1 import Soldier
from player.card_number_2 import Clown
from player.card_number_3 import Knight
from player.card_number_4 import Monk
from player.card_number_5 import Magician
from player.card_number_6 import General
from player.card_number_7 import Minister


class Loveletter:
  def __init__(self):
    self.deck = Deck()
    self.player_hand = []
    self.com_hand = []
    self.player_protect = False
    self.com_protect = False
    
  def deal_initial_cards(self):
    self.player_hand = [self.deck.draw()]
    self.com_hand = [self.deck.draw()]
  
  def player_draw(self):
    self.player_hand.append(self.deck.draw())
  
  def com_draw(self):
    self.com_hand.append(self.deck.draw())
  
  def deck_len(self):
    return self.deck.remaining_cards()
  
  def player_play(self, card_number):
    if card_number == 1:
      if Soldier(self.player_hand, self.com_hand, self.com_protect).process():
        return 1
      return 2
    elif card_number == 2:
      Clown(self.player_hand, self.com_hand, self.com_protect).process()
      return 2
    elif card_number == 3:
      value = Knight(self.player_hand, self.com_hand, self.com_protect).process()
      if int(value) == 1:
        return 1
      elif int(value) == 0:
        return 0
      else:
        return 2
    elif card_number == 4:
      self.player_protect = Monk().process()
      return 2
    elif card_number == 5:
      value = Magician(self.deck, self.player_hand, self.com_hand, self.com_protect).process()
      self.deck = value[0]
      self.player_hand = value[1]
      self.com_hand = value[2]
      if value[3] == 1:
        return 1
      elif value[3] == 0:
        return 0
      else:
        return 2
    elif card_number == 6:
      value = General(self.player_hand, self.com_hand, self.com_protect).process()
      self.player_hand = value[0]
      self.com_hand = value[1]
      return 2
    elif card_number == 7:
      Minister().process()
      return 2
    else:
      print("姫(8)はプレイできません。")
      return 2
    
  def com_play(self, card_number):
    if card_number == 1:
      if Soldier_com(self.player_hand, self.com_hand, self.player_protect).process():
        return 0
      return 2
    elif card_number == 2:
      Clown_com(self.player_hand, self.com_hand, self.player_protect).process()
      return
    elif card_number == 3:
      value = Knight_com(self.player_hand, self.com_hand, self.player_protect).process()
      if int(value) == 0:
        return 0
      elif int(value) == 1:
        return 1
      else:
        return 2
    elif card_number == 4:
      self.com_protect = Monk_com().process()
      return 2
    elif card_number == 5:
      value = Magician_com(self.deck, self.player_hand, self.com_hand, self.player_protect).process()
      self.deck = value[0]
      self.player_hand = value[1]
      self.com_hand = value[2]
      if value[3] == 1:
        return 1
      elif value[3] == 0:
        return 0
      else:
        return 2
    elif card_number == 6:
      value = General_com(self.player_hand, self.com_hand, self.player_protect).process()
      self.player_hand = value[0]
      self.com_hand = value[1]
      return 2
    elif card_number == 7:
      Minister_com().process()
      return 2
    else:
      return 2