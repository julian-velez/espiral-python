import turtle

# Configurar la ventana
window = turtle.Screen()
window.bgcolor("white")

# Crear la "tortuga"
spiral = turtle.Turtle()
spiral.shape("turtle")
spiral.color("blue")
spiral.speed(5)  # Velocidad de dibujo (1 es lento, 10 es rápido)

# Dibujo de la espiral
for i in range(50):  # Puedes ajustar el rango para una espiral más larga
    spiral.forward(i * 10)  # Avanza cada vez un poco más lejos
    spiral.right(45)        # Gira a la derecha un ángulo fijo

# Finalizar y cerrar la ventana al hacer clic
window.exitonclick()
