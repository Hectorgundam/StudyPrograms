/*
Upload Assignment: Laboratorio 7 - Polimorfismo
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscarán el módulo 16
Lean la lección 18 y vean los archivos allí contenidos

Luego haga los siguiente:
Realice el ejercicio 1 que se encuentra en página 16
Documente el código describiendo sus distintas partes utilizando comentarios
Entregue la nueva jeraquía del diagrama de la figura 1 (Word, Paint, etc.) mostrando las modificaciones
Recuerde participar en el foro de discusión correspondiente
Después que vea su perfecto funcionamiento entregue aquí el código (.java) del programa y la nueva jeraquía
También entregue un “print screen” del código y la corrida del programa

Modulo 16 - Leccion 18 - Ejercicio 1 
Modifique la estructura de la Figura 1 para incluir el atributo pico en la clase Animal
y que el mismo se maneje en los constructores y en toString(). Las clases que
hereden directa o indirectamente de Animal tienen que hacer los ajustes
correspondientes para incluir el valor de este atributo. Construya una clase
Ornitorrinco que herede de mamífero. Añada la clase Reptil que hereda directamente
de Animal y las clases Serpiente y Cocodrilo que heredan directamente de Reptil.
Escriba una clase con el código necesario para demostrar que su diseño es correcto


*/

//Class Declaration for Animal 
//In this case, this is the superclass or the parent class
class Animal
{

//Variable declarations
 String especie = "";
 int totalDePatas = 0;
 boolean tieneEscamas = false,
 tienePelo = false,
 tienePlumas = false,
 tieneSangreCaliente = false, 
 tienePico = false; ;
 String sonido;

//Constructor for Animal that takes in several arguments 
 Animal(int totPatas, boolean escamas, boolean pelo, boolean plumas, boolean sangreCaliente, boolean pico)
 {
 
 //The pointer totalDePatas will point to the location of totPatas 
 this.totalDePatas = totPatas;
 //The pointer tieneEscamas will point to the location of escamas 
 this.tieneEscamas = escamas;
 //The pointer tienePelo will point to the location of pelo 
 this.tienePelo = pelo;
 //The pointer tienePlumas will point to the location of plumas 
 this.tienePlumas = plumas;
//The pointer tieneSangreCaliente will point to the location of sangreCaliente
 this.tieneSangreCaliente = sangreCaliente;
 //The pointer tienepico will point to the locatio of sangraCalient 
 this.tienePico = pico; 
 
 }

//Uses a pointer to point to the location of especie 
 void setEspecie(String especie)
 {
 
 //The pointer especie will point to the location of especie 
 this.especie = especie;
 
 }

//Returns the string especie 
 String getEspecie()
 {
 
 //The value of especie will be returned 
 return especie;
 
 }

//Currently empty but will be used and overloaded by it's subclasses 
 void hacerSonido()
 {
 
 //Empty for now 
 
 }

//Returns the value of sonido
 String getSonido()
 {
 
 //The value of sonido will be returned 
 return(sonido);
 
 }


//Creates a string that contains information that can be printed 
 public String toString()
 {
 
 //String declaration 
 String str;
 
 //Defining the contents of the string
 str = "Especie = " + especie + "\n" +
 "patas = " + totalDePatas + "\n" +
 "escamas = " + tieneEscamas + "\n" +
 "pelo = " + tienePelo + "\n" +
 "plumas = " + tienePlumas + "\n" +
 "sang cal = " + tieneSangreCaliente + "\n" +
 "pico = " + tienePico;

//The value of the string str will be returned 
 return(str);
 
 }
}

//Subclasses

//Subclass Mamifero that inherits from the class Animal 
class Mamifero extends Animal
{

//Constructor for Mamifero
 Mamifero()
 {
 
//Makes use of the controller from it's parent class Animal and provides the values of the arguments being passed 
 super(4, false, true, false, true, false);
 
 }
}

//Subclass Ave that inherits from the class Animal 
class Ave extends Animal
{

//Constructor for Ave
 Ave()
 {
 
 //Makes use of the controller from it's parent class Animal and provides the values of the arguments being passed 
 super(2, true, false, true, true, true);
 
 }
}

