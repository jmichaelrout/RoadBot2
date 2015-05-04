//Arduino Motor Control 
//Nathaniel Jackson, Jerrod Rout, Blake Taylor, Akash Patel
//Allows robot to move forward, backward, left, right, and stop when given commands
//

//Initialize pins to be used as inputs to H Bridges.
  int input8 = 8;
  int input9 = 9;
  int input10 = 10;
  int input11 = 11;

void setup() {
  
 //Initialize serial communications with a baud rate of 38400 b/s
 Serial.begin(38400);
 
 //Declare pins to be used as outputs - can turn on and off.
 //Pins 8,9 = Left motor inputs, Pins 10,11 = Right motor inputs
 pinMode(input8, OUTPUT);
 pinMode(input9, OUTPUT);
 pinMode(input10, OUTPUT);
 pinMode(input11, OUTPUT);
 
}

void loop() {
 
    String input = "";
     
    // Read serial input
    while (Serial.available() > 0)
    {
        input += (char) Serial.read(); // Read in one char at a time
        delay(5); // Delay for 5 ms so the next char has time to be received
    }
    

    //pin8 = 0, pin9 = 1: left motors spin clockwise
    //pin10 = 0, pin11 = 1: right motors spin clockwise
    //Since all motors spin clockwise, motion is forward.
    if (input == "GO")//Forward
    {
          digitalWrite(input8, LOW);
          digitalWrite(input9, HIGH);
          digitalWrite(input10, LOW);
          digitalWrite(input11, HIGH);
          delay(700);
    }
    //pin8 = 1, pin9 = 0: left motors spin counterclockwise
    //pin10 = 1, pin11 = 0: tight motors spin counterclockwise
    //Since all motors spin counterclockwise, motion is backward.
    else if (input == "BACK") //Backward
    {
          digitalWrite(input8, HIGH);
          digitalWrite(input9, LOW);
          digitalWrite(input10, HIGH);
          digitalWrite(input11, LOW);
          delay(700);
    }
    //pin8 = 0, pin9 = 0: left motors do not spin
    //pin10 = 0, pin11 = 0:right motors do not spin
    //When all pins are off or all pins are on motors will stop turning
     else if (input == "STOP") //Stop
     {
          digitalWrite(input8, LOW);
          digitalWrite(input9, LOW);
          digitalWrite(input10, LOW);
          digitalWrite(input11, LOW);
          delay(700);
     }
     //pin8 = 0, pin9 = 1: left motors spin clockwise
     //pin10 = 1, pin11 = 0: right motors spin counterclockwise
     //Robot turns right
     else if (input == "RIGHT") //Right
     {
          digitalWrite(input8, LOW);
          digitalWrite(input9, HIGH);
          digitalWrite(input10, HIGH);
          digitalWrite(input11, LOW);
          delay(700);
     }
     //pin8 = 1, pin9 = 0: left motors spin counterclockwise
     //pin10 = 0, pin11 = 1: right motors spin clockwise
     //Robot turns Left
     else if (input == "LEFT") //Left
     {
          digitalWrite(input8, HIGH);
          digitalWrite(input9, LOW);
          digitalWrite(input10, LOW);
          digitalWrite(input11, HIGH);
          delay(700);
     }

}
