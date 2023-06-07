import googletrans
import time
from googletrans import Translator
from random import randint
start_time = time.time()


class BadTranslator():

    def __init__(self):
        self.translator = Translator()
        self.counter = 0
        self.language_list = googletrans.LANGUAGES
        self.language_list_new = list(self.language_list.keys())

    def translate(self, sentence, iterations):

        if self.counter == iterations:
            translation = self.translator.translate(sentence, dest='fi')
            print(translation.text)
            return

        translation = self.translator.translate(sentence, dest=f'{self.language_list_new[randint(0, len(self.language_list_new)-1)]}')
        sentence = translation.text
        self.counter += 1
        self.translate(sentence, iterations)

sentence = "Umberto Komulainen ei mikään tavallinen Mikael"
b = BadTranslator()
iterations = 20
b.translate(sentence, iterations)

print("Kesto: " + str((time.time() - start_time)))
