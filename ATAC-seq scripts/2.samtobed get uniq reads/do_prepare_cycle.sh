#fqdir='rmdup_bw.file'
for f in  ../bw.file/*.sam
do
    root=`basename $f`
    #echo $root

    if [[ $root == *.sam ]]
    then 
        bf=`echo $root | sed 's/.sam/.bed/g'`
        echo sam ... $root
        qsub -N $bf.se -v inp=../bw.file/$root,out=$bf do_se.sh
        sleep 1
    fi
done
