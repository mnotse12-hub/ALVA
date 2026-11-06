# ALVA - Resolutor de los 40 problemas del dossier
# Proyecto escolar: uso de las matemáticas en contextos técnicos y académicos

def resolver_problema(n):
    # Convierte la entrada a número por si llega como texto desde el cuaderno.
    try:
        n = int(str(n).strip())
    except (TypeError, ValueError):
        print("Número de problema no válido. Escribe un número del 1 al 40.")
        return

    if n == 1:
        x = 120 * 7 / 4
        print("Problema 1. Proporción de piezas")
        print("120 piezas en 4 horas; buscamos piezas en 7 horas.")
        print("x = (120 * 7) / 4")
        print(f"x = {x:.0f} piezas")

    elif n == 2:
        x = 2 * 175 / 50
        print("Problema 2. Escala de un plano")
        print("2 cm en el plano representan 50 cm reales.")
        print("x = (2 * 175) / 50")
        print(f"x = {x:g} cm en el plano")

    elif n == 3:
        x = 3 * 8 / 2
        print("Problema 3. Mezcla para un proceso")
        print("3 L de agua por cada 2 L de producto; se usan 8 L de producto.")
        print("x = (3 * 8) / 2")
        print(f"x = {x:g} L de agua")

    elif n == 4:
        x = 20 * 600 / 40
        print("Problema 4. Engranajes")
        print("20 dientes a 600 rpm; el engranaje B tiene 40 dientes.")
        print("20 * 600 = 40 * x")
        print(f"x = (20 * 600) / 40 = {x:g} rpm")

    elif n == 5:
        x = 3.5 * 100
        print("Problema 5. Conversión de longitud")
        print("3.5 m * 100 cm/m")
        print(f"Resultado: {x:g} cm")

    elif n == 6:
        x = 2.5 * 1000
        print("Problema 6. Conversión de corriente")
        print("2.5 A * 1000 mA/A")
        print(f"Resultado: {x:g} mA")

    elif n == 7:
        seconds = 45 * 8
        minutes = seconds / 60
        print("Problema 7. Tiempo de producción")
        print("45 s por pieza * 8 piezas = 360 s")
        print(f"360 / 60 = {minutes:g} minutos")

    elif n == 8:
        x = 2.5 * 1000
        print("Problema 8. Conversión de potencia")
        print("2.5 kW * 1000 W/kW")
        print(f"Resultado: {x:g} W")

    elif n == 9:
        c = 80
        f = c * 9 / 5 + 32
        print("Problema 9. Conversión de temperatura")
        print("F = (C * 9/5) + 32")
        print(f"F = (80 * 9/5) + 32 = {f:g} °F")

    elif n == 10:
        x = (950 - 250) / 35
        print("Problema 10. Costo de materiales")
        print("250 + 35x = 950")
        print("x = (950 - 250) / 35")
        print(f"x = {x:g} piezas")

    elif n == 11:
        x = 25 - 8
        print("Problema 11. Longitud de un cable")
        print("x + 8 = 25")
        print(f"x = 25 - 8 = {x:g} m")

    elif n == 12:
        x = (250 - 50) / 2
        y = x + 50
        print("Problema 12. Producción diaria")
        print("x + (x + 50) = 250")
        print(f"x = (250 - 50) / 2 = {x:g}")
        print(f"Segunda máquina = x + 50 = {y:g} piezas")

    elif n == 13:
        t = 25 + 15 * 8
        print("Problema 13. Temperatura de un horno")
        print("T = 25 + 15x")
        print(f"T = 25 + 15(8) = {t:g} °C")

    elif n == 14:
        i = 12 / 4
        print("Problema 14. Corriente eléctrica")
        print("I = V / R = 12 / 4")
        print(f"I = {i:g} A")

    elif n == 15:
        r = 24 / 2
        print("Problema 15. Resistencia")
        print("R = V / I = 24 / 2")
        print(f"R = {r:g} Ω")

    elif n == 16:
        v = 3 * 10
        print("Problema 16. Voltaje")
        print("V = I * R = 3 * 10")
        print(f"V = {v:g} V")

    elif n == 17:
        p = 120 * 2
        print("Problema 17. Potencia eléctrica")
        print("P = V * I = 120 * 2")
        print(f"P = {p:g} W")

    elif n == 18:
        r = 4 + 6 + 10
        print("Problema 18. Resistencias en serie")
        print("Rt = 4 + 6 + 10")
        print(f"Rt = {r:g} Ω")

    elif n == 19:
        y = 25 * 6
        print("Problema 19. Producción por hora")
        print("Función: y = 25x")
        print(f"y = 25(6) = {y:g} piezas")

    elif n == 20:
        d = 2 * 15
        print("Problema 20. Distancia recorrida")
        print("d = v * t = 2 * 15")
        print(f"d = {d:g} m")

    elif n == 21:
        c = 100 + 20 * 15
        print("Problema 21. Costo de fabricación")
        print("C = 100 + 20x")
        print(f"C = 100 + 20(15) = ${c:g}")

    elif n == 22:
        x = 40 * 5
        print("Problema 22. Interpretación de una gráfica")
        print("La máquina produce 40 piezas por hora.")
        print(f"40 * 5 = {x:g} piezas")

    elif n == 23:
        t = 30 + 10 * 7
        print("Problema 23. Función de temperatura")
        print("T = 30 + 10x")
        print(f"T = 30 + 10(7) = {t:g} °C")

    elif n == 24:
        # x resistencias, y sensores: x+y=10; 5x+20y=125
        y = (125 - 5 * 10) / (20 - 5)
        x = 10 - y
        print("Problema 24. Compra de componentes")
        print("x + y = 10; 5x + 20y = 125")
        print(f"y = (125 - 50) / 15 = {y:g}")
        print(f"x = 10 - {y:g} = {x:g}")
        print(f"Respuesta: {x:g} resistencias y {y:g} sensores")

    elif n == 25:
        x = (90 - 10) / 2
        y = x + 10
        print("Problema 25. Motores")
        print("x + y = 90; y = x + 10")
        print(f"x = (90 - 10) / 2 = {x:g}")
        print(f"y = x + 10 = {y:g} piezas/h")

    elif n == 26:
        x = (40 - 6) / 2
        y = x + 6
        print("Problema 26. Edades de dos técnicos")
        print("x + y = 40; y = x + 6")
        print(f"x = (40 - 6) / 2 = {x:g}")
        print(f"y = x + 6 = {y:g} años")

    elif n == 27:
        x = (30 - 8) / 2
        y = x + 8
        print("Problema 27. Resistencias")
        print("x + y = 30; y = x + 8")
        print(f"x = (30 - 8) / 2 = {x:g}")
        print(f"y = x + 8 = {y:g} Ω")

    elif n == 28:
        x = 60 * 8 / 3
        print("Problema 28. Proporcionalidad directa")
        print("60 / 3 = x / 8")
        print(f"x = (60 * 8) / 3 = {x:g} piezas")

    elif n == 29:
        x = 4 * 12 / 6
        print("Problema 29. Proporcionalidad inversa")
        print("4 * 12 = 6 * x")
        print(f"x = (4 * 12) / 6 = {x:g} horas")

    elif n == 30:
        d = 3 * 20
        t = d / 5
        print("Problema 30. Velocidad y tiempo")
        print(f"Distancia: d = 3 * 20 = {d:g} m")
        print(f"Tiempo nuevo: t = d / 5 = {t:g} s")

    elif n == 31:
        x = 5 * 10 / 10
        print("Problema 31. Personal de producción")
        print("5 * 10 = 10 * x")
        print(f"x = (5 * 10) / 10 = {x:g} horas")

    elif n == 32:
        x = 10 + (6 - 1) * 5
        print("Problema 32. Producción")
        print("a_n = a_1 + (n - 1)d")
        print(f"a_6 = 10 + (6 - 1)(5) = {x:g} piezas")

    elif n == 33:
        x = 100 + (5 - 1) * 50
        print("Problema 33. Patrón de programación")
        print("a_n = a_1 + (n - 1)d")
        print(f"a_5 = 100 + (5 - 1)(50) = {x:g} datos")

    elif n == 34:
        base = 800
        interval = 200
        print("Problema 34. Mantenimiento")
        print("Horas actuales: 800; mantenimiento cada 200 h.")
        for k in range(1, 4):
            print(f"Mantenimiento {k}: {base + interval * k} horas")

    elif n == 35:
        a = 12 * 8
        print("Problema 35. Área de una pieza")
        print("A = largo * ancho = 12 * 8")
        print(f"A = {a:g} cm²")

    elif n == 36:
        v = 40 * 30 * 20
        print("Problema 36. Volumen de una caja")
        print("V = largo * ancho * alto = 40 * 30 * 20")
        print(f"V = {v:g} cm³")

    elif n == 37:
        p = 24 * 5
        print("Problema 37. Potencia eléctrica")
        print("P = V * I = 24 * 5")
        print(f"P = {p:g} W")

    elif n == 38:
        # x^2 + 3x - 40 = 0; raíces -8 y 5, se toma la positiva
        ancho = 5
        largo = ancho + 3
        print("Problema 38. Área de una pieza")
        print("x(x + 3) = 40")
        print("x² + 3x - 40 = 0")
        print("(x + 8)(x - 5) = 0")
        print("Soluciones: x = -8 o x = 5; se descarta la negativa.")
        print(f"Ancho = {ancho} cm; largo = {largo} cm")

    elif n == 39:
        # h = -t^2 + 6t, vertex at t=-b/(2a)
        t = -6 / (2 * -1)
        h = -(t ** 2) + 6 * t
        print("Problema 39. Trayectoria de un objeto")
        print("h = -t² + 6t")
        print(f"t máximo = -b/(2a) = -6/(2*(-1)) = {t:g}")
        print(f"h = -({t:g}²) + 6({t:g}) = {h:g} m")
        print(f"Altura máxima = {h:g} m")

    elif n == 40:
        ancho = 6
        largo = ancho + 2
        print("Problema 40. Diseño de un área de trabajo")
        print("x(x + 2) = 48")
        print("x² + 2x - 48 = 0")
        print("(x + 8)(x - 6) = 0")
        print("Soluciones: x = -8 o x = 6; se descarta la negativa.")
        print(f"Ancho = {ancho} m; largo = {largo} m")
        print(f"Área = {ancho} * {largo} = {ancho*largo} m²")

    else:
        print("Número de problema no válido. Elige del 1 al 40.")


