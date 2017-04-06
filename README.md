# nsynth-convert

[NSynth](https://magenta.tensorflow.org/datasets/nsynth) is "A large-scale and high-quality dataset of annotated musical notes". The dataset is provided as a [tfrecord](https://www.tensorflow.org/api_guides/python/python_io#tfrecords_format_details) file. However, if you are not using tensorflow (like me) you may find it quite inconvenient to use. This is a little converter that read the tfrecord files and writes out pcm audio + json metadata as __one file per sample__.

## Install

Make sure you have installed `libsndfile`. Then install the python requirements by

```bash
pip install -r requirements.txt
```

to convert a `tfrecord` file and write standard json + audio files into a folder called `NSynth-Test` just run

```bash
python convert.py nsynth-test.tfrecord NSynth-Test
```
