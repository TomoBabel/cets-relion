
# version 50001

data_job

_rlnJobTypeLabel             relion.framealigntomo
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
  box_size        512 
 do_motion        Yes 
  do_queue         No 
do_shift_align         No 
do_sq_exp_ker         No 
in_halfmaps Reconstruct/job058/half1.mrc 
in_optimisation CtfRefine/job057/optimisation_set.star 
in_particles         "" 
   in_post PostProcess/job059/postprocess.star 
in_refmask mask_align.mrc 
in_tomograms         "" 
in_trajectories         "" 
 max_error          5 
min_dedicated        112 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript my-cpu-localbuild.sh 
 queuename        cpu 
shift_align_type "Entire micrographs" 
 sigma_div       5000 
 sigma_vel        0.2 
use_direct_entries         No 
 
