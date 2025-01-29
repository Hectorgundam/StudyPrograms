/* 
Program purpose: 
The program takes the values of mass (m) and acceleration (a) provided by the user and determines the force (F) in Kg.m/s2 (equivalent to one Newton). The program then 
returns the results to the user on the screen in units of Newton. 

Program tasks: 
Ask user to enter value of mass (m), read the value from keyboard and assign value to the variable userMass
Ask user to enter value of acceleration (a), read the value from keyboard and assign value to the variable userAcceleration 
Calculate the force (F) using the equation F = m*a [Force = mass x acceleration] and store the value in the variable forceResult
Print out the result to the screen 
*/

//Importing Scanner utility so that we can read user input from the keyboard
import java.util.Scanner;

public class ForceCalculator {

public static void main(String args[]){


//Declaring a scanner called keyboard that we can use to read input from the user 
Scanner keyboard = new Scanner(System.in);

//Declaring variables that will be used to store values 
float userMass,
      userAcceleration,
      forceResult;
      
//Asking user for the value of mass in Kg, reading the input from the keyboard and storing the value in the variable userMass
System.out.print("Enter the mass in Kg, m = ");
userMass = keyboard.nextFloat(); 

//Asking user for the value of acceleration in m/s, reading th einput from the keyboard and storing the value in the variable userAcceleration
System.out.print("Enter a acceleration in m/s, a = ");
userAcceleration = keyboard.nextFloat(); 

//Calculating the force using the equation F = m * a 
forceResult = userMass * userAcceleration; 

//Printing 
System.out.print("The value of mass provided was m = " + userMass + " Kg\n");

System.out.print("The value of acceleration provided was a = " + userAcceleration + " m/s \n");

System.out.println("The formula for this equation will be F = m * a \nWith the values entered this would be:");

System.out.println("F = " + userMass + "Kg * " + userAcceleration + "m/s");

System.out.println(forceResult + "N = " + userMass + "Kg * " + userAcceleration + "m/s");

System.out.print("The resulting force is F = " + forceResult + "N \n");

}


}