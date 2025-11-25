import random
import time
story = random.randint(1, 2)

if(story == 1):
	print("enter an adjective: ")
	adjective = input()

	print("enter another adjective: ")
	adjective2 = input()

	print("enter a color: ")
	color = input()

	print("enter the name of an animal: ")
	noun = input()

	print("enter the name of another animal: ")
	noun2 = input()

	print(f"the {adjective} {color} {noun} jumps over the {adjective2} {noun2}.")
else:
	print("enter the name of a language: ")
	language = input()

	print("enter the name of a game:")
	game = input()

	print("enter the name of a food:")
	food = input()

	print("enter an object: ")
	objectinput = input()

	print(f"apolgy for bad {language}")
	time.sleep(1)
	print(f"where were u wen {game} die")
	time.sleep(1)
	print(f"i was at house eating {food} when {objectinput} ring")
	time.sleep(1)
	print(f"{game} is kil")
	time.sleep(1)
	print(f"no")