# nsynth-convert

[NSynth](https://magenta.tensorflow.org/datasets/nsynth) is "A large-scale and high-quality dataset of annotated musical notes". The dataset is provided as a [tfrecord](https://www.tensorflow.org/api_guides/python/python_io#tfrecords_format_details) file. If you are not using tensorflow I found it quite inconvenient to use. This this little converter converts the tfrecord files into json + pcm audio as one file per sample.

## Install

Make sure you have installed `libsndfile`. Then install the python requirements by

```bash
pip install -r requirements.txt
```

to convert a `tfrecord` file and write standard json + audio files into a folder called `NSynth-Test` just run

```bash
python convert.py nsynth-test.tfrecord NSynth-Test
```
