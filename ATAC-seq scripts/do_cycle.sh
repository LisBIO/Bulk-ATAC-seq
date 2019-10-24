
#fqdir='bed.file'

for f in  ./*.bed
do
    root=`basename $f`            # 不带路径的文件名
    #echo $root
    
    if [[ $root == *.bed ]]   # root 为含有uniq_peaks*.bed的文件 
    then 
        #echo PE $root
        bf=`echo $root | sed -r 's/.bed//g'` 
        #删除uniq_peaks_ 和 .bed 部分->bf
        p1=`echo $root`                      # p1=$root
        #echo $bf
        echo $p1
        echo  ...  $bf
        qsub -N $bf.pe -v p1=./$p1,out=$bf do_mt.sh
        sleep 1
    fi 
done
