Algoritmo Inicio_Nota_Final
	Escribir "Para conocer cual sera su nota final escriba lo siguiente:"
	Escribir "Nota de primer parcial"
	Leer Nota_Parcial_1
	Escribir "Nota de segundo parcial"
	Leer Nota_Parcial_2
	Escribir "Nota de tercer parcial"
	Leer Nota_Parcial_3
	Nota_Parciales<-((Nota_Parcial_1+Nota_Parcial_2+Nota_Parcial_3)/3)*0.55
	Escribir "Nota de examen final"
	Leer Nota_Examen_Final
	Nota_Examen_Final_Resultado<-Nota_Examen_Final*0.30
	Escribir "Nota trabajo final"
	Leer Nota_Trabajo_Final 
	Nota_Trabajo_Final_Resultado<-Nota_Trabajo_Final*0.15
	Nota_Final<-Nota_Parciales+Nota_Examen_Final_Resultado+Nota_Trabajo_Final_Resultado
	Escribir "Su nota final es: " Nota_Final
FinAlgoritmo
