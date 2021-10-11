Algoritmo Inicio_Cambio_Velocidad
	i = 0
	Escribir "¿Cuál es la distancia entre los dos vehiculos?"
	Leer x
    Mientras i = 0 
		Escribir "¿Cúal es la velocidad del vehiculo que va atras?"
		Leer v_0
		Escribir "¿Cuál es la velocidad del vehiculo que va adelante? "
		Leer v_1
		Si v_0 < v_1 o v_0 = v_1 Entonces
			Escribir "--> la velocidad del vehiculo de atras debe ser mayor y diferente que la del de adelante, de otra forma nunca lo alcanzara"
			Escribir "  "
		SiNo
			i = 1
		Fin Si
	fin Mientras
	Tiempo = x/(v_0-v_1) 
	Tm = Tiempo*60
	Escribir "El vehiculo de atras tardará " Tm "m en alcanzar al de adelante"
FinAlgoritmo
