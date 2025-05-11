#!/usr/bin/env python3

class MyString:
  pass

  def __init__(self,value = ''):
    self._value = ''
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,new_value):
    if not isinstance(new_value,str):
      print("The value must be a string.")  
    self._value = new_value

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    temp_value = self.value.replace('?','.').replace('!','.')

    sentences = [s for s in temp_value.split('.') if s.strip()]
    return len(sentences)


