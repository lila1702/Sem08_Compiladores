from Consts import Consts
from Token import Token
from Error import Error
class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.indice, self.coluna, self.linha = -1, -1, 0
        self.__advance()
    def __advance(self):
        self.__advanceCalc(self.current)
        self.current = self.code[self.indice] if self.indice<len(self.code) else None

    def __advanceCalc(self, _char=None):
        self.indice +=1
        self.coluna +=1
        if self.current == '\n':
            self.coluna = 0
            self.linha += 1
        return self
    
    def makeTokens(self):
        tokens = []
        while self.current != None:
            if self.current in ' \t':
                self.__advance()
            elif self.current == Consts.PLUS:
                tokens.append(Token(Consts.PLUS))
                self.__advance()
            elif self.current in Consts.DIGITOS:
                tokens.append(self.__makeNumber())
            else:
                return tokens, Error(Error.lexerError)
            
        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        strNum = ''
        conta_ponto = 0
        while self.current != None and self.current in Consts.DIGITOS + '.': 
            if self.current == '.':
                if conta_ponto == 1: break
                conta_ponto +=1
            strNum +=self.current
            self.__advance()

        if conta_ponto == 0:
            return Token(Consts.INT, int(strNum))
        return Token(Consts.FLOAT, float(strNum))

