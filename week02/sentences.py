import random

def main():
   quantities = [1, 2, 3, 4, 5, 6]
   tenses = ['present', 'past', 'future']
   for _ in range(6):
       quantity = random.choice(quantities)
       tense = random.choice(tenses)
       sentence = make_sentence(quantity, tense)
       print(sentence)

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
  """Return a randomly chosen noun.
  If quantity is 1, this function will
  return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
  Otherwise, this function will return one of
  these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
  Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.
  Return: a randomly chosen noun.
    """
  if quantity == 1:
    words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
    words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]  
  word = random.choice(words)
  return word

def get_verb(quantity, tense):
  """Return a randomly chosen verb. If tense is "past",
  this function will return one of these ten verbs:
      "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"
  If tense is "present" and quantity is 1, this
  function will return one of these ten verbs:
      "drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"
  If tense is "present" and quantity is NOT 1,
  this function will return one of these ten verbs:
      "drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"
  If tense is "future", this function will return one of
  these ten verbs:
      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"
  Parameters
      quantity: an integer that determines if the
          returned verb is single or plural.
      tense: a string that determines the verb conjugation,
          either "past", "present" or "future".
  Return: a randomly chosen verb.
  """
  if tense == "present" :
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:  
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  if tense == "past":
    words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"] 
  elif tense == "future":
    words = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
  word = random.choice(words)
  return word

def make_sentence(quantity, tense):
  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense param eters.
  """
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)
  adverb = get_adverb()
  preposition = get_prepositional_phrase(quantity)
  sentence = determiner + ' ' + noun + ' ' + adverb + ' ' + verb + ' ' + preposition
  return sentence

def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
  preposition = random.choice(prepositions)
  return preposition

def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or pluaral.
  Return: a prepositional phrase.
  """
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity) 
  preposition_determiner_noun = preposition + ' ' + determiner + ' ' + noun 
  return preposition_determiner_noun

#Creativity: Adding an adverb to the sentences
def get_adverb():
  """This function will return a randomly chosen adverb
    to describe how the action is done. Examples of adverbs include:
    "quickly", "slowly", "happily", "sadly", "carefully", "eagerly",
    "gracefully", "lazily", "loudly", "softly"
  The adverb will modify the verb, adding more detail to the sentence."""
  adverbs = ["quickly", "slowly", "happily", "sadly", "carefully", "eagerly", "gracefully", "lazily", "loudly", "softly"]
  adverb = random.choice(adverbs)
  return adverb

main()
   