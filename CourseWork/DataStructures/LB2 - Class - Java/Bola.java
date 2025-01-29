/*
Upload Assignment: Laboratorio#2 Clase Bola
COMP2400 - 202310-70846
Dr. Edgardo Vargas Moya

Assignment: 
Buscaran el modulo 9 y leeran la leccion 10. Luego haran lo siguiente: 
- Copiaran la Clase Bola y la Clase Ejemplo (en archivos separados, pero en una misma carpeta) que encuentra en las paginas 5 y 6. 
- Documente el codigo describiendo sus distintas partes utilizando comentarios. 
- Despues que vea su perfecto funcionamiento entregue aqui e; codigo (.java) del programa.
- Entregue un "print screen" del codigo y la corrida del programa. 

*/
 
//Class declaration for Bola
class Bola{

//Variable declaration for our class 
private float radio, 
               peso; 
       
//Assigning the values for our 2 variables, works sort of as a preset in a way 
Bola(){

radio = 1; 
peso = 2; 

}

//Assigning the values of our variables radio and peso to our class 
Bola (float r, float p){

radio = r; 
peso = p; 

}

//Assigning the value for our peso variable 
void setPeso(float p){

peso = p; 

}

//Obtaining and storing the value of the peso variable 
float getPeso()
{

return peso; 

}

//Assigning the value of our radio variable 
void setRadio(float r){

radio = r;

}

//Obtaining and storing the value of the radio variable 
float getRadio(){

return radio; 

}

//Multiplying the value of factor and the current value of radio and assigning the resulting value to the variable radio
void ampliarRadio(float factor){

radio = radio * factor; 

}

//Returning the message that will be printed onto the screen 
public String toString()
{

return ("radio = " + radio + "\npeso = " + peso);

}

}