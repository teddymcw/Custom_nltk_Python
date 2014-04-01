from ze_app import app #db
from ze_app.forms import BigText, SingleWord
from flask import request, render_template, flash 
from custom_nltk import gen_tokens, get_non_stop_words, get_content_percentage, get_text_and_content_length, get_substance
from custom_nltk import get_freq_dist, get_lexical_diversity_ratio, gen_english_vocab
from custom_nltk import compare_unusual_words, get_all_lemmas, play_with_lemmas
import json

#util web functions
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')
#end util web functions

@app.route('/', methods=['GET', 'POST'])
def get_landing():
	form = BigText(request.form)
	error = None
	return render_template('landing.html', form=form, error=error)

@app.route('/content_percentage', methods=['GET', 'POST'])
def run_content_percentage():
	form = BigText(request.form)
	form_single_word = SingleWord(request.form)
	error = None

	if form:
		user_text_input = str(form.play.data)
		content_percentage = get_content_percentage(user_text_input)
		#need to return percentage functions below
		#convert all input to unicode in wtforms as well
		fl_nswl, fl_content = get_text_and_content_length(user_text_input)
		lex_diversity = get_lexical_diversity_ratio(user_text_input)
		unusual_words = compare_unusual_words(user_text_input)
	
	return render_template('content_percentage.html', form=form, form_single_word=form_single_word, error=error, 
		fl_nswl=fl_nswl, fl_content=fl_content, content_percentage=content_percentage, 
		lex_diversity=lex_diversity, unusual_words=unusual_words)

@app.route('/lemmas', methods=['GET', 'POST'])
def run_lemmas():
	form_single_word = SingleWord(request.form)
	error = None

	if form_single_word:

		the_word = str(form_single_word.single_word.data)
		show_lemmas_of_given_word = get_all_lemmas(the_word)
		lemmas_of_given_word = show_lemmas_of_given_word.split(', ')
		lemmas = json.dumps(lemmas_of_given_word)
	return render_template('lemmas.html', lemmas=lemmas, form_single_word=form_single_word, error=error, 
		the_word=the_word,show_lemmas_of_given_word=show_lemmas_of_given_word,
		lemmas_of_given_word=lemmas_of_given_word)