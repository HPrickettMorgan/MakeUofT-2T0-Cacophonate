#include <MIDI.h>
const int potPin = A0; 
const int  buttonPin0 = 2;
const int buttonPin1 = 3;
const int buttonPin2 = 4;
const int baseOffset = 28;

int potValue = 0;
int buttonValue0 = 0;
int buttonValue1 = 0;
int buttonValue2 =  0;        
int prevNote = 0;
int note; 

 // Created and binds the MIDI interface to the default hardware Serial port
 MIDI_CREATE_DEFAULT_INSTANCE();

 void setup()
 {
     MIDI.begin();// Listen to all incoming messages
     Serial.begin(115200);
     pinMode(buttonPin0, INPUT_PULLUP);
 }

 void loop()
 {
   // potValue = analogRead(potPin);
   buttonValue0 = digitalRead(buttonPin0);
   Serial.println(buttonValue0);
   // buttonValue1 = digitalRead(buttonPin1);
   // buttonValue2 = digitalRead(buttonPin2);

   // note = int(potValue * (12.0/1023.0));

   // if (buttonValue0 == 1) {
   //    note += baseOffset;
   // } else if (buttonValue1 == 1) {
   //    note += baseOffset + 12;
   // } else if (buttonValue2 == 1) {
   //    note += baseOffset + 24
   // } else {
   //    continue;
   // }
   // MIDI.sendNoteOn(note, 127, 1);
   // delay(100); 
}
