# bad-apple-quilt
I made Mesmerizer only using frames from Bad Apple. Code can be altered to create pretty much any video using only Bad Apple frames.
## Useful ffmpeg scripts

To populate training and testing frame folders, I recommend ffmpeg.

To populate the training frames:
```
ffmpeg -i training/badapple.mp4 -r 30 training/frames/output_%04d.jpg
ffmpeg -i testing/mesmer.mp4 -r 30 testing/frames/output_%04d.jpg
```
To populate the testing frames:
```
ffmpeg -i testing/mesmer.mp4 -r 30 testing/frames/output_%04d.jpg
```
To combine frames into an mp4:
```
ffmpeg -framerate 30 -i path/output_%04d.jpg out.mp4
```