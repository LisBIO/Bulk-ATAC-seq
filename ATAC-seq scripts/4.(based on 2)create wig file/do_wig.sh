#PBS -l walltime=336:00:00
#PBS -l nodes=1:ppn=4
#PBS -j oe
#PBS -o ${out}.log
#PBS -V 
cd $PBS_O_WORKDIR
sort -k1,1 -k2,2n ${inp} > ${out}.bed.sorted
genomeCoverageBed -bg -i ${out}.bed.sorted -scale $nf -g /public/home/dwli/UCSC_hg38/hg38_chr_size.txt > ${out}.bg
bedGraphToBigWig ${out}.bg /public/home/dwli/UCSC_hg38/hg38_chr_size.txt ${out}.bw.txt
#genomeCoverageBed -bg -i ../H3K9me3_rep1.bed.sorted -scale 3 -g ~/UCSC_mm10/Annotation/Genes/ChromInfo.txt > test.bg
rm ${out}.bg

