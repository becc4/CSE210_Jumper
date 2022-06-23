import random

class word():
    
    def __init__(self):
        _chosen_Word = ''

    def gen_Word(self):
        _wordList = ["clock","spray","index","paint","smash","aware","theme","ranch","grass","solve","album",
                    "elbow","worry","fence","house","basis","trait","piano","stain","thumb","plane","merit","print",
                    "woman","dream","child","tasty","glass","climb","layer","watch","snarl","giant","beach","money",
                    "Bible","joint","issue","image","proof","plant","metal","night","catch","pride","knock","chord",
                    "alive","force","clash","car","cat","dog","bat","fat","set", "is", "at", "or", "if"]
        
        self._chosen_Word = _wordList[random.randint(0,len(_wordList))]

    def word_Len(self):
        return len(self._chosen_Word)

    def get_Word(self):
        return self._chosen_Word