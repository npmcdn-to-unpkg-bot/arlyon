import mido

output = mido.open_output()
output.send(mido.Message('note_on', note=60, velocity=64))
