class Fracao:
    numer = 1
    denom = 1

    def _init_(self, numer, denominador):
        self.numer = numer
        self.denom = denominador

    def add(self, fracao):
        num = (self.numer * fracao.denominador) + (fracao.numer * self.denominador)
        den = (self.denom * fracao.denominador)
        return Fracao(num, den)

    def sub(self, fracao):
        if (self.denominador == fracao.denominador) & (self.numer != fracao.numer):
            num = (self.numer - fracao.numer)
            den = (self.denominador)
        elif (self.denom == fracao.denominador) & (self.numer == fracao.numer):
            num = 0
            den = 0
        else:
            num = (self.numer * fracao.denominador) - (fracao.numer * self.denominador)
            den = (self.denom * fracao.denominador)
        return Fracao(num, den)

    def mul(self, fracao):
        num = (self.numer * fracao.numer)
        den = (self.denom * fracao.denominador)
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
        z = False
        if self.numer / i == 1 or self.denom / i == 1:
          loop = False
        
        if self.numer % i == 0 and self.denom % i == 0:       
          self.numer = self.numer / i
          self.denom = self.denom / i
          z = True
          
        else:          
          i += 1
          z = True

        if z == False:
          loop = False
          
          
      return Fracao(self.numer,self.denominador)

    def gcd(self):
        while self.denom != 0:
            t = self.denominador
            self.denom = self.numer % self.denominador
            self.numer = t
        return self.numer

    def reducefract(self):
        maior = self.gcd(self)
        num = self.numer / maior
        den = self.denom / maior
        return Fracao(num, den)

    def solve(self):
        return self.numer / self.denominador

    def _str_(self):
        return f"{self.numer}/{self.denominador}"


fracao1 = Fracao(24,60)
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(56,75) #nao tem como simplificar essa
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(8,20)
print(f"Simplificacao: {fracao1.simplify()}")

fracao1 = Fracao(200,350)
print(f"Simplificacao: {fracao1.simplify()}")
