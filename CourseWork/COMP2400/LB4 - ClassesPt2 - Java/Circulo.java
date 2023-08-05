/*
Upload Assignment: Laboratorio#3 Clase Circulo
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscaran el modulo 9 y leeran nuevamente las lecciones 10 y 10B. Luego haran lo siguiente: 
- Realice el ejercicio 2 que se encuentra en la ultima pagina de la lectura 10B Clase Automovil
- Documente el codigo describiendo sus distintas partes utilizando comentarios. 
- Despues que vea su perfecto funcionamiento entregue aqui e; codigo (.java) del programa.
- Entregue un "print screen" del codigo y la corrida del programa. 

Ejercicion 2: 
- Escriba un programa que cree la clase Circulo. 
- La clase tendra dos constructores
   - Uno para crear un circulo con un radio por defecto igual a 5 
   - Otro en donde se pueda especificar el radio deseado
- La clase tendra un metodo que devuelve su area y otro que devuelva su perimetro
- El codigo del programa debera crear objetos de la clase Circulo y demostrar que todos sus componentes funcionan de forma adecuada


Program needs to read radio
- Calculate area 
- Calculate perimeter
*/
 
//Class declaration for Circulo
class Circulo{

//Variable declaration for our class 
private double radio, 
               perimeter, 
               area; 
       
//Assigning the values for our 2 variables, works sort of as a preset in a way 
Circulo(){

radio = 1; 
perimeter = 2; 

}

//Assigning the values of our variables radio, perimeter and are to our class 
Circulo (double r, double p, double a){

radio = r; 
perimeter = p; 
area = a;

}

//Assigning the value for our perimeter variable 
void setPerimeter(double p){

perimeter = p; 

}

//Calculating the perimeter of the circle using the formula perimeter = 2 * PI * radius
double getPerimeter()
{

perimeter = ( 2 * java.lang.Math.PI) * radio; 

return perimeter; 

}

//Assigning the value of our radio variable 
double setRadio(double r){

radio = r;

return radio;

}

//Obtaining and storing the value of the radio variable 
double getRadio(){

return radio; 

}

//Calculating the area of the circle using the formula area = PI * radio * radio 
void calculateArea(){

area =  java.lang.Math.PI * (radio * radio); 

}

//Returning the message that will be printed onto the screen 
public String toString()
{

return ("radio = " + radio + "\nperimeter = " + perimeter + "\narea = " + area);

}

}