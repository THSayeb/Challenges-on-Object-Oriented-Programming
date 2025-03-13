class FlashCard:
    def __init__(self, Word, meaning):
        self.Word = Word
        self.meaning = meaning

    def arrange(self):
        return self.Word+"("+self.meaning+")"

Flash = []
while (True):
    word = input("Enter the flashcared word : ")
    Difinition = input("Enter the difinition : ")
    Flash.append(FlashCard(word,Difinition))

    option = input("0 or 1 : ")
    if (option):
        break

for cards in Flash:
    print(cards)
