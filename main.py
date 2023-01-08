# Minecraft mob farm autoclicker

from time import sleep

from mouse import click, _os_mouse

ACTION_DELAY_SEC = 45

ATTACK_DELAY_SEC = 0.625 + 0.125  # min 0.625 (sword attack cooldown)
ATTACKS_PER_TRY = 3

X_OFFSET = 75


def attack() -> None:
	for _ in range(ATTACKS_PER_TRY):
		R = 1
		L = -1
		for direction in [L, L, L, R, R, R, R, R, R, L, L, L]:
			click()
			sleep(ATTACK_DELAY_SEC)
			_os_mouse.move_relative(direction * X_OFFSET, 0)


def countdown() -> None:
	for sec in list(range(5))[::-1]:
		print(f"Starting in {sec + 1} sec...")
		sleep(1)


def main():
	countdown()
	while True:
		attack()
		sleep(ACTION_DELAY_SEC)


if __name__ == "__main__":
	main()
