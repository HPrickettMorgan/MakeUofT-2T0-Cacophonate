from fuzzywuzzy.StringMatcher import StringMatcher as SequenceMatcher
import mido
from itertools import chain
exemplar = mido.MidiFile('twinkle_twinkle.mid')
practice = mido.MidiFile('practice.mid')

exemplar = [{"type": msg.type,
             "channel": msg.channel,
             "note": msg.note,
             "velocity": msg.velocity,
             "time": msg.time}
            for msg in exemplar if msg.type in ("note_on", "note_off")]

practice = [{"type": msg.type,
             "channel": msg.channel,
             "note": msg.note,
             "velocity": msg.velocity,
             "time": msg.time}
            for msg in practice if msg.type in ("note_on", "note_off")]


sum_time = 0
for msg in exemplar:
    sum_time += msg["time"]
    msg["time"] = sum_time
    
sum_time = 0
for msg in practice:
    sum_time += msg["time"]
    msg["time"] = sum_time


time_delta = 0.03

exemplar_notes = [msg for msg in exemplar if msg["type"] == 'note_on']
practice_notes = [msg for msg in practice if msg["type"] == 'note_on']

current_notoquard = []
exemplar_notoquards = []
for i in range(len(exemplar_notes)-1):
    current_notoquard.append(exemplar_notes[i])
    if(exemplar_notes[i+1]["time"] - exemplar_notes[i]["time"] >= time_delta):
        exemplar_notoquards.append(sorted([msg["note"] for msg in current_notoquard]))
        current_notoquard = []

current_notoquard.append(exemplar_notes[-1])
exemplar_notoquards.append(sorted([msg["note"] for msg in current_notoquard]))

current_notoquard = []
practice_notoquards = []
for i in range(len(practice_notes)-1):
    current_notoquard.append(practice_notes[i])
    if(practice_notes[i+1]["time"] - practice_notes[i]["time"] >= time_delta):
        practice_notoquards.append(sorted([msg["note"] for msg in current_notoquard]))
        current_notoquard = []

current_notoquard.append(exemplar_notes[-1])
practice_notoquards.append(sorted([msg["note"] for msg in current_notoquard]))

for i, msg in enumerate(zip(chain(*exemplar_notoquards),
               chain(*practice_notoquards))):
    print(f"{i}: {str(msg[0])},  {str(msg[1])}")

sm = SequenceMatcher(None,
                     "".join(map(chr,chain(*practice_notoquards))),
                     "".join(map(chr,chain(*exemplar_notoquards))))
sm_opcodes = sm.get_opcodes()
for opcode in sm_opcodes:
    if opcode[0] == 'replace':
        print("Practice", str(opcode[1]) + ":" + str(opcode[2]), "should be replaced by Exemplar", str(opcode[3]) + ":" + str(opcode[4]))
    elif opcode[0] == 'delete':
        print("Practice", str(opcode[1]) + ":" + str(opcode[2]), "should be deleted")
    elif opcode[0] == 'insert':
        print("Exemplar", str(opcode[3]) + ":" + str(opcode[4]), "should be inserted at Practice", opcode[1])
