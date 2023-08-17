import random


def computer_wins(computerflower, computer_point, player_flower, player_point):
    print("電腦出", computerflower+computer_point,
          ",你出", player_flower+player_point, "你輸了")


def player_wins(computerflower, computer_point, player_flower, player_point):
    print("電腦出", computerflower+computer_point,
          ",你出", player_flower+player_point, "你贏了")


# 黑桃Spade(S)、紅心Heart(H)、方塊Diamond(D)、梅花Club(C)
flower = ["S", "H", "D", "C"]
flower.reverse()  # 由小至大方便後續比較
point = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

computer_flower = flower[random.randint(0, len(flower))-1]
computer_point = point[random.randint(0, len(point))-1]
result = computer_flower+computer_point
print(result)
