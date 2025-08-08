
# version 50001

data_job

_rlnJobTypeLabel             relion.postprocess
_rlnJobIsContinue                       0
_rlnJobIsTomo                           1
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
adhoc_bfac      -1000 
    angpix         -1 
autob_lowres         10 
do_adhoc_bfac         No 
do_auto_bfac         No 
  do_queue         No 
do_skip_fsc_weighting         No 
     fn_in Reconstruct/job065/half1.mrc 
   fn_mask mask_fsc.mrc 
    fn_mtf         "" 
  low_pass          5 
min_dedicated         24 
mtf_angpix          1 
other_args         "" 
      qsub     sbatch 
qsubscript /public/EM/RELION/relion-slurm-gpu-4.0.csh 
 queuename    openmpi 
 
