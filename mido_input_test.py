import mido
import time 

print(mido.get_input_names())
print(mido.get_output_names())

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

start = time.time()
now = 0

##ticks_per_beat = 480
tempo = 500000

##with mido.open_input('2- LoopBe Internal MIDI 1') as idevice, mido.open_output('Microsoft GS Wavetable Synth 0') as odevice:
##    last = 0
##    while now < 7:
##        msgs = idevice.iter_pending()
##        now = time.time() - start
##        first = True
##        for msg in msgs:
##            if first:
##                first=False
##                ticks = int(mido.second2tick(now-last, mid.ticks_per_beat, tempo))
##                if(len(track) > 0):
##                    track[-1].time = ticks
##                last = now
##            odevice.send(msg)
##            track.append(msg)
##    for msg in track:
##        print(msg)
##mid.save('new_song.mid')

mid.ticks_per_beat = 2000

with mido.open_input('2- LoopBe Internal MIDI 1') as idevice, mido.open_output('Microsoft GS Wavetable Synth 0') as odevice:
    while now < 10:
        msg = idevice.poll()
        now = time.time() - start

        if msg:
            odevice.send(msg)
            msg.time = int(mido.second2tick(now, mid.ticks_per_beat, tempo))
            track.append(msg)

    for event in track:
        print(event)

    deltatick = [track[i].time - track[i-1].time for i in range(1, len(track))]
    deltatick.insert(0, 0)
    
    for i in range(len(track)):
        track[i].time = deltatick[i]

    for event in track:
        print(event)    
        
mid.save('new_song.mid')