def mostrar_menu():
    print("\n" + "=" * 45)
    print("             ALVA - DOSSIER")
    print("       Resolución de 40 problemas")
    print("=" * 45)
    print("Escribe el número del problema que quieres resolver.")
    print("Escribe 0 para salir.")
    print("-" * 45)
    for inicio, fin, tema in [
        (1, 4, "Razones y proporciones"),
        (5, 9, "Conversiones y regla de tres"),
        (10, 13, "Ecuaciones lineales"),
        (14, 18, "Ley de Ohm y circuitos"),
        (19, 23, "Gráficas y funciones"),
        (24, 27, "Sistemas de ecuaciones"),
        (28, 31, "Proporcionalidad directa e inversa"),
        (32, 34, "Sucesiones y patrones"),
        (35, 37, "Fórmulas con varias variables"),
        (38, 40, "Ecuaciones cuadráticas y aplicaciones"),
    ]:
        print(f"{inicio:02d}-{fin:02d} | {tema}")


def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nNúmero de problema: "))
        except ValueError:
            print("Por favor, escribe un número entero.")
            continue

        if opcion == 0:
            print("¡Gracias por usar ALVA!")
            break

        if 1 <= opcion <= 40:
            print("\n" + "-" * 45)
            resolver_problema(opcion)
            print("-" * 45)
        else:
            print("Opción inválida. Selecciona un problema del 1 al 40, o 0 para salir.")


if __name__ == "__main__":
    main()
