
for f in  ./*.bed.sorted
do
    root=`basename $f`

    if [[ $root == *.bed.sorted ]]
    then 
        bf=`echo $root | sed -r 's/.bed.sorted//g'`
        echo trk ...  $bf
        p1=$bf
        sed -i s/NNNNNNNN/$p1/g 8.creat_tracks_single.py 
        grep seqToTrk 8.creat_tracks_single.py 
        qsub -N $bf -v inp=$root,out=$bf do_python.sh
        sleep 10
        sed -i s/$p1/NNNNNNNN/g 8.creat_tracks_single.py
        echo #######  this run is submitting ##########
        
    
    fi 
done
