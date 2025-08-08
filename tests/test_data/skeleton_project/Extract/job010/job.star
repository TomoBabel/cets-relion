
# version 50001

data_job

_rlnJobTypeLabel             relion.pseudosubtomo
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
   binning          6 
  box_size        192 
 crop_size         96 
do_float16        Yes 
  do_queue         No 
do_stack2d        Yes 
in_optimisation Picks/job009/optimisation_set.star 
in_particles         "" 
in_tomograms         "" 
in_trajectories         "" 
  max_dose         50 
min_dedicated         24 
min_frames          1 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript /public/EM/RELION/relion-slurm-gpu-4.0.csh 
 queuename    openmpi 
use_direct_entries         No 
 
