
# version 50001

data_job

_rlnJobTypeLabel             relion.ctfrefinetomo
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
  box_size        512 
do_defocus        Yes 
do_frame_scale        Yes 
  do_queue         No 
do_reg_def        Yes 
  do_scale        Yes 
do_tomo_scale         No 
focus_range       3000 
in_halfmaps Reconstruct/job035/half1.mrc 
in_optimisation Refine3D/job034/run_optimisation_set.star 
in_particles         "" 
   in_post PostProcess/job036/postprocess.star 
in_refmask mask_align.mrc 
in_tomograms         "" 
in_trajectories         "" 
    lambda        0.1 
min_dedicated        112 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript my-cpu-localbuild.sh 
 queuename        cpu 
use_direct_entries         No 
 
