import mido

print(mido.get_input_names())
print(mido.get_output_names())

with mido.open_input('2- LoopBe Internal MIDI 1') as idevice, mido.open_output('Microsoft GS Wavetable Synth 0') as odevice:
    while True:
        msg = idevice.receive()
        print(msg)
        odevice.send(msg)
        
