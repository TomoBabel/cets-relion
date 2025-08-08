
# version 50001

data_job

_rlnJobTypeLabel             relion.picktomo
_rlnJobIsContinue                       1
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
  do_queue         No 
in_star_file         "" 
in_tomoset Denoise/job008/tomograms.star 
min_dedicated         24 
other_args         "" 
particle_spacing         60 
 pick_mode    spheres 
      qsub     sbatch 
qsubscript /public/EM/RELION/relion-slurm-gpu-4.0.csh 
 queuename    openmpi 
 
