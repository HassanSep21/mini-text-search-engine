import math
import re

class VectorCompare:
    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError("Argument should be a dict")

        total = 0
        for word, count in concordance.items():
            total += count**2

        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError("Argument 1 should be a dict")
        if type(concordance2) != dict:
            raise ValueError("Argument 2 should be a dict")

        top_value = 0
        for word, count in concordance1.items():
            if concordance2.get(word):
                top_value += count * concordance2[word]

        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return top_value / (self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
            return 0

    def concordance(self, document):
        if type(document) != str:
            raise ValueError("Argument should be a str")

        con = dict()
        for word in document.split(" "):
            con[word] = con.get(word, 0) + 1

        return con


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    return text
