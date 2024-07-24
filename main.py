import pandas as pd
from audio_processing import transcribe_audio
from text_analysis import analyze_text, extract_entities

def process_accident_report(audio_file):
    # Step 1: Transcribe audio to text
    text = transcribe_audio(audio_file)

    # Step 2: Analyze text
    word_freq = analyze_text(text)
    entities = extract_entities(text)

    return text, word_freq, entities

def save_to_csv(data, filename='transcriptions.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # Define your audio file details
    audio_files = [
        'recorded_audio (13).wav',
        'recorded_audio (14).wav',
        'recorded_audio (15).wav',
        'recorded_audio (16).wav',
   
    ]

    results = []
    for audio_file in audio_files:
        text, word_freq, entities = process_accident_report(audio_file)
        
        result = {
            'audio_file': audio_file,
            'transcription': text,
            'word_frequency': str(word_freq),  # Convert dict to string for CSV
            'entities': str(entities)          # Convert dict to string for CSV
        }
        results.append(result)

    # Save results to CSV
    save_to_csv(results)
