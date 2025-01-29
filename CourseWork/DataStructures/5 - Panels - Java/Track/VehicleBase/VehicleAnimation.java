/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Asignacion 4B - Animacion con codigo
2022-12-04
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
- En el módulo 11 “Introducción a la Animación con Panels, Frames y Canvas”, se les dejó un archivo comprimido con varios ejemplos
   Estos ejemplos muestran dos diferentes maneras de hacer animaciones con Panels, Frames y Canvas. Una de las técnicas es la animación por código 
- Basándose en ese ejemplo usted creará un programa en donde se muestre una animación de una escena de dos autos compitiendo uno con el otro
   Uno de los dos autos debe ganar la competencia
- El fondo a utilizarse es el que esta adjuntado en esta asignación
- Los dos autos deben ser creados en base a una misma clase y por código
- Debe poderse notar cuando las ruedas están girando según el auto avanza  
- Después que vea su perfecto funcionamiento entregue los archivos (.java) del programa
- También entregue un “print screen” del código y la corrida del programa

Author: Edgardo Vargas Moya
	        November 24, 2019 
           
 Program that shows how to make animations using Graphics drawLine and drawOval methods
 
 Please be advised that this is a top secret undisclosed new vehicle model and you are being trusted with this information. 
 If the design or functionality of the video is leaked ... we will find you .. and we will [redacted] you
*/

//import java.awt.*;
import java.awt.Color;
import java.awt.Image;
import java.awt.Canvas;
import java.awt.Toolkit;
import java.awt.Graphics;
import javax.swing.JFrame;

//Class to define Vehicle objects

class Vehicle {
//Object position variables
  int x,     
      y;

//Vehicle constructor that assigns the value of 0 to both position variables (x and y) 
  Vehicle()
  {
    x = 0;
	 y = 0;
  }

  Vehicle(int initX, int initY)
  {
    x = initX;
	 y = initY;
  }
  
  void move(int xInc, int yInc)
  {
    x = x + xInc;
	 y = y + yInc;
  }
  
  void drawFrame(Graphics g, int f,int x, int y)
  {
    //g = Graphics object
	 //f = frame to draw
	 //x = horizontal location
	 //y = vertical location
	 
    switch (f)
	 {
	   case 0:  //Drawing frame 0
        {
        g.setColor( Color.WHITE);
        g.drawOval(  0+x, 0+y, 80,35);  //body
        g.fillOval( 50+x, 5+y, 20,20);   //windshield
        g.drawOval( -5+x,20+y, 40,40);   //rear wheel
        g.fillOval( 0+x,25+y, 30,30);   //rear wheel rim
        g.drawLine( 20+x,32+y,-5+x,40+y);
        g.drawLine( 0+x,0+y,25+x,10+y); //antenna
        g.drawOval( 55+x,30+y, 30,30);   //front wheel
        g.fillOval( 60+x,35+y, 20,20);   //front wheel rim
        g.drawLine( 67+x,32+y,67+x,40+y);
          break;
        }
       case 1:  //Drawing frame 1
        {
          g.drawOval(  0+x, 0+y, 80,35);  //body
        g.fillOval( 50+x, 5+y, 20,20);   //windshield
        g.drawOval( -5+x,20+y, 40,40);   //rear wheel
        g.fillOval( 0+x,25+y, 30,30);   //rear wheel rim
        g.drawLine( 15+x,45+y,25+x,55+y);
        g.drawLine( 0+x,0+y,25+x,10+y); //antenna
        g.drawOval( 55+x,30+y, 30,30);   //front wheel
        g.fillOval( 60+x,35+y, 20,20);   //front wheel rim
        g.drawLine( 70+x,45+y,80+x,55+y);
          break;
        }
       case 2:  //Drawing frame 2
        {
          g.drawOval(  0+x, 0+y, 80,35);  //Vehicle body
        g.fillOval( 50+x, 5+y, 20,20);   //Vehicle windshield
        g.drawOval( -5+x,20+y, 40,40);   // Vehicle rear wheel
        g.fillOval( 0+x,25+y, 30,30);   //Vehicle rear wheel rim
        g.drawLine( 0+x,0+y,25+x,10+y); //Vehicle antenna
        g.drawOval( 55+x,30+y, 30,30);   //Vehicle front wheel
        g.fillOval( 60+x,35+y, 20,20);   //Vehicle front wheel rim

		}
	 } //switch	
  }
}
public class VehicleAnimation extends Canvas
 {
   public void paint(Graphics g) {  
     Image img;
     
            Toolkit t = Toolkit.getDefaultToolkit(); 
            //Returns an image pixel data from a file 
            img = t.getImage("pista.png"); 
            
             //Creating two Vehicle objects
             Vehicle vehicle1 = new Vehicle();
		       Vehicle vehicle2 = new Vehicle();
         
         for (int i=0; i<200; i++)
		    {
             //Erasing image
             g.clearRect(0,0,400,400);   
             //Drawing image  
             g.drawImage(img, 0, 0,this);  
             
             vehicle1.drawFrame(g,(i+1)%3,i,170);
             vehicle2.drawFrame(g,i%3,i*4,250);
             
             //Implementing a time delay to hold 100ms before the next Canvas
             try{
	              Thread.sleep(100); 
	             }
	               catch(InterruptedException e)
	             {
                }    
           }
    }    
   
   public static void main( String args[] )
 	{
     //Creating a frame and placing the title on it 
     JFrame frame = new JFrame("Vehicle Race Animation");	 
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
     
     //Creating a canvas and placing the Vahicle animation on it 
     VehicleAnimation canvas = new VehicleAnimation(); 
     
     //Change the background color of the canvas to RED
     canvas.setBackground(Color.RED);  
     
     //Add the canvas to the frame 
     frame.add(canvas); 
     
     //Set frame size 
     frame.setSize(400,400); 
     
     //Set the frame location
     frame.setLocationRelativeTo(null); 
     
     //Makes the frame visible 
     frame.setVisible(true); 
   }
}