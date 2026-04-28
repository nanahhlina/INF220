class Fraccion:
    """Representa una fracción matemática con numerador y denominador."""
    def __init__(self, num = 0, den = 0):
        self.num = num
        self.den = den

    def limpiar(self):
        """Reinicia la fracción a su estado inicial."""
        self.num = 0
        self.den = 1 
        return ""
    
    def simplificar(self):
        """Devuelve una nueva fracción reducida usando el algoritmo de Euclides."""
        a, b = abs(self.num), self.den
        while b:
            a, b = b, a % b
        return Fraccion(self.num // a, self.den // a)

    def sumar(self, other):
        """Suma self con other. Devuelve una nueva fracción resultado."""
        nuevo_num = self.num * other.den + other.num * self.den
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)
    
    def restar(self, other):
        """Resta other de self. Devuelve una nueva fracción resultado."""
        nuevo_num = self.num * other.den - other.num * self.den
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def multiplicar(self, other):
        """Multiplica self por other. Devuelve una nueva fracción resultado."""
        nuevo_num = self.num * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def dividir(self, other):
        """Divide self entre other. Devuelve una nueva fracción resultado."""
        if other.num == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return Fraccion(self.num * other.den,
                        self.den * other.num)
    
    def __str__(self):
        """Devuelve una representación en cadena de la fracción."""
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"
