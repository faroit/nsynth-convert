import tensorflow as tf
import numpy as np
import json
import soundfile as sf
import os
import argparse


def nsynth_generator(tfrecords_filename):
    for serialized_example in tf.python_io.tf_record_iterator(tfrecords_filename):
        example = tf.train.Example()
        example.ParseFromString(serialized_example)
        f = example.features.feature

        audio = np.array(f['audio'].float_list.value)

        data = {
            'note':
                f['note'].int64_list.value[0],
            'note_str':
                f['note_str'].bytes_list.value[0],
            'instrument':
                f['instrument'].int64_list.value[0],
            'instrument_str':
                f['instrument_str'].bytes_list.value[0],
            'pitch':
                f['pitch'].int64_list.value[0],
            'velocity':
                f['pitch'].int64_list.value[0],
            'samplerate':
                f['sample_rate'].int64_list.value[0],
            'qualities':
                map(int, f['qualities'].int64_list.value),
            'qualities_str':
                map(str, f['qualities_str'].int64_list.value),
            'instrument_family':
                f['instrument_family'].int64_list.value[0],
            'instrument_family_str':
                f['instrument_family_str'].bytes_list.value[0],
            'instrument_source':
                f['instrument_family'].int64_list.value[0],
            'instrument_source_str':
                f['instrument_source_str'].bytes_list.value[0],
        }

        yield data, audio

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input',
    )
    parser.add_argument(
        'out_dir',
    )
    args = parser.parse_args()

    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    for data, audio in nsynth_generator(args.input):
        base_file_str = '_'.join([
            data['instrument_family_str'],
            str(data['pitch']),
            str(data['note'])
        ])

        json_path = os.path.join(args.out_dir, base_file_str + '.json')
        audio_path = os.path.join(args.out_dir, base_file_str + '.wav')
        with open(json_path, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False)

        sf.write(audio_path, audio, data['samplerate'])
