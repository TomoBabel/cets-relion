
# version 50001

data_pipeline_general

_rlnPipeLineJobCounter                      84
 

# version 50001

data_pipeline_processes

loop_ 
_rlnPipeLineProcessName #1 
_rlnPipeLineProcessAlias #2 
_rlnPipeLineProcessTypeLabel #3 
_rlnPipeLineProcessStatusLabel #4 
Import/job001/       None relion.importtomo  Succeeded 
MotionCorr/job002/       None relion.motioncorr.own  Succeeded 
CtfFind/job003/       None relion.ctffind.ctffind4  Succeeded 
ExcludeTiltImages/job004/       None relion.excludetilts  Succeeded 
AlignTiltSeries/job005/       None relion.aligntiltseries  Succeeded 
Tomograms/job006/       None relion.reconstructtomograms  Succeeded 
Denoise/job007/ Denoise/train/ relion.denoisetomo  Succeeded 
Denoise/job008/ Denoise/predict/ relion.denoisetomo  Succeeded 


# version 50001

data_pipeline_nodes

loop_ 
_rlnPipeLineNodeName #1 
_rlnPipeLineNodeTypeLabel #2 
_rlnPipeLineNodeTypeLabelDepth #3 
Import/job001/tilt_series.star TomogramGroupMetadata.star.relion.tomo.import            1 
MotionCorr/job002/corrected_tilt_series.star TomogramGroupMetadata.star.relion.tomo.motioncorr            1 
MotionCorr/job002/logfile.pdf LogFile.pdf.relion.motioncorr            1 
CtfFind/job003/tilt_series_ctf.star TomogramGroupMetadata.star.relion.tomo.ctffind            1 
CtfFind/job003/logfile.pdf LogFile.pdf.relion.ctffind            1 
ExcludeTiltImages/job004/selected_tilt_series.star TomogramGroupMetadata.star.relion.tomo.excludeimages            1 
AlignTiltSeries/job005/aligned_tilt_series.star TomogramGroupMetadata.star.relion.tomo.aligntiltseries            1 
Tomograms/job006/tomograms.star TomogramGroupMetadata.star.relion.tomo.reconstruct            1 
Denoise/job007/tomograms.star TomogramGroupMetadata.star.relion.tomo.denoise            1 
Denoise/job008/tomograms.star TomogramGroupMetadata.star.relion.tomo.denoise            1 


# version 50001

data_pipeline_input_edges

loop_ 
_rlnPipeLineEdgeFromNode #1 
_rlnPipeLineEdgeProcess #2 
Import/job001/tilt_series.star MotionCorr/job002/ 
MotionCorr/job002/corrected_tilt_series.star CtfFind/job003/ 
CtfFind/job003/tilt_series_ctf.star ExcludeTiltImages/job004/ 
ExcludeTiltImages/job004/selected_tilt_series.star AlignTiltSeries/job005/ 
AlignTiltSeries/job005/aligned_tilt_series.star Tomograms/job006/ 
Tomograms/job006/tomograms.star Denoise/job007/ 
Tomograms/job006/tomograms.star Denoise/job008/ 


# version 50001

data_pipeline_output_edges

loop_ 
_rlnPipeLineEdgeProcess #1 
_rlnPipeLineEdgeToNode #2 
Import/job001/ Import/job001/tilt_series.star 
MotionCorr/job002/ MotionCorr/job002/corrected_tilt_series.star 
MotionCorr/job002/ MotionCorr/job002/logfile.pdf 
CtfFind/job003/ CtfFind/job003/tilt_series_ctf.star 
CtfFind/job003/ CtfFind/job003/logfile.pdf 
ExcludeTiltImages/job004/ ExcludeTiltImages/job004/selected_tilt_series.star 
AlignTiltSeries/job005/ AlignTiltSeries/job005/aligned_tilt_series.star 
Tomograms/job006/ Tomograms/job006/tomograms.star 
Denoise/job007/ Denoise/job007/tomograms.star 
Denoise/job008/ Denoise/job008/tomograms.star 

