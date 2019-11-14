players = ["황의조","황희찬","구자철","이재성","기성용"]

# # 1단계
num = len(players)
for i in range(num):
    print(players[i])

# 2단계
OUT = int(input("OUT 시킬 선수 번호 :"))
IN = input("IN  시킬 선수 이름 :")

# if IN in players:
#     del IN

del players[OUT-1]
players.append(IN)
for i in range(num):
    print(players[i])