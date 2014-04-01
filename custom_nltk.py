import nltk
from nltk import corpus #for eng_dictionary rt now
from stop_words import sw, support_words

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import ne_chunk, pos_tag, word_tokenize

def gen_tokens(text):
	""" str -> gen 
	call nltk's work_tokenize function on our text,
	which differs from just splitting our list by spaces"""
	tokens = nltk.word_tokenize(text)
	#punct = [',' , '.' , '?' , '!']
	#subtract_period_tokens = [word[:-1] for word in tokens if word[-1] in punct]
	"""for word in tokens:
		if word[-1] == '.':
			word = word[:-1]""" #why can we have just a floating fucking string in there?
	#tokens = (tokens - set(subtract_period_tokens))
	for word in tokens:
		yield word

def gen_lowercase_tokens(text):
	""" str -> gen 
	maintain generator type for lowercase words, 
	useful for comparing against stop word lists"""
	for word in gen_tokens(text):
		yield word.lower()

def get_non_stop_words(text):
	""" str -> list 
	take a text file and compare its tokens against custom stop words list 
	returning only what we deem acceptable words"""
	tokens = gen_lowercase_tokens(text)
	non_stop_words = [word for word in tokens if word not in sw]
	return non_stop_words

def get_content_percentage(text):
	""" str -> str(int)
	gives percentage of words that are not listed in the support words list
	by returning numbers of tokens over number of total tokens. Note the difference between
	this ratio and the lexical diversity ratio""" 
	ns_words = get_non_stop_words(text)
	fl_nswl = float(len(ns_words))
	text_tokens = gen_tokens(text) #note non-stop words are not being used here
	content = [word for word in text_tokens if word.lower() not in support_words]
	fl_content = float(len(content))
	try:
		result = round(fl_nswl / fl_content, 2) * 100
	except ZeroDivisionError:
		pass
		result = 0
		#error = "caught the zero division error"
		#return error
	return "{}".format(result)

def get_text_and_content_length(text):
	""" str -> float, float
	return length of text list with stop_words omitted and length of 'content'
	defined as non 'support words' """ 
	ns_words_list = get_non_stop_words(text)
	fl_nswl = float(len(ns_words_list))
	text = gen_tokens(text) #note non-stop words are not being used here
	content = [word for word in text if word not in support_words]
	fl_content = float(len(content))
	return fl_nswl, fl_content

def get_substance(text): #NOTE THAT THIS IS A STUB FOR NOW
	""" str -> list 
	take a text file and compare its tokens against custom stop words list 
	returning only what we deem substantive words"""
	substance_words = ['real', 'fancy', 'words']
	tokens = gen_tokens(text)
	tokens = [token.lower() for token in tokens]
	substantive = [word for word in tokens if word not in substance_words]
	return substantive

def get_freq_dist(text):
    """ str -> FreqDist 
    retrieve frequency distribution of each 'substantive' word in text using nltk"""
    substantive = get_non_stop_words(text)
    text_class = nltk.Text(substantive)
    fdist = nltk.FreqDist(text_class)
    return fdist

def get_lexical_diversity_ratio(text):
	""" str -> float 
	lexical diversity is calculated by taking the number 
	of unique words over the number of total words"""
	return round(float(len(set(get_non_stop_words(text))) / float(len(get_non_stop_words(text)))), 5)

def gen_english_vocab(dictionary):
	sane_dictionary = set([word.lower() for word in dictionary])
	for word in sane_dictionary:
		yield word

def compare_unusual_words(text):
    """ str -> set 
    compare text to words in unix english dictionary and return alphabetized set"""
    each_word_set = set(get_non_stop_words(text))
    only_alpha_set = set(w.lower() for w in each_word_set if w.isalpha())
    sane_eng_dict = corpus.words.words()
    english_vocab = gen_english_vocab(sane_eng_dict)
    unusual = sorted(only_alpha_set.difference(english_vocab))
    plain_unusual_words_str = ", ".join(unusual)
    return plain_unusual_words_str

#Begin Lem section 

lemmatizer = WordNetLemmatizer()
lemmatize = lambda word: lemmatizer.lemmatize(word.lower())

def gen_words(text):
	for word in get_non_stop_words(text):
		yield word

def get_word_features(text):
	words = gen_words(text)
	lemmed = [lemmatize(word) for word in words]
	return lemmed
#End Lem Section

def extract_interesting_lines(text):
	""" str -> generator object """
	for line in text:
		line = line.strip()
		if line.startswith("-"): #non-sensical just practicing idioms here
			continue 
		if not line:
			continue
		yield line  #instead of do_something(line)

#SYNSET SECTION

def gen_all_lemmas(word):
	""" str -> set 
	"""
	synsets = wn.synsets(word)
	ls = list()
	for i in synsets:
		ls.append(i.lemma_names)
	result = list()
	for i in ls:
		for y in i:
			if y not in result:
				result.append(y)
	res = set(result)	
	for lemma in res:
		yield lemma

def get_all_lemmas(word):
	""" (single word) str -> (word list) str
	just one applicable definition of a lemma is 
	A subsidiary proposition assumed to be valid 
	and used to demonstrate a principal proposition"""
	all_lemmas = [word for word in gen_all_lemmas(word)]
	return ', '.join(all_lemmas)

def play_with_lemmas(word):
	""" str -> set 
	"""
	synsets = wn.synsets(word)
	ls = list()
	for i in synsets:
		ls.append(i.lemma_names)
	result = list()
	for i in ls:
		for y in i:
			if y not in result:
				result.append(y)
	res = set(result)	
	for word in res:
		yield word

#END SYNSET

#START CHUNKING

def get_entities(text):
	""" str -> Tree('X', list[(tuple pairs)], Trees(...))
	uses pos 'parts of speech' tagging""" 
	entities = ne_chunk(pos_tag(word_tokenize(text)))
	return entities


def get_syn_words(word):
	""" (single word) str -> str """
	syn_word = nltk.wordnet.wordnet.synsets(word)[0]
	return syn_word

def get_synonyms(word):
	all_syns = nltk.wordnet.wordnet.synsets(word)
	ls_all_syns = [syn.lemmas for syn in all_syns]
	names = [syn.name for syn in all_syns]
	return ls_all_syns, names

