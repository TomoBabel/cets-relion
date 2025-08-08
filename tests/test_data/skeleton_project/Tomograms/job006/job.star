
# version 50001

data_job

_rlnJobTypeLabel             relion.reconstructtomograms
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
binned_angpix         10 
  do_queue         No 
generate_split_tomograms        Yes 
in_tiltseries AlignTiltSeries/job005/aligned_tilt_series.star 
min_dedicated         24 
    nr_mpi          5 
nr_threads         12 
other_args         "" 
      qsub     sbatch 
qsubscript /public/EM/RELION/relion-slurm-gpu-4.0.csh 
 queuename    openmpi 
tiltangle_offset          0 
 tomo_name         "" 
      xdim       4000 
      ydim       4000 
      zdim       2000 
 
