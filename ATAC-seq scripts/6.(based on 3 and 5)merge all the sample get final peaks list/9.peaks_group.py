
import os,glob
from glbase3 import *

config.draw_mode = "png"
filenames=[]
for i in glob.glob('../uniq_run_peaks/only_peak/ATAC*bed'):
    head=os.path.split(i)[-1].replace('.bed','')
    filenames.append(head)
#print filename

 # I want to avoid the unnecessary mini groups arising from 6m17p, but I still want it on te figure.
trks = [track(filename="../uniq_reads_trk/%s.trk" % f, name=f) for f in filenames]
peaks = [genelist(filename="../uniq_run_peaks/only_peak/%s.bed" % f, name=f, format=format.minimal_bed) for f in filenames]

gl = glglob() 
ret = gl.chip_seq_cluster_heatmap(peaks, trks, "cluster_plot/input_cluster_350bp_heatmap.png",normalise=True,merge_peaks_distance=350, cache_data=False, bins=50,
    pileup_distance=350)
gl.chip_seq_cluster_pileup(filename="cluster/cluster_350bp_lusters.png")

for cid in ret:
    print ("cid:", cid, "len:", len(ret[cid]["genelist"]))
    ret[cid]["genelist"].saveBED(filename="group_member/cluster_350bp_cid_%s.bed" % cid)

