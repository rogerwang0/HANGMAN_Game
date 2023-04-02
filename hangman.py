from IPython.display import clear_output
import os
class HANGMAN():

    def __init__(self,word):
        self.screen = '''
 ___________________________________
|                       ________    |
|                       |      |    |
|      HANGMAN                 |    |
|                              |    |
|                              |    |
|                            __|__  |
|                                   |
|___________________________________|'''
        print(self.screen)
        self.word = word
        self.knownWord = len(word)*"_"
        self.currentGuess = ''
        self.dummy = 0
        self.defaultDummy = [['O','|','/','\\','/','\\',],[(4,25),(5,25),(5,24),(5,26),(6,24),(6,26)]]
        self.changeStatus()
        self.index = []

    def changeStatus(self):
        str = self.defaultDummy[0][0:self.dummy]
        str.append(self.divideWord(self.knownWord))
        cood = self.defaultDummy[1][0:self.dummy]
        cood.append((8,4))
        self.refresh(self.screen,str,cood)
        
    def refresh(self,screen,str,coodinates):
        #clear_output(wait=False) #刷新屏幕
        os.system('cls')
        screen = screen.split('\n')
        for index,s in enumerate(str):
            c = coodinates[index]
            screen[c[0]] = self.replaceLine(screen[c[0]],s,c[1]-1,c[1]+len(s)-1)
        for i in screen:
            print(i)

    def find_all_indexes(self,input_string, character):
        indexes = []
        start = -1
        while True:
            start = input_string.find(character, start+1)
            if start == -1:
                return indexes
            indexes.append(start)

    def divideWord(self,str):
        str = list(str)
        return " ".join(i for i in str)
    
    def replaceLine(self,s,sub,start,end):
        s = list(s)
        s[start:end] = list(sub)
        s = "".join(str(i) for i in s)
        return s
    
    def checkGuess(self): 
        index = self.find_all_indexes(self.word,self.currentGuess)
        for i in index:
            self.knownWord = self.replaceLine(self.knownWord,self.currentGuess,i,i+1)
        return index

    def guess(self,s):
        self.currentGuess = s
        self.checkGuess()
        self.index = len(self.checkGuess())
        if self.index == 0:
            self.dummy += 1
        self.changeStatus()

    def gameover(self):
        self.refresh(self.screen,["GAMEOVER!",self.divideWord(self.word)],[(6,8),(8,4)])

    def win(self):
        self.refresh(self.screen,["YOU WIN!"],[(6,7)])


def main():
    word =  input("请输入谜面字母：")
    hangman = HANGMAN(word)
    while hangman.dummy < 6 and hangman.knownWord.find('_') != -1:
        guess = input("请输入要猜测的字母：")
        hangman.guess(guess)
    if hangman.knownWord.find('_') == -1:
        hangman.win()
    else:
        hangman.gameover()
main()