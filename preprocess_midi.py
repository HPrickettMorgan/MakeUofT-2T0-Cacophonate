import mido
from itertools import chain


def get_note_dicts(midifile):
    """Returns a list of dicts where each dict represents a midi event. Times are absolute since the beginning of the song"""
    dicts = [{"type": msg.type, "note": msg.note, "time": msg.time} for msg in midifile if msg.type in ("note_on", "note_off")]
    fix_times(dicts)
    return dicts

def fix_times(dicts):
    """Converts a list of dicts of timedelta midi to absolutely timed event"""
    sum_time = 0
    for msg in dicts:
        sum_time += msg["time"]
        msg["time"] = sum_time

def sort_chords(dicts, chord_tolerance=0.01):
    current_chord = []
    all_chords = []
    for i in range(len(dicts)):
        current_chord.append(dicts[i])
        if(i == len(dicts)-1 or dicts[i+1]["time"] - dicts[i]["time"] >= chord_tolerance):
            all_chords.append(sorted(current_chord, key=lambda x: x["note"]))
            current_chord = []
    return chain(*dicts)

def stringify_notes(dicts):
    return "".join(map(lambda x: chr(x["note"]), dicts))

def print_opcodes(opcodes):
    for opcode in opcodes:
        if opcode[0] == 'replace':
            print("Practice", str(opcode[1]) + ":" + str(opcode[2]), "should be replaced by Exemplar", str(opcode[3]) + ":" + str(opcode[4]))
        elif opcode[0] == 'delete':
            print("Practice", str(opcode[1]) + ":" + str(opcode[2]), "should be deleted")
        elif opcode[0] == 'insert':
            print("Exemplar", str(opcode[3]) + ":" + str(opcode[4]), "should be inserted at Practice", opcode[1])
