#  🎤 Audio to 📝Text, 🌐Translate & Convert to 🔊Speech

This project is a complete pipeline that:

1. **Splits** long audio files into smaller chunks.
2. **Transcribes** the audio chunks to text using speech recognition.
3. **Translates** the transcribed text into a specified language (default is Telugu).
4. **Converts** the translated text back to speech and saves it as an audio file.

The pipeline uses **PyDub** for audio processing, **Google Speech Recognition API** for transcribing, **Google Translate API** for translation, and **gTTS** (Google Text-to-Speech) for converting the translated text back to audio.

## 🧠 Features

* 🎤 **Audio Splitting**: Splits long audio files into smaller chunks based on silence.
* 📝 **Speech-to-Text**: Transcribes audio to text using Google's Speech Recognition.
* 🌐 **Text Translation**: Translates the transcribed text into the desired language (default: Telugu).
* 🔊 **Text-to-Speech**: Converts the translated text into speech and saves the result as an audio file.

## 🧱 Project Structure

* `main.py`: The main Python script that handles the entire audio-to-text, translate, and speech synthesis process.
* `requirements.txt`: List of dependencies required to run the project.

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://bayojuvikas/Dubbing_X-Language-Script-to-Y-Language-Audio.git
   cd Dubbing_X-Language-Script-to-Y-Language-Audio
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have **ffmpeg** installed for PyDub to work properly.

   You can download **ffmpeg** from [FFmpeg.org](https://ffmpeg.org/download.html), and then ensure it's in your system's PATH.

4. Ensure you have the necessary API keys set up for Google services (Google Speech API, Google Translate API).

## 🏃‍♂️ Running the Application

To run the pipeline, simply execute the `main.py` script:

```bash
python main.py
```

### Example Input and Output

* Input: A long audio file (`WhatsApp Audio.wav`).
* Output:

  1. Transcribed text from the audio.
  2. Translated text (default language: Telugu).
  3. A new audio file (`translated_audio.mp3`) with the translated text spoken in Telugu.

### Customize the Language

You can change the translation language by modifying the `dest_language` argument in the `translate_text()` function. For example:

```python
translated_text = translate_text(full_transcription, dest_language="hi")  # For Hindi
```

## 📦 Requirements

The project requires the following Python packages:

* `pydub` - For audio manipulation.
* `speech_recognition` - For speech-to-text conversion.
* `googletrans` - For translating text using Google Translate.
* `gtts` - For text-to-speech conversion.

You can install these dependencies by running:

```bash
pip install pydub SpeechRecognition googletrans==4.0.0-rc1 gTTS
```

## 💡 How It Works

1. **Splitting Audio**: The `split_audio` function takes the audio file and splits it into smaller chunks whenever it detects silence.
2. **Transcription**: The `transcribe_audio` function processes each chunk and uses Google’s Speech Recognition to convert audio into text.
3. **Translation**: The transcribed text is then translated into the target language (Telugu by default) using Google Translate API.
4. **Speech Synthesis**: The translated text is converted back into audio using the `gTTS` library and saved as a `.mp3` file.

## ⚙️ Configuration

* The audio file path and the chunk length (default: 30 seconds) can be adjusted as needed in the `main.py` script.
* Ensure the **Google Translate API** and **Google Speech Recognition API** are properly configured for the script to work effectively.

## 📄 License

This project is licensed under the MIT License.
