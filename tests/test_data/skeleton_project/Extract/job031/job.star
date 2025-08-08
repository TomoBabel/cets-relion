
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
   binning          1 
  box_size        512 
 crop_size        192 
do_float16        Yes 
  do_queue         No 
do_stack2d        Yes 
in_optimisation Polish/job030/optimisation_set.star 
in_particles         "" 
in_tomograms         "" 
in_trajectories         "" 
  max_dose         50 
min_dedicated        112 
min_frames          1 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript my-cpu-localbuild.sh 
 queuename        cpu 
use_direct_entries         No 
 
