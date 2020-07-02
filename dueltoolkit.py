import random

def players():
	global x
	x = dict()
	player = ""
	while player != "APQ":
		player = input()
		x[player] = 100

def attack():
	while x.values() != 0 or len(x) != 0:
		try:
			playerToAttack = input("Введите имя игрока которого нужно атаковать: \n")
			if x[playerToAttack] == None:
				x[playerToAttack] = 100
			else:
				x[playerToAttack] -= random.randint(75, 100)

			if x[playerToAttack] == 0:
				print("{player} был убит!")
				x.pop(player)
		except KeyError:
			print("Такого игрока не существует!") 