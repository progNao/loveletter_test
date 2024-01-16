import time

class Clown_com:
  def __init__(self, player_hand, com_hand, player_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.player_protect = player_protect
  
  def process(self):
    print("道化(2)をプレイしました。\n")
    print("【説明】：道化(2)は、相手の手札を確認します。\n")
    time.sleep(2)
    if self.player_protect:
      print("僧侶の効果中なので、対象に選ばれません。\n")
    else:
      print("相手がプレイヤーの手札を確認しました。\n")
      time.sleep(2)