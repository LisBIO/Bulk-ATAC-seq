from glbase3 import *
import glob,os
import numpy as np
import matplotlib.cm as cm

config.draw_mode = 'svg'
#geo_high=expression(filename='./anno_class_merge/anno_long_merge_peaks_number.csv',format={'force_tsv':True,'skiplines':0,'name':0},expn="column[1:]")
geo_high=expression(filename='./motif_table_only/main_motif_5.txt',format={'force_tsv':True,'skiplines':0,'name':0},expn="column[1:]")
print (geo_high.getConditionNames())


# bracket=[-5,5],
# geo_high.heatmap(filename='plot/peaks_anno_enrich.svg' , size=[6,8],
# 	row_cluster=False, col_cluster=False, col_font_size=10,row_font_size=8,
# 	heat_wid=0.03*len(geo_high.getConditionNames()), heat_hei=0.015*len(geo_high),cmap=cm.bwr, border=True,
# 	grid=True, colbar_label='Log2 enrichment',
# 	draw_numbers=False)


# anno heatmap peaks_num 
#geo_high.heatmap(filename='plot/peaks_anno_enrich.svg' , size=[6,15],bracket=[0,5],
#        row_cluster=True, col_cluster=False,col_font_size=10,row_font_size=8,
#        draw_numbers=True,draw_numbers_threshold=3,draw_numbers_fmt='*',
#        heat_wid=0.03*len(geo_high.getConditionNames()), heat_hei=0.01*len(geo_high),
#                              log=10, cmap=cm.Reds,border=True,
#        grid=True, colbar_label='Log10(peak num)',)


# motif heatmap  sample
geo_high.heatmap(filename='plot/motif_anno_enrich_5.svg' , size=[6,15],bracket=[0,50],
	row_cluster=True, col_cluster=False,col_font_size=10,row_font_size=8,
	draw_numbers=True,draw_numbers_threshold=40,draw_numbers_fmt='*',
	heat_wid=0.03*len(geo_high.getConditionNames()), heat_hei=0.01*len(geo_high),
				 cmap=cm.Reds,border=True,
	grid=True, colbar_label='-Log10(P value)',)



