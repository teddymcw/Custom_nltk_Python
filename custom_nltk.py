import nltk
import sys
from stop_words import sw

def make_tokens(text):
	""" str -> list 
	call nltk's work_tokenize function on our text,
	which differs from just splitting our list by spaces"""
	return nltk.word_tokenize(text)

def get_substance(text):
	""" str -> list 
	take a text file and compare its tokens against custom stop words list 
	returning only what we deem substantive words"""
	tokens = make_tokens(text)
	tokens = [token.lower() for token in tokens]
	substantive = [word for word in tokens if word not in sw]
	return substantive

def get_freq_dist(text):
    """ str -> FreqDist """
    substantive = get_substance(text)
    text_class = nltk.Text(substantive)
    fdist = nltk.FreqDist(text_class)
    return fdist

def get_lexical_diversity_ratio(text):
	""" str -> float 
	lexical diversity is calculated by taking the number 
	of unique words over the number of total words"""
	return round(float(len(set(get_substance(text))) / float(len(get_substance(text)))), 5)

#Begin Lem section 
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatize = lambda word: lemmatizer.lemmatize(word.lower())

def gen_words(text):
	for word in get_substance(text):
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



def generate_short_names(lists):
	for name in almost_all_names_list:
		if len(name) < 8:
			yield name




#fun with names and zip(list, list)
us_male_first_names_ten = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas",]
french_male_first_names_ten = ["Lucas", "Nathan", "Enzo", "Leo", "Gabriel", "Louis", "Hugo", "Raphael", "Jules", "Arthur",]
french_female_first_names_ten = ["Emma", "Lea", "Chloe", "Ines", "Manon", "Jade", "Lola", "Camille", "Louise", "Zoe",]
arab_states_first_names = ['Bari', 'Ababneh', 'Hussain', 'Hossein', 'Khatib', 'Mustafa', 'Khoury', 'Sleiman', 'Sulaiman', 'Sulayman', 'Yaseen', 'Ibrahim', 'Ibraheem', 'Ibrahim', 'Qassem', 'Abbas', 'Abbas', 'Hamdan', 'Abolhassan', 'Amin', 'Ameen', 'Ismail', 'Salman', 'Rashid', 'Karim', 'Saad', 'Sad', 'Temiz', 'Hamid', 'Ayasha', 'Saleem', 'Salim', 'Shadi', 'Omar', 'Omer', 'Ommar', 'Murat', 'Habib', 'Shareef', 'Sharif', 'Mahmad', 'Najeeb', 'Armanjani', 'Shahriar', 'Rasheed', 'Mohammad']
india_first_names = ['Subramanian', 'Nirmal', 'Pawan', 'Manohar', 'Sahni', 'Lalit', 'Rajan', 'Sehgal', 'Uddin', 'Saini', 'Neel', 'Jana', 'Darsha', 'Ranga', 'Vish', 'Mehra', 'Puri', 'Muthu', 'Gandhi', 'Lata', 'Chauhan', 'Saxena', 'Swami', 'Neela', 'Chandrasekar', 'Soni', 'Dhawan', 'Nagpal', 'Joshi', 'Krishnamurthy', 'Persaud', 'Punj', 'Veena', 'Mahajan', 'Manju', 'Dutta', 'Sandeep', 'Narang', 'Naran', 'Veer', 'Tyagi', 'Samuel', 'Srivastava', 'Sudha', 'Srivas', 'Mati', 'Neelam', 'Rastogi', 'Bhatt', 'Rajagopal', 'Srivastav', 'Ganesh', 'Jindal']
china_last_names = ['Li', 'Wang', 'Zhang', 'Liu', 'Chen', 'Y\xc3\xa1ng', 'Huang', 'Zhao', 'Zhou', 'Wu', 'X\xc3\xba', 'S\xc5\xabn', 'Zhu', 'M\xc7\x8e', 'Hu', 'Gu\xc5\x8d', 'L\xc3\xadn', 'H\xc3\xa9', 'G\xc4\x81o', 'Li\xc3\xa1ng']
colombia_last_names = ['Rodr\xc3\xadguez', 'G\xc3\xb3mez', 'Gonz\xc3\xa1lez', 'Mart\xc3\xadnez', 'Garc\xc3\xadav', 'L\xc3\xb3pez', 'Hern\xc3\xa1ndez', 'S\xc3\xa1nchez', 'Ram\xc3\xadrez', 'P\xc3\xa9rez', 'D\xc3\xadas', 'Mu\xc3\xb1oz', 'Rojas', 'Moreno', 'Jim\xc3\xa9nez']

