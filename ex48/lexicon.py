WORD_TYPES = {
	"verb" : ["go", "stop", "kill", "eat"],
	"direction" : ["north", "south", "east", "west", "down", "up", "down", "right"],
	"noun" : ["door", "bear", "princess", "cabinet"], 
	"stop" : ["the"., "in", "at", "of", "from", "at", "it"]
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}


def scan(sentence):
	result = []
	for word in sentence.split():
		try:
			word_type = VOCABULARY[word]
		except KeyError:
			try:
				value = int(word)
			except ValueError:
				tokens.append(("error", word))
			else: 
				tokens.append(("int", value))
		else: 
			tokens.append((word_type, word))
		return tokens