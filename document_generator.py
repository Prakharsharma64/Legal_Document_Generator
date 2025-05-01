from openai import OpenAI
import os
from dotenv import load_dotenv
import httpx
import json

# Load environment variables
load_dotenv()

# Configuration
OPENROUTER_CONFIG = {
    "base_url": "https://openrouter.ai/api/v1",
    "api_key": os.getenv('OPENROUTER_API_KEY'),
    "site_url": os.getenv('SITE_URL', 'https://github.com/yourusername/legal-document-generator'),
    "site_name": os.getenv('SITE_NAME', 'Legal Document Generator'),
    "model": "google/gemini-2.5-flash-preview"
}

# Initialize OpenAI client
client = OpenAI(
    base_url=OPENROUTER_CONFIG["base_url"],
    api_key=OPENROUTER_CONFIG["api_key"],
    http_client=httpx.Client(
        base_url=OPENROUTER_CONFIG["base_url"],
        headers={
            "HTTP-Referer": OPENROUTER_CONFIG["site_url"],
            "X-Title": OPENROUTER_CONFIG["site_name"]
        }
    )
)

def generate_legal_document(document_type, language, details):
    """Generate a legal document based on type, language and details."""
    
    # Format details into a structured string
    details_text = "\n".join([f"{key}: {value}" for key, value in details.items()])
    
    # Create the prompt with enhanced instructions
    prompt = f"""Generate a professional {document_type} in {language} based on the following details. 
The document should be legally sound and properly formatted.

Document Details:
{details_text}

Document Requirements:
1. Use proper legal document structure with numbered sections and subsections
2. Include a clear title at the top in ALL CAPS
3. Use appropriate legal language and terminology
4. Include proper signature blocks at the end
5. Format dates in long form
6. Include proper paragraph indentation and spacing
7. Use appropriate section headings
8. Include a proper introductory paragraph
9. End with proper signature sections
10. Include a definitions section if necessary
11. Use consistent formatting throughout
12. Ensure all legal terms are properly defined
13. Include appropriate disclaimers and notices
14. Use proper legal citations if required
15. Include proper jurisdiction and governing law clauses"""

    try:
        # Generate document using the language model
        response = client.chat.completions.create(
            model=OPENROUTER_CONFIG["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,  # Controls randomness
            max_tokens=4000,  # Maximum length of the generated document
            top_p=0.9,       # Controls diversity
            frequency_penalty=0.5,  # Reduces repetition
            presence_penalty=0.5    # Encourages topic coverage
        )
        
        # Extract and clean the generated content
        generated_content = response.choices[0].message.content.strip()
        
        # Validate the generated content
        if not generated_content:
            raise ValueError("Generated document is empty")
            
        return generated_content
        
    except Exception as e:
        print(f"Error generating document: {str(e)}")
        raise ValueError(f"Failed to generate document: {str(e)}")

def validate_document_content(content):
    """Validate the generated document content."""
    if not content:
        return False
    if len(content) < 100:  # Minimum length check
        return False
    if not any(keyword in content.lower() for keyword in ["agreement", "contract", "terms", "conditions"]):
        return False
    return True 