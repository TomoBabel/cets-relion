
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
Picks/job009/       None relion.picktomo  Succeeded 
Extract/job010/ Extract/bin6/ relion.pseudosubtomo  Succeeded 
Reconstruct/job011/       None relion.reconstructparticletomo  Succeeded 
Refine3D/job012/ Refine3D/bin6/ relion.refine3d.tomo  Succeeded 
Extract/job013/ Extract/bin2/ relion.pseudosubtomo  Succeeded 
Reconstruct/job014/ Reconstruct/bin2reference/ relion.reconstructparticletomo  Succeeded 
Refine3D/job015/ Refine3D/bin2/ relion.refine3d.tomo  Succeeded 
Select/job016/ Select/remove-dups/ relion.select.removeduplicates  Succeeded 
Class3D/job017/       None relion.class3d  Succeeded 
Select/job018/ Select/best-class/ relion.select.interactive  Succeeded 
Picks/job019/       None relion.picktomo  Succeeded 
Extract/job020/ Extract/bin1/ relion.pseudosubtomo  Succeeded 
Reconstruct/job021/ Reconstruct/bin1reference/ relion.reconstructparticletomo  Succeeded 
PostProcess/job022/       None relion.postprocess  Succeeded 
Refine3D/job023/ Refine3D/bin1/ relion.refine3d.tomo  Succeeded 
Select/job024/ Select/remove-dups2/ relion.select.removeduplicates  Succeeded 
Reconstruct/job025/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job026/ PostProcess/bin1/ relion.postprocess  Succeeded 
CtfRefine/job027/ CtfRefine/cycle0/ relion.ctfrefinetomo  Succeeded 
Reconstruct/job028/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job029/       None relion.postprocess  Succeeded 
Polish/job030/ Polish/cycle0/ relion.framealigntomo  Succeeded 
Extract/job031/       None relion.pseudosubtomo  Succeeded 
Reconstruct/job032/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job033/       None relion.postprocess  Succeeded 
Refine3D/job034/ Refine3D/cycle0/ relion.refine3d.tomo  Succeeded 
Reconstruct/job035/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job036/ PostProcess/cycle0/ relion.postprocess  Succeeded 
CtfRefine/job037/ CtfRefine/cycle1/ relion.ctfrefinetomo  Succeeded 
Reconstruct/job038/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job039/       None relion.postprocess  Succeeded 
Polish/job040/ Polish/cycle1/ relion.framealigntomo  Succeeded 
Extract/job041/       None relion.pseudosubtomo  Succeeded 
Reconstruct/job042/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job043/       None relion.postprocess  Succeeded 
Refine3D/job044/ Refine3D/cycle1/ relion.refine3d.tomo  Succeeded 
Reconstruct/job045/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job046/       None relion.postprocess  Succeeded 
CtfRefine/job047/ CtfRefine/cycle2/ relion.ctfrefinetomo  Succeeded 
Reconstruct/job048/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job049/       None relion.postprocess  Succeeded 
Polish/job050/ Polish/cycle2/ relion.framealigntomo  Succeeded 
Extract/job051/       None relion.pseudosubtomo  Succeeded 
Reconstruct/job052/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job053/       None relion.postprocess  Succeeded 
Refine3D/job054/ Refine3D/cycle2/ relion.refine3d.tomo  Succeeded 
Reconstruct/job055/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job056/       None relion.postprocess  Succeeded 
CtfRefine/job057/ CtfRefine/cycle3/ relion.ctfrefinetomo  Succeeded 
Reconstruct/job058/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job059/       None relion.postprocess  Succeeded 
Polish/job060/ Polish/cycle3/ relion.framealigntomo  Succeeded 
Extract/job061/       None relion.pseudosubtomo  Succeeded 
Reconstruct/job062/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job063/       None relion.postprocess  Succeeded 
Refine3D/job064/ Refine3D/cycle3/ relion.refine3d.tomo  Succeeded 
Reconstruct/job065/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job066/       None relion.postprocess  Succeeded 
CtfRefine/job067/ CtfRefine/cycle4/ relion.ctfrefinetomo  Succeeded 
Reconstruct/job068/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job069/       None relion.postprocess  Succeeded 
Polish/job070/ Polish/cycle4/ relion.framealigntomo  Succeeded 
Extract/job071/       None relion.pseudosubtomo  Succeeded 
Reconstruct/job072/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job073/       None relion.postprocess  Succeeded 
Refine3D/job074/ Refine3D/cycle4/ relion.refine3d.tomo  Succeeded 
Reconstruct/job075/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job076/       None relion.postprocess  Succeeded 
Select/job077/ Select/remove-dups3/ relion.select.removeduplicates  Succeeded 
Reconstruct/job078/       None relion.reconstructparticletomo  Succeeded 
PostProcess/job079/ PostProcess/final/ relion.postprocess  Succeeded 
ModelAngelo/job080/       None modelangelo  Succeeded 
 

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
Select/job018/particles.star ParticleGroupMetadata.star.relion            1 
Picks/job019/particles.star ParticleGroupMetadata.star.relion.tomo.manualpick.particles            1 
Picks/job019/optimisation_set.star TomoOptimisationSet.star.relion.tomo.manualpick            1 
Extract/job020/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job020/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job021/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job021/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job021/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
mask_fsc.mrc Mask3D.mrc            1 
PostProcess/job022/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job022/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job022/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job022/postprocess.star ProcessData.star.relion.postprocess            1 
mask_align.mrc Mask3D.mrc            1 
Refine3D/job023/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job023/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job023/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job023/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job023/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Select/job024/particles.star ParticleGroupMetadata.star.relion            1 
Reconstruct/job025/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job025/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job025/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job026/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job026/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job026/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job026/postprocess.star ProcessData.star.relion.postprocess            1 
CtfRefine/job027/optimisation_set.star TomoOptimisationSet.star.relion.tomo.ctfrefine            1 
CtfRefine/job027/tomograms.star TomogramGroupMetadata.star.relion.tomo.ctfrefine            1 
CtfRefine/job027/logfile.pdf LogFile.pdf.relion.tomo.ctfrefine            1 
Reconstruct/job028/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job028/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job028/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job029/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job029/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job029/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job029/postprocess.star ProcessData.star.relion.postprocess            1 
Polish/job030/optimisation_set.star TomoOptimisationSet.star.relion.tomo.polish            1 
Polish/job030/tomograms.star TomogramGroupMetadata.star.relion.tomo.polish            1 
Polish/job030/particles.star ParticleGroupMetadata.star.relion.tomo.polish            1 
Polish/job030/motion.star TomoTrajectoryData.star.relion.polish            1 
Polish/job030/logfile.pdf LogFile.pdf.relion.tomo.polish            1 
Extract/job031/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job031/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job032/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job032/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job032/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job033/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job033/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job033/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job033/postprocess.star ProcessData.star.relion.postprocess            1 
Refine3D/job034/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job034/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job034/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job034/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job034/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Reconstruct/job035/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job035/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job035/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job036/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job036/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job036/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job036/postprocess.star ProcessData.star.relion.postprocess            1 
CtfRefine/job037/optimisation_set.star TomoOptimisationSet.star.relion.tomo.ctfrefine            1 
CtfRefine/job037/tomograms.star TomogramGroupMetadata.star.relion.tomo.ctfrefine            1 
CtfRefine/job037/logfile.pdf LogFile.pdf.relion.tomo.ctfrefine            1 
Reconstruct/job038/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job038/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job038/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job039/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job039/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job039/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job039/postprocess.star ProcessData.star.relion.postprocess            1 
Polish/job040/optimisation_set.star TomoOptimisationSet.star.relion.tomo.polish            1 
Polish/job040/tomograms.star TomogramGroupMetadata.star.relion.tomo.polish            1 
Polish/job040/particles.star ParticleGroupMetadata.star.relion.tomo.polish            1 
Polish/job040/motion.star TomoTrajectoryData.star.relion.polish            1 
Polish/job040/logfile.pdf LogFile.pdf.relion.tomo.polish            1 
Extract/job041/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job041/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job042/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job042/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job042/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job043/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job043/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job043/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job043/postprocess.star ProcessData.star.relion.postprocess            1 
Refine3D/job044/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job044/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job044/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job044/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job044/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Reconstruct/job045/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job045/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job045/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job046/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job046/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job046/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job046/postprocess.star ProcessData.star.relion.postprocess            1 
CtfRefine/job047/optimisation_set.star TomoOptimisationSet.star.relion.tomo.ctfrefine            1 
CtfRefine/job047/tomograms.star TomogramGroupMetadata.star.relion.tomo.ctfrefine            1 
CtfRefine/job047/logfile.pdf LogFile.pdf.relion.tomo.ctfrefine            1 
Reconstruct/job048/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job048/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job048/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job049/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job049/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job049/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job049/postprocess.star ProcessData.star.relion.postprocess            1 
Polish/job050/optimisation_set.star TomoOptimisationSet.star.relion.tomo.polish            1 
Polish/job050/tomograms.star TomogramGroupMetadata.star.relion.tomo.polish            1 
Polish/job050/particles.star ParticleGroupMetadata.star.relion.tomo.polish            1 
Polish/job050/motion.star TomoTrajectoryData.star.relion.polish            1 
Polish/job050/logfile.pdf LogFile.pdf.relion.tomo.polish            1 
Extract/job051/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job051/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job052/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job052/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job052/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job053/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job053/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job053/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job053/postprocess.star ProcessData.star.relion.postprocess            1 
Refine3D/job054/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job054/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job054/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job054/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job054/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Reconstruct/job055/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job055/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job055/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job056/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job056/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job056/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job056/postprocess.star ProcessData.star.relion.postprocess            1 
CtfRefine/job057/optimisation_set.star TomoOptimisationSet.star.relion.tomo.ctfrefine            1 
CtfRefine/job057/tomograms.star TomogramGroupMetadata.star.relion.tomo.ctfrefine            1 
CtfRefine/job057/logfile.pdf LogFile.pdf.relion.tomo.ctfrefine            1 
Reconstruct/job058/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job058/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job058/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job059/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job059/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job059/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job059/postprocess.star ProcessData.star.relion.postprocess            1 
Polish/job060/optimisation_set.star TomoOptimisationSet.star.relion.tomo.polish            1 
Polish/job060/tomograms.star TomogramGroupMetadata.star.relion.tomo.polish            1 
Polish/job060/particles.star ParticleGroupMetadata.star.relion.tomo.polish            1 
Polish/job060/motion.star TomoTrajectoryData.star.relion.polish            1 
Polish/job060/logfile.pdf LogFile.pdf.relion.tomo.polish            1 
Extract/job061/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job061/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job062/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job062/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job062/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job063/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job063/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job063/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job063/postprocess.star ProcessData.star.relion.postprocess            1 
Refine3D/job064/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job064/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job064/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job064/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job064/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Reconstruct/job065/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job065/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job065/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job066/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job066/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job066/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job066/postprocess.star ProcessData.star.relion.postprocess            1 
CtfRefine/job067/optimisation_set.star TomoOptimisationSet.star.relion.tomo.ctfrefine            1 
CtfRefine/job067/tomograms.star TomogramGroupMetadata.star.relion.tomo.ctfrefine            1 
CtfRefine/job067/logfile.pdf LogFile.pdf.relion.tomo.ctfrefine            1 
Reconstruct/job068/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job068/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job068/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job069/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job069/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job069/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job069/postprocess.star ProcessData.star.relion.postprocess            1 
Polish/job070/optimisation_set.star TomoOptimisationSet.star.relion.tomo.polish            1 
Polish/job070/tomograms.star TomogramGroupMetadata.star.relion.tomo.polish            1 
Polish/job070/particles.star ParticleGroupMetadata.star.relion.tomo.polish            1 
Polish/job070/motion.star TomoTrajectoryData.star.relion.polish            1 
Polish/job070/logfile.pdf LogFile.pdf.relion.tomo.polish            1 
Extract/job071/optimisation_set.star TomoOptimisationSet.star.relion.tomo.extract            1 
Extract/job071/particles.star ParticleGroupMetadata.star.relion.tomo.extract            1 
Reconstruct/job072/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job072/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job072/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job073/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job073/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job073/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job073/postprocess.star ProcessData.star.relion.postprocess            1 
Refine3D/job074/run_data.star ParticleGroupMetadata.star.relion.refine3d            1 
Refine3D/job074/run_optimiser.star OptimiserData.star.relion.refine3d            1 
Refine3D/job074/run_half1_class001_unfil.mrc DensityMap.mrc.relion.halfmap.refine3d            1 
Refine3D/job074/run_class001.mrc DensityMap.mrc.relion.refine3d            1 
Refine3D/job074/run_optimisation_set.star TomoOptimisationSet.star.relion.refine3d            1 
Reconstruct/job075/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job075/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job075/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job076/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job076/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job076/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job076/postprocess.star ProcessData.star.relion.postprocess            1 
Select/job077/particles.star ParticleGroupMetadata.star.relion            1 
Reconstruct/job078/merged.mrc DensityMap.mrc.relion.tomo.map.reconstruct            1 
Reconstruct/job078/half1.mrc DensityMap.mrc.relion.tomo.halfmap.reconstruct           99 
Reconstruct/job078/optimisation_set.star TomoOptimisationSet.star.relion.tomo.reconstruct            1 
PostProcess/job079/postprocess.mrc DensityMap.mrc.relion.postprocess            1 
PostProcess/job079/postprocess_masked.mrc DensityMap.mrc.relion.postprocess.masked            1 
PostProcess/job079/logfile.pdf LogFile.pdf.relion.postprocess            1 
PostProcess/job079/postprocess.star ProcessData.star.relion.postprocess            1 
rcsb_pdb_5L93.fasta Sequence.fasta            1 
ModelAngelo/job080/job080.cif AtomCoords.cif            1 
 

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
Class3D/job017/run_it025_optimiser.star Select/job018/ 
Select/job018/particles.star Picks/job019/ 
Denoise/job008/tomograms.star Picks/job019/ 
Select/job018/particles.star Extract/job020/ 
Denoise/job008/tomograms.star Extract/job020/ 
Extract/job020/optimisation_set.star Reconstruct/job021/ 
mask_fsc.mrc PostProcess/job022/ 
Reconstruct/job021/half1.mrc PostProcess/job022/ 
Extract/job020/optimisation_set.star Refine3D/job023/ 
Reconstruct/job021/half1.mrc Refine3D/job023/ 
mask_align.mrc Refine3D/job023/ 
Refine3D/job023/run_data.star Select/job024/ 
Select/job024/particles.star Reconstruct/job025/ 
Denoise/job008/tomograms.star Reconstruct/job025/ 
mask_fsc.mrc PostProcess/job026/ 
Reconstruct/job025/half1.mrc PostProcess/job026/ 
Select/job024/particles.star CtfRefine/job027/ 
Denoise/job008/tomograms.star CtfRefine/job027/ 
Reconstruct/job025/half1.mrc CtfRefine/job027/ 
mask_align.mrc CtfRefine/job027/ 
PostProcess/job026/postprocess.star CtfRefine/job027/ 
CtfRefine/job027/optimisation_set.star Reconstruct/job028/ 
mask_fsc.mrc PostProcess/job029/ 
Reconstruct/job028/half1.mrc PostProcess/job029/ 
CtfRefine/job027/optimisation_set.star Polish/job030/ 
Reconstruct/job028/half1.mrc Polish/job030/ 
mask_align.mrc Polish/job030/ 
PostProcess/job029/postprocess.star Polish/job030/ 
Polish/job030/optimisation_set.star Extract/job031/ 
Extract/job031/optimisation_set.star Reconstruct/job032/ 
mask_fsc.mrc PostProcess/job033/ 
Reconstruct/job032/half1.mrc PostProcess/job033/ 
Extract/job031/optimisation_set.star Refine3D/job034/ 
Reconstruct/job032/half1.mrc Refine3D/job034/ 
mask_align.mrc Refine3D/job034/ 
Refine3D/job034/run_optimisation_set.star Reconstruct/job035/ 
mask_fsc.mrc PostProcess/job036/ 
Reconstruct/job035/half1.mrc PostProcess/job036/ 
Refine3D/job034/run_optimisation_set.star CtfRefine/job037/ 
Reconstruct/job035/half1.mrc CtfRefine/job037/ 
mask_align.mrc CtfRefine/job037/ 
PostProcess/job036/postprocess.star CtfRefine/job037/ 
CtfRefine/job037/optimisation_set.star Reconstruct/job038/ 
mask_fsc.mrc PostProcess/job039/ 
Reconstruct/job038/half1.mrc PostProcess/job039/ 
CtfRefine/job037/optimisation_set.star Polish/job040/ 
Reconstruct/job038/half1.mrc Polish/job040/ 
mask_align.mrc Polish/job040/ 
PostProcess/job039/postprocess.star Polish/job040/ 
Polish/job040/optimisation_set.star Extract/job041/ 
Extract/job041/optimisation_set.star Reconstruct/job042/ 
mask_fsc.mrc PostProcess/job043/ 
Reconstruct/job042/half1.mrc PostProcess/job043/ 
Extract/job041/optimisation_set.star Refine3D/job044/ 
Reconstruct/job042/half1.mrc Refine3D/job044/ 
mask_align.mrc Refine3D/job044/ 
Refine3D/job044/run_optimisation_set.star Reconstruct/job045/ 
mask_fsc.mrc PostProcess/job046/ 
Reconstruct/job045/half1.mrc PostProcess/job046/ 
Refine3D/job044/run_optimisation_set.star CtfRefine/job047/ 
Reconstruct/job045/half1.mrc CtfRefine/job047/ 
mask_align.mrc CtfRefine/job047/ 
PostProcess/job046/postprocess.star CtfRefine/job047/ 
CtfRefine/job047/optimisation_set.star Reconstruct/job048/ 
mask_fsc.mrc PostProcess/job049/ 
Reconstruct/job048/half1.mrc PostProcess/job049/ 
CtfRefine/job047/optimisation_set.star Polish/job050/ 
Reconstruct/job048/half1.mrc Polish/job050/ 
mask_align.mrc Polish/job050/ 
PostProcess/job049/postprocess.star Polish/job050/ 
Polish/job050/optimisation_set.star Extract/job051/ 
Extract/job051/optimisation_set.star Reconstruct/job052/ 
mask_fsc.mrc PostProcess/job053/ 
Reconstruct/job052/half1.mrc PostProcess/job053/ 
Extract/job051/optimisation_set.star Refine3D/job054/ 
Reconstruct/job052/half1.mrc Refine3D/job054/ 
mask_align.mrc Refine3D/job054/ 
Refine3D/job054/run_optimisation_set.star Reconstruct/job055/ 
mask_fsc.mrc PostProcess/job056/ 
Reconstruct/job055/half1.mrc PostProcess/job056/ 
Refine3D/job054/run_optimisation_set.star CtfRefine/job057/ 
Reconstruct/job055/half1.mrc CtfRefine/job057/ 
mask_align.mrc CtfRefine/job057/ 
PostProcess/job056/postprocess.star CtfRefine/job057/ 
CtfRefine/job057/optimisation_set.star Reconstruct/job058/ 
mask_fsc.mrc PostProcess/job059/ 
Reconstruct/job058/half1.mrc PostProcess/job059/ 
CtfRefine/job057/optimisation_set.star Polish/job060/ 
Reconstruct/job058/half1.mrc Polish/job060/ 
mask_align.mrc Polish/job060/ 
PostProcess/job059/postprocess.star Polish/job060/ 
Polish/job060/optimisation_set.star Extract/job061/ 
Extract/job061/optimisation_set.star Reconstruct/job062/ 
mask_fsc.mrc PostProcess/job063/ 
Reconstruct/job062/half1.mrc PostProcess/job063/ 
Extract/job061/optimisation_set.star Refine3D/job064/ 
Reconstruct/job062/half1.mrc Refine3D/job064/ 
mask_align.mrc Refine3D/job064/ 
Refine3D/job064/run_optimisation_set.star Reconstruct/job065/ 
mask_fsc.mrc PostProcess/job066/ 
Reconstruct/job065/half1.mrc PostProcess/job066/ 
Refine3D/job064/run_optimisation_set.star CtfRefine/job067/ 
Reconstruct/job065/half1.mrc CtfRefine/job067/ 
mask_align.mrc CtfRefine/job067/ 
PostProcess/job066/postprocess.star CtfRefine/job067/ 
CtfRefine/job067/optimisation_set.star Reconstruct/job068/ 
mask_fsc.mrc PostProcess/job069/ 
Reconstruct/job068/half1.mrc PostProcess/job069/ 
CtfRefine/job067/optimisation_set.star Polish/job070/ 
Reconstruct/job068/half1.mrc Polish/job070/ 
mask_align.mrc Polish/job070/ 
PostProcess/job069/postprocess.star Polish/job070/ 
Polish/job070/optimisation_set.star Extract/job071/ 
Extract/job071/optimisation_set.star Reconstruct/job072/ 
mask_fsc.mrc PostProcess/job073/ 
Reconstruct/job072/half1.mrc PostProcess/job073/ 
Extract/job071/optimisation_set.star Refine3D/job074/ 
Reconstruct/job072/half1.mrc Refine3D/job074/ 
mask_align.mrc Refine3D/job074/ 
Refine3D/job074/run_optimisation_set.star Reconstruct/job075/ 
mask_fsc.mrc PostProcess/job076/ 
Reconstruct/job075/half1.mrc PostProcess/job076/ 
Refine3D/job074/run_data.star Select/job077/ 
Select/job077/particles.star Reconstruct/job078/ 
Polish/job070/tomograms.star Reconstruct/job078/ 
Polish/job070/motion.star Reconstruct/job078/ 
mask_fsc.mrc PostProcess/job079/ 
Reconstruct/job078/half1.mrc PostProcess/job079/ 
PostProcess/job079/postprocess_masked.mrc ModelAngelo/job080/ 
rcsb_pdb_5L93.fasta ModelAngelo/job080/ 
 

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
Select/job018/ Select/job018/particles.star 
Picks/job019/ Picks/job019/particles.star 
Picks/job019/ Picks/job019/optimisation_set.star 
Extract/job020/ Extract/job020/optimisation_set.star 
Extract/job020/ Extract/job020/particles.star 
Reconstruct/job021/ Reconstruct/job021/merged.mrc 
Reconstruct/job021/ Reconstruct/job021/half1.mrc 
Reconstruct/job021/ Reconstruct/job021/optimisation_set.star 
PostProcess/job022/ PostProcess/job022/postprocess.mrc 
PostProcess/job022/ PostProcess/job022/postprocess_masked.mrc 
PostProcess/job022/ PostProcess/job022/logfile.pdf 
PostProcess/job022/ PostProcess/job022/postprocess.star 
Refine3D/job023/ Refine3D/job023/run_data.star 
Refine3D/job023/ Refine3D/job023/run_optimiser.star 
Refine3D/job023/ Refine3D/job023/run_half1_class001_unfil.mrc 
Refine3D/job023/ Refine3D/job023/run_class001.mrc 
Refine3D/job023/ Refine3D/job023/run_optimisation_set.star 
Select/job024/ Select/job024/particles.star 
Reconstruct/job025/ Reconstruct/job025/merged.mrc 
Reconstruct/job025/ Reconstruct/job025/half1.mrc 
Reconstruct/job025/ Reconstruct/job025/optimisation_set.star 
PostProcess/job026/ PostProcess/job026/postprocess.mrc 
PostProcess/job026/ PostProcess/job026/postprocess_masked.mrc 
PostProcess/job026/ PostProcess/job026/logfile.pdf 
PostProcess/job026/ PostProcess/job026/postprocess.star 
CtfRefine/job027/ CtfRefine/job027/optimisation_set.star 
CtfRefine/job027/ CtfRefine/job027/tomograms.star 
CtfRefine/job027/ CtfRefine/job027/logfile.pdf 
Reconstruct/job028/ Reconstruct/job028/merged.mrc 
Reconstruct/job028/ Reconstruct/job028/half1.mrc 
Reconstruct/job028/ Reconstruct/job028/optimisation_set.star 
PostProcess/job029/ PostProcess/job029/postprocess.mrc 
PostProcess/job029/ PostProcess/job029/postprocess_masked.mrc 
PostProcess/job029/ PostProcess/job029/logfile.pdf 
PostProcess/job029/ PostProcess/job029/postprocess.star 
Polish/job030/ Polish/job030/optimisation_set.star 
Polish/job030/ Polish/job030/tomograms.star 
Polish/job030/ Polish/job030/particles.star 
Polish/job030/ Polish/job030/motion.star 
Polish/job030/ Polish/job030/logfile.pdf 
Extract/job031/ Extract/job031/optimisation_set.star 
Extract/job031/ Extract/job031/particles.star 
Reconstruct/job032/ Reconstruct/job032/merged.mrc 
Reconstruct/job032/ Reconstruct/job032/half1.mrc 
Reconstruct/job032/ Reconstruct/job032/optimisation_set.star 
PostProcess/job033/ PostProcess/job033/postprocess.mrc 
PostProcess/job033/ PostProcess/job033/postprocess_masked.mrc 
PostProcess/job033/ PostProcess/job033/logfile.pdf 
PostProcess/job033/ PostProcess/job033/postprocess.star 
Refine3D/job034/ Refine3D/job034/run_data.star 
Refine3D/job034/ Refine3D/job034/run_optimiser.star 
Refine3D/job034/ Refine3D/job034/run_half1_class001_unfil.mrc 
Refine3D/job034/ Refine3D/job034/run_class001.mrc 
Refine3D/job034/ Refine3D/job034/run_optimisation_set.star 
Reconstruct/job035/ Reconstruct/job035/merged.mrc 
Reconstruct/job035/ Reconstruct/job035/half1.mrc 
Reconstruct/job035/ Reconstruct/job035/optimisation_set.star 
PostProcess/job036/ PostProcess/job036/postprocess.mrc 
PostProcess/job036/ PostProcess/job036/postprocess_masked.mrc 
PostProcess/job036/ PostProcess/job036/logfile.pdf 
PostProcess/job036/ PostProcess/job036/postprocess.star 
CtfRefine/job037/ CtfRefine/job037/optimisation_set.star 
CtfRefine/job037/ CtfRefine/job037/tomograms.star 
CtfRefine/job037/ CtfRefine/job037/logfile.pdf 
Reconstruct/job038/ Reconstruct/job038/merged.mrc 
Reconstruct/job038/ Reconstruct/job038/half1.mrc 
Reconstruct/job038/ Reconstruct/job038/optimisation_set.star 
PostProcess/job039/ PostProcess/job039/postprocess.mrc 
PostProcess/job039/ PostProcess/job039/postprocess_masked.mrc 
PostProcess/job039/ PostProcess/job039/logfile.pdf 
PostProcess/job039/ PostProcess/job039/postprocess.star 
Polish/job040/ Polish/job040/optimisation_set.star 
Polish/job040/ Polish/job040/tomograms.star 
Polish/job040/ Polish/job040/particles.star 
Polish/job040/ Polish/job040/motion.star 
Polish/job040/ Polish/job040/logfile.pdf 
Extract/job041/ Extract/job041/optimisation_set.star 
Extract/job041/ Extract/job041/particles.star 
Reconstruct/job042/ Reconstruct/job042/merged.mrc 
Reconstruct/job042/ Reconstruct/job042/half1.mrc 
Reconstruct/job042/ Reconstruct/job042/optimisation_set.star 
PostProcess/job043/ PostProcess/job043/postprocess.mrc 
PostProcess/job043/ PostProcess/job043/postprocess_masked.mrc 
PostProcess/job043/ PostProcess/job043/logfile.pdf 
PostProcess/job043/ PostProcess/job043/postprocess.star 
Refine3D/job044/ Refine3D/job044/run_data.star 
Refine3D/job044/ Refine3D/job044/run_optimiser.star 
Refine3D/job044/ Refine3D/job044/run_half1_class001_unfil.mrc 
Refine3D/job044/ Refine3D/job044/run_class001.mrc 
Refine3D/job044/ Refine3D/job044/run_optimisation_set.star 
Reconstruct/job045/ Reconstruct/job045/merged.mrc 
Reconstruct/job045/ Reconstruct/job045/half1.mrc 
Reconstruct/job045/ Reconstruct/job045/optimisation_set.star 
PostProcess/job046/ PostProcess/job046/postprocess.mrc 
PostProcess/job046/ PostProcess/job046/postprocess_masked.mrc 
PostProcess/job046/ PostProcess/job046/logfile.pdf 
PostProcess/job046/ PostProcess/job046/postprocess.star 
CtfRefine/job047/ CtfRefine/job047/optimisation_set.star 
CtfRefine/job047/ CtfRefine/job047/tomograms.star 
CtfRefine/job047/ CtfRefine/job047/logfile.pdf 
Reconstruct/job048/ Reconstruct/job048/merged.mrc 
Reconstruct/job048/ Reconstruct/job048/half1.mrc 
Reconstruct/job048/ Reconstruct/job048/optimisation_set.star 
PostProcess/job049/ PostProcess/job049/postprocess.mrc 
PostProcess/job049/ PostProcess/job049/postprocess_masked.mrc 
PostProcess/job049/ PostProcess/job049/logfile.pdf 
PostProcess/job049/ PostProcess/job049/postprocess.star 
Polish/job050/ Polish/job050/optimisation_set.star 
Polish/job050/ Polish/job050/tomograms.star 
Polish/job050/ Polish/job050/particles.star 
Polish/job050/ Polish/job050/motion.star 
Polish/job050/ Polish/job050/logfile.pdf 
Extract/job051/ Extract/job051/optimisation_set.star 
Extract/job051/ Extract/job051/particles.star 
Reconstruct/job052/ Reconstruct/job052/merged.mrc 
Reconstruct/job052/ Reconstruct/job052/half1.mrc 
Reconstruct/job052/ Reconstruct/job052/optimisation_set.star 
PostProcess/job053/ PostProcess/job053/postprocess.mrc 
PostProcess/job053/ PostProcess/job053/postprocess_masked.mrc 
PostProcess/job053/ PostProcess/job053/logfile.pdf 
PostProcess/job053/ PostProcess/job053/postprocess.star 
Refine3D/job054/ Refine3D/job054/run_data.star 
Refine3D/job054/ Refine3D/job054/run_optimiser.star 
Refine3D/job054/ Refine3D/job054/run_half1_class001_unfil.mrc 
Refine3D/job054/ Refine3D/job054/run_class001.mrc 
Refine3D/job054/ Refine3D/job054/run_optimisation_set.star 
Reconstruct/job055/ Reconstruct/job055/merged.mrc 
Reconstruct/job055/ Reconstruct/job055/half1.mrc 
Reconstruct/job055/ Reconstruct/job055/optimisation_set.star 
PostProcess/job056/ PostProcess/job056/postprocess.mrc 
PostProcess/job056/ PostProcess/job056/postprocess_masked.mrc 
PostProcess/job056/ PostProcess/job056/logfile.pdf 
PostProcess/job056/ PostProcess/job056/postprocess.star 
CtfRefine/job057/ CtfRefine/job057/optimisation_set.star 
CtfRefine/job057/ CtfRefine/job057/tomograms.star 
CtfRefine/job057/ CtfRefine/job057/logfile.pdf 
Reconstruct/job058/ Reconstruct/job058/merged.mrc 
Reconstruct/job058/ Reconstruct/job058/half1.mrc 
Reconstruct/job058/ Reconstruct/job058/optimisation_set.star 
PostProcess/job059/ PostProcess/job059/postprocess.mrc 
PostProcess/job059/ PostProcess/job059/postprocess_masked.mrc 
PostProcess/job059/ PostProcess/job059/logfile.pdf 
PostProcess/job059/ PostProcess/job059/postprocess.star 
Polish/job060/ Polish/job060/optimisation_set.star 
Polish/job060/ Polish/job060/tomograms.star 
Polish/job060/ Polish/job060/particles.star 
Polish/job060/ Polish/job060/motion.star 
Polish/job060/ Polish/job060/logfile.pdf 
Extract/job061/ Extract/job061/optimisation_set.star 
Extract/job061/ Extract/job061/particles.star 
Reconstruct/job062/ Reconstruct/job062/merged.mrc 
Reconstruct/job062/ Reconstruct/job062/half1.mrc 
Reconstruct/job062/ Reconstruct/job062/optimisation_set.star 
PostProcess/job063/ PostProcess/job063/postprocess.mrc 
PostProcess/job063/ PostProcess/job063/postprocess_masked.mrc 
PostProcess/job063/ PostProcess/job063/logfile.pdf 
PostProcess/job063/ PostProcess/job063/postprocess.star 
Refine3D/job064/ Refine3D/job064/run_data.star 
Refine3D/job064/ Refine3D/job064/run_optimiser.star 
Refine3D/job064/ Refine3D/job064/run_half1_class001_unfil.mrc 
Refine3D/job064/ Refine3D/job064/run_class001.mrc 
Refine3D/job064/ Refine3D/job064/run_optimisation_set.star 
Reconstruct/job065/ Reconstruct/job065/merged.mrc 
Reconstruct/job065/ Reconstruct/job065/half1.mrc 
Reconstruct/job065/ Reconstruct/job065/optimisation_set.star 
PostProcess/job066/ PostProcess/job066/postprocess.mrc 
PostProcess/job066/ PostProcess/job066/postprocess_masked.mrc 
PostProcess/job066/ PostProcess/job066/logfile.pdf 
PostProcess/job066/ PostProcess/job066/postprocess.star 
CtfRefine/job067/ CtfRefine/job067/optimisation_set.star 
CtfRefine/job067/ CtfRefine/job067/tomograms.star 
CtfRefine/job067/ CtfRefine/job067/logfile.pdf 
Reconstruct/job068/ Reconstruct/job068/merged.mrc 
Reconstruct/job068/ Reconstruct/job068/half1.mrc 
Reconstruct/job068/ Reconstruct/job068/optimisation_set.star 
PostProcess/job069/ PostProcess/job069/postprocess.mrc 
PostProcess/job069/ PostProcess/job069/postprocess_masked.mrc 
PostProcess/job069/ PostProcess/job069/logfile.pdf 
PostProcess/job069/ PostProcess/job069/postprocess.star 
Polish/job070/ Polish/job070/optimisation_set.star 
Polish/job070/ Polish/job070/tomograms.star 
Polish/job070/ Polish/job070/particles.star 
Polish/job070/ Polish/job070/motion.star 
Polish/job070/ Polish/job070/logfile.pdf 
Extract/job071/ Extract/job071/optimisation_set.star 
Extract/job071/ Extract/job071/particles.star 
Reconstruct/job072/ Reconstruct/job072/merged.mrc 
Reconstruct/job072/ Reconstruct/job072/half1.mrc 
Reconstruct/job072/ Reconstruct/job072/optimisation_set.star 
PostProcess/job073/ PostProcess/job073/postprocess.mrc 
PostProcess/job073/ PostProcess/job073/postprocess_masked.mrc 
PostProcess/job073/ PostProcess/job073/logfile.pdf 
PostProcess/job073/ PostProcess/job073/postprocess.star 
Refine3D/job074/ Refine3D/job074/run_data.star 
Refine3D/job074/ Refine3D/job074/run_optimiser.star 
Refine3D/job074/ Refine3D/job074/run_half1_class001_unfil.mrc 
Refine3D/job074/ Refine3D/job074/run_class001.mrc 
Refine3D/job074/ Refine3D/job074/run_optimisation_set.star 
Reconstruct/job075/ Reconstruct/job075/merged.mrc 
Reconstruct/job075/ Reconstruct/job075/half1.mrc 
Reconstruct/job075/ Reconstruct/job075/optimisation_set.star 
PostProcess/job076/ PostProcess/job076/postprocess.mrc 
PostProcess/job076/ PostProcess/job076/postprocess_masked.mrc 
PostProcess/job076/ PostProcess/job076/logfile.pdf 
PostProcess/job076/ PostProcess/job076/postprocess.star 
Select/job077/ Select/job077/particles.star 
Reconstruct/job078/ Reconstruct/job078/merged.mrc 
Reconstruct/job078/ Reconstruct/job078/half1.mrc 
Reconstruct/job078/ Reconstruct/job078/optimisation_set.star 
PostProcess/job079/ PostProcess/job079/postprocess.mrc 
PostProcess/job079/ PostProcess/job079/postprocess_masked.mrc 
PostProcess/job079/ PostProcess/job079/logfile.pdf 
PostProcess/job079/ PostProcess/job079/postprocess.star 
ModelAngelo/job080/ ModelAngelo/job080/job080.cif 
 
