
# translator app
# all vowels turn into the letter g

def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiouy":
      if letter.isupper():
        translation = translation + "G"
      else:
        translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print(translate("cat"))

