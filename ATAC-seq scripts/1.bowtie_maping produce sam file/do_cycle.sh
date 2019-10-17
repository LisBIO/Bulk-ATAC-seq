fqdir='fastq.file'

# PE reads first, as they are likely to be faster.

for f in  ../$fqdir/*.fastq.gz
do
    root=`basename $f`
    #echo $root

    if [[ $root == *L000_R1_001.fastq.gz ]]
    then 
        #echo PE $root
        bf=`echo $root | sed -r 's/_L000_R1_001.fastq.gz//g'`
        #rep=`echo $root |sed s/_*.fastq//g`
        p1=`echo $root`
        p2=`echo $root | sed 's/_R1/_R2/g'`
        #echo $bf
        echo $p1
        echo $p2
        echo PE ...  $bf
        qsub -N bowtie.pe -v p1=../$fqdir/$p1,p2=../$fqdir/$p2,out=$bf do_pe.sh
        sleep 1
    
     else
     if [[ $root == *_NNNNN.fastq.gz ]]
        then 
            bf=`echo $root | sed -r 's/.fastq.gz//g'`
            echo SE ... $root
            echo qsub -N $bf.se -v inp=../$fqdir/$root,out=$bf do_se.sh
            sleep 1
        fi
    fi 
done
