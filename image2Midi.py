import mido
import numpy as np

data = np.load("data.npy")
print(data.shape)
m = mido.MidiFile()
#(9, 1000, 129, 17)
tracks = []
for i in range(data.shape[3]):
	tracks.append(mido.MidiTrack())
	m.tracks.append(tracks[-1])

lasttime=0
for i in range(data.shape[0]):
	print(i, "/", data.shape[0])
	for j in range(data.shape[1]//2,data.shape[1]):
		for k in range(data.shape[2]):
			for q in range(data.shape[3]):
				if data[i,j,k,q] > 32:
					tracks[q].append(mido.Message('note_on', note=k, velocity=int(data[i,j,k,q]), time=100*(j-lasttime)))
					lasttime = j
	lasttime -= data.shape[1]//2
	
m.save('output/output.mid')
