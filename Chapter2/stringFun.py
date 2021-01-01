# exercise 1 - use your own first and last name
print("-----------------------------------------------")
print("Exercise 1")
name="lisa balbach"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# exercise 2 - make up your own noun, adjective, verb and ending
# use concatenation to create sentence1
# use an f-string to create sentence2
print("-----------------------------------------------")
print("Exercise 2")
noun = "monkey"
adj = "hungry"
verb= "ate"
ending="all the bananas"
sentence1="the " + adj + " little " + noun + " " + verb + " " + ending
sentence2=f"the {adj} little {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

# exercise 3 - find a multiple line quote or excerpt from a poem or book
# that you like, store it and print it out
# (do not use the same quote as the example below)
print("-----------------------------------------------")
print("Exercise 3")
jabberwocky="""
Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.
Beware the Jabberwock, my son!
      The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
      The frumious Bandersnatch!"""
print(jabberwocky)
# exercise 4 - make up a two column printout using \t and \n
# (you need to create your own column headings and data instead of copying the ones below)
print("-----------------------------------------------")
print("Exercise 4\n")
print("Colors\t\t\tFood\n")
print("Orange\t\t\tPizza\n")
print("Green\t\t\tYogurt\n")
print("Turquoise\t\tShrimp\n")

