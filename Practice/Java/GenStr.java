// Total strings calculation = 7!/(7-7)! = 5040

// String manipulation
// Take your first name and from left to right remove all repeated letters: 
// Resullting string: Charlen (Total characters 7)
// If the total of letters is less than 6 then repeat the process after adding you first last name: 
// Resulting string: Charlen 
// If the total of letters is still less than 6 then repeat the process after adding your second last name: 
// Resulting string: Charlen 
// If after doing this you have over 9 letters then only keep the first 9 
// Resulting string: Charlen 

// Calculations for total of string possibilities 
// 7!/(7-7)! = 5040
// 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
// (7-7)! = (0)! = 1
// 5040 / 1
// 5040

// Hard code a string with charlen
// Create permutation print method 
// Create swap - interchange - mixup function to change the order of characters within the string 
   // Need to make sure the variations don't repeat 
   // Need to make sure to keep count of each different variation and print it onto screen in the specified format 
      // stringVariationPermutation (counter)

// Importing library to read user input from keyboard 
import java.util.Scanner; 

// Program that takes in a string and prints out the total amount of possible string combinations that can
// from it without repetition 
public class GenStr {

   // Counter variable to keep track of possible combinations/permutations
    private static int counter = 1;
    
   // Main program function 
    public static void main(String[] args) {

        //Declaring a scanner called keyboard that we can use to read input from the user 
        Scanner keyboard = new Scanner(System.in);

        // Hardcoded string I got after following instructions provided 
        // String mystring = "charlen"; 

        String mystring;

        int possibleCombinations; 

        // Asking user for string and reading from keyboard

        //Asking user for the value of mass in Kg, reading the input from the keyboard and storing the value in the variable userMass
        System.out.print("Enter a string with no spaces: ");
        mystring = keyboard.nextLine(); 
    
        // Checking and printing the total possible amount of combinations for the given string 
        possibleCombinations = stringPossibilities(mystring.length()); 

        // System.out.println("The contents of possibleCombinations is: " + possibleCombinations);

        // Printing out the total number of possible combinations for the given string 
        System.out.println("The total number of possible combinations for the given string are: " + possibleCombinations);

        // Generate all permutations and print them  
        // Function call for stringPermutation
        stringPermutation(mystring, 0, mystring.length() - 1);
        
    }

    // Function to generate the permutations for our string
    // Takes in the string and two ranges for our string as left and right 
    private static void stringPermutation(String str, int left, int right) {
    
        // Once all the changes/permutations have been made we print out the new string with its count
        // count here acts as a counter for the amount of permutations and the value will increase with each one
        if (left == right) {
        
            // TEST 
            // System.out.println("The current value of counter is: " + counter);
            
            //TEST 
            // System.out.println("The following value of counter should be: " + counter);
        
            System.out.println(str + "(" + counter++ + ")");
            
        } else {
        
            for (int i = left; i <= right; i++) {
            
                // Interchanging the current index with the current one in index 
                str = swap(str, left, i);
                
                // TEST 
                // System.out.println("The current content of str is: " + str);
                
                stringPermutation(str, left + 1, right);
                
                // Resetting the string back to its original form 
                // Sort of like backtracking 
                str = swap(str, left, i); 
            }
        }
    }

    // Method to swap characters in a string
    // Using a classic swap function to move characters inside the string 
    // This uses a "temporary" variable to store a value while the others are swapped 
    // With this, we can create different variatios/permutations of our string 
    private static String swap(String a, int i, int j) {
    
        char[] charArray = a.toCharArray();

        char temp = charArray[i];
        
        // TEST 
        // System.out.println("The current content of temp is: " + temp);
        
        charArray[i] = charArray[j];
        
        charArray[j] = temp;
        
        // Once the swapping modifications have been made we can return the new string 
        return String.valueOf(charArray);

    }


    // Test function 
    // Function that calculates the total possible amount of permutations / combinations for the given string 
    // Need to take in the length of the string 
    // Once we have the length of the string we can complete the calculations 
    // Formula would be something like 
    // String of 7 characters
    // 7!/(7-7)! = 5040
    // 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
    // (7-7)! = (0)! = 1
    // 5040 / 1
    // 5040
    private static int stringPossibilities(int size){

        // The numberPossibilities is equal to the value of size as a starting point 
        int numberPossibilities = size;

        // Used to cycle through the top section of calculations and loop 
        int counter = size;

        // Test printing the current contents of counter 
        // System.out.println("The contents of counter are: " + counter);

        // Test printing the current contents of size 
        // System.out.println("The contents of size received are: " + size);

        // Test printing the current contents of numberPossibilities 
        // System.out.println("The contents of numberPossibilities are: " + numberPossibilities);

        // Loop that runs while the value of is less than the value of size 
        for(int i = 0; i < size; i++){

            // Decreasing the current value of counter by 1 with each iteration 
            counter--;

            // Test printing the current contents of counter
            // System.out.println("The contents of counter are: " + counter);

            // If the value of counter is not 0 
            if(counter != 0){

                // The number of possibilitie is multiplied by the current value of counter
                numberPossibilities *= counter; 

                // Test printing the current contents of numberPossibilities 
                // System.out.println("The contents of numberPossibilities are: " + numberPossibilities);
            }

        }

        // Return the value of numberPossibilities
        return numberPossibilities; 

    }


}