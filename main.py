import string

class Alphabet:

    def __init__(self, language, letters_str):
        self.language = language
        self.letters = list(letters_str)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)

class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self,letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_Num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("English example:\nDon't eat this burger!!!")

if __name__ == '__main__':
    telo_End = EngAlphabet()
    telo_End.print()
    print(telo_End.letters_Num)
    print(telo_End.is_en_letter('F'))
    print(telo_End.is_en_letter('Щ'))
    EngAlphabet.example()
