#include <MIDI.h>
const int analogInPin = A0;  
int sensorValue = 0;        
int prevNote = 0;
int note; 

 // Created and binds the MIDI interface to the default hardware Serial port
 MIDI_CREATE_DEFAULT_INSTANCE();

 void setup()
 {
     MIDI.begin();// Listen to all incoming messages
     Serial.begin(115200);
 }

 void loop()
 {
    sensorValue = analogRead(analogInPin);
    note = int(sensorValue/85);
  
  if (note != prevNote){
     MIDI.sendNoteOn(40+note, 127, 1);
     prevNote = note;
     delay(100); 
  }
  
 }
