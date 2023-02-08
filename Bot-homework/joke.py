import pyjokes
# from googletrans import Translator

# translator = Translator()


def rand_joke():
    joke = pyjokes.get_joke()
    return joke
