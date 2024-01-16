import time

class Knight_com:
  def __init__(self, player_hand, com_hand, player_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.player_protect = player_protect
    self.is_win = 2
  
  def process(self):
    print("騎士(3)をプレイしました。\n")
    print("【説明】：騎士(3)は、お互いの手札の数字を比較し、低い方を脱落させます。\n")
    time.sleep(2)
    if self.player_protect:
      print("僧侶の効果中なので、対象に選ばれません。\n")
      return self.is_win
    else:
      print(f"プレイヤーの手札:{self.player_hand}\n")
      print(f"相手の手札:{self.com_hand}\n")
      time.sleep(2)
      if self.player_hand[0] > self.com_hand[0]:
        self.is_win = 1
        return self.is_win
      elif self.player_hand[0] < self.com_hand[0]:
        self.is_win = 0
        return self.is_win
      else:
        print("同じ数字なので何も起きません。\n")
        return self.is_win