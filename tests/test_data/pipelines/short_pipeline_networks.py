FULL_NODES = [
    "Import/job001/",
    "MotionCorr/job002/",
    "CtfFind/job003/",
    "ExcludeTiltImages/job004/",
    "AlignTiltSeries/job005/",
    "Tomograms/job006/",
    "Denoise/job007/",
    "Denoise/job008/",
    "Import/job001/tilt_series.star",
    "MotionCorr/job002/corrected_tilt_series.star",
    "MotionCorr/job002/logfile.pdf",
    "CtfFind/job003/tilt_series_ctf.star",
    "CtfFind/job003/logfile.pdf",
    "ExcludeTiltImages/job004/selected_tilt_series.star",
    "AlignTiltSeries/job005/aligned_tilt_series.star",
    "Tomograms/job006/tomograms.star",
    "Denoise/job007/tomograms.star",
    "Denoise/job008/tomograms.star",
]
FULL_EDGES = [
    ("Import/job001/", "Import/job001/tilt_series.star"),
    ("MotionCorr/job002/", "MotionCorr/job002/corrected_tilt_series.star"),
    ("MotionCorr/job002/", "MotionCorr/job002/logfile.pdf"),
    ("CtfFind/job003/", "CtfFind/job003/tilt_series_ctf.star"),
    ("CtfFind/job003/", "CtfFind/job003/logfile.pdf"),
    (
        "ExcludeTiltImages/job004/",
        "ExcludeTiltImages/job004/selected_tilt_series.star",
    ),
    (
        "AlignTiltSeries/job005/",
        "AlignTiltSeries/job005/aligned_tilt_series.star",
    ),
    ("Tomograms/job006/", "Tomograms/job006/tomograms.star"),
    ("Denoise/job007/", "Denoise/job007/tomograms.star"),
    ("Denoise/job008/", "Denoise/job008/tomograms.star"),
    ("Import/job001/tilt_series.star", "MotionCorr/job002/"),
    ("MotionCorr/job002/corrected_tilt_series.star", "CtfFind/job003/"),
    ("CtfFind/job003/tilt_series_ctf.star", "ExcludeTiltImages/job004/"),
    (
        "ExcludeTiltImages/job004/selected_tilt_series.star",
        "AlignTiltSeries/job005/",
    ),
    ("AlignTiltSeries/job005/aligned_tilt_series.star", "Tomograms/job006/"),
    ("Tomograms/job006/tomograms.star", "Denoise/job007/"),
    ("Tomograms/job006/tomograms.star", "Denoise/job008/"),
]
JOBS_NODES = [
    "Import/job001/",
    "MotionCorr/job002/",
    "CtfFind/job003/",
    "ExcludeTiltImages/job004/",
    "AlignTiltSeries/job005/",
    "Tomograms/job006/",
    "Denoise/job007/",
    "Denoise/job008/",
]
JOBS_EDGES = [
    ("Import/job001/", "MotionCorr/job002/"),
    ("MotionCorr/job002/", "CtfFind/job003/"),
    ("CtfFind/job003/", "ExcludeTiltImages/job004/"),
    ("ExcludeTiltImages/job004/", "AlignTiltSeries/job005/"),
    ("AlignTiltSeries/job005/", "Tomograms/job006/"),
    ("Tomograms/job006/", "Denoise/job007/"),
    ("Tomograms/job006/", "Denoise/job008/"),
]
FILES_EDGES = [
    (
        "Import/job001/tilt_series.star",
        "MotionCorr/job002/corrected_tilt_series.star",
    ),
    ("Import/job001/tilt_series.star", "MotionCorr/job002/logfile.pdf"),
    (
        "MotionCorr/job002/corrected_tilt_series.star",
        "CtfFind/job003/tilt_series_ctf.star",
    ),
    (
        "MotionCorr/job002/corrected_tilt_series.star",
        "CtfFind/job003/logfile.pdf",
    ),
    (
        "CtfFind/job003/tilt_series_ctf.star",
        "ExcludeTiltImages/job004/selected_tilt_series.star",
    ),
    (
        "ExcludeTiltImages/job004/selected_tilt_series.star",
        "AlignTiltSeries/job005/aligned_tilt_series.star",
    ),
    (
        "AlignTiltSeries/job005/aligned_tilt_series.star",
        "Tomograms/job006/tomograms.star",
    ),
    ("Tomograms/job006/tomograms.star", "Denoise/job007/tomograms.star"),
    ("Tomograms/job006/tomograms.star", "Denoise/job008/tomograms.star"),
]

FILES_NODES = [
    "Import/job001/tilt_series.star",
    "MotionCorr/job002/corrected_tilt_series.star",
    "MotionCorr/job002/logfile.pdf",
    "CtfFind/job003/tilt_series_ctf.star",
    "CtfFind/job003/logfile.pdf",
    "ExcludeTiltImages/job004/selected_tilt_series.star",
    "AlignTiltSeries/job005/aligned_tilt_series.star",
    "Tomograms/job006/tomograms.star",
    "Denoise/job007/tomograms.star",
    "Denoise/job008/tomograms.star",
]