zip(french_female_first_names_ten, colombia_last_names, india_first_names, us_male_first_names_ten, arab_states_first_names, china_last_names)

two_zip = zip(french_female_first_names_ten, india_first_names)
dict_it = dict(two_zip)

for k, v in dict_it.iteritems():
    print(k, v)

almost_all_names_list = us_male_first_names_ten + colombia_last_names + china_last_names + india_first_names + arab_states_first_names
 

for name in generate_short_names(almost_all_names_list):
	print("{}, what's up?".format(name))

#this is really interesting actually
#I need a set of words that are marked as "powerful" or 
#having some bold meaning to filter texts


with open("my_config.ini") as file:
	for line in extract_interesting_lines(file):
		print("gen line: {}".format(line)) #do_something(line)

with open("my_config.ini") as file:
	for line in extract_interesting_lines(file):
		enumerate(line) #just showing we can do_something_else(line)

#breaking out of using nested loops
#understand why making a generator solves this problem
def gen_2d_range(width, height):
	"""produce a stream of two-D values"""
	for y in range(height):
		for x in range(width):
			yield x, y 

for x,y in gen_2d_range(5, 6):   
   print(x, y)

for x, y in gen_2d_range(india_first_names, arab_states_first_names):
	print(x)
	#print("{0} - {1}".format(x, y))

#note that this example around(21:00) was just a bit hazy but fine for now



#generators produce and then consume

#generator expressions look just like list comprehensions
#but they work like generators and only produce when they need to
#they are lazy

#polymorphic duck typing, which means that this function can 
#process anything that can process a string
#will take any value that can produce strings!
#we can test this much more easily, no files actually necessary
#for mocking

#you can iterate over xrange multiple times. 
#not practical to know but maybe theory

#xrange is a generator
#too_big_num = 100000000000000000000000
#range(too_big_num) will run out of space whereas xrange(too_big_num) will run out of time

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

text_features = get_word_features(zen)
for num, word in enumerate(text_features):
	print(num, word)


random_stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']


def substance(tokens):
	#EXCLUSION LIST AND SUBSTANCE FUNCTION
	prepositions = ['to','at', 'on', 'in']
	conjunctions = ['and','but', 'when', 'of', 'for', 'with', 'as', 'not', 'from', 'my']
	pronouns = ['i', 'you', 'he','she', 'that', 'it', 'they', 'their', 'we', 'this', 'our', 'these', 'who']
	bs_adjectives = ['a', 'an', 'the']
	bs_verbs = ['to', 'be', 'do', 'are', 'was','were', 'will', 'is', 'have', 'must']
	punc = [':', ',', "'s", '...', "'"," ","--", " '"]
	excluded_words = prepositions + conjunctions + pronouns + bs_adjectives + bs_verbs + punc

	#need to lower both tokens list and substance list here
	lower_tokens = [t.lower() for t in tokens]
	substance_words = [word.lower() for word in lower_tokens if word not in excluded_words]
	return substance_words







with open (sys.argv[1]) as text1:
	text1 = text1.read()
	print(type(text1)) #type string
	#print(get_words(text1)) produces generator object
	lem_words1 = get_word_features(text1)
	print("Lemmatized words text1: {}".format(lem_words1))
	#print(type(text1))
	tokens = nltk.word_tokenize(text1)
	print("length of tokens text1: {}".format(len(tokens)))
	print(type(tokens))
	sub1 = substance(tokens)
	print("first ten sub1: {}".format(sub1[:11]))
	#CHANGE TO TEXT CLASS
	text1 = nltk.Text(tokens)
	print(type(text1))
	print("text1 collocations: {}".format(text1.collocations))
	text1_substance = substance(text1)
	print(type(text1_substance))
	print("First ten of substance set: {}".format(text1_substance[:10]))
	fdist1_substance = nltk.FreqDist(text1_substance)
	print("Frequency distribution of text1:\n {}".format(fdist1_substance))

with open (sys.argv[2]) as text2:
	text2 = text2.read()
	
	lem_words2 = get_word_features(text2)
	print("Lemmatized words text1: {}".format(lem_words2))
	#print(type(text2))
	tokens = nltk.word_tokenize(text2)
	print("length of tokens text2: {}".format(len(tokens)))
	text2 = nltk.Text(tokens)
	print(type(text2))
	print("text2 collocations: {}".format(text2.collocations))
	text2_substance = substance(text2_string)
	fdist2_substance = nltk.FreqDist(text2_substance)
	print("Frequency distribution of text2:\n {}".format(fdist2_substance))




if __name__ == "__main__":
	print(lexical_diversity(sys.argv[1]))