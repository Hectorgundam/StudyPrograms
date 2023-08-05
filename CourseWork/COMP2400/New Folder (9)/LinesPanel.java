/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Laboratorio#4 Panel y Frame
2022-11-06
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

//Ejemplo 11B.2

import java.awt.Color; 
import javax.swing.JFrame;

public class LinesPanel{

   public static void main(String args[]){
   
      //Creating the object frame and determining the title it will have on the top part 
      JFrame frame = new JFrame("Draw lines and Message");
      
      //Establishing the values the panel will have as default when closing 
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
      
      //Creating the object lineMessagePanel with the class created in the previous one
      PrimerPanel lineMessagePanel = new PrimerPanel(); 
      
      //Adding object to the corresponding frame
      frame.add(lineMessagePanel); 
      
      //Establishing the background color of the frame as white 
      lineMessagePanel.setBackground(Color.WHITE); 
      
      //Setting dimensions for the frame panel
      frame.setSize(450, 450); 
      
      //Enabling visibility for the frame 
      frame.setVisible(true); 
   
   }

}