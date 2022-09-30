class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def sub(self, fracao):
        if (self.denominador == fracao.denominador) & (self.numerador != fracao.numerador):
            num = (self.numerador - fracao.numerador)
            den = (self.denominador)
        elif (self.denominador == fracao.denominador) & (self.numerador == fracao.numerador):
            num = 0
            den = 0
        else:
            num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
            den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def mul(self, fracao):
        num = (self.numerador * fracao.numerador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def infinito():
        teste = 0
        while True:
            yield teste
            teste += 1

    def simplify(self):        
      loop = True
      i = 2
      
      while loop == True:               
        controle = False
        if self.numerador / i == 1 or self.denominador / i == 1:
          loop = False
        
        if self.numerador % i == 0 and self.denominador % i == 0:       
          self.numerador = self.numerador / i
          self.denominador = self.denominador / i
          controle = True
          
        else:          
          i += 1
          controle = True

        if controle == False:
          loop = False
          
          
      return Fracao(self.numerador,self.denominador)

    def gcd(self):
        while self.denominador != 0:
            t = self.denominador
            self.denominador = self.numerador % self.denominador
            self.numerador = t
        return self.numerador

    def reducefract(self):
        greatest = self.gcd(self)
        num = self.numerador / greatest
        den = self.denominador / greatest
        return Fracao(num, den)

    def solve(self):
        return self.numerador / self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


fracao1 = Fracao(24,60)
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(56,75) #nao tem como simplificar essa
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(8,20)
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(200,350)
print(f"Simplificacao: {fracao1.simplify()}")
