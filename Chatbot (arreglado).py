#Chatbot by Codecademy
#Upgraded by Juan - 2021
#Some examples of input:
#your planet
#why do you make
#why come
#what resources
#it is certain
#i think sure
#you
#I need what this code reconogize {0}
# importing regex and random libraries
import re
import random
# potential negative responses
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
# keywords for exiting the conversation
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop", "good bye")
# random starter questions
random_questions = ("Why are you here?", 
    "Are there many humans like you?", 
    "What do you consume for sustenance?", 
    "Is there intelligent life on this planet?", 
    "Does Earth have a leader?", 
    "What planets have you visited?", 
    "What technology do you have on this planet?"
    )
the_name = ""
the_speak = (
    # Your planet...
  {r'.*\s*your planet':
    ("My planet is a utopia of diverse organisms and species.",
    "I am from Earth, the capital of the Wayward Galaxies.")
    },
  # why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
     ("What makes you think I {0}?",
     "Because I am on a great mission. Have you been on a mission?",
     "Because I'm bored! What do you do for fun around here?")
    },
  # why... ?
    {r'.*why\s+.*':
     ("I come in peace.",
      "Everyone on my planet is funny looking. Why do you ask?",
      "Why not?!")
    },
  # what... ?
    {r'.*what\s+.*':
     ("My planet is out of resources, so I am here looking for help.", 
      "I need more gasoline to the launcher.",
      "I am looking for help, because I need resources.")
    },
  # it is...
    {r'.*it\s+is':
     ("You seem very certain. Why is that?", 
      "Do you have any evidence?", 
      "You people know so little. Why is that?")
    },
  # I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
     ("But you're not sure {0}?", 
      "Why do you think {0}?")
    },    
  # Other responses
    {r'.*':
     ("Please tell me more.", 
      "Tell me more!", 
      "Why do you say that?", 
      "I see. Can you elaborate?", 
      "Interesting. Can you tell me more?", 
      "I see. How do you think?", 
      "Why?", 
      "How do you think I feel when you say that?")
    }
)
# Define the_greet() below:
def the_greet():
  the_name = input(text_with_end_space("What's your name?"))
  will_help = lower_case(input(text_with_end_space("Hi {}, I'm Juan. Will you help me?".format(the_name))))
  if will_help in negative_responses:
    print("Ok, have a great Earth day!")
    return ""
  return will_help
# Define the_make_exit() here:
def the_make_exit(reply):
  for exit_command in exit_commands:
    if lower_case(exit_command) in reply:
      print("Ok, have a great Earth day!")
      return True
# Define the_chatbot() next:
def the_chatbot():
  will_hlp = the_greet()
  if will_hlp != "":
    reply = lower_case(input(text_with_end_space(random.choice(random_questions),will_hlp)))
    while not the_make_exit(reply):
      reply = the_converse(reply)
# Define the_converse() below:      
def the_converse(reply):
  for pair in the_speak:
    for regex_pattern, the_answers in pair.items():
      found_match = re.match(regex_pattern, reply)
      if found_match:
        the_answer = random.choice(the_answers)
        reply = input(text_with_end_space(the_answer,reply))
        the_formatted_answer = the_answer.format(*[the_reflect(matching_group) for matching_group in found_match.groups()])
        reply = input(text_with_end_space(the_formatted_answer))
        print(reply)
        return lower_case(reply)
# dictionary used to switch pronouns
# and verbs in responses      
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}
#Define the reflections to merge words
def the_reflect(response):
  words = the_split(response)
  for index, word in enumerate(words):
    if word in reflections:
        words[index] = reflections[word]
  return the_space().join(words)
# Additional scripts
def the_space():
  return " "
def text_with_end_space(the_text,reply=""):
  textoRetorno = the_text + the_space()
  if the_text.find("{0}"):
    textoRetorno = textoRetorno.replace('{0}', reply)
  return textoRetorno
def lower_case(the_text):
  return the_text.lower()
def upper_case(the_text):
  return the_text.upper()
def the_split(the_text):
    return the_text.split()
def text_to_list(the_text):
  return list(the_text)
the_chatbot()
#python3 ""