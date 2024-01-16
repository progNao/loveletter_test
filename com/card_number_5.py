import random
import time

class Magician_com:
  def __init__(self, deck, player_hand, com_hand, player_protect):
    self.deck = deck
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.player_protect = player_protect
    self.is_win = 2
  
  def process(self):
    print("魔術師(5)をプレイしました。\n")
    print("【説明】：魔術師(5)は、プレイヤーもしくは相手の手札を捨て、山札から一枚引きます。\n")
    time.sleep(2)
    print("相手が対象を選択します。(プレイヤー:1 相手:2)\n")
    time.sleep(2)
    input_number = random.randint(1, 2)
    print(f"相手が宣言した番号: {input_number}")
    if input_number == 1:
      if self.player_protect:
        print("僧侶の効果中なので、対象に選ばれません。\n")
        return [self.deck, self.player_hand, self.com_hand, self.is_win]
      else:
        print("プレイヤーが手札を捨て、山札から1枚引きます。\n")
        time.sleep(2)
        if self.player_hand[0] == 8:
          print("姫(8)が捨てられたため、プレイヤーは脱落します。\n")
          self.is_win = 0
          return [self.deck, self.player_hand, self.com_hand, self.is_win]
        else:
          self.player_hand.pop()
          self.player_hand.append(self.deck.draw())
          return [self.deck, self.player_hand, self.com_hand, self.is_win]
    else:
      print("相手が手札を捨て、山札から1枚引きます。")
      time.sleep(2)
      if self.com_hand[0] == 8:
        print("姫(8)が捨てられたため、相手は脱落します。\n")
        self.is_win = 1
        return [self.deck, self.player_hand, self.com_hand, self.is_win]
      else:
        self.com_hand.pop()
        self.com_hand.append(self.deck.draw())
        return [self.deck, self.player_hand, self.com_hand, self.is_win]