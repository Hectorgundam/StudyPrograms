/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Asignacion 4 - Animacion Cuadro a Cuadro 
2022-11-13
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
- Buscaran el módulo 11
- Se les colocó un archivo comprimido "Animación" con varios ejemplos
   Estos ejemplos muestran dos diferentes maneras de hacer animaciones con Panels, Frames y Canvas.  
   Una de las técnicas es la animación cuadro por cuadro
   
- Basándose en este programa usted hara lo siguiente:

- Utilizando Frames y Canvas creará un programa en donde se muestre una animación de una escena de una película famosa
- Las imágenes que utilice deben ser tipo .png o .jpg
- Coloque una imagen de fondo para crear un mejor ambiente
- El trabajo requiere que utilice al menos 8 y no más de 12 imágenes para su animación 
- Cuando envíe la asignación entregará el archivo .java, el .class y todas las imágenes 
   en un solo archivo comprimido con el nombre suNombreAnimacionCuadro.zip
- Asegúrese de que el archivo comprimido no ocupa más de 4MB
- (Verifique el enlace en la asignación para más detalles).

Shows how to make stick animations using predesigned images
   using Frames and Canvas. 
	
	Author: Edgardo Vargas Moya
	        November 24, 2019 
*/

//import java.awt.*;
import java.awt.Color;
import java.awt.Image;
import java.awt.Canvas;
import java.awt.Toolkit;
import java.awt.Graphics;
import javax.swing.JFrame;

//Class to define the Baseball Game object

public class BaseballGame3 extends Canvas
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
            img = t.getImage("baseball0" + i + ".png");
          }
		    else
		    {
            Toolkit t = Toolkit.getDefaultToolkit();  
            //Returns an image pixel data from a file
            img = t.getImage("baseball" + i + ".png"); 
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
     JFrame frame = new JFrame("Baseball Game"); 	 
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

     //Create the canvas and place image
     BaseballGame3 canvas = new BaseballGame3(); 
     
     //Change the background color of the canvas to CYAN 
     canvas.setBackground(Color.CYAN);  
     
     //Add the canvas to the frame   
     frame.add(canvas); 
     
     //Set frame size  
     frame.setSize(600,300);  
     
     //Set the frame location 
     frame.setLocationRelativeTo(null); 
     
     //Makes the frame visible
     frame.setVisible(true);  
      
   }
}