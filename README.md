# MakeUofT-2T0-Cacophonate

Problem statement:

People want to be able to get automated feedback for their piano practices.

High-level Objectives:

To develop a device that:
- Records and store piano practice data (MIDI input or audio)
- Store an exemplar of the piece being practiced
- Compare practice with exemplar
- Provide meaningful feedback for the practice about their pitch, accuracy, rhythm, articulation, dynamics
	* MIDI notes store attack, release, velocity data

Detailed Objectives:

1. Get MIDI input directly from the keyboard (analog to MIDI: hardware. another option is audio to MIDI)
2. Store a practice session
3. Stream a MIDI using the same interface as if it were being played in real time
4. Segment different pieces (?)
5. Get some exemplar pieces
6. Generate test data for the exemplars
7. Compare exemplar data to test data

Hardware needs:

- Raspberry Pi
- Microphone
- MIDI keyboard

Notes:

- If you stumble and it sets you back a beat, the program should adjust for the tempo
