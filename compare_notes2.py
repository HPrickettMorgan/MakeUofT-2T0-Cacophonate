import mido
import preprocess_midi
from fuzzywuzzy.StringMatcher import StringMatcher as SequenceMatcher

exemplar = preprocess_midi.get_note_dicts(mido.MidiFile('twinkle_twinkle.mid'))
practice = preprocess_midi.get_note_dicts(mido.MidiFile('practice.mid'))

exemplar_notes = preprocess_midi.sort_chords([msg for msg in exemplar if msg["type"] == 'note_on'])
practice_notes = preprocess_midi.sort_chords([msg for msg in practice if msg["type"] == 'note_on'])

for i, msg in enumerate(zip(exemplar_notes, practice_notes)):
        print(f"{i}: {str(msg[0]['note'])},  {str(msg[1]['note'])}")

sm = SequenceMatcher(None,
                     preprocess_midi.stringify_notes(practice_notes),
                     preprocess_midi.stringify_notes(exemplar_notes))

opcodes = sm.get_opcodes()
preprocess_midi.print_opcodes(opcodes)
