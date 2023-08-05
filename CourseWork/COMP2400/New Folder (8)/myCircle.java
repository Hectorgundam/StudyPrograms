/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio#3 Clase Circulo
2022-10-30
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
- Create a circle with a set radius 

- Create a circle with a desired radius (not from user it seems) 
- Calculate area 
- Calculate perimeter
*/
 
public class myCircle{
 
public static void main (String args[]){
 
//Declaring objects using the class Circulo
Circulo circulo1 = new Circulo(); 
 
Circulo circulo2 = new Circulo();

//Preset value circle 
//Calculating the area of our circulo1 object 
circulo1.calculateArea(); 

//Calculating the perimeter of our circulo1 object 
circulo1.getPerimeter();

//Desired value circle
//The value of the desired radio is received as an argument within the parenthesis
circulo2.setRadio(9); 
 
//Calculating the area of our circulo2 object 
circulo2.calculateArea(); 

//Calculating the perimeter of our circulo2 object 
circulo2.getPerimeter();

//Objects 1 and 2 are being printed onto the screen 
System.out.println("\ncirculo1:\n" + circulo1);
System.out.println("\ncirculo2:\n" + circulo2);
 
 }
 
 }