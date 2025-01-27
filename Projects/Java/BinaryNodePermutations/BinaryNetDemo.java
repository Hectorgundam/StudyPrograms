/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio #11 - Recursion y Otras Estructuras 
2023-05-13
COMP2900 - 202330-60188
Dr. Edgardo Vargas Moya

Assignment: 
Leerán la lección 11 “Recursión” y la lección 13 “Otras Estructuras” que están en el Módulo 12
También leerán la presentación “Estructuras de Datos No Lineales Grafos” en la carpeta de 
Material Suplementario.

Luego haga lo siguiente:
Copie el ejemplo (BNode y BinaryNetDemo2) de las páginas 6 a la 9 de la lección 13
Utilizando comentarios (//) describa en forma corta “cada línea” de código del programa

*/

//Class declaration for BNode
class BNode{
   
   //Variable declarations
   char caracter;
   BNode leftPtr,
   rightPtr;
   
   //Constructor for class BNode
   BNode(char c, BNode lft, BNode rght)
   {
   
      caracter = c;
      leftPtr = lft;
      rightPtr = rght;
      
   }
   
   //Overloaded constructor
   BNode (char c)
   {
   
      this(c,null,null);
      
   }
   
   //Method to edit the characters within the nodes of the tree 
   protected void editNodeInNet(String path, char c){
   
      //Variable declaration
      BNode tempPtr;
      int i,
      strLength = 0;
      boolean validPath = true;
      
     
      //If the current node is not empty/null we start by assigning the current node to our tempPtr
      if (this != null)
      {
         //Assigning the current node to our tempPtr and determining the length to be used for the loop
         strLength = path.length();
         tempPtr = this;
         
         //Using a for loop to cycle through the contents of the string until it reaches null
         for (i = 0; (i < strLength) && (validPath); i++){
         
            //Analyzing the contents of the string and updating the values using tempPtr
            //If it's 'L' then we update the left child node
            if (path.charAt(i) == 'L')
            {
            
               tempPtr = tempPtr.leftPtr;
               
            }
            else if (path.charAt(i) == 'R')
            {
               //If it's 'R' we update the right child node
               tempPtr = tempPtr.rightPtr;
               
            }
            else
            {
            
               //The character is not 'L' or 'R' then it means the path is invalid and loop ends
               validPath = false;
               
            }
            if ((tempPtr == null) && (i < strLength - 1))
            {
            
               //Checking to see if null is reached within the string and stops the loop
               validPath = false;
               
            }
         }
         
         //If a valid node is reached the contents are substituted / replaced
         //If the loop finished cycling through the specified path and reached a valid node then it updates
         //the character 
         if (i == strLength)
         {
         
            tempPtr.caracter = c;
            
         }
      }
      else
      {
      
         //The net is empty / null and we do nothing 
         
      }
   }
}

//Class declaration for BinaryNetDemo
public class BinaryNetDemo{

   //Main function for our program
   public static void main(String[] args){
   
      //Variable declaration
      BNode root = new BNode('A');
      BNode tempPtr;
      
      //Assigning content to the tree
      //The structure is built by assigning child nodes to parent nodes and so forth
      root.rightPtr = new BNode('E');
      root.rightPtr.leftPtr = root;
      root.leftPtr = new BNode('B');
      root.leftPtr.rightPtr = root.rightPtr;
      root.rightPtr.rightPtr = new BNode('D');
      root.rightPtr.rightPtr.rightPtr = root.leftPtr;
      root.leftPtr.leftPtr = new BNode('C');
      root.leftPtr.leftPtr.leftPtr = root;
      root.leftPtr.leftPtr.rightPtr =
      root.leftPtr.rightPtr.rightPtr;
      
      //Following code prints out the contents of the nodes before and after modifications
      //Different routes are being used to print out the content before being modified and to modify
      //them, that way it demonstrates the method that allows us to access the nodes from any route
      tempPtr = root.rightPtr.leftPtr.leftPtr.leftPtr;
      System.out.println(tempPtr.caracter);
      root.editNodeInNet("LL", 'X');
      System.out.println(tempPtr.caracter);
      
      tempPtr = root.leftPtr.leftPtr.rightPtr;
      System.out.println(tempPtr.caracter);
      
      root.editNodeInNet("LRLLRR", 'W');
      System.out.println(tempPtr.caracter);
      
      root.editNodeInNet("", 'M');
      System.out.println(root.caracter);
   
   }
}
