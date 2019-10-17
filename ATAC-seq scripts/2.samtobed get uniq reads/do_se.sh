#PBS -l walltime=336:00:00
#PBS -l nodes=1:ppn=4
#PBS -j oe
#PBS -o ${out}.log
#PBS -V 
cd $PBS_O_WORKDIR

samtools view -q 35 -b ${inp} | bedtools bamtobed | awk 'BEGIN {FS="\t";OFS="\t"}; {if ($6=="+" ) print $1,$2,$2+200,"Read","0",$6; else if ($6=="-") print $1,$3-200,$3,"Read","0",$6;}' | grep -v 'chrUn_' | grep -v 'random' | grep -v 'chrM' | awk '!x[$0]++' | sort -k 1,1 >${out}.sorted
	# No -q swithc as I want multimapping reads


