import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

def split_audio(file_path, chunk_length_ms=30000):
    audio = AudioSegment.from_file(file_path)
    chunks = split_on_silence(
        audio,
        min_silence_len=500,
        silence_thresh=-40,
        keep_silence=500
    )

    for i, chunk in enumerate(chunks):
        chunk.export(f"chunk_{i}.wav", format="wav")

    return [f"chunk_{i}.wav" for i in range(len(chunks))]

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    return ""

def translate_text(text, dest_language="te"):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='te')
    tts.save(output_file)

# Example usage
audio_file = 'C:\\Users\\umad3\\WhatsApp Audio.wav'
chunks = split_audio(audio_file)

transcribed_texts = []
for chunk in chunks:
    text = transcribe_audio(chunk)
    if text:
        transcribed_texts.append(text)
    os.remove(chunk)  # Clean up the chunk file after processing

full_transcription = " ".join(transcribed_texts)
print(f"Full transcription: {full_transcription}")

translated_text = translate_text(full_transcription)
print(f"Translated text: {translated_text}")

output_audio_file = 'translated_audio.mp3'
text_to_speech(translated_text, output_audio_file)
print(f"Output audio file: {output_audio_file}")
