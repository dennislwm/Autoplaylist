import Data_Collector as dc
import Related_Finder as gr
import numpy as np
import pandas as pd
import Dataset_Merger as dm
import collections
import Cluster as CT
import Song_NN_class as NN
import Cluster_Reassignment as CR
import Cluster_Spliter as CS
import Playlist_Creator as PC
ms = dc.map_songs
mp = dc.map_playlist
merge = dm.merge_datasets
f = gr.get_related
playlist = 'Swagger'
mp('37i9dQZF1DWSlw12ofHcMM', 'Spotify', playlist)
DF = pd.read_csv(playlist + '.csv')
a = list(set(DF['3'].values))
print(len(a))
# print(a)
# a = ['7mnBLXK823vNxN3UWB7Gfz', '37J1PlAkhRK7yrZUtqaUpQ']
b = f(a)
# print(b)
b = [item for item, count in collections.Counter(
    b).items() if count > min(5, (int(1 + .15 * len(a))))]
print(len(b))
a.extend(b)
a = list(set(a))
print(len(a))
# print(a)
ms(a, 1.0, n_keep=0, arquivo='Total')
n = CT.cluster()
NN.Classifier()
CR.reassigner(playlist)
CS.list_spliter(playlist)
PC.create_playlists(n, playlist)