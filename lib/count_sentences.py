#!/usr/bin/env python3
import pdb


class MyString:
    def __init__(self, value = ""):
        if not isinstance(value, str) or len(value) == 0:
          print("The value must be a string.")
        self.value = value

    def is_sentence(self):
       return self.value[-1] == "."
    
    def is_question(self):
       return self.value[-1] == "?"
    
    def is_exclamation(self):
       return self.value[-1] == "!" 
    
    def count_sentences(self):
        value = self.value
        for punc in ["!", "?"]:
           value = value.replace(punc, ".")

        sentences = [s for s in value.split(".") if s]

        return len(sentences)
          

   