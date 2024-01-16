import time

class General:
  def __init__(self, player_hand, com_hand, com_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.com_protect = com_protect
  
  def process(self):
    print("将軍(6)をプレイしました。\n")
    print("【説明】：将軍(6)は、プレイヤーと相手の手札を交換します。\n")
    time.sleep(2)
    if self.com_protect:
      print("相手は僧侶の効果で対象にできません。\n")
      return [self.player_hand, self.com_hand]
    else:
      value1 = self.player_hand.pop()
      value2 = self.com_hand.pop()
      self.player_hand.append(value2)
      self.com_hand.append(value1)
      return [self.player_hand, self.com_hand]