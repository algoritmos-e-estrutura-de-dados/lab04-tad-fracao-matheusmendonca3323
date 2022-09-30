class Fracao:
    numerador = 1 
    denominador = 1


   
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador


    
    def add(self, fracao): 
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num,den)


    def sub(self, fracao): 
        if(self.denominador == fracao.denominador) & (self.numerador != fracao.numerador):
            num = (self.numerador - fracao.numerador) 
            den = (self.denominador)
        elif(self.denominador == fracao.denominador) & (self.numerador == fracao.numerador):
            num = 0
            den = 0
        else :     
            num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
            den = (self.denominador * fracao.denominador)
        return Fracao(num,den)

    def mul(self, fracao): 
        num = (self.numerador * fracao.numerador) 
        den = (self.denominador * fracao.denominador)
        return Fracao(num,den)

    def simplify(self): 
        return

    def gcd(self):
            while self.denominador != 0:
                t = self.denominador
                self.denominador = self.numerador % self.denominador
                self.numerador = t
            return self.numerador

    def reducefract(self):
        greatest=self.gcd(self)
        num = self.numerador/greatest
        den = self.denominador/greatest
        return Fracao(num, den)
            

    def solve(self):
        return self.numerador/self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"    


fracao1 = Fracao(1,2)
fracao2 = Fracao(2,4)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)
fracao6 = fracao2.reducefract
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao3: {fracao3.solve()}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5.solve()}")
print(f"fracao6: {fracao6}")