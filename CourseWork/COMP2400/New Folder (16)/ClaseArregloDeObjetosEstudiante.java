import java.io.*;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

class Estudiante
{
  String nombre,
         id;
  int    edad,
         cantidadDeNotas;
  double evaluaciones[];
 
  Estudiante()
  {
  }
  
  Estudiante(String nombre, String id, 
             int edad, int cantidadDeNotas)
  {
    this.nombre = nombre;
    this.id = id;
    this.edad = edad;
    this.cantidadDeNotas = cantidadDeNotas;
    evaluaciones = new double[cantidadDeNotas];
  }
  
  void setEvaluaciones(double evaluaciones[])
  {
    for (int i = 0; i < cantidadDeNotas; i++)
    {
      this.evaluaciones[i] = evaluaciones[i];
    }
  }
  
  double getPromedio()
  {
    double suma = 0,
           promedio;
    for (int i = 0; i < cantidadDeNotas; i++)
    {
      suma = suma + evaluaciones[i];
    }
    promedio = suma / cantidadDeNotas;

    return(promedio);
  }
  
  public String toString()
  {
    String str;
    str = "ID: " + id + " nombre: " + nombre;
    return(str); 
  }
}

public class ClaseArregloDeObjetosEstudiante
{
  public static void main(String[] args)
  {
    Scanner teclado = new Scanner(System.in);
    FileReader lectorDeArchivo;
    Scanner escanerDeArchivo;
    PrintWriter escritorAArchivo;
    
    Estudiante estudiantes[];
    
    String nombre,
           id,
           nombreDeArchivo,
           strLine;
    int    edad,
           numNotas,
           totalEstudiantes = 0,
           contadorEst = 0;
    double listaNotas[] = new double[10];       
      
    System.out.print("Archivo de datos: ");
    nombreDeArchivo = teclado.nextLine();
      
    try
		{
			lectorDeArchivo = new FileReader(nombreDeArchivo);
			escanerDeArchivo = new Scanner (lectorDeArchivo);	
      
      strLine = escanerDeArchivo.nextLine();
      totalEstudiantes = Integer.valueOf(strLine);
      estudiantes = new Estudiante[totalEstudiantes];

			while (escanerDeArchivo.hasNextLine())
			{
				strLine = escanerDeArchivo.nextLine();
				nombre = strLine;
				strLine = escanerDeArchivo.nextLine();
				id = strLine;
				strLine = escanerDeArchivo.nextLine();
				edad = Integer.valueOf(strLine);
				strLine = escanerDeArchivo.nextLine();
				numNotas = Integer.valueOf(strLine);

        for (int i = 0; i < numNotas; i++)
        {
          strLine = escanerDeArchivo.nextLine();
          listaNotas[i] = Double.valueOf(strLine);
        }
        
        estudiantes[contadorEst] = new Estudiante(nombre,id,edad,numNotas);
        estudiantes[contadorEst].setEvaluaciones(listaNotas);
        
        contadorEst = contadorEst + 1;
			
			}
			escanerDeArchivo.close();
      
      for (int i = 0; i < totalEstudiantes; i++)
      {
        System.out.println(estudiantes[i] + " promedio: " + 
        estudiantes[i].getPromedio());
      }      
      
		}
		catch (IOException e)
		{
			System.out.println("File error " + e);
		}
  }
}