directions = ["north", "south", "east", "west", "down", "up", "down", "right"]
verbs = ["go", "stop", "kill", "eat"]
stops = ["the"., "in", "at", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
vocab = {"verb":verb, "direction":direction, "noun":noun, "stop": stop}

def scan(sentence):
	words = sentence.split()
	result = []

	for word in words:
		for key,value in vocab.items():
			if word.lower() in value:
				result.append((key,word))
				break
			else:
				try:
					word = int(word)
					result.append(("number", word))
				except ValueError:
					result.append(("error", word))

	return result