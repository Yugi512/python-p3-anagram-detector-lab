# your code goes here!

class Anagram:
    def __init__(self,anagram = "hello"):
        self.anagram = anagram

    @property
    def anagram(self):
        return self._anagram
    
    @anagram.setter
    def anagram(self,anagram):
        self._anagram = anagram
    
    def match(self,anagram):

        lists = []
        listen = sorted(self.anagram)
        for match in anagram:
            sortd = sorted(match)
            if sortd == listen:
                lists.append(match)
        return lists