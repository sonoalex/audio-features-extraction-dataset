from essentia.standard import MonoLoader, ZeroCrossingRate,Loudness, SpectralCentroidTime, Energy, RMS
from audio_loader import AudioLoader
import csv
import os

rootdir = './genres'
tagged = './genres/bextract_single.mf'
audio_with_tag = {}
audio_loader  = AudioLoader(rootdir)
paths = audio_loader.get_audio_filepaths()
results = []
zcr = ZeroCrossingRate()
loudness = Loudness()
sct = SpectralCentroidTime()
energy = Energy()
rms = RMS()


with open(tagged) as file:
    for line in file:
        basename = os.path.basename(line)
        splitted = basename.split()
        audio_with_tag.update({splitted[0]:splitted[1]})
        
for path in paths:
    loader = MonoLoader(filename=path)
    audio = loader()
    file_basename = os.path.basename(path)
    
    results.append(
        [
            zcr(audio), 
            loudness(audio),
            sct(audio),
            energy(audio),
            rms(audio),
            file_basename,
            audio_with_tag[file_basename]
        ]
    )

with open('data_genres_features.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results)