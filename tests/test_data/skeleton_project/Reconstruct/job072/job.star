
# version 50001

data_job

_rlnJobTypeLabel             relion.reconstructparticletomo
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
  do_queue         No 
in_optimisation Extract/job071/optimisation_set.star 
in_particles         "" 
in_tomograms         "" 
in_trajectories         "" 
min_dedicated        112 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript my-cpu-localbuild.sh 
 queuename        cpu 
       snr          0 
  sym_name         C6 
use_direct_entries         No 
 
