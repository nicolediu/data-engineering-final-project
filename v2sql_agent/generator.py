import yaml
import os
from google import genai  # The NEW unified 2026 SDK
from dotenv import load_dotenv

load_dotenv()

def get_sql_from_ai(user_question):
    # Dynamic pathing for metadata
    base_dir = os.path.dirname(__file__)
    metadata_path = os.path.join(base_dir, "metadata.yaml")
    
    with open(metadata_path, "r") as f:
        metadata = yaml.safe_load(f)

    # Force the client to use the modern, unified architecture
    client = genai.Client(
        vertexai=True, 
        project="infra-vertex-494802-i0", 
        location="us-central1"
    )

    prompt = f"""
    Target: Google BigQuery SQL
    Table: {metadata['table_name']}
    Schema Context: {metadata['semantic_mapping']}
    Constraint Rules: {metadata['query_constraints']}
    
    Task: Convert the user question into a valid BigQuery SQL query.
    Question: {user_question}
    
    Output Format: Return ONLY the raw SQL. No markdown, no triple backticks, no preamble.
    """

    # Using the flagship stable model for 2026
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    
    return response.text.strip()

if __name__ == "__main__":
    try:
        sql = get_sql_from_ai("Top 3 niches by revenue in Sao Paulo?")
        print(f"\n🤖 AI Generated SQL:\n{sql}")
    except Exception as e:
        print(f"❌ Error: {e}")