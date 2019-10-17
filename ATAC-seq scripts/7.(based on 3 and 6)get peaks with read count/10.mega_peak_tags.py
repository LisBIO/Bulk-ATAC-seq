
from __future__ import division
import numpy, math, pickle,glob
from glbase3 import *
import matplotlib.pyplot as plot
## load the mega peaks list
tracks = {}
'''
####just for the perpose -- get the library size
'''
##load one trk file
tracks['NNNNNNNN'] = track(filename='../uniq_reads_trk/NNNNNNNN.trk', name='NNNNNNNN')
expn = genelist(filename='/public/home/dwli/homer_ann_motif/peaks_file/human_peaks_list_1805.bed',format={'force_tsv':True,"loc": "location(chr=column[0], left=column[1], right=column[2])"})
expn.sort('loc')

track_sizes = {}
for t in tracks:
    track_sizes[t] = tracks[t].get_total_num_reads() / 1e6
#print track_sizes


#TR_res = {t: [] for t in tracks}

last_chrom = None
chr_data = {t: None for t in tracks}

valid_chroms = [str(i) for i in range(30)] + ['X', 'Y']

TE_table = []
for peak in expn: 
    scores = []
    for t in tracks:
        loc = peak['loc']      
        if peak['loc']['chr'] != last_chrom:    
            chr_data = tracks[t].get_array_chromosome(loc['chr'], read_extend=100) # use the fast cache system
            last_chrom = loc['chr']
            #print last_chrom
	    # It is taken from the density, don't divide by track_sizes, so that below it is more intelligible as median tags
        score = chr_data[loc['left']:loc['right']] 
    
        scores.append(numpy.mean(score)/track_sizes[t])
        
        #print "> %s	%.1f" % (loc, scores[-1])
        TE_table.append({'loc': peak['loc'],'conditions': scores})
#print len(TE_table)
#print TE_table
gl = expression(loadable_list=TE_table, cond_names=tracks.keys())
gl.saveTSV('map_tags/NNNNNNNN.tsv')
#gl.save('S-D1_S6_peak_table.glb')

