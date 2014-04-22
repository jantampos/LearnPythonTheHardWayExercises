WORD_TYPES = {
	"verb" : ["go", "stop", "kill", "eat"],
	"direction" : ["north", "south", "east", "west", "down", "up", "down", "right"],
	"noun" : ["door", "bear", "princess", "cabinet"], 
	"stop" : ["the", "in", "at", "of", "from", "at", "it"]
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}


def scan(sentence):
	results = []
	for word in sentence.split():
		try:
			word_type = VOCABULARY[word]
		except KeyError:
			try:
				value = int(word)
			except ValueError:
				results.append(("error", word))
			else: 
				results.append(("int", value))
		else: 
			results.append((word_type, word))
		return results