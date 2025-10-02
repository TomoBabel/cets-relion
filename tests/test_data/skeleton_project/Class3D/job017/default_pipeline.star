
# version 50001

data_pipeline_general

_rlnPipeLineJobCounter                      18
 

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
Picks/job009/       None relion.picktomo  Succeeded 
Extract/job010/ Extract/bin6/ relion.pseudosubtomo  Succeeded 
Reconstruct/job011/       None relion.reconstructparticletomo  Succeeded 
Refine3D/job012/ Refine3D/bin6/ relion.refine3d.tomo  Succeeded 
Extract/job013/ Extract/bin2/ relion.pseudosubtomo  Succeeded 
Reconstruct/job014/ Reconstruct/bin2reference/ relion.reconstructparticletomo  Succeeded 
Refine3D/job015/ Refine3D/bin2/ relion.refine3d.tomo  Succeeded 
Select/job016/ Select/remove-dups/ relion.select.removeduplicates  Succeeded 
Class3D/job017/       None relion.class3d    Running 
 

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
Picks/job009/particles.star ParticleGroupMetadata.star.relion.tomo.manualpick.spheres            1 
Picks/job009/optimisation_set.star TomoOptimisationSet.star.relion.tomo.manualpick            1 
Extract/job010/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job010/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job011/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job011/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job011/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
Refine3D/job012/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job012/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job012/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job012/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job012/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Extract/job013/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job013/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job014/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job014/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job014/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
Refine3D/job015/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job015/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job015/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job015/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job015/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Select/job016/particles.star ParticleGroupMetadata.star.relion            1 
Class3D/job017/run_it025_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Class3D/job017/run_it025_optimiser.star OptimiserData.star.relion.class3d            1 
Class3D/job017/run_it025_class001.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class002.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class003.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class004.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class005.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class006.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class007.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class008.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_class009.mrc DensityMap.mrc.relion.class3d            1 
Class3D/job017/run_it025_optimisation_set.star TomoOptimisationSet.star.relion.class3d            1 
Class3D/job017/run_optimisation_set.star TomoOptimisationSet.star.relion.class3d            1 
 

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
Denoise/job008/tomograms.star Picks/job009/ 
Picks/job009/optimisation_set.star Extract/job010/ 
Extract/job010/optimisation_set.star Reconstruct/job011/ 
Extract/job010/optimisation_set.star Refine3D/job012/ 
Reconstruct/job011/merged.mrc Refine3D/job012/ 
Refine3D/job012/run_optimisation_set.star Extract/job013/ 
Extract/job013/optimisation_set.star Reconstruct/job014/ 
Extract/job013/optimisation_set.star Refine3D/job015/ 
Reconstruct/job014/half1.mrc Refine3D/job015/ 
Refine3D/job015/run_data.star Select/job016/ 
Select/job016/particles.star Class3D/job017/ 
Denoise/job008/tomograms.star Class3D/job017/ 
Refine3D/job015/run_class001.mrc Class3D/job017/ 
 

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
Picks/job009/ Picks/job009/particles.star 
Picks/job009/ Picks/job009/optimisation_set.star 
Extract/job010/ Extract/job010/optimisation_set.star 
Extract/job010/ Extract/job010/particles.star 
Reconstruct/job011/ Reconstruct/job011/merged.mrc 
Reconstruct/job011/ Reconstruct/job011/half1.mrc 
Reconstruct/job011/ Reconstruct/job011/optimisation_set.star 
Refine3D/job012/ Refine3D/job012/run_data.star 
Refine3D/job012/ Refine3D/job012/run_optimiser.star 
Refine3D/job012/ Refine3D/job012/run_half1_class001_unfil.mrc 
Refine3D/job012/ Refine3D/job012/run_class001.mrc 
Refine3D/job012/ Refine3D/job012/run_optimisation_set.star 
Extract/job013/ Extract/job013/optimisation_set.star 
Extract/job013/ Extract/job013/particles.star 
Reconstruct/job014/ Reconstruct/job014/merged.mrc 
Reconstruct/job014/ Reconstruct/job014/half1.mrc 
Reconstruct/job014/ Reconstruct/job014/optimisation_set.star 
Refine3D/job015/ Refine3D/job015/run_data.star 
Refine3D/job015/ Refine3D/job015/run_optimiser.star 
Refine3D/job015/ Refine3D/job015/run_half1_class001_unfil.mrc 
Refine3D/job015/ Refine3D/job015/run_class001.mrc 
Refine3D/job015/ Refine3D/job015/run_optimisation_set.star 
Select/job016/ Select/job016/particles.star 
Class3D/job017/ Class3D/job017/run_it025_data.star 
Class3D/job017/ Class3D/job017/run_it025_optimiser.star 
Class3D/job017/ Class3D/job017/run_it025_class001.mrc 
Class3D/job017/ Class3D/job017/run_it025_class002.mrc 
Class3D/job017/ Class3D/job017/run_it025_class003.mrc 
Class3D/job017/ Class3D/job017/run_it025_class004.mrc 
Class3D/job017/ Class3D/job017/run_it025_class005.mrc 
Class3D/job017/ Class3D/job017/run_it025_class006.mrc 
Class3D/job017/ Class3D/job017/run_it025_class007.mrc 
Class3D/job017/ Class3D/job017/run_it025_class008.mrc 
Class3D/job017/ Class3D/job017/run_it025_class009.mrc 
Class3D/job017/ Class3D/job017/run_it025_optimisation_set.star 
Class3D/job017/ Class3D/job017/run_optimisation_set.star 
 
