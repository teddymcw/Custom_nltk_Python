from nltk import word_tokenize
from custom_nltk import gen_tokens, get_non_stop_words, get_content_percentage, get_text_and_content_length, get_substance
from custom_nltk import get_freq_dist, get_printable_freq_dist, get_lexical_diversity_ratio, gen_english_vocab
from custom_nltk import compare_unusual_words, get_all_lemmas, play_with_lemmas
import unittest

zen = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"

class TestFreqDistFunctions(unittest.TestCase):

	def setUp(self):
		self.generated_tokens = gen_tokens(zen)
		self.list_gen_tokens = list(self.generated_tokens)
		self.nltk_tokens = word_tokenize(zen)

	def test_list_equals_gen_list(self):

		self.AssertEqual(self.list_gen_tokens, self.nltk_tokens)