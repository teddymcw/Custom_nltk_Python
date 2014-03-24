from ze_app import app #db
from ze_app.forms import BigText
from flask import request, render_template, flash 
from custom_nltk import gen_tokens, get_non_stop_words, get_content_percentage, get_substance
from custom_nltk import get_freq_dist, get_lexical_diversity_ratio, gen_english_vocab
from custom_nltk import compare_unusual_words, get_all_lemmas, play_with_lemmas

#util web functions
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')
#end util web functions

@app.route('/', methods=['GET', 'POST'])
def main():
	form = BigText(request.form)
	error = None
	return render_template('main.html', form=form, error=error)
