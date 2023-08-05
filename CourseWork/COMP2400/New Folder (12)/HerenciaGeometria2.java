/*
Charleen Ramirez Rios 
R00417213
Upload Assignment: Asignacion 7 - Geometria 2
2022-11-27
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscarán el módulo 13
Verán la lección 15, lecturas y video allí contenidos
El archivo HerenciaGeometria2.java que esta adjuntado es una versión modificada del archivo HerenciaGeometria.java que estudiamos previamente 
Utilizando el mismo haga lo siguiente:
Realice los ejercicios que se presentan el el archivo adjunto
Algunos de los ejercicios se contestarán en este mismo documento Para esos casos escribirá la contestación bajo el ejercicio correspondiente y en bold
 Otros requieren que escriba código en el programa HerenciaGeometria.java
Para entregar su trabajo utilizará este documento con el nombre suNombreAsigHerencia y el archivo en Java con el nombre suNombreAsigHerencia.java
Ambos archivos se comprimirán en un archivo de nombre suNombreAsigHerencia en formato .zip
Por ejemplo edgardoVargasAsigHerencia.zip
No utilice espacios en blanco, acentos o caracteres que no sean letras
Recuerde participar en el foro de discusión correspondiente
Entregará el archivo como un documento adjunto a través de la herramienta 
Assignments en donde obtuvo este documento

*/

import java.awt.*;
import java.applet.*;
import java.awt.Graphics;
import java.util.*;

class Polygon
{
  double x[], //contains x coordinate for vertices
         y[], //contains y coordinate for vertices
         xc,  //(xc,yc) = figure's center or
         yc;  //reference point
      
  int    totalPoints; //number of vertices
  
  //Given method: Explain function
  Polygon()
  {
  }
     
  Polygon(int totalPoints, double xc, double yc)
  {
    this.totalPoints = totalPoints;
    x = new double[totalPoints];
    y = new double[totalPoints]; 
    this.xc = xc;
    this.yc = yc;
  }
  
  void setCenterCoords(double xc, double yc)
  {
    this.xc = xc;
    this.yc = yc;
  }
  
  void setCoordForOneVertex(int index, double x, double y)
  {
    if ((index < totalPoints)&& (index >= 0))
    {
      this.x[index] = x;
      this.y[index] = y;
    }
  }
  
  void grow(double factor)
  {
    int i;
    
    for (i = 0; i < totalPoints; i++)
    {
      x[i] = (x[i] - xc) * factor + xc;
      y[i] = (y[i] - yc) * factor + yc;
    }
  }
  
  //New method: TO DO
  double getPerimeter()
  {
    double perimeter = 0;
    {
      //requires the code to calculate the perimeter
    }
    return (perimeter);
  }
  
  void moveDown(double displacement)
  {
    for (int i = 0; i < totalPoints; i++)
    {
      y[i] = y[i] + displacement;
    }
    yc = yc + displacement;
  }
  
  void draw(Graphics g)
  {
    int i;
    for (i = 0; i < totalPoints - 1; i++)
    {
      g.drawLine((int)x[i],(int)y[i],(int)x[i+1],(int)y[i+1]);
    }
    g.drawLine((int)x[0],(int)y[0],(int)x[totalPoints - 1],(int)y[totalPoints - 1]);
  }
}

class Triangle extends Polygon
{
  Triangle(double x1, double y1, double x2, double y2,
           double x3, double y3, double xc, double yc)
  {
    super(3,xc,yc);
    setCoordForOneVertex(0, x1, y1);
    setCoordForOneVertex(1, x2, y2);
    setCoordForOneVertex(2, x3, y3);
  }
  
  //New method: TO DO
  double getArea()
  {
    double area = 0.0;
    {
      //requires code to calculate area
    }
    return (area);
  }
  
  //New method: TO DO
  void displayStringInside(String theString)
  {
    //requires code to display theString centralized
    //within the figure
  }
}

class Rectangle extends Polygon
{
  //New: Given constructor
  Rectangle ()
  {
    super(4,0.0,0.0);
  }
  
  Rectangle (double x1, double y1, double x2, double y2)
  {
    super(4,0.0,0.0);
    double midX,
           midY;
           
    midX = (x1 + x2)/2.0;
    midY = (y1 + y2)/2.0;
    setCenterCoords(midX,midY);
    setCoordForOneVertex(0, x1, y1);
    setCoordForOneVertex(1, x2, y1);
    setCoordForOneVertex(2, x2, y2);        
    setCoordForOneVertex(3, x1, y2);    
  }
  
  //New method: TO DO
  double getArea()
  {
    double area = 0.0;
    {
      //requires code to calculate area
    }
    return (area);
  }
  
  //New method: TO DO
  void displayStringInside(String theString)
  {
    //requires code to display theString centralized
    //within the figure
  }
}

//*** New class: Given and to be Explained
class Cuadrado extends Rectangle
{
  Cuadrado (double x1, double y1, double width)
  {
    super(x1,y1,x1+width,y1+width);
  }
}

public class HerenciaGeometria2 extends java.applet.Applet
{
  Polygon poly1;
  Triangle triangle1;
  Rectangle rectangle1;
  Graphics g;
	
  void delayMiliSecs(int delay)
  {
    try
	 {
	   Thread.sleep(delay);
	 }
	 catch(InterruptedException e)
	 {
	 }
  }
  
  public void init() 
  {
   
    triangle1 = new Triangle(10,10,30,50,40,20,25,30);
    rectangle1 = new Rectangle(80,80,140,100);
    
    poly1 = new Polygon(5,40,25);
    poly1.setCoordForOneVertex(0,20,40);
    poly1.setCoordForOneVertex(1,60,40);
    poly1.setCoordForOneVertex(2,60,10);
    poly1.setCoordForOneVertex(3,20,10);  
    poly1.setCoordForOneVertex(4,30,30);  
    poly1.moveDown(100); 
                
    setBackground(Color.red);
    setForeground(Color.black);
  }
   
  public void start() 
  {
	  //no code here
  }
   
  public void paint(Graphics g) 
  {
    triangle1.draw(g);
    triangle1.moveDown(50);
    delayMiliSecs(1000);
    triangle1.draw(g);
	  poly1.draw(g);
    delayMiliSecs(1000);
    poly1.grow(2);
	  poly1.draw(g);
    delayMiliSecs(1000);
    rectangle1.grow(2);
    rectangle1.draw(g);
	}
}	