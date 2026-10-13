# Speech Signal Processing

A notebook that transcribes a recorded speech clip and analyzes its acoustic structure.

## What it does

1. **Speech-to-text:** transcribes the clip in English and in Hindi (`hi-IN`) with the `SpeechRecognition` library.
2. **Signal basics:** loads the audio with `librosa` and reports the sampling rate and number of samples.
3. **Waveform:** plots amplitude over time.
4. **Spectrogram:** applies a short-time Fourier transform and plots it on a log-frequency, decibel scale.
5. **Formants:** tracks the first three formants (F1–F3) over time with Praat's Burg method through `parselmouth`.

## Running it

[Open in Colab](https://colab.research.google.com/github/sahiljangra12/Academic-Projects/blob/main/06-speech-signal-processing/speech_signal_processing.ipynb). The notebook expects a WAV file named `NLP Assignment.wav`, which you upload when the upload cell runs. The original recording isn't included, but any short speech clip will work.

## Tools

Python, SpeechRecognition, librosa, matplotlib, NumPy, praat-parselmouth, gTTS
