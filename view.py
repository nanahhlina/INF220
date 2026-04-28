from tkinter import Tk, Label, Button, Frame, Entry, StringVar

class CalculadoraView:
    def __init__(self, master):
        self.master = master
        self.controller = None
        master.title("Calculadora de Fracciones")

        # --- Display ---
        display = Frame(master, bg="#441075", pady=10, padx=16)
        display.pack(fill="x")

        self.num_var    = StringVar(value="0")
        self.den_var    = StringVar(value="1")
        self.op_var     = StringVar(value="")
        self.f1_num_var = StringVar(value="")
        self.f1_den_var = StringVar(value="")

        inner = Frame(display, bg="#441075")
        inner.pack(anchor="e")

        # Fracción 1 (opaca, ya ingresada)
        self.f1_frame = Frame(inner, bg="#441075")
        self.f1_frame.pack(side="left", padx=(0, 6))
        Label(self.f1_frame, textvariable=self.f1_num_var, bg="#441075", fg="#c9a8e8",
              font=("Arial", 20, "bold"), anchor="center").pack()
        Frame(self.f1_frame, bg="#c9a8e8", height=2).pack(fill="x", pady=2)
        Label(self.f1_frame, textvariable=self.f1_den_var, bg="#441075", fg="#c9a8e8",
              font=("Arial", 20, "bold"), anchor="center").pack()

        # Operador
        Label(inner, textvariable=self.op_var, bg="#441075", fg="#e0c4f5",
              font=("Arial", 22, "bold")).pack(side="left", padx=6)

        # Fracción activa
        frac_frame = Frame(inner, bg="#441075")
        frac_frame.pack(side="left", padx=(6, 0))
        Label(frac_frame, textvariable=self.num_var, bg="#441075", fg="white",
              font=("Arial", 22, "bold"), anchor="center").pack()
        Frame(frac_frame, bg="white", height=2).pack(fill="x", pady=3)
        Label(frac_frame, textvariable=self.den_var, bg="#441075", fg="white",
              font=("Arial", 22, "bold"), anchor="center").pack()

        # --- Cuerpo --- (igual que tienes)
        body = Frame(master, bg="#85449e", padx=10, pady=10)
        body.pack(fill="both", expand=True)

        left = Frame(body, bg="#85449e")
        left.grid(row=0, column=0, padx=(0, 8))

        ops = [
            ('C', 0, 0, '#a0233a'), ('.', 0, 1, '#9574ca'), ('±', 0, 2, '#9574ca'),
            ('7', 1, 0, "#9574ca"), ('8', 1, 1, '#9574ca'), ('9', 1, 2, '#9574ca'),
            ('4', 2, 0, '#9574ca'), ('5', 2, 1, '#9574ca'), ('6', 2, 2, '#9574ca'),
            ('1', 3, 0, '#9574ca'), ('2', 3, 1, '#9574ca'), ('3', 3, 2, '#9574ca'),
            ('0', 4, 0, '#9574ca'), ('⌫', 4, 2, '#111111'),
        ]
        for (txt, r, c, color) in ops:
            Button(left, text=txt, bg=color, fg="white", font=("Arial", 16, "bold"),
                   width=3, height=1, relief="flat", bd=0,
                   command=lambda t=txt: self._on_left_key(t)
            ).grid(row=r, column=c, padx=3, pady=3)

        op_frame = Frame(left, bg="#441075")
        op_frame.grid(row=5, column=0, columnspan=3, pady=(6, 0))
        self.op_buttons = {}
        for txt in ['+', '-', '×', '÷']:
            b = Button(op_frame, text=txt, bg="#441075", fg="white",
                       font=("Arial", 16, "bold"), width=3, height=1,
                       relief="flat", bd=0,
                       command=lambda t=txt: self._on_op(t))
            b.pack(side="left", padx=3)
            self.op_buttons[txt] = b

        right = Frame(body, bg="#441075")
        right.grid(row=0, column=1)

        Label(right, text="Numerador", bg="#441075", fg="#b2e8e8",
              font=("Arial", 10)).grid(row=0, column=0, columnspan=3)
        num_keys = [
            ('7',1,0),('8',1,1),('9',1,2),
            ('4',2,0),('5',2,1),('6',2,2),
            ('1',3,0),('2',3,1),('3',3,2),
            ('0',4,0),('⌫',4,2),
        ]
        for (txt, r, c) in num_keys:
            Button(right, text=txt, bg="#9574ca" if txt!='⌫' else '#111',
                   fg="white", font=("Arial", 14, "bold"),
                   width=3, height=1, relief="flat", bd=0,
                   command=lambda t=txt: self._on_frac_key('n', t)
            ).grid(row=r, column=c, padx=3, pady=2)

        Label(right, text="Denominador", bg="#441075", fg="#b2e8e8",
              font=("Arial", 10)).grid(row=5, column=0, columnspan=3, pady=(8,0))
        den_keys = [
            ('7',6,0),('8',6,1),('9',6,2),
            ('4',7,0),('5',7,1),('6',7,2),
            ('1',8,0),('2',8,1),('3',8,2),
            ('0',9,0),('⌫',9,2),
        ]
        for (txt, r, c) in den_keys:
            Button(right, text=txt, bg="#9574ca" if txt!='⌫' else '#111',
                   fg="white", font=("Arial", 14, "bold"),
                   width=3, height=1, relief="flat", bd=0,
                   command=lambda t=txt: self._on_frac_key('d', t)
            ).grid(row=r, column=c, padx=3, pady=2)

        bottom = Frame(body, bg="#441075")
        bottom.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="ew")
        Button(bottom, text="Simplificar", bg="#222", fg="white",
               font=("Arial", 12), relief="flat", bd=0,
               command=self._on_simplificar).pack(side="left", padx=4, expand=True, fill="x")
        Button(bottom, text="= OK", bg="#441075", fg="white",
               font=("Arial", 14, "bold"), relief="flat", bd=0,
               command=self._on_calcular).pack(side="left", padx=4, expand=True, fill="x")

        # --- Resultado como fracción ---
        result_frame = Frame(master, bg="#441075", pady=8)
        result_frame.pack(fill="x")
        Label(result_frame, text="Resultado", bg="#441075", fg="#c9a8e8",
              font=("Arial", 10)).pack()

        self.res_num_var = StringVar(value="—")
        self.res_den_var = StringVar(value="")
        res_inner = Frame(result_frame, bg="#441075")
        res_inner.pack()
        Label(res_inner, textvariable=self.res_num_var, bg="#441075", fg="white",
              font=("Arial", 22, "bold")).pack()
        self.res_line = Frame(res_inner, bg="white", height=2)
        Label(res_inner, textvariable=self.res_den_var, bg="#441075", fg="white",
              font=("Arial", 22, "bold")).pack()

    def set_controller(self, controller):
        self.controller = controller

    def update_display(self, num, den, op="", f1_num="", f1_den=""):
        self.num_var.set(num)
        self.den_var.set(den)
        self.op_var.set(f" {op} " if op else "")
        self.f1_num_var.set(f1_num)
        self.f1_den_var.set(f1_den)

    def update_resultado(self, num, den=""):
        self.res_num_var.set(num)
        self.res_den_var.set(den)
        if den:
            self.res_line.pack(fill="x", pady=2)
        else:
            self.res_line.pack_forget()

    def _on_left_key(self, tecla):
        if self.controller:
            self.controller.on_left_key(tecla)

    def _on_op(self, op):
        if self.controller:
            self.controller.on_op(op)

    def _on_frac_key(self, parte, tecla):
        if self.controller:
            self.controller.on_frac_key(parte, tecla)

    def _on_simplificar(self):
        if self.controller:
            self.controller.on_simplificar()

    def _on_calcular(self):
        if self.controller:
            self.controller.on_calcular()