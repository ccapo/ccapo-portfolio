import streamlit as st
import pickle
import numpy as np
from music21 import instrument, note, stream, chord
from keras.saving import load_model
import numpy as np
import pretty_midi
from scipy.io import wavfile
import io

@st.cache_resource
def load_notes():
    notes_filepath = 'models/music_notes.pkl'
    with open(notes_filepath, 'rb') as filepath:
        notes = pickle.load(filepath)
        pitchnames = pickle.load(filepath)
        n_vocab = pickle.load(filepath)
    return (notes, pitchnames, n_vocab)

@st.cache_resource
def model_load():
    model_filepath = 'models/music_model.keras'
    model = load_model(model_filepath)
    return model

@st.cache_data
def prepare_sequences(notes, pitchnames, n_vocab, sequence_length=100):
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

    network_input = []
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])

    return network_input

def generate_notes(model, network_input, pitchnames, n_vocab, nlength, istart=-1):
    # pick a random sequence from the input as a starting point for the prediction
    if istart < 0 or istart > len(network_input) - 1:
        start = np.random.randint(0, len(network_input) - 1)
        print(f"Starting Position = {start}")
    else:
        start = istart

    int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

    pattern = network_input[start]
    prediction_output = []

    # generate nlength notes
    for note_index in range(nlength):
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(n_vocab)

        prediction = model.predict(prediction_input, verbose=0)

        index = np.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)

        pattern.append(index)
        pattern = pattern[1:len(pattern)]

    return prediction_output

def create_midi(prediction_output, output_filepath):
    offset = 0
    output_notes = []

    # create note and chord objects based on the values generated by the model
    for pattern in prediction_output:
        # pattern is a chord
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        # pattern is a note
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        # increase offset each iteration so that notes do not stack
        offset += 0.5

    # Write notes to a MIDI file
    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp='output.mid')

def generate(model, network_input, pitchnames, n_vocab, nlength=500, istart=-1):
    output_filepath = 'output.mid'
    if nlength < 1:
        print(f"Song length must be at least one note, defaulting to 250 notes")
        nlength = 500
    if nlength > 500:
        print(f"Cannot exceed 500 notes for song length")
        nlength = 500

    prediction_output = generate_notes(model, network_input, pitchnames, n_vocab, nlength, istart)
    create_midi(prediction_output, output_filepath)
    return output_filepath

st.header('Generative Music', divider='green')

# Load notes
notes, pitchnames, n_vocab = load_notes()

# Prepare note sequences
network_input = prepare_sequences(notes, pitchnames, n_vocab)

# Load model
model = model_load()

st.markdown("This a model that I trained on a collection of MIDI files")

midi_file = None
generated_midi = None
sample_midi = None

st.markdown("You can select one of the samples below")

sample_midi = st.selectbox(
    'Select a sample MIDI file to play',
    ('assets/sample_01.mid', 'assets/sample_02.mid', 'assets/sample_03.mid'),
    index=None,
    placeholder="Please select a sample...",
)

st.markdown("Or generate a new sample by clicking the generate button")

n_notes = st.slider("How many notes do you want?", 1, 500, 250)
start_pos = st.slider("Where do you want to start? Negative will start at a random position.", -1, len(network_input) - 1, -1)

if st.button('Generate'):
    with st.spinner(f"Generating a new MIDI file"):
        generated_midi = generate(model, network_input, pitchnames, n_vocab, n_notes, start_pos)

if generated_midi:
    midi_file = generated_midi
    sample_midi = None
elif sample_midi:
    midi_file = sample_midi

if midi_file:
    with st.spinner(f"Transcribing to FluidSynth"):
        midi_data = pretty_midi.PrettyMIDI(midi_file)
        audio_data = midi_data.fluidsynth()
        audio_data = np.int16(
            audio_data / np.max(np.abs(audio_data)) * 32767 * 0.9
        )  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py

        virtualfile = io.BytesIO()
        wavfile.write(virtualfile, 44100, audio_data)

    st.audio(virtualfile)
    st.markdown("Download the audio by right-clicking on the media player")
else:
    st.markdown("Either generate a new MIDI file, or select one of the samples")