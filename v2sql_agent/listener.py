import sounddevice as sd
import soundfile as sf
import whisper
import numpy as np
import os

def record_audio(duration=5, sample_rate=16000, filename="query.wav"):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    
    print(f"\n🎙️ Recording started for {duration} seconds... Speak now!")
    # Record as float32, which Whisper handles beautifully natively
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  
    print("🛑 Recording stopped.")
    
    # Save using soundfile instead of scipy
    sf.write(file_path, audio_data, sample_rate)
    return file_path

def transcribe_voice(file_path):
    print("⏳ Transcribing speech using Whisper AI...")
    
    # Using the tiny model to keep it lightning fast on CPU
    model = whisper.load_model("tiny")
    
    # Read the audio array natively using soundfile to completely bypass ffmpeg
    audio_array, sample_rate = sf.read(file_path)
    
    # Whisper expects a 1D float32 array
    audio_array = audio_array.astype(np.float32)
    
    # Transcribe directly from the raw data
    result = model.transcribe(audio_array, fp16=False)
    text = result["text"]
    
    print(f"🗣️ You said: \"{text}\"")
    return text

if __name__ == "__main__":
    audio_file = record_audio(duration=5)
    transcribe_voice(audio_file)