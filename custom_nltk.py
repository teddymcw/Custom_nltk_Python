import nltk
from nltk import corpus #for eng_dictionary rt now
from stop_words import sw, support_words
from collections import Counter

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import ne_chunk, pos_tag, word_tokenize

def gen_tokens(text):
	""" str -> gen 
	call nltk's work_tokenize function on our text,
	which differs from just splitting our list by spaces
	"""
	for word in nltk.word_tokenize(text):
		yield word

def gen_cleaner_words(text):
	""" str -> str 
	removes commonly 'attached' punctuation marks such as ',''.''*word*' etc.
	"""
	for i in list(gen_tokens(text)):
		yield i.translate(None, "!@#$%^&*().,[]+=-_`~<>?")

def gen_lowercase_tokens(text):
	""" str -> gen 
	maintain generator type for lowercase words, 
	useful for quick comparisons against certain stop word lists
	"""
	for word in gen_tokens(text):
		yield word.lower()

def gen_ns_words(text):
	""" str -> gen 
	need non stop words before non support words
	"""
	for i in (word for word in gen_cleaner_words(text) if word.lower() not in sw):
		yield i

#note for this module's purpose the default type for stop_words will be lowercase
def gen_ns_and_nsup_words(text):
	""" str -> gen 
	generate words not in stop or support words list 
	"""
	for i in (word for word in gen_ns_words(text) if word.lower() not in support_words):
		yield i

def get_text_len_and_content_len(text):
	""" str -> float, float
	return length of text list with stop_words omitted and length of 'content'
	defined as non 'support words' """ 
	num_ns_tokens = float(len(list(gen_ns_words(text))))
	num_content_tokens = float(len(list(gen_ns_and_nsup_words(text))))
	return (num_ns_tokens, num_content_tokens)

def get_content_percentage(text):
	""" str -> float
	number of words in text - stop words and support words / number of tokens in text. 
	Note the difference between this ratio and the lexical diversity ratio, 
	which only accounts for unique words.
	"""  
	try: 
		result = float(len(list(gen_ns_and_nsup_words(text)))) / float(len(list(gen_tokens(text))))
		result = round(result, 2)
	except ZeroDivisionError:
		pass
		result = 0
	return result #any string conversion will be done in the controller

def gen_true_substance(text): #NOTE THAT THIS IS A STUB FOR NOW
	""" str -> list 
	take a text file and compare its tokens against custom stop words list 
	returning only what we deem substantive words"""
	#need a whole new list of substantial words
	substance_words = ['real', 'fancy', 'words']
	for i in (word for word in gen_ns_and_nsup_words(text) if word.lower() not in substance_words):
		yield i 

def get_freq_dist(text):
    """ str -> FreqDist 
    retrieve frequency distribution of each 'substantive' word in text using nltk
    """
    ns_words = list(gen_ns_words(text)) 
    text_class = nltk.Text(ns_words)
    freq_dist = nltk.FreqDist(text_class)
    return freq_dist

def get_printable_freq_dist(text):  
	""" str -> str 
	function to essentially pretty print the freq_dist values for readability
	"""
	first_ten = get_freq_dist(text).items()[:10]
	fd_flat_ls = []
	for i in first_ten:
		a, b = i
		fd_flat_ls.append(a)
		fd_flat_ls.append(str(b) + ', ')
	return ' '.join(fd_flat_ls)
		#print("{0} {1},".format(a, b))   
		#must be a better and more obvious way to get format desired than what is above

def get_counter_class_freq_dist(text):
	""" str -> Counter
	enables use of Counter class and provides more ways to test
	"""
	text_ls = text.split() #default value of split() is all white space
	coun = Counter(text_ls)
	coun = [word for word in coun.items() if word[0].lower() not in sw]
	return coun 

def get_lexical_diversity_ratio(text):
	""" str -> float 
	lexical diversity is calculated by taking the number 
	of unique words over the number of total words"""
	return round(float(len(set(gen_ns_words(text))) / float(len(gen_ns_words(text)))), 5)

def gen_lower_english_vocab(dictionary):
	""" str -> gen 
	yields a lower case gen object of words passed in to a dictionary 
	"""
	sane_dictionary = set([word.lower() for word in dictionary])
	for i in (word.lower() for word in sane_dictionary):
		yield i 

def compare_unusual_words(text):
    """ str -> set 
    compare text to words in unix english dictionary and return alphabetized set"""
    each_word_set = set(gen_ns_words(text))
    only_alpha_set = set(w.lower() for w in each_word_set if w.isalpha())
    sane_eng_dict = corpus.words.words()
    english_vocab = gen_lower_english_vocab(sane_eng_dict)
    unusual = sorted(only_alpha_set.difference(english_vocab))
    plain_unusual_words_str = ", ".join(unusual)
    return plain_unusual_words_str

#Begin Lem section 

lemmatizer = WordNetLemmatizer()
lemmatize = lambda word: lemmatizer.lemmatize(word.lower())

def get_word_features(text):
	words = gen_ns_words(text)
	lemmed = [lemmatize(word) for word in words]
	return lemmed
#End Lem Section

def extract_interesting_lines(text): #Stub for now
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

def get_all_lemmas(single_word):
	""" (single word) str -> (word list) str
	just one applicable definition of a lemma is 
	A subsidiary proposition assumed to be valid 
	and used to demonstrate a principal proposition"""
	all_lemmas = [word for word in gen_all_lemmas(single_word)]
	return ', '.join(all_lemmas)

def gen_play_with_lemmas(word):
	""" str -> gen 
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
	return (ls_all_syns, names)