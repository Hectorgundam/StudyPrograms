/*
Upload Assignment: Laboratorio#2 Clase Bola
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscaran el modulo 9 y leeran la leccion 10. Luego haran lo siguiente: 
- Copiaran la Clase Bola y la Clase Ejemplo (en archivos separados, pero en una misma carpeta) que encuentra en las paginas 5 y 6. 
- Documente el codigo describiendo sus distintas partes utilizando comentarios. 
- Despues que vea su perfecto funcionamiento entregue aqui e; codigo (.java) del programa.
- Entregue un "print screen" del codigo y la corrida del programa. 

*/
 
 public class Ejemplo{
 
 public static void main (String args[]){
 
 //Declaring an obkect using the class Bola.  This one uses the one that doesn't require arguments
 Bola bola1 = new Bola(); 
 
 //Declaring an object using the class Bola.  The numbers within the parenthesis are passed on as arguments
 Bola bola2 = new Bola(3, 5);
 
 //Objects 1 and 2 are being printed onto the screen 
 System.out.println("Bola1:\n" + bola1);
 System.out.println("Bola2:\n" + bola2);
 
 //The value of the radio is received as an argument within the parenthesis 
 bola1.setRadio(9); 
 
 //The factor is obtained using the current value of factor that is being passed as an argument 
 bola2.ampliarRadio(5.2f); 
 
 //Objects 1 and 2 are being printed onto the screen 
 System.out.println("Bola1:\n" + bola1);
 System.out.println("Bola2:\n" + bola2);
 
 }
 
 }