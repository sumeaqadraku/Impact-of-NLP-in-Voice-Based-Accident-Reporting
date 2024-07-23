from audio_processing import transcribe_audio
from text_analysis import analyze_text, extract_entities

def process_accident_report(audio_file):
    # Step 1: Transcribe audio to text
    text = transcribe_audio(audio_file)

    # Step 2: Analyze text
    word_freq = analyze_text(text)
    entities = extract_entities(text)

    return text, word_freq, entities

if __name__ == "__main__":
    audio_file = 'recorded_audio (12).wav'
    text, word_freq, entities = process_accident_report(audio_file)

    print("Transcribed Text:", text)
    print("Word Frequency:", word_freq)
    print("Entities:", entities)
