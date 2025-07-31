"""
Things we'll want to track

Raw Movies
Tilt series
Subtomograms
Subtomogram averages

select terminal job(s)
make subgraph
trace back each terminal job making objects

raw movies, movieset movieframes- jobs that use as import relion.motioncorr.own

"""

# for each input type find the latest job that used it as an input and use that to
# create the CETS object

# type dicts {jobs that use it as input: joboption name}
raw_movies = {"relion.motioncorr.own": "input_star_mics"}
raw_tilt_series = {
    "relion.ctffind.ctffind4": "input_star_mics",
    "relion.excludetilts": "in_tiltseries",
    "relion.aligntiltseries": "in_tiltseries",
}
aligned_tilt_series = {"relion.reconstructtomograms": "in_tiltseries"}
tomograms = {
    "relion.denoisetomo": "in_tomoset",
    "relion.picktomo": "in_tomoset",
    "relion.pseudosubtomo": "in_tomograms",
}
subtomo_coords = {"relion.pseudosubtomo": "in_particles"}
