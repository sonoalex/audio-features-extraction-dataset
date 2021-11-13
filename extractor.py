from essentia.standard import MonoLoader, ZeroCrossingRate,Loudness, SpectralCentroidTime, Energy, RMS, MFCC, Spectrum, Windowing
from audio_loader import AudioLoader
import csv
import os
import sys

rootdir = './genres'
tagged = './genres/input.mf'
audio_with_tag = {}
audio_loader  = AudioLoader(rootdir)
paths = audio_loader.get_audio_filepaths()
results = []
zcr = ZeroCrossingRate()
loudness = Loudness()
sct = SpectralCentroidTime()
energy = Energy()
rms = RMS()
spectrum = Spectrum()
w = Windowing(type='hann')
mfcc = MFCC(inputSize=4096)

with open(tagged) as file:
    for line in file:
        basename = os.path.basename(line)
        splitted = basename.split()
        audio_with_tag.update({splitted[0]:splitted[1]})
        
for path in paths:
    loader = MonoLoader(filename=path)
    audio = loader()
    file_basename = os.path.basename(path)
    frame = audio[2*44100 : 2*44100 + 8192]
    mX = spectrum(w(frame))
    bands, m = mfcc(mX)
    list1 = [zcr(audio), 
            loudness(audio),
            sct(audio),
            energy(audio),
            rms(audio)
            ]
    list_file = [file_basename, audio_with_tag[file_basename]]
    results.append([*list1 , *m, *list_file])

with open('data_genres_features.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results)