# 🧮 Calculadora de Fracciones

Calculadora de fracciones con interfaz gráfica desarrollada en Python con Tkinter, usando arquitectura **MVC (Modelo-Vista-Controlador)**.

---

## 📋 Descripción

Permite realizar operaciones aritméticas básicas entre fracciones — suma, resta, multiplicación y división — mostrando los resultados en formato de fracción real (numerador sobre denominador) y simplificados automáticamente.

---

## ✨ Funcionalidades

- Entrada de fracciones por teclado separado (numerador y denominador)
- Operaciones: suma, resta, multiplicación y división
- Simplificación automática del resultado
- Botón de simplificación manual de la fracción activa
- Visualización del resultado en formato fracción real
- Manejo de errores: división entre cero, denominador cero

---

## 🗂️ Estructura del proyecto

```
Proyecto #1/
├── main.py                  # Punto de entrada
├── models/
│   ├── __init__.py
│   └── model.py             # Clase Fraccion 
├── views/
│   ├── __init__.py
│   └── view.py              # Interfaz gráfica con Tkinter
└── controllers/
    ├── __init__.py
    └── controller.py        # Conexión entre Model y View
```

---

## 🏗️ Arquitectura MVC

| Capa | Archivo | Responsabilidad |
|------|---------|-----------------|
| **Model** | `models/model.py` | Aritmética de fracciones, simplificación con algoritmo de Euclides |
| **View** | `views/view.py` | Interfaz gráfica, botones, display visual de fracciones |
| **Controller** | `controllers/controller.py` | Maneja eventos, parsea entradas, conecta Model y View |

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)

---

## 🚀 Instalación y uso

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/calculadora-fracciones.git
cd calculadora-fracciones
```

2. Ejecuta el proyecto:
```bash
python main.py
```

> No requiere instalar dependencias externas.

---
