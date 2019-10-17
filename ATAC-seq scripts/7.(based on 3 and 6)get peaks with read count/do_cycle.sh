#fqdir='/public/home/dwli/DNA-seq/ATAC-seq/OSK_shSap30/uniq_reads_trk'
#fqdir='../../GFP_sort_data/uniq_reads_trk/'
# PE reads first, as they are likely to be faster.
fqdir='../uniq_reads_trk'
for f in  $fqdir/*.trk
do
    root=`basename $f`

    if [[ $root == *.trk ]]
    then 
        bf=`echo $root | sed -r 's/.trk//g'`
        echo map ...  $bf
        p1=$bf
        sed -i s/NNNNNNNN/$p1/g 10.mega_peak_tags.py
        grep saveTSV 10.mega_peak_tags.py
        qsub -N map -v inp=$root,out=$bf do_python.sh
        sleep 10
        sed -i s/$p1/NNNNNNNN/g 10.mega_peak_tags.py
        grep saveTSV 10.mega_peak_tags.py
        echo #######  this run is submitting ##########
        
    
    fi 
done
