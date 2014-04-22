	directions = ["north", "south", "east", "west", "down", "up", "down", "right"]
	verbs = ["go", "stop", "kill", "eat"]
	stops = ["the"., "in", "at", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]

	def scan(userInput):
		words = userInput.split()
		sentence = []

		for word in words:
			if word in directions:
				sentence.append(("direction", word))
			elif word in verbs:
				sentence.append(("verb", word))
			elif word in stops:
				sentence.append(("stop", word))
			elif word in nouns:
				sentence.append(("noun", word))
			elif word.isDigit():
				sentence.append("number", convert_number(word))
			else:
				sentence.append(("error", word))

		return sentence
				

	def convert_number(s):
		try:
			return int(s)
		except ValueError:
			return None


"""
def scan(sentence):
	userinput = sentence
	words = sentence.split(" ")
	pairs = []

	for word in words:
		if word in (item[1] for item in lexicon):
			wordType = lexicon[word]
		else:
			wordType = "error"

		tupes = (word, wordType)
		pairs.append(tupes)

		return pairs 
"""
