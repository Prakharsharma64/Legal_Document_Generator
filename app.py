from flask import Flask, render_template, request, jsonify, url_for
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import httpx
from document_formatter import LegalDocumentFormatter
from document_templates import DocumentTemplates
from document_generator import generate_legal_document, client as openai_client

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_url_path='/static')
document_formatter = LegalDocumentFormatter()
document_templates = DocumentTemplates()

# Get API key from environment variable
api_key = os.getenv('OPENROUTER_API_KEY')
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

# Document history file path
HISTORY_FILE = 'document_history.json'

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

@app.context_processor
def inject_request():
    return dict(request=request)

@app.route('/')
def home():
    document_types = document_templates.get_document_types()
    history = load_history()
    return render_template('index.html', document_types=document_types, history=history)

@app.route('/get_questions/<document_type>')
def get_questions(document_type):
    template = document_templates.get_template_questions(document_type)
    if template:
        return jsonify(template)
    return jsonify({"error": "Document type not found"}), 404

@app.route('/generate', methods=['POST'])
def generate_document():
    try:
        data = request.get_json()
        document_type = data.get('document_type')
        language = data.get('language')
        details = data.get('details')

        if not all([document_type, language, details]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Generate the document based on type and language
        document = generate_legal_document(document_type, language, details)
        
        # Format the document with proper styling
        formatted_document = f"""
        <div class="document-content">
            <div class="legal-document">
                {document}
            </div>
        </div>
        """

        return jsonify({'document': formatted_document})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    history = load_history()
    return render_template('history.html', history=history)

@app.route('/document/<int:doc_id>')
def get_document(doc_id):
    history = load_history()
    document = next((doc for doc in history if doc['id'] == doc_id), None)
    if document:
        return jsonify(document)
    return jsonify({"error": "Document not found"}), 404

# Add route to serve document CSS
@app.route('/static/css/legal-document.css')
def legal_document_css():
    return document_formatter.get_document_css(), 200, {'Content-Type': 'text/css'}

if __name__ == '__main__':
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 10000))
    # Run app on 0.0.0.0 to make it accessible externally
    app.run(host='0.0.0.0', port=port, debug=True)


