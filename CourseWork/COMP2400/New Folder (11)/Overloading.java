/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Asignacion 6 - Metodos Sobrecargados 
2022-11-20
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscar�n  el m�dulo 12. Ver�n las lecciones 13 y 14. 
Copiaran el ejemplo 14.6 M�todos sobrecargados que se encuentra en las p�ginas 8 a la 9 de la lecci�n 14.
Documente el c�digo describiendo sus distintas partes utilizando comentarios. 
Despu�s que vea su perfecto entregue aqu� el c�digo (.java) del programa. 
Tambi�n entregue un �print screen� del c�digo y la ejecuci�n del programa.
*/

//Overloading.java
//Demonstrating an overloaded constructor and common method of overloading
//import java.util.*;

//Class Declaration section 
class Tree
{

 int height;

//Constructor that prints out a message and sets the height as 0
 Tree()
 {
 
    prt("Planting a seedling");
    
    height = 0;
 
 }

//Overloaded constructor that prints out a message and takes in an argument that will initialize the height to the value of i 
 Tree(int i)
 {
 
    prt("Creating new Tree that is " + i + " feet tall");
    
    height = i;
 
 }

//Prints out a message that indicates the value of height 
 void info()
 {
 
   prt("Tree is " + height + " feet tall");
 
 }

//Overloaded - Prints out a message that indicates the value of height that was received as an argument 
 void info(String s)
 {
 
   prt(s + ": Tree is " + height + " feet tall");
 
 }

//Prints out the string using a common overloaded method 
 static void prt(String s)
 {
 
   System.out.println(s);
 
 }
 
}

//Overloading.java

public class Overloading
{

 public static void main(String[] args)
 {

//Using a loop to cycle through the creation and and initialization of the created object using constructor, 
//overloaded constructor, and overloaded common method 
 for(int i = 0; i < 5; i++)
 {
 
    Tree t = new Tree(i);
 
    t.info();
    
    t.info("overloaded method");
 
 }
 
// Overloaded constructor
 new Tree();
 
 }
} //end