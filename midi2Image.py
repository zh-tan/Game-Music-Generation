import mido
import numpy as np
import scipy.misc
from os import listdir

TIMESTEP = 0.2
TIME_BREAK = 1000

def preprocess(mid):
	max_time = int(mid.length / TIMESTEP)
	max_channel = 15
	max_pitch = 127
	"""for msg in mid:
		if msg.type == 'note_on':
			max_channel = max(max_channel, msg.channel)"""
	arr = np.zeros((max_time+1, max_pitch+1, max_channel+1))
	time = 0
	for msg in mid:
		time = time + msg.time
		if msg.type == 'note_on':
			arr[int(time/TIMESTEP), msg.note, msg.channel] = msg.velocity
		#else:
		#	print(msg)
	seq = int(max_time / TIME_BREAK)*2 + 3
	out = np.zeros((seq,TIME_BREAK,max_pitch+1,max_channel+1))
	tb = TIME_BREAK//2
	for i in range(0,max_time, tb):
		i_ind = int(i/tb)
		tmp = arr[i:(i+tb),:,:]
		out[i_ind,tb:(tb+tmp.shape[0]),:,:] = tmp
		out[i_ind+1,:tmp.shape[0],:,:] = tmp
	return out[:,:,:,:1]

pows = [2,4,8]
def im_encode(arr):
	arr_copy = np.zeros((arr.shape[0], arr.shape[1], 3))
	for i in range(arr.shape[2]):
		i = i + 1
		for j in range(3):
			if i % pows[j] >= pows[j]/2:
				arr_copy[:,:,j] = np.maximum(arr_copy[:,:,j],arr[:,:,i])
	return arr_copy
files = [m for m in listdir('SNES')]
allfiles = []
for i in range(0,10):
	m = files[i]
	print(m)
	print(i, "/", len(files))
	allfiles.append(preprocess(mido.MidiFile("/".join(['SNES',m]),clip=True)))
data = np.concatenate(allfiles,axis=0)
print(data.shape)
np.save("data",data)
