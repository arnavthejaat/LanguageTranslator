import googletrans
from googletrans import Translator

def translate():
    translator = Translator()
    userInput = input("Type something in a different language: ")
    #src = translator.translate(userInput, src="auto", dest="en")

    if userInput == "{}".format(userInput):
        """
        
        :param lang: source = auto
        :return: Language in english
        """
        print(translator.translate(userInput, src="auto", dest="en"))
        trans_lang = translator.translate(userInput)
        print("translated in english: ", trans_lang.text)

translate()
