from models.model import Fraccion
from views.view import CalculadoraView

class CalculadoraController:
    """Controlador que maneja la lógica de la calculadora de fracciones."""
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_controller(self)

        self.num_str = ""
        self.den_str = ""
        self.f1 = None
        self.pending_op = None
        self.step = 0  # 0: ingresando f1, 1: ingresando f2

    def _actualizar_display(self):
        """Actualiza el display de la vista según el estado actual."""
        n = self.num_str or "0"
        d = self.den_str or "1"
        if self.step == 0:
            self.view.update_display(n, d)
        else:
            self.view.update_display(n, d,
                op=self.pending_op,
                f1_num=str(self.f1.num),
                f1_den=str(self.f1.den))

    def on_left_key(self, tecla):
        """Maneja las teclas de la parte izquierda (C, ⌫, ±)."""
        if tecla == 'C':
            self.num_str = ""
            self.den_str = ""
            self.f1 = None
            self.pending_op = None
            self.step = 0
            self.view.update_resultado("—")
        elif tecla == '⌫':
            self.num_str = self.num_str[:-1]
        elif tecla == '±':
            if self.num_str.startswith('-'):
                self.num_str = self.num_str[1:]
            elif self.num_str:
                self.num_str = '-' + self.num_str
        else:
            self.num_str += tecla
        self._actualizar_display()

    def on_op(self, op):
        """Maneja la selección de operación (+, -, ×, ÷)."""
        if not self.num_str and not self.den_str:
            return
        n = int(self.num_str or 0)
        d = int(self.den_str or 1)
        self.f1 = Fraccion(n, d)
        self.pending_op = op
        self.step = 1
        self.num_str = ""
        self.den_str = ""
        self._actualizar_display()

    def on_frac_key(self, parte, tecla):
        """Maneja las teclas de la parte de fracción (numerador/denominador)."""
        if tecla == '⌫':
            if parte == 'n':
                self.num_str = self.num_str[:-1]
            else:
                self.den_str = self.den_str[:-1]
        else:
            if parte == 'n':
                self.num_str += tecla
            else:
                self.den_str += tecla
        self._actualizar_display()

    def on_simplificar(self):
        """Maneja la acción de simplificar la fracción actual."""
        n = int(self.num_str or 0)
        d = int(self.den_str or 1)
        s = Fraccion(n, d).simplificar()
        self.num_str = str(s.num)
        self.den_str = str(s.den)
        self._actualizar_display()

    def on_calcular(self):
        """Maneja la acción de calcular el resultado de la operación pendiente."""
        if self.step == 0 or not self.pending_op:
            return
        try:
            n2 = int(self.num_str or 0)
            d2 = int(self.den_str or 1)
            f2 = Fraccion(n2, d2)
            ops = {
                '+': self.f1.sumar,
                '-': self.f1.restar,
                '×': self.f1.multiplicar,
                '÷': self.f1.dividir,
            }
            resultado = ops[self.pending_op](f2)

            if resultado.den == 1:
                self.view.update_resultado(str(resultado.num))
            else:
                self.view.update_resultado(str(resultado.num), str(resultado.den))

            self.f1 = resultado
            self.num_str = str(resultado.num)
            self.den_str = str(resultado.den)
            self.step = 0
            self.pending_op = None
            self._actualizar_display()
        except (ZeroDivisionError, ValueError) as e:
            self.view.update_resultado(f"Error: {e}")