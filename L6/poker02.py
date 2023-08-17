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
player_flower = flower[random.randint(0, len(flower))-1]
player_point = point[random.randint(0, len(point))-1]

# 先比較點數
if point.index(computer_point) > point.index(player_point):
    # 電腦贏
    computer_wins(computer_flower, computer_point, player_flower, player_point)
elif point.index(computer_point) < point.index(player_point):
    # 玩家贏
    player_wins(computer_flower, computer_point, player_flower, player_point)

elif point.index(computer_point) == point.index(player_point):
    # 電腦玩家點數一樣比花色
    # 花色大小為 黑桃>紅心>方塊>梅花
    if flower.index(computer_flower) > flower.index(player_flower):
        # 點數平手，電腦花色贏
        computer_wins(computer_flower, computer_point,
                      player_flower, player_point)
    elif flower.index(computer_flower) < flower.index(player_flower):
        # 點數平手，玩家花色贏
        player_wins(computer_flower, computer_point,
                    player_flower, player_point)
    else:  # 大家都一樣 平手
        print("平手")