# job007 is missing in the critical paths because there is no edge for the trained
# model in this version of the pipeline
FULL_CRIT_NODES = [
    "Import/job001/",
    "MotionCorr/job002/",
    "CtfFind/job003/",
    "ExcludeTiltImages/job004/",
    "AlignTiltSeries/job005/",
    "Tomograms/job006/",
    "Denoise/job008/",
    "Import/job001/tilt_series.star",
    "MotionCorr/job002/corrected_tilt_series.star",
    "CtfFind/job003/tilt_series_ctf.star",
    "ExcludeTiltImages/job004/selected_tilt_series.star",
    "AlignTiltSeries/job005/aligned_tilt_series.star",
    "Tomograms/job006/tomograms.star",
    "Denoise/job008/tomograms.star",
]
FULL_CRIT_EDGES = [
    ("Import/job001/", "Import/job001/tilt_series.star"),
    ("MotionCorr/job002/", "MotionCorr/job002/corrected_tilt_series.star"),
    ("CtfFind/job003/", "CtfFind/job003/tilt_series_ctf.star"),
    (
        "ExcludeTiltImages/job004/",
        "ExcludeTiltImages/job004/selected_tilt_series.star",
    ),
    (
        "AlignTiltSeries/job005/",
        "AlignTiltSeries/job005/aligned_tilt_series.star",
    ),
    ("Tomograms/job006/", "Tomograms/job006/tomograms.star"),
    ("Denoise/job008/", "Denoise/job008/tomograms.star"),
    ("Import/job001/tilt_series.star", "MotionCorr/job002/"),
    ("MotionCorr/job002/corrected_tilt_series.star", "CtfFind/job003/"),
    ("CtfFind/job003/tilt_series_ctf.star", "ExcludeTiltImages/job004/"),
    (
        "ExcludeTiltImages/job004/selected_tilt_series.star",
        "AlignTiltSeries/job005/",
    ),
    ("AlignTiltSeries/job005/aligned_tilt_series.star", "Tomograms/job006/"),
    ("Tomograms/job006/tomograms.star", "Denoise/job008/"),
]
FILES_CRIT_NODES = [
    "Import/job001/tilt_series.star",
    "MotionCorr/job002/corrected_tilt_series.star",
    "CtfFind/job003/tilt_series_ctf.star",
    "ExcludeTiltImages/job004/selected_tilt_series.star",
    "AlignTiltSeries/job005/aligned_tilt_series.star",
    "Tomograms/job006/tomograms.star",
    "Denoise/job008/tomograms.star",
]
FILES_CRIT_EDGES = [
    (
        "Import/job001/tilt_series.star",
        "MotionCorr/job002/corrected_tilt_series.star",
    ),
    (
        "MotionCorr/job002/corrected_tilt_series.star",
        "CtfFind/job003/tilt_series_ctf.star",
    ),
    (
        "CtfFind/job003/tilt_series_ctf.star",
        "ExcludeTiltImages/job004/selected_tilt_series.star",
    ),
    (
        "ExcludeTiltImages/job004/selected_tilt_series.star",
        "AlignTiltSeries/job005/aligned_tilt_series.star",
    ),
    (
        "AlignTiltSeries/job005/aligned_tilt_series.star",
        "Tomograms/job006/tomograms.star",
    ),
    ("Tomograms/job006/tomograms.star", "Denoise/job008/tomograms.star"),
]
JOBS_CRIT_NODES = [
    "Import/job001/",
    "MotionCorr/job002/",
    "CtfFind/job003/",
    "ExcludeTiltImages/job004/",
    "AlignTiltSeries/job005/",
    "Tomograms/job006/",
    "Denoise/job008/",
]
JOBS_CRIT_EDGES = [
    ("Import/job001/", "MotionCorr/job002/"),
    ("MotionCorr/job002/", "CtfFind/job003/"),
    ("CtfFind/job003/", "ExcludeTiltImages/job004/"),
    ("ExcludeTiltImages/job004/", "AlignTiltSeries/job005/"),
    ("AlignTiltSeries/job005/", "Tomograms/job006/"),
    ("Tomograms/job006/", "Denoise/job007/"),
    ("Tomograms/job006/", "Denoise/job008/"),
]

DOWNSTREAM_CRIT_FILES_NODES = [
    "MotionCorr/job002/corrected_tilt_series.star",
    "CtfFind/job003/tilt_series_ctf.star",
    "CtfFind/job003/logfile.pdf",
    "ExcludeTiltImages/job004/selected_tilt_series.star",
    "AlignTiltSeries/job005/aligned_tilt_series.star",
    "Tomograms/job006/tomograms.star",
    "Denoise/job007/tomograms.star",
    "Denoise/job008/tomograms.star",
]

DOWNSTREAM_CRIT_FILES_EDGES = [
    (
        "MotionCorr/job002/corrected_tilt_series.star",
        "CtfFind/job003/tilt_series_ctf.star",
    ),
    (
        "MotionCorr/job002/corrected_tilt_series.star",
        "CtfFind/job003/logfile.pdf",
    ),
    (
        "CtfFind/job003/tilt_series_ctf.star",
        "ExcludeTiltImages/job004/selected_tilt_series.star",
    ),
    (
        "ExcludeTiltImages/job004/selected_tilt_series.star",
        "AlignTiltSeries/job005/aligned_tilt_series.star",
    ),
    (
        "AlignTiltSeries/job005/aligned_tilt_series.star",
        "Tomograms/job006/tomograms.star",
    ),
    ("Tomograms/job006/tomograms.star", "Denoise/job007/tomograms.star"),
    ("Tomograms/job006/tomograms.star", "Denoise/job008/tomograms.star"),
]

UPSTREAM_JOBS_CRIT_EDGES = [
    ("Import/job001/", "MotionCorr/job002/"),
    ("MotionCorr/job002/", "CtfFind/job003/"),
    ("CtfFind/job003/", "ExcludeTiltImages/job004/"),
    ("ExcludeTiltImages/job004/", "AlignTiltSeries/job005/"),
    ("AlignTiltSeries/job005/", "Tomograms/job006/"),
    ("Tomograms/job006/", "Denoise/job008/"),
]
