import time

class Monk_com:
  def __init__(self):
    self.is_protect = True
  
  def process(self):
    print("僧侶(4)をプレイしました。\n")
    print("【説明】：僧侶(4)は、次の手番まで効果を無効にします。\n")
    time.sleep(2)
    return self.is_protect