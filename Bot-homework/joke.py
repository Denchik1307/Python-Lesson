import pyjokes
# from googletrans import Translator

# translator = Translator()


def rand_joke():
    joke = pyjokes.get_joke()
    # joke_result = translator.translate(joke, dest='ru')
    # print(joke_result)
    return joke
    # return joke_result.text


# print(rand_joke())
# rand_joke()