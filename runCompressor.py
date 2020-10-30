''' Written By Dave Moffat 30/10/2020'''
'''Copyright 2020'''

#!/usr/bin/python

import numpy as np
import soundfile as sf
import compressor

audio,sr = sf.read('test.wav')

print(audio.shape, sr)

for sample in audio:
	mono_sample = np.mean(sample)
	control_gain = compressor.gain_computer(mono_sample, threshold=-20, ratio=3, attack=100, release=200, makeupGain=None, kneeWidth=2.5, samplerate=sr)
	sample *= control_gain

print('Writing Audio')
sf.write('test_compressed.wav', audio, sr)