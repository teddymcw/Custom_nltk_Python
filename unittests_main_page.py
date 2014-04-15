#self.assertRaises(ZeroDivisionError, get_cont_perc_int, str())

from custom_nltk import word_tokenize
from custom_nltk import gen_tokens, gen_ns_words, get_content_percentage, get_cont_perc_int, get_text_and_content_length, get_substance
from custom_nltk import get_freq_dist, get_printable_freq_dist, get_counter_class_freq_dist, get_lexical_diversity_ratio, gen_english_vocab
from custom_nltk import compare_unusual_words, get_all_lemmas, play_with_lemmas
import unittest
import random
import nltk 
from nltk.probability import FreqDist 

zen = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"

class TestFreqDistFunctions(unittest.TestCase):

	def setUp(self):
		self.generated_tokens = gen_tokens(zen)
		self.list_gen_tokens = sorted(list(self.generated_tokens))
		self.nltk_tokens = sorted(word_tokenize(zen))
		#still not sure why sorting is necessary

	def test_nltk_tokens_equals_gen_tokens(self):

		self.assertEqual(self.list_gen_tokens, self.nltk_tokens)

		for word in random.sample(self.list_gen_tokens, 10):
			self.assertTrue(word in self.list_gen_tokens)

		with self.assertRaises(ValueError):
			random.sample(self.list_gen_tokens, 156)


	def test_content_percentage_errors(self):
		self.cont_percentage = get_cont_perc_int(zen)
		#self.zero_percentage = get_cont_perc_int(" ")

		self.assertEqual(self.cont_percentage, 87.0)
		#I don't understand why the ZDE isn't raised in this test case
		self.assertRaises(ZeroDivisionError, get_cont_perc_int, " ")
		#gotta know more about how these exceptions and assertRaises statements work
		

	def test_words_in_tokens(self):
		word = random.choice(self.nltk_tokens)
		self.assertTrue = (word in self.nltk_tokens)

	def test_freq_dist(self):
		self.coun = get_counter_class_freq_dist(zen)[:10]
		self.freq_dist = get_freq_dist(zen)

		self.assertIsInstance(self.freq_dist, FreqDist)
		self.assertNotEqual(self.coun[:10], self.freq_dist.items()[:10])

	def test_get_printable_freq_dist(self):
		self.first_ten_str = get_printable_freq_dist(zen)
		self.bad_punc = [".",",",":",";",'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=','{','}']
		#this order is from the unittest docs
		#punctuation still needs removal!
		self.assertEqual(self.first_ten_str, 'better 8,  although 3,  one 3,  explain 2,  idea. 2,  implementation 2,  may 2,  never 2,  obvious 2,  special 2, ')
		self.assertNotEqual(self.first_ten_str[:9], 'Better 8')
		for punc in self.bad_punc:
			self.assertTrue(punc not in self.first_ten_str)
		self.assertFalse(len(self.first_ten_str < 100)) #114
		self.assertIs(self.first_ten_str, type)
		self.assertIsNot(self.first_ten_str, int)
		self.assertIsNone(self.first_ten_str + [])
		self.assertIsNotNone(self.first_ten_str)
		self.assertIn('obvious', self.first_ten_str)
		self.assertNotIn('Tim Peters', self.first_ten_str)
		self.assertIsInstance(self.first_ten_str, str)
		self.assertIsInstance(self.first_ten_str, tuple)

	def test_get_lexical_diversity_ratio(self):
		self.lex_div_ratio = get_lexical_diversity_ratio(zen)

		self.assertEqual(self.lex_div_ratio, 0.7619)
		self.assertNotEqual(self.lex_div_ratio, 0.7619999)
		self.assertAlmostEqual(self.lex_div_ratio, 0.761900001) #7 places is default
		self.assertNotAlmostEqual(self.lex_div_ratio, 0.7619001)
		self.assertLess(self.lex_div_ratio, .77)
		self.assertLessEqual(self.lex_div_ratio, .7619000000000)

		




if __name__ == '__main__':
    unittest.main()
