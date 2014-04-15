import json
from ze_app import app #db
from ze_app.forms import BigText, SingleWord
from flask import request, render_template, flash 
from custom_nltk import word_tokenize,
gen_tokens, gen_cleaner_words, gen_lowercase_tokens, gen_ns_words, gen_ns_and_nsup_words
get_text_len_and_content_len, get_content_percentage, get_true_substance,
get_freq_dist, get_printable_freq_dist, get_counter_class_freq_dist, get_lexical_diversity_ratio, 
gen_lower_english_vocab, compare_unusual_words, get_word_features, extract_interesting_lines
gen_all_lemmas, get_all_lemmas, gen_play_with_lemmas, get_entities, get_syn_words, get_synonyms


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

	if form: #.validate_on_submit() catches fl_nswl
		user_text_input = str(form.play.data)
		content_percentage = get_content_percentage(user_text_input)
		#need to return percentage functions below
		#convert all input to unicode in wtforms as well
		fl_nswl, fl_content = get_text_and_content_length(user_text_input)
		lex_diversity = get_lexical_diversity_ratio(user_text_input)
		unusual_words = compare_unusual_words(user_text_input)
		fd = get_freq_dist(user_text_input)
		freq_dist = json.dumps(fd.items()[:10])
		print_fd = get_printable_freq_dist(user_text_input)
	
	return render_template('content_percentage.html', form=form, form_single_word=form_single_word, error=error, 
		fl_nswl=fl_nswl, fl_content=fl_content, content_percentage=content_percentage, 
		lex_diversity=lex_diversity, unusual_words=unusual_words, freq_dist=freq_dist, print_fd=print_fd)

@app.route('/lemmas', methods=['GET', 'POST'])
def run_lemmas():
	form_single_word = SingleWord(request.form)
	error = None

	if form_single_word: #.validate_on_submit()

		the_word = str(form_single_word.single_word.data)
		show_lemmas_of_given_word = get_all_lemmas(the_word)
		lemmas_of_given_word = show_lemmas_of_given_word.split(', ')
		lemmas = json.dumps(lemmas_of_given_word)

	return render_template('lemmas.html', lemmas=lemmas, form_single_word=form_single_word, error=error, 
		the_word=the_word, show_lemmas_of_given_word=show_lemmas_of_given_word,
		lemmas_of_given_word=lemmas_of_given_word)