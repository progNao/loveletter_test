import time

class Clown:
  def __init__(self, player_hand, com_hand, com_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.com_protect = com_protect
  
  def process(self):
    print("道化(2)をプレイしました。\n")
    print("【説明】：道化(2)は、相手の手札を確認します。\n")
    time.sleep(2)
    if self.com_protect:
      print("相手は僧侶の効果で対象にできません。\n")
    else:
      print(f"相手の手札は{self.com_hand}です。\n")
      time.sleep(2)