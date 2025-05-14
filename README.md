# bad-apple-quilt
This is how I made Mesmerizer only using frames from Bad Apple. Code can be altered to create pretty much any video using only Bad Apple frames if you change the variables a bit.

## Files
* project.ipynb : Notebook that contains the process of creating Mesmerizer frames using Bad Apple frames
* data_prep.ipynb : Maps image hash values to Bad Apple frame indices. Don't really need to change.
* hash_indices.json : Mappings from data_prep is saved here. Automatically created from above notebook.
* image_similarity.py : Contains useful functions regarding image hashes. Used in project notebook.


## Useful ffmpeg scripts

I recommend ffmpeg when dealing with video to image conversions. Below are some commands I found useful during my process.

To populate the training frames:
```
ffmpeg -i training/badapple.mp4 -r 30 training/frames/output_%04d.jpg
```
To populate the testing frames:
```
ffmpeg -i testing/mesmer.mp4 -r 30 testing/frames/output_%04d.jpg
```
To combine frames into an mp4:
```
ffmpeg -framerate 30 -i path/output_%04d.jpg out.mp4
```
