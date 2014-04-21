from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")

	#
	#if "0" in next or "1" in next:
	#	how_much = int(next)
	#else:
	#	dead("Man, learn to type a number")
	
	#if how_much < 50:
	#	print "Nice, you're not greedy, you win!"
	#	exit(0)
	#else:
	#	dead("You greedy bastard!")

	#if next.isdigit():
	#	if int(next) < 50:
	#		print "Nice, you're not greedy, you win!"
	#else:
	#		dead("You greedy bastard!")

	try:
		if int(next) < 50:
			print "Nice, you're not greedy, you win!"
		else:
			dead("You were to greedy")
	except ValueError:
		dead("Man, learn to type a number!")

	

def bear_room():
	print "There is a bear here"
	print "The bear has a bunch of honey"
	print "The fat bear is in from of another door"
	print "How are you gong to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews ur leg off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He, it, whatever stares at you and u go insane"
	print "Do u flee for ur life or eat ur head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is door to ur right and left"
	print "Which one do u take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")

start()


