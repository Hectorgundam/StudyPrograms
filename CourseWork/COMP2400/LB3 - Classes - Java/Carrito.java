/*
Upload Assignment: Laboratorio#3 Clase Automovil
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
 
 public class Carrito{
 
 public static void main(String [] args){
 
 //Creating an object of class Automovil
 Automovil miCarro = new Automovil(); 
 
 //Printing the current content within our object 
 System.out.println(miCarro); 
 
 //Creating an object of class Automovil while passing speciic values as its parameter arguments
 Automovil tuCarro = new Automovil(0,6,true); 
 
 //Printing out the current content within our object 
 System.out.println(tuCarro); 
 
 //Using acelerar within our object to increase its value vy the present amount of 5
 tuCarro.acelerar(); 
 
 //Printing out the current content within our object 
 System.out.println(tuCarro); 
 
 //Using acelerar(parameter) by passing a specific value as its argument for incremento
 miCarro.acelerar(30); 
 
 //Printing out the current contents within our object 
 System.out.println(miCarro); 
 
 }
 
 }