/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio 5 - Archivos
2022-11-28
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscarán el módulo 14. Lean la lección 16 y vean los tres demos allí contenidos. Luego haga lo siguiente:
Copie el programa de archivo que se encuentra en la lección 16 en la página 4
Después que vea su perfecto funcionamiento ejecute las instrucciones del ejercicio número 1 de la página 4
Documente el código describiendo sus distintas partes utilizando comentarios
Entregue aquí el código (.java) del programa
También entregue un “print screen” del código y la corrida del programa mostrando los mensajes de error
*/

//Importing the necessary libraries
import java.io.*;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class IntroManejoArchivos
{

  public static void main(String[] args) {
    //Declaring an object of class FileReader to read from file
    FileReader reader;
    //Declaring an object of class Scanner to read 
    Scanner fileInput;
    //Declaring an object of class PrintWriter to print to file
    PrintWriter fileOutput;
    //Declaring a string
    String strLine;
    //Declaring integers
    int valor,
	      suma = 0;
   //Inside the try section is the code that should run if no errors occur 
    try
    {
     //Reader will be reading from the file called input.txt
      reader = new FileReader("input.txt");
      //Scanner will be reading from the file that reader has within it 
      fileInput = new Scanner (reader);
      //PrintWriter will be printing to the file called output.txt
      fileOutput = new PrintWriter("output.txt");
      
      //Printing to file 
      fileOutput.println("Primera línea en el archivo");
      fileOutput.println("Segunda línea para el archivo");
      fileOutput.close();

      //While loop that runs while 
      while (fileInput.hasNextLine())
      {
        //The string strLine will contain what's being read from the file's next line
        strLine = fileInput.next();
        //valor will contain the integer "equivalent" of the value of strLine
        valor = Integer.valueOf(strLine);
        //suma is equal to the current value of suma plus the value of valor
        suma = suma + valor;
      }
      fileInput.close();
      //Printing onto the screen the total value of suma
      System.out.println("suma = " + suma);
    }
    //If an error occurs this section of code will run instead and print a message onto the screen 
    catch (IOException e)
    {
      System.out.println("Error manejando los archivos" + e);
    }
  }
}