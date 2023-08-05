//Charleen Ramirez Rios 
//R00417213
//Test 
//2022-12-13
//COMP2400 - 202310-70846
//Dr. Edgardo Vargas Moya

//invierte.java

//Importing Scanner utility so that we can read user input from the keyboard
import java.util.Scanner;

public class InvertedEvens
{

//invierte function goes here 
//Cycles through the user's array and prints out the inverted even numbers version of the array 
private static void invierte(int numbersArr[])
{

//Using a loop to cycle through the array in reverse while printing out only the even numbers within it 
System.out.println("Here is your inverted array of even numbers: ");

for(int i = numbersArr.length - 1; i >= 0; i--)
{
   //If the numbers are even they can be printed on the screen 
   //Using the % to determine whether the number is even or not
   if(numbersArr[i] %2 == 0)
   {
         System.out.print(numbersArr[i] + " ");
   }
} 

//Notifying the user that the game has been completed 
System.out.println("\n even inversion completed"); 
System.out.println("---------------");

}

public static void main(String args[])
{

//Declaring a scanner called teclado that we can use to read input from the user 
Scanner keyboard = new Scanner(System.in);

//Declaring variables that will be used to store values 
int counter,
    tryAgain = 1; 

int numbersArr[]; 

//While the user states that they would like to try again (1) the loop will run
//By using a while loop, we secure at least one successful run before the user enters their selection
while(tryAgain == 1)
{

System.out.println("Welcome to even inversion"); 

//Asking user how many numbers would they like to enter and assigning the value to our counter variable 
System.out.println("How many numbers would you like to enter?");
counter = keyboard.nextInt(); 

//Defining the size of the array based off the user's entry 
numbersArr = new int[counter];

//Asking user to start entering numbers
for(int i = 0; i < counter; i++)
{

   System.out.println("Please enter a number");
   numbersArr[i] = keyboard.nextInt(); 

}

//Calling the invierte function 
invierte(numbersArr);

//Asking user if they would like to play again 
System.out.println("Would you like to use even inversion again?");
System.out.println("Enter 1 of yes or 2 for no");
tryAgain = keyboard.nextInt(); 

if(tryAgain == 2)
{
   System.out.println("Thank you for using even inversion, goodbye!");
}else
{
   System.out.println("Restarting inversion . . .");
}


}

}

}
