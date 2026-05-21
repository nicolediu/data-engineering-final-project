import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from listener import record_audio, transcribe_voice
from generator import get_sql_from_ai
from connector import run_query

def clean_sql_string(raw_sql):
    """
    Defensive Engineering: Removes markdown code block wrappers 
    if the LLM accidentally includes them.
    """
    cleaned = raw_sql.strip()
    if cleaned.startswith("```"):
        # Remove the opening ```sql or ```
        cleaned = "\n".join(cleaned.split("\n")[1:])
    if cleaned.endswith("```"):
        # Remove the closing ```
        cleaned = cleaned.rsplit("```", 1)[0]
    return cleaned.strip()

def main():
    print("\n=============================================")
    print("🎙️ 🤖 WELCOME TO THE OLIST VOICE-TO-SQL AGENT")
    print("=============================================\n")
    
    input("Press Enter when you are ready to speak your data question...")
    audio_path = record_audio(duration=5)
    
    user_text = transcribe_voice(audio_path)
    
    if not user_text.strip():
        print("❌ Could not detect any speech. Please try running the script again.")
        return

    print("\n⏳ Mapping semantic terms and translating to SQL...")
    raw_sql = get_sql_from_ai(user_text)
    
    # Apply our new string scrubbing function
    generated_sql = clean_sql_string(raw_sql)
    
    print("\n💻 Generated SQL (Cleaned):")
    print("-" * 50)
    print(generated_sql)
    print("-" * 50)
    
    print("\n📊 Executing on BigQuery Warehouse...")
    results_df = run_query(generated_sql)
    
    print("\n✨ Query Results:")
    print("=" * 50)
    print(results_df)
    print("=" * 50)

if __name__ == "__main__":
    main()