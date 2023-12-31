/*
Upload Assignment: Asignacion 4 - Animacion Cuadro a Cuadro 
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
- Buscaran el m�dulo 11
- Se les coloc� un archivo comprimido "Animaci�n" con varios ejemplos
   Estos ejemplos muestran dos diferentes maneras de hacer animaciones con Panels, Frames y Canvas.  
   Una de las t�cnicas es la animaci�n cuadro por cuadro
   
- Bas�ndose en este programa usted hara lo siguiente:

- Utilizando Frames y Canvas crear� un programa en donde se muestre una animaci�n de una escena de una pel�cula famosa
- Las im�genes que utilice deben ser tipo .png o .jpg
- Coloque una imagen de fondo para crear un mejor ambiente
- El trabajo requiere que utilice al menos 8 y no m�s de 12 im�genes para su animaci�n 
- Cuando env�e la asignaci�n entregar� el archivo .java, el .class y todas las im�genes 
   en un solo archivo comprimido con el nombre suNombreAnimacionCuadro.zip
- Aseg�rese de que el archivo comprimido no ocupa m�s de 4MB
- (Verifique el enlace en la asignaci�n para m�s detalles).

Shows how to make stick animations using predesigned images
   using Frames and Canvas. 
	
	Prof Dr Edgardo Vargas Moya
*/

//import java.awt.*;
import java.awt.Color;
import java.awt.Image;
import java.awt.Canvas;
import java.awt.Toolkit;
import java.awt.Graphics;
import javax.swing.JFrame;

//Class to define the FrameByFrame object

public class FrameByFrame extends Canvas
 {
 
 //g = Graphics object 
   public void paint(Graphics g) {  
     Image img;
     
     for (int j=0; j<5; j++)
		{
		  for (int i=1; i<=11; i++)
		  {  
        
        //Erase image
     g.clearRect(0,0,600,300); 
     
     if (i < 10)
		    {
            Toolkit t = Toolkit.getDefaultToolkit();  
            //Returns an image pixel data from a file
            //img = t.getImage("nine0" + i + ".png");
            img = t.getImage("nine0" + i + ".png");


          }
		    else
		    {
            Toolkit t = Toolkit.getDefaultToolkit();  
            //Returns an image pixel data from a file
            img = t.getImage("nine" + i + ".png"); 
		    }
             //Draw image
             g.drawImage(img, 120,100,this);
             
             //to implement a time delay
             try{
               //hold 400ms before next Canvas
	              Thread.sleep(400);
	             }
	               catch(InterruptedException e)
	             {
                }
		  }
	  	}      
    }    
   public static void main( String args[] )
 	{
     //Create the frame and place the title 
     JFrame frame = new JFrame("Nine Movie"); 	 
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

     //Create the canvas and place image
     FrameByFrame canvas = new FrameByFrame(); 
     
     //Change the background color of the canvas to red
     canvas.setBackground(Color.RED);  
     
     //Add the canvas to the frame   
     frame.add(canvas); 
     
     //Set frame size  
     //Adjustments were made to fit the image I was using 
     frame.setSize(1350,800);  
     
     //Set the frame location 
     frame.setLocationRelativeTo(null); 
     
     //Makes the frame visible
     frame.setVisible(true);  
      
   }
}