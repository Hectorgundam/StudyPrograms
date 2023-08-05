/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio#3 Clase Automovil
2022-10-24
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscaran el modulo 9 y leeran la leccion 10B. Luego haran lo siguiente: 
- Copiaran la Clase Automovil y la Clase Carrito (en archivos separados, pero en una misma carpeta) que se encuentra en las paginas 2 a la 3.
- Documente el codigo describiendo sus distintas partes utilizando comentarios. 
- Despues que vea su perfecto funcionamiento entregue aqui e; codigo (.java) del programa.
- Entregue un "print screen" del codigo y la corrida del programa. 

*/
 
 //Carrito.java
 
 //Class declaration 
 class Automovil{
 
 //Variable declaration
 int velocidad, 
      pasajeros; 
 boolean encendido; 
 
 //Assigns a preset value to our variables 
 Automovil()
 {
 
 velocidad = 0; 
 pasajeros = 4; 
 encendido = false; 
 
 }
 
 //Takes in the values contained within the arguments parameters and assigns them to the variables within our class 
 Automovil(int v, int p, boolean e)
 {
 
 velocidad = v; 
 pasajeros = p; 
 encendido = e; 
 
 }
 
 //Increasing the current value of velocidad by the current value of incremento and the resulting value is assigned to the variable velocidad 
 void acelerar()
 {
 
 velocidad = velocidad + 5; 
 
 }
 
 //Increasing the current value of velocidad by the current value of incremento and the resulting value is assigned to the variable velocidad 
 void acelerar(int incremento)
 {
 
 velocidad = velocidad + incremento; 
 
 }
 
 //When called it prints out the message to the screen 
 public String toString()
 {
 
 return ("Velocidad = " + velocidad + "\npasajeros = " + pasajeros + "\nencendido = " + encendido);
 
 }
 
 }