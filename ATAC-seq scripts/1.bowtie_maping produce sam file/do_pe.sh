#PBS -l walltime=336:00:00
#PBS -l nodes=2:ppn=10
#PBS -j oe
#PBS -o ${out}.log
#PBS -V 
cd $PBS_O_WORKDIR

pts='-p 10 --very-sensitive --end-to-end'
ropts='--no-unal --phred33'
bowtie2 $pts $ropts -x '/public/software/genomics/genome/bt2_index/hg38' -1 ${p1} -2 ${p2} -S ${out}.sam 
