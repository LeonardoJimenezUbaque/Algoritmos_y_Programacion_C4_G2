Algoritmo Inicio_Sueldo_Y_Comision_Ventas
	Escribir "Para saber el total que recibira en el mes escriba lo siguiente:"
	Escribir "Sueldo Base"
	Leer Sueldo_Base
	Escribir "Valor de las ventas realizadas en el mes (3)"
	Escribir "Venta 1"
	Leer Venta_1
	Escribir "Venta 2"
	Leer Venta_2
	Escribir "Venta 3"
	Leer Venta_3
	Comision_Ventas<-(Venta_1+Venta_2+Venta_3)*0.1
	Total<-((Venta_1+Venta_2+Venta_3)*0.1)+Sueldo_Base
	Escribir "Su dinero por comisiones de venta durante el mes es: " Comision_Ventas
	Escribir "El dinero total que recibira en el mes es: "  Total
FinAlgoritmo
