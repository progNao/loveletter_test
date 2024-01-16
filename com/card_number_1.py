import random
import time

class Soldier_com:
  def __init__(self, player_hand, com_hand, player_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.player_protect = player_protect
    self.is_apply = False
  
  def process(self):
    print("兵士(1)をプレイしました。\n")
    print("【説明】：兵士(1)は、2-8の番号を宣言し、相手の手札と一致したら脱落させます。\n")
    time.sleep(2)
    print("相手が兵士(1)以外のカード番号(2-8)を宣言します。\n")
    time.sleep(2)
    input_number = random.randint(2, 8)
    print(f"相手が宣言した番号: {input_number}")
    time.sleep(2)
    if self.player_protect:
      print("僧侶の効果中なので、対象に選ばれません。")
      return self.is_apply
    else:
      if self.player_hand == input_number:
        self.is_apply = True
        print("プレイヤーの手札を当てられました。\n")
        print("プレイヤーは脱落しました。\n")
        return self.is_apply
      else:
        print("外れました。\n")
        return self.is_apply