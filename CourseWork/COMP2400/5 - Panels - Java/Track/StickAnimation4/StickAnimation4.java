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
		  g.drawOval(  0+x, 0+y, 18,18);     //head
		  g.drawLine(  9+x,17+y, 9+x,47+y);  //body
		  g.drawLine(  9+x,47+y,18+x,56+y);  //right tight
		  g.drawLine( 18+x,56+y,22+x,70+y);
		  g.drawLine( 22+x,70+y,28+x,70+y);

		  g.drawLine( 9+x,27+y,-3+x,33+y);   //left arm
		  g.drawLine(-3+x,33+y, 1+x,47+y);   //left forearm
		  g.drawLine( 9+x,27+y,18+x,34+y);   //right arm
		  g.drawLine( 18+x,34+y,25+x,30+y);  //right forearm
		  
		  g.drawLine( 9+x,47+y, 6+x,60+y);
		  g.drawLine( 6+x,60+y,-3+x,65+y);
		  g.drawLine(-3+x,65+y, 0+x,71+y);
		  break;
		}
	   case 1:  //draws frame 1
		{
		  g.drawOval(  0+x, 0+y, 18,18);        //head
		  g.drawLine(  9+x,17+y, 9+x,47+y);     //body
		  g.drawLine(  9+x,47+y,21+x,55+y);     //right tight
		  g.drawLine( 21+x,55+y,27+x,65+y);     //right lowerleg
		  g.drawLine( 27+x,65+y,32+x,63+y);     //right foot

		  g.drawLine( 9+x,27+y,-3+x,29+y);      //left arm
		  g.drawLine(-3+x,29+y, 2+x,38+y);      //left forearm
		  g.drawLine( 9+x,27+y,18+x,31+y);      //right arm
		  g.drawLine( 18+x,31+y,24+x,23+y);     //right forearm
		  
		  g.drawLine( 9+x,47+y, 2+x,56+y);      //left tight
		  g.drawLine( 2+x,56+y,-7+x,59+y);      //left lowerleg
		  g.drawLine(-7+x,59+y, -7+x,64+y);     //left foot
		  break;
		}
	   case 2:  //draws frame 2
		{
		  g.drawOval(  0+x, 0+y, 18,18);        //head
		  g.drawLine(  9+x,17+y, 9+x,65+y);     //body
		  g.drawLine( 9+x,65+y, 13+x, 71+y);

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
		       StickMan stickMan3 = new StickMan();
         
         for (int i=0; i<200; i++)
		    {
             g.clearRect(0,0,400,400);     //Erase image
             g.drawImage(img, 0, 0,this);  //Draw image
             
             stickMan1.drawFrame(g,(i+1)%3,i,170);
             stickMan2.drawFrame(g,i%3,i*4,250);
             stickMan3.drawFrame(g,i%3,400-2*i,250);
             
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