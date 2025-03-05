class reverse:
    def __init__(self,word_s):
        self.s = word_s
   
    def reverse_word(self):
        return self.s[::-1]
    
word = input("enter the word to be reversed: ")
revob = reverse(word)
result = revob.reverse_word()
print('reversed string: ', result)
