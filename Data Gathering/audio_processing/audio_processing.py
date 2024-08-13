import subprocess

def download_youtube_audio(url, output):
    try:
        command = [
            'yt-dlp',
            '--extract-audio',
            '--audio-format', 'mp3',
            '-o', output,
            url,
            '--progress',  # Show progress information
            '--verbose'    # Detailed output for debugging
        ]

        print("Running command:", ' '.join(command))

        result = subprocess.run(command, check=True, text=True, capture_output=True)

        print("Download successful!")
        print("Output:", result.stdout)
        print("Error (if any):", result.stderr)

    except subprocess.CalledProcessError as e:
        print("Error during download.")
        print("Error message:", e.stderr)

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=V8ptd56JKa8&list=PLUacZbEyhMuI3YixcJ7gHaAWHv149huIP&index=13'
output_file = '/content/podcast_episode.mp3'
download_youtube_audio(youtube_url, output_file)

from pydub import AudioSegment
import os

# Convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

mp3_file = '/content/podcast_episode.mp3'
wav_file = '/content/podcast_episode.wav'
convert_mp3_to_wav(mp3_file, wav_file)

import speech_recognition as sr
from pydub import AudioSegment

def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(file_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def transcribe_audio_chunks(chunks, max_chunks=20):
    recognizer = sr.Recognizer()
    transcriptions = []
    for i, chunk in enumerate(chunks):
        if i >= max_chunks:
            break  # Stop after processing max_chunks
        chunk_path = f"chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        with sr.AudioFile(chunk_path) as source:
            audio = recognizer.record(source)
            try:
                transcript = recognizer.recognize_sphinx(audio)
                transcriptions.append(transcript)
            except sr.UnknownValueError:
                transcriptions.append("Sphinx could not understand audio")
            except sr.RequestError as e:
                transcriptions.append(f"Sphinx error: {e}")
    return " ".join(transcriptions)

# Split the audio into chunks
chunks = split_audio('/content/podcast_episode.wav')

# Transcribe up to 20 chunks
full_transcription = transcribe_audio_chunks(chunks, max_chunks=20)

# Save the transcription to a text file
transcription_file_path = '/content/transcription.txt'
with open(transcription_file_path, 'w', encoding='utf-8') as file:
    file.write(full_transcription)

print(f"Transcription saved to {transcription_file_path}")
