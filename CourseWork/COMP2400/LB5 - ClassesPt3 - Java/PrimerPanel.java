/*
Upload Assignment: Laboratorio#4 Panel y Frame
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
- Buscaran el modulo 10
- Leeran la leccion 11B 
- Copiaran el ejemplo de la seccion 11B.1 en la pagina 1. Lo verificaran su correcto funcionamiento
- Luego copiaran el ejemplo de la seccion 11B.2 en la pagina 2 y verificaran su correcto funcionamiento. Este debe 
   generar un panel como el que se muestra en la pagina 3 de la lectura
- Ambos archivos deben estar colocados en la misma carpeta
- Debe documentar ambos codigos completamente 
- Recuerde participar en el foro de discusion correspondiente 
- Despues que vea su perfecto funcionamiento entregue los archivos (.java y .html) del programa 
- Tambien entregue un "print screen" del codigo y la corrida del programa

*/

//Ejemplo 11B.1 

//Importing JPanel so that the JPanel class can be used
//Importing the Graphics class so that its coordinates can be used
import java.awt.Graphics; 
import java.awt.Color; 
import javax.swing.JPanel; 

//Creating the PrimerPanel Class and linking it with the JPanel class
public class PrimerPanel extends JPanel{

//The sentence "My Primer Panel Funciona" 
   public void paint (Graphics g){
   
   super.paintComponent(g); 
   
   //Establishing the background color as white 
   this.setBackground(Color.WHITE); 
   
   //Establushing the wordsletters to be red
   g.setColor(Color.RED);
   
   //Adding the message and the size of the string
   g.drawString("Mi Primer Panel Funciona", 20, 20);
   
   //Adding the coordinates of the lines
   g.drawLine(15, 5, 165, 5);
   
   g.drawLine(15, 25, 165, 25); 
   
   
   }

}
