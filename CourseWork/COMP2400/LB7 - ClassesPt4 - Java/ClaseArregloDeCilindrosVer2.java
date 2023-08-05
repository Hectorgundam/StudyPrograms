/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio 6 - Arreglos de Objetos
2022-12-06
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscarán el módulo 15
Lean la lección 17 y vean los cuatro demos allí contenidos

Luego haga lo siguiente:
Realice el ejercicio 1 que se encuentra en página 11
Documente el código describiendo sus distintas partes utilizando comentarios
Recuerde participar en el foro de discusión correspondiente
Después que vea su perfecto funcionamiento entregue aquí el código (.java) del programa
También entregue un “print screen” del código y la corrida del programa

Modulo 15 - Leccion 17 - Ejercicio 1
Disene una clase Cilindro que tenga de atributos radio y altura, un constructor con el que se puedan 
establecer los valores de ambos atributos y los metodos getRadio(), getAltura(), setRadio(),, setAltura(). 
La clase tendra ademas el metodo toString() que devolvera un string que indica los valores de sus atributos. 
Cree dos objetos de clase Cilindro (cilindroA) y )cilindroB). Muestre en la pantalla el contenido de los 
atributos de uno de los objetos y muestre en la pantalla el contenido del otro. Explique detalladamente lo 
que ocurre durante todo el programa de forma que se vizualize claramente lo que ocurre con los apuntadores. 
Utilice diagramas para apoyar su explicacion. 

*/

//Libraries used 
import java.util.Scanner;

//Class declaration for Cilindro 
class Cilindro
{
   
  //Variable declaration for radio and altura
  double radio;
  double altura;
  
  //Constructor for Cilindro that helps declare and assign a value to our radio and altura 
  Cilindro()
  {
    //Variable radio and altura are being assigned a value of 1 inside the constructor 
    radio = 1;
    altura = 1; 
    
  }
  
  //Overloaded constructor that allows us to use the values entered by the user for the radio and altura 
  //This will use pointers that point to the location that radio and altura are in 
  Cilindro(double radio, double altura)
  {
  
    //The pointer radio wil point to the location of radio and the pointer altura will point to the location of altura
    this.radio = radio;
    this.altura = altura; 
 
  }
  
  //Will fetch and return the value of radio
  double getRadio()
  {
    return(radio);
  }
  
  //Will fetch and return the value of altura 
  double getAltura()
  {
    return(altura); 
  }
   
  //Prints on to the string the values of the elements in our class 
  public String toString()
  {
    //String that will be used to print onto the screen
    String str;
    
    //Our string will contain the values of the elements in the order specified within 
    str = "radio: " + radio + " altura: " + altura;
    
    //Return the contents of the string
    return(str); 
    
  }
}
  
//ClaseArregloDeCilindrosVer2 class 
public class ClaseArregloDeCilindrosVer2
{

  //Creating a static Cilindro object 
  static Cilindro[] leeDatosDeCilindros()
  {
  
    //Declaring a scanner element to read user input 
    Scanner teclado = new Scanner(System.in);

    //Variable declaration
    int radioTemp,
        alturaTemp,
        totalDeCilindros;
    
    //Declaring an array object of Cilindro called listaDeCilindros, note that the array was not created, only the pointer for it was created 
    Cilindro listaDeCilindros[];

    //Asking the user to enter how many items they would like to enter, reading the user input and assigning it to totalDeCilindros
    System.out.print("For how many Cilindros would you like to enter the information for? ");
    totalDeCilindros = teclado.nextInt();
    
    //Creating the array listaDeCilindros that is the size of the value contained within totalDeCilindros 
    listaDeCilindros = new Cilindro[totalDeCilindros];
    
    //Using a loop to cycle through the array as long as the value of i is less than the value that was entered by the user
    //Note that the value entered by the user was to determine the size of the array 
    for (int i = 0; i < totalDeCilindros; i++)
    {
    
      //Asking the user to enter the radio for the current value of i Cilinder, reading the user input and assigning it radioTemp
      System.out.print("esfera[" + i + "].radio = ");
      radioTemp = teclado.nextInt();
      
      //Asking the user to enter the altura for the current value of i Cilinder, reading the user input and assigning it to alturaTemp
      System.out.print("esfera[" + i + "].altura = ");
      alturaTemp = teclado.nextInt(); 
      
      //Within the listaDeCilindros location i a new array of class Cilindro is created and the values of the variables radioTemp, alturaTemp and colorTemp
      //are passed as arguments 
      listaDeCilindros[i] = new Cilindro(radioTemp, alturaTemp);
    }
    
    //Return the listaDeCilindros array 
    return(listaDeCilindros);
  }

  //Main function 
  public static void main(String[] args)
  {
  
    //Declaring a scanner element to read user input 
    Scanner teclado = new Scanner(System.in);
    
    //Variable declaration
    int    totalDeCilindros,
           radioTemp, 
           alturaTemp;
        
    //An object of class 
    //Declaring an array object of Cilindro called arregloDeCilindros, note that the array was not created, only the pointer for it was created 
    Cilindro arregloDeCilindros[];
           
    //Declaring        
    Cilindro cilindroA[], 
             cilindroB[]; 
    
    //The cilindroA is equal to the information returned by the method leeDatosDeCilindros, which allowed it to read and store the values for each 
    //element that were provided by the user 
    System.out.println("Lets start by inputting the information for cilindroA");
    cilindroA = leeDatosDeCilindros(); 
    
    //The cilindroB is equal to the information returned by the method leeDatosDeCilindros, which allowed it to read and store the values for each 
    //element that were provided by the user 
    System.out.println("\nNow lets input the information for cilindroB");
    cilindroB = leeDatosDeCilindros(); 
    
    System.out.println("\nPrinting the contents of cilindroA");
    
    //Using a loop to cycle through the items within the arrays and print them onto the screen
    for(int i = 0; i < cilindroA.length; i++)
    {
    
      //Printing out the contents within cilindroA 
      System.out.println("The contents of cilindroA[" + i + "] are: " + cilindroA[i]);
    
    }
    
    System.out.println("\nPrinting the contents of cilindroB");
    
    for(int j = 0; j < cilindroB.length; j++) 
    {
    
      //Printing out the contents within cilindroB 
      System.out.println("The contents of cilindroB[" + j + "] are: " + cilindroB[j]);
    
    }
  
}

}