import random

class GeradorSernha:

    def __init__(self):

        self.letras = 'abcdefghijklmnopqrstuvwxyz'
        self.numeros = '0123456789'
        self.phrase = ''
        self.senha = ''
    
    def formatation(self):
        self.passwordFormat = ['444', '372', '327', '183', '237', '336', '552']
        self.formatType = random.choice(self.passwordFormat)
        return self.formatType
    
    def createPassword(self):
        self.formasenha = self.formatation()

        for number in range(int(self.formasenha[0])):
            self.phrase += random.choice(self.numeros)
        for lower in range(int(self.formasenha[1])):
            self.phrase += random.choice(self.letras)
        for upper in range(int(self.formasenha[2])):
            self.phrase += random.choice(self.letras).upper()

        self.union = random.sample(self.phrase, len(self.phrase))
        for i in self.union: self.senha += i
        return self.senha

    def MostrarSenha(self):
        self.shufledPassword = self.createPassword()
        return f'Senha: {self.shufledPassword}'

p1 = GeradorSernha()
print(p1.MostrarSenha())
