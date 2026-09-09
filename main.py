
"""
Code qui compte le nombre de mots dans un string
Par Bradley Perreault
Groupe 4567
"""


# compte le # de mots dans un string en comptant les nombres d`espaces
def count_word(text: str):
    word_count = 0 # nombre de mots
    in_word = False # pour que 2 espaces ne comptent pas comme 2 mots etc etc

    for letter in text:
        if letter != " " and letter != "'":
            if not in_word: 
                word_count += 1
                in_word = True # assure que plus que 1 espaces n'est pas confus comme plus que 1 mot
        else:
            in_word = False

    return word_count


print(f"il y a {count_word("   c'est des    mots   des  mots des     mots")} mots dans cette phrase")

