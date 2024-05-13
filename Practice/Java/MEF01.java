
// Importing Scanner Java library to be able to read user input from keyboard 
import java.util.Scanner;

// Our MEF01 class 
public class MEF01
{

    // Our Statuses 
    enum Status {
        READY,
        CALCULATING,
        WAITING_DEPOSIT,
        DISPENSING,
        REFUNDING
        }
  
  public static void main(String args[])
  {
    Scanner keyboard = new Scanner(System.in);
    Status estado = Status.READY;
    int pennies = 0;
    
    while(true)
    {

        // Printing out the current state of the vending machine 
        System.out.println("--------------------------------------------------------------------------");

        System.out.println("Current vending machine state: " + estado);

        System.out.println("--------------------------------------------------------------------------");

      if (estado == Status.READY)
      {
        System.out.println("Make a deposit to make a purchase. Machine only accepts pennies.");
        pennies = keyboard.nextInt();
      }
      
      switch(estado)
      {
        case Status.READY:
          if (pennies > 0)
          {
            estado = Status.CALCULATING;
          }
          break;
          
        case Status.CALCULATING:
          if (pennies >= 100)
          {
            estado = Status.DISPENSING;
          }
          else
          {
            estado = Status.WAITING_DEPOSIT;
          }
          break;
                  
        case Status.WAITING_DEPOSIT:
          System.out.println("Current balance: " + pennies);
          System.out.println("Make a deposit to make a purchase. Machine only accepts pennies.");
          pennies = pennies + keyboard.nextInt();
          estado = Status.CALCULATING;
          break;
                  
        // The vending machine's DISPENSING status
        case Status.DISPENSING:

          // Notifying the user that a bottle will be dispensed 
          System.out.println("Dispensing bottle, enjoy!");

          // If the value of pennies is equal to 100 
          // No change needs to be refunded to the users 
          if (pennies == 100)
          {

            // The value of pennies is reset back to 0 
            pennies = 0;

            // The status of the vending machine goes back to READY
            estado = Status.READY;

          }
          // The user's balance is over 100 pennies and a refund should be issued 
          else
          {

            // The vending machine enters the REFUNDING status 
            estado = Status.REFUNDING;
          }

          // We exit the case 
          break;
              
        // The vending machine's REFUNDING status
        case Status.REFUNDING:

          // Once the user's balance reaches 100 we dispense a bottle so we can deduct that amount and 
          // we end up with spare change or extra coins that we will refund to the user 
          int cambio = pennies - 100;

          // Notifying the user of the amount that's being refunded after the bottle was dispensed 
          System.out.println("Refunding " + cambio + " pennies");

          // After refunding, we reset the pennies balance back to 0 
          pennies = 0;

          // The vending machine returns to READY status
          estado = Status.READY;
      }
    }
  }
}