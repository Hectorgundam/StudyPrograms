/* 
Charleen Ramirez Rios 
R00417213
Laboratorio 1 - I/O Dialogs
2022-10-9
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Ejercicio: 
Haga el ejercicio 4 que se encuentra en la ultima pagina de esa lectura. 
Debe utilizar las opciones JOptionPane para las entradas y salidas. 
Para la operacion de exponentes utilizaran el metodo Math.pow. Investigue como funciona este metodo. 
Documente el codigo describiendo sus distintas partes utilizando comentarios. 


Ejercicio Investigue como se manejan exponentes en Java y escriba un programa que le pida al usuario que entre una base y un exponente, y que imprima el resultado numerico. 
Por ejemplo: 

Base = 5
Exponente = 3
Resultado = 125

Como haria para que el programa calculara el resultado de ^3raizcuadradade200? 
Demuestrelo con la corrida del programa. 

*/

//Importing components from the swing package
import javax.swing.*; 

public class InOutDialogs{

public static void main(String args[]){

String strBaseNumber, 
         strExponentNumber,
         strRootNumber; 
     
Double baseNumber, 
         exponentNumber, 
         result,
         rootNumber, 
         rootResult; 
     
//Asking the user to enter the value for the exponent number and assigning the value entered by the user to strBaseNumber
strBaseNumber = JOptionPane.showInputDialog("Please enter your base number: ");

//Asking the user to enter the value for the exponent number and assigning the value entered by the user to strExponentNumber
strExponentNumber = JOptionPane.showInputDialog("Please enter your exponent number: ");

//Converting the string obtained from the user into a double value that is stored inside baseNumber
baseNumber = Double.parseDouble(strBaseNumber); 

//Converting the string obtained from the user into a double value that is stored inside exponentNumber
exponentNumber = Double.parseDouble(strExponentNumber); 

//Determining the result of the equation based on ther user's entries for base and exponent numbers
result = Math.pow(baseNumber, exponentNumber);

//Displaying the result of the ecuation to the user 
JOptionPane.showMessageDialog(null, "The resulting number is " + result , "Operation Results" , JOptionPane.PLAIN_MESSAGE);  

//Determine the cube root of a given number excercise 

//Asking the user to enter the number they want to determine the cube root of
strRootNumber = JOptionPane.showInputDialog("Please enter a number to determine it's cube root");

//Converting the string obtained from the user into a double value that is stored inside rootNumber 
rootNumber = Double.parseDouble(strRootNumber);

//Math.cbrt(double x) - provides us a way to calculate the cube root if the specified parameter
//In this case we are determining the cube root of the value entered by the user 
rootResult = Math.cbrt(rootNumber);

//Displaying on the screen the cube root equation result 
JOptionPane.showMessageDialog(null, "The cube root of the number " + rootNumber + " is: " + rootResult , "Operation Results" , JOptionPane.PLAIN_MESSAGE); 


}

}