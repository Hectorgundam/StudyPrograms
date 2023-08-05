//Charleen Ramirez Rios 
//R00417213
//Upload Assignment: Asignación 2: Format()
//2022-10-17
//COMP2400 - 202310-70846
//Dr. Edgardo Vargas Moya

//Programa formatos.java

//Importing Scanner utility so that we can read user input from the keyboard
import java.util.Scanner;

public class ScannerAndStrings
{

public static void main(String args[])
{

//Declaring a scanner called teclado that we can use to read input from the user 
Scanner teclado = new Scanner(System.in);

//Declaring variables that will be used to store values 
double userDecimal; 

float userFloats; 

int userInt; 

boolean userBool; 

String noSpaceWord, 
       spaceWord, 
       str1; 
       
//Asking user for a double, reading user input from keyboard and assigning the value to the variable userDecimal
System.out.print("Enter a double: ");
userDecimal = teclado.nextDouble(); 

//Asking user for a float, reading the user's input from keyboard and assigning the value to the variable userFloats
System.out.print("Enter a float: ");
userFloats = teclado.nextFloat(); 

//Asking the user for an int, reading the user's input from keyboard and assigning the value to the variable userInt
System.out.print("Enter a integer: ");
userInt = teclado.nextInt(); 

//Asking the user for a boolean, reading the user's input from keyboard and assigning the value to the variable userBool
System.out.print("Enter a boolean value: ");
userBool = teclado.nextBoolean(); 

//Asking the user for a string without blank spaces, reading the user's input from keyboard and assigning the value to the variable noSpaceWord
System.out.print("Enter a word without including blank spaces: ");
noSpaceWord = teclado.next();
str1 = teclado.nextLine(); 

//Asking the user for a string with blank spaces, reading the user's input from keyboard and assigning the value to the variable spaceWord
System.out.print("Enter a word that includes a blank space: ");
spaceWord = teclado.nextLine();

//Printing out values to the screen 

System.out.println("\nPrinting out the values here:");

System.out.println("The word with spaces you entered was =[" + spaceWord + "]");

System.out.println("The word without spaces you entered was =[" + noSpaceWord + "]");

System.out.println("The boolean you entered was =[" + userBool + "]");

System.out.println("The integer you entered was =[" + userInt + "]");

System.out.println("The float you entered was =[" + userFloats + "]");

System.out.println("The double you entered was =[" + userDecimal + "]");

}

}
