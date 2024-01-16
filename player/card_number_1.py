class Soldier:
  def __init__(self, player_hand, com_hand, com_protect):
    self.player_hand = player_hand
    self.com_hand = com_hand
    self.com_protect = com_protect
    self.is_apply = False
  
  def process(self):
    print("兵士(1)をプレイしました。\n")
    print("【説明】：兵士(1)は、2-8の番号を宣言し、相手の手札と一致したら脱落させます。\n")
    while True:
      input_number = input("兵士(1)以外のカード番号(2-8)を入力してください: ")
      if input_number.lower() not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("無効な入力です。")
        continue
      else:
        if int(input_number) == 1:
          print("兵士(1)以外で入力してください。")
          continue
        elif int(input_number) in [2,3,4,5,6,7,8]:
          if self.com_protect:
            print("相手は僧侶の効果で対象にできません。\n")
            return self.is_apply
          else:
            if self.com_hand == input_number:
              self.is_apply = True
              print("相手のカードを当てました!\n")
              print("相手は脱落しました。\n")
              return self.is_apply
            else:
              print("外れました...\n")
              return self.is_apply
        else:
          print("無効な入力です。\n")
          continue