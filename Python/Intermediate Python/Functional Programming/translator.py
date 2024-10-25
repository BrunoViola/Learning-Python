# Example of higher-order functions

def translator(language):
   translations = {
   'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
   'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
   'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'},
   'portuguese': {'hello': 'olá', 'goodbye': 'adeus', 'thank you': 'obrigado'}
   }

   def translate_word(word):
      try:
         if word.lower() in translations[language]:
            translation = translations[language][word.lower()]
            return translation
      except: # if the language isn't declared in the dictionary, it captures the error
         return 'We couldn\'t translate'
      
   return translate_word # here we return the function that will translate the word according the language
   
def main():
   language = input('Translate to? ')
   language = language.lower()

   word = input('What\'s the word? ')

   translate_word = translator(language) # we can assign the function returned to a variable

   print(translate_word(word)) # then, we use the variable to pass parameters to the function

if __name__ == "__main__":
   main()