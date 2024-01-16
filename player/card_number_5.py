import time

class Magician:
  def __init__(self, deck, player_hand, com_hand, com_protect):
    self.deck = deck
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.com_protect = com_protect
    self.is_win = 2
  
  def process(self):
    print("魔術師(5)をプレイしました。\n")
    print("【説明】：魔術師(5)は、プレイヤーもしくは相手の手札を捨て、山札から一枚引きます。\n")
    time.sleep(2)
    while True:
      input_number = input("カードを捨てる対象を選んでください(プレイヤー:1 相手:2): ")
      if input_number.lower() not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("無効な入力です。")
        continue
      else:
        if int(input_number) == 1:
          print("手札を捨て、山札から1枚引きます。\n")
          time.sleep(2)
          if self.player_hand[0] == 8:
            print("姫(8)が捨てられたため、プレイヤーは脱落します。\n")
            self.is_win = 0
            return [self.deck, self.player_hand, self.com_hand, self.is_win]
          else:
            self.player_hand.pop()
            self.player_hand.append(self.deck.draw())
            return [self.deck, self.player_hand, self.com_hand, self.is_win]
        elif int(input_number) == 2:
          if self.com_protect:
            print("相手は僧侶の効果で対象にできません。\n")
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
        else:
          print("無効な入力です。\n")
          continue