//Subclass Reptil inherits from Animal 
class Reptil extends Animal
{

//Constructor for Reptil
 Reptil()
 {
 
 //Makes use of the controller from it's parent class Animal and provides the values of the arguments being passed 
 super(4, true, false, false, false, false);
 
 }
}

//Subclass Perro that inherits from Mamifero
//Subclass Mamifero inherits from Animal
class Perro extends Mamifero
{

//Constructor for Perro
 Perro()
 {
 
 //String especie is assigned a value 
 especie = "perro";
 
 }
 
 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //Printing out a message onto the screen 
 System.out.println("Guau guau");
 
 }
}

//Subclass Gato inherits from Mamifero
//Subclass Mamifero inherits from Animal 
class Gato extends Mamifero
{

 //Constructor for Gato 
 Gato()
 {
 
 //String especie is assigned a value 
 especie = "gato";
 
}

 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //Prints out a message onto the screen 
 System.out.println("Miau miau");
 
 }
}

//Subclass Gallo inherits from Ave 
//Subclass Ave inherits from Animal 
class Gallo extends Ave
{

//Constructor for Gallo 
 Gallo()
 {
 
 //String especie is assigned a value 
 especie = "gallo";

 }

 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //String sonido is assigned a value
 sonido = "cucurucucuuuu";
 
 }

//The subclass Gallo creates a new method for itself
//It is empty for now 
 void escarbar()
 {
 
 //Empty for now 
 
 }
}

//Subclass Ornitorrinco inherits from Mamifero 
//Mamifero inherits from Animal 
class Ornitorrinco extends Mamifero
{

//Constructor for Ornitorrinco
 Ornitorrinco()
 {
 
 //String especie is assigned a value 
 especie = "ornitorrinco";
 
 }
 
 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //Printing out a message onto the screen 
 System.out.println("rrrRRRRtktktkt");
 
 }
}

//Subclass Serpiente inherits from Reptil
//Reptil inherits from Animal
class Serpiente extends Reptil
{

//Constructor for Reptil
 Serpiente()
 {
 
 //Overriding the value of totalDePatas for Serpiente, since snakes have no legs
 totalDePatas = 0; 
 
 //String especie is assigned a value 
 especie = "serpiente";
 
 }
 
 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //Printing out a message onto the screen 
 System.out.println("ssssssst");
 
 }
}

//Subclass Cocodrilo inherits from Reptil
//Reptil inherits from Animal
class Cocodrilo extends Reptil
{

//Constructor for Reptil
 Cocodrilo()
 {
  
 //String especie is assigned a value 
 especie = "cocodrilo";
 
 }
 
 //Implements its own method by overloading the hacerSonido() method from the Animal class
 void hacerSonido()
 {
 
 //Printing out a message onto the screen 
 System.out.println("zzzzcrrRRRRRRKH");
 
 }
}


//Main
public class Polimorfismo
{

public static void main (String args[])
{

//Creating an array object of class Animal that contains array objects w
Animal[] listaDeAnimales = new Animal[6];
listaDeAnimales[0] = new Perro();
listaDeAnimales[1] = new Gato();
listaDeAnimales[2] = new Gallo();
listaDeAnimales[3] = new Ornitorrinco();
listaDeAnimales[4] = new Serpiente(); 
listaDeAnimales[5] = new Cocodrilo(); 

//Printing out the contents of the specified array cell 
System.out.println(listaDeAnimales[0] + "\n");
System.out.println(listaDeAnimales[1] + "\n");
System.out.println(listaDeAnimales[2] + "\n");
System.out.println(listaDeAnimales[3] + "\n");
System.out.println(listaDeAnimales[4] + "\n");
System.out.println(listaDeAnimales[5] + "\n");

//Printing out the contents of the hacerSonido method of each object within the array 
listaDeAnimales[0].hacerSonido();
listaDeAnimales[1].hacerSonido();
listaDeAnimales[2].hacerSonido();
listaDeAnimales[3].hacerSonido();
listaDeAnimales[4].hacerSonido();
listaDeAnimales[5].hacerSonido();

//Also prints out the contents of the hacerSonido method of each object within the array 
//The difference in this one is that the value returned was a string, so we need to print it out 
System.out.println("Sonido del gallo: " + listaDeAnimales[2].getSonido());

}
}
