import time

class General_com:
  def __init__(self, player_hand, com_hand, player_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.player_protect = player_protect
  
  def process(self):
    print("将軍(6)をプレイしました。\n")
    print("【説明】：将軍(6)は、プレイヤーと相手の手札を交換します。\n")
    time.sleep(2)
    if self.player_protect:
      print("僧侶の効果中なので、対象に選ばれません。\n")
      return [self.player_hand, self.com_hand]
    else:
      value1 = self.player_hand.pop()
      value2 = self.com_hand.pop()
      self.player_hand.append(value2)
      self.com_hand.append(value1)
      return [self.player_hand, self.com_hand]