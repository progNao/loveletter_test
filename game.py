import random
import time
from loveletter import Loveletter

is_win = 0
card = ["1", "2", "3", "4", "5", "6", "7", "8"]

print("-----Game Start!-----\n\n")

game = Loveletter()
game.deal_initial_cards()

while True:
  if game.deck_len() == 0:
    print("山札が0になったので、お互いの手札を公開し、数字を大きさを比較します。\n")
    print(f"プレイヤーの手札:{game.player_hand}")
    print(f"相手の手札:{game.com_hand}")
    if game.player_hand[0] > game.com_hand[0]:
      print("You Win!\n")
      break
    elif game.player_hand[0] < game.com_hand[0]:
      print("You Loose...\n")
      break
    else:
      print("引き分けです。")
      break
    
  game.player_protect = False
  
  print("プレイヤーの番です。カードをドローします。\n")
  game.player_draw()
  print(f"プレイヤーの手札:{game.player_hand}\n")
  if 12 <= sum(game.player_hand) and 7 in game.player_hand:
    print("手札に大臣(7)があり、かつ合計が12以上のためプレイヤーは脱落します。")
    print("相手の勝利です...\n")
    break
  
  while True:
    play_number = input("手札のカードを1枚プレイしてください: ")
    if play_number.lower() not in card:
      print("無効な入力です。")
      continue
    else:
      if int(play_number) == 8:
        print("姫(8)はプレイできません。")
        continue
      elif int(play_number) not in game.player_hand:
        print("手札にあるカードをプレイしてください。\n")
        continue
      else:
        game.player_hand.remove(int(play_number))
        is_win = game.player_play(int(play_number))
        break
    
  print(f"プレイヤーの手札:{game.player_hand}\n")
  
  if is_win == 1:
    print("You Win!\n")
    break
  elif is_win == 0:
    print("You Loose...\n")
    break
  else:
    print("脱落者はいません。\n")
    
  game.com_protect = False
  
  print("相手の番です。相手がカードをドローします。\n")
  time.sleep(2)
  game.com_draw()
  if 12 <= sum(game.com_hand) and 7 in game.com_hand:
    print("相手の手札に大臣(7)があり、かつ合計が12以上のため相手は脱落します。\n")
    print("プレイヤーの勝利です!\n")
    break
  
  print("相手がカードをプレイします。\n")
  time.sleep(2)
  while True:
    com_play_number = random.choice(game.com_hand)
    if com_play_number == 8:
      continue
    else:
      game.com_hand.remove(int(com_play_number))
      is_win = game.com_play(com_play_number)
      break
  
  if is_win == 1:
    print("You Win!\n")
    break
  elif is_win == 0:
    print("You Loose...\n")
    break
  else:
    print("脱落者はいません。\n")

print("-----Game Over-----\n")