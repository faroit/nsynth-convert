# nsynth-convert
NSynth for the rest of us

## Install

Make sure you have installed `libsndfile`. Then install the python requirements by

```bash
pip install -r requirements.txt
```

to convert a `tfrecord` file and write standard json + audio files into a folder called `NSynth-Test` just run
```bash
python convert.py nsynth-test.tfrecord NSynth-Test
```
