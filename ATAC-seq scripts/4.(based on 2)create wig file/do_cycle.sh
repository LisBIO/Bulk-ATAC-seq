file='uniq_read'
for f in  ../$file/*.sorted
do
    root=`basename $f`
    #echo $root

    if [[ $root == *.sorted ]]
    then 
        bf=`echo $root | sed 's/.bed.sorted//g'`
        total=10000000
	x=$( cat ../$file/$root | wc -l )
	nf=` echo "scale=3; $total / $x "| bc `
	echo $nf
	echo bg ... $root
        qsub -N $bf.se -v inp=../$file/$root,nf=$nf,out=$bf do_wig.sh
        sleep 1
    fi
done
