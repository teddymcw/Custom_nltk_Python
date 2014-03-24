import nltk

word = input("please type your word ")
word = str(word)

def get_syn_words(word):
	syn_word = nltk.wordnet.wordnet.synsets(word)[0]
	return syn_word

def get_synonyms(word):
	all_syns = nltk.wordnet.wordnet.synsets(word)
	ls_all_syns = [syn.lemmas for syn in all_syns]
	names = [syn.name for syn in all_syns]
	return ls_all_syns, names