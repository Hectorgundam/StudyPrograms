//Charleen Ramirez Rios 
//R00417213
//Upload Assignment: Asignacion 6: Aritmetica
//2022-10-2
//COMP2400 - 202310-70846
//Dr. Edgardo Vargas Moya

//Programa Aritmetica.java

import java.io.*;
public class Aritmetica {
public static void main (String args[])
 throws IOException {
BufferedReader in = new BufferedReader( new
 InputStreamReader( System.in));
 
//Declaring variables that will be used 
int entero1, //int entero1;
 entero2, //int entero2;
 suma; //int suma;

double real1, //double real1;
 real2, //double real2;
 cociente; //double cociente;
 
 //Asking user to enter a number, reading the user's entry and assigning the value to entero1 
System.out.print("Entre un numero entero: ");

entero1 = Integer.valueOf(in.readLine()).intValue();

 //Asking user to enter a number, reading the user's entry and assigning the value to entero2
System.out.print("Entre un otro numero entero: ");

entero2 = Integer.parseInt(in.readLine());

//Adding the values of entero1 and entero2 and assigning the resulting value to suma
suma = entero1 + entero2;

//Printing out the value of suma to the screen for the user to see the result of the sum 
System.out.println("Entero1 + Entero2 =" + suma);

//Asking user to enter a number, reading the user's entry and assigning the value to real1
System.out.print("Entre un numero real: ");

real1 = Double.valueOf(in.readLine()).doubleValue();

//Asking user to enter a number, reading the user's entry and assigning the value to real2
System.out.print("Entre otro numero real: ");

real2 = Double.valueOf(in.readLine()).doubleValue();

//Dividing real1 by real2 to determine the coefficient and assigning the resulting value to cociente 
cociente = real1 / real2;

//Printing out the value of cociente to the screen for the user to see the result of the coefficient 
System.out.println("real1 / real2 = " + cociente);

}

}