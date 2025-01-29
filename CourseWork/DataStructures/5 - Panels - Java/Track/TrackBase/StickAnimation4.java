/* Shows how to make stick animations using Graphics drawLine
   and drawOval methods.
	
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

//Class to define the Stickman objects

class StickMan {

  int x,     //object position
      y;
		
  StickMan()
  {
    x = 0;
	 y = 0;
  }

  StickMan(int initX, int initY)
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
	   case 0:  //draws frame 0
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
       case 1:  //draws frame 1
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
       case 2:  //draws frame 2
        {
          g.drawOval(  0+x, 0+y, 80,35);  //body
        g.fillOval( 50+x, 5+y, 20,20);   //windshield
        g.drawOval( -5+x,20+y, 40,40);   //rear wheel
        g.fillOval( 0+x,25+y, 30,30);   //rear wheel rim
        g.drawLine( 0+x,0+y,25+x,10+y); //antenna
        g.drawOval( 55+x,30+y, 30,30);   //front wheel
        g.fillOval( 60+x,35+y, 20,20);   //front wheel rim

		}
	 } //switch	
  }
}
public class StickAnimation4 extends Canvas
 {
   public void paint(Graphics g) {  
     Image img;
     
            Toolkit t = Toolkit.getDefaultToolkit();  
            img = t.getImage("pista.png"); //Returns an image pixel data from a file
            
             //Create to StickMan objects
             StickMan stickMan1 = new StickMan();
		       StickMan stickMan2 = new StickMan();
         
         for (int i=0; i<200; i++)
		    {
             g.clearRect(0,0,400,400);     //Erase image
             g.drawImage(img, 0, 0,this);  //Draw image
             
             stickMan1.drawFrame(g,(i+1)%3,i,170);
             stickMan2.drawFrame(g,i%3,i*4,250);
             
             //to implement a time delay
             try{
	              Thread.sleep(100); //hold 100ms before next Canvas
	             }
	               catch(InterruptedException e)
	             {
                }    
           }
    }    
   
   public static void main( String args[] )
 	{
     
     JFrame frame = new JFrame("Stick Animation");	//Create the frame and place the title 
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
     
     StickAnimation4 canvas = new StickAnimation4(); //Create the canvas and place the Stick Animation
     canvas.setBackground(Color.RED); //Change the background color of the canvas to RED     
     frame.add(canvas); //Add the canvas to the frame 
     frame.setSize(400,400); //Set frame size 
     frame.setLocationRelativeTo(null); //Set the frame location
     frame.setVisible(true); //Makes the frame visible 
   }
}