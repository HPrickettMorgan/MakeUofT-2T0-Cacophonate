import mido
import time 

print(mido.get_input_names())
print(mido.get_output_names())

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

tempo = 500000

with mido.open_input('2- LoopBe Internal MIDI 1') as idevice, mido.open_output('Microsoft GS Wavetable Synth 0') as odevice:
    start = time.time()
    last = 0
    now = 0

    while now < 10:
        msg = idevice.poll()
        now = time.time() - start

        if msg:
            odevice.send(msg)
            msg.time = int(mido.second2tick(now-last, mid.ticks_per_beat, tempo))
            last = now
            track.append(msg)

    for event in track:
        print(event)    
        
mid.save('new_song.mid')
