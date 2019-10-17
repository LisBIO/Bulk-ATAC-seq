#PBS -l walltime=336:00:00
#PBS -l nodes=1:ppn=2
#PBS -j oe
#PBS -q gpu
#PBS -o ${out}.log
#PBS -V 
cd $PBS_O_WORKDIR
python 8.creat_tracks_single.py
