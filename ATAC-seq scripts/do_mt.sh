#PBS -l walltime=336:00:00
#PBS -l nodes=2:ppn=2
#PBS -j oe
#PBS -o ${out}.log
#PBS -V 
cd $PBS_O_WORKDIR

mkdir ${out}_output

#findMotifsGenome.pl $p1 hg38 ${out}_output/ -preparsedDir /public/home/yuliu_gibh/DNA-seq/human_ATAC/H1_to_iCM/motifs_genome/motif_a/

findMotifsGenome.pl ${p1} mm10 ${out}_output/ -size 200 -mask -preparsedDir ./

#findMotifsGenome.pl ./uniq_peaks_s308-2.bed mm10 s308-2out/ -size 200 -mask
