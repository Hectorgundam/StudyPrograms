/*
Upload Assignment: Asignacion 2: Format()
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Programa Formatos.java

Purpose: 
Program prints the sin and cos of a given angle that increases in value from 0 to 360 and prints out the results on the screen using format()

*/ 

//Import the math library to use it's methods
import java.io.*;

public class Formatos {

public static void main (String args[]){
 
//Declaring variables that will be used 
double radianCounter = 0, 
         sinVar = 0, 
          cosVar = 0, 
          angle = 0; 
 
for (int counter = 0; counter <= 360; counter += 5){

//Obtaining the radians 
angle = Math.toRadians(radianCounter);

//Obtaining the sin value using Math.sin(angleVar) 
sinVar = Math.sin(angle);

//Obtaining the cos value using Math.cos(angleVar) 
cosVar = Math.cos(angle);

//Printing output 
//System.out.println("sin ( " + counter + ") = " + sinVar + "and cos (" +  counter + ") = " + cosVar);

//Conditional statement for obtaining the values.  The value will increase by values of 5 as it runs
if(counter < 360){

radianCounter += 5; 

}

//Using format() to print to screen
System.out.format("sin(%d) = %8.3f and cos(%d) = %8.3f %n", counter, sinVar, counter, cosVar); 

}

}

}