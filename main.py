import flask
import game
app = flask.Flask(__name__)
DEFAULT_NUMBER_OF_SOURCE_WORDS = 15

active_game = game.Game()


@app.route('/')
def main():
    words = game.choose_source_words(DEFAULT_NUMBER_OF_SOURCE_WORDS)
    active_game.guessed_words.clear()
    assert not(len(words) % 5), "To display the page correctly, number of words must be multiple of 5"
    return flask.render_template('main.html', words=words)


@app.route('/solve')
def solve():
    active_game.set_source_word(flask.request.args.get('word'))
    return flask.render_template('solve.html', word=flask.request.args.get('word'))


@app.route('/enter_word', methods=['POST'])
def enter_word():
    active_game.set_source_word(flask.request.form['word'])
    return flask.redirect(flask.url_for('solve', word=flask.request.form['word'], words=active_game.guessed_words))


@app.route('/solve/try_word', methods=['POST'])
def try_word():
    message = active_game.get_message(flask.request.form['word'])
    return flask.render_template('solve.html', word=active_game.get_source_word(), words=active_game.guessed_words,
                                 message=message)
