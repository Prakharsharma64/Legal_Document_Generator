# Legal Document Generator

A comprehensive web application for generating professional legal documents with customizable templates. The application supports multiple document types and languages, providing a streamlined process for creating legally-sound documents based on user inputs.

## Table of Contents

- [Legal Document Generator](#legal-document-generator)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Deployment](#deployment)
  - [Document Types](#document-types)
  - [Technical Architecture](#technical-architecture)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The Legal Document Generator is a web-based tool designed to simplify the creation of legal documents through an intuitive interface. It leverages AI-powered text generation to produce customized legal content based on user inputs, supporting a wide range of document types from employment contracts to intellectual property agreements.

## Features

- **Multiple Document Types**: Support for various legal documents including contracts, agreements, and licenses
- **Dynamic Form Generation**: Custom form fields based on selected document type
- **Multilingual Support**: Generate documents in multiple languages including English, Hindi, and regional Indian languages
- **Professional Formatting**: Clean, professionally styled document output
- **Document History**: Keep track of previously generated documents
- **Responsive UI**: Mobile-friendly interface with modern design
- **Real-time Processing**: Instant document generation

## Project Structure

The project is structured as follows:

```
legal-document-generator/
├── app.py                  # Main Flask application
├── render_app.py           # Render deployment wrapper
├── render.yaml             # Render configuration
├── requirements.txt        # Python dependencies
├── document_generator.py   # AI-powered document generation logic
├── document_formatter.py   # Document styling and formatting
├── document_templates.py   # Templates and questions for each document type
├── document_history.json   # Stores generated document history
└── .env                    # Environment variables for API keys
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/legal-document-generator.git
cd legal-document-generator
```

2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys

```
OPENROUTER_API_KEY=your_api_key_here
SITE_URL=your_site_url_here
SITE_NAME=your_site_name_here
```

5. Run the application locally

```bash
python app.py
```

6. Visit `http://localhost:5000` in your browser

## Deployment

The application can be deployed on Render with minimal configuration:

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set the following environment variables in Render:
   - `OPENROUTER_API_KEY`
   - `SITE_URL`
   - `SITE_NAME`
5. Render will automatically detect the `render.yaml` configuration and deploy your application

The application will be available at your Render-provided URL.

## Document Types

The application supports the following document types:

### Business Agreements

- Non-Disclosure Agreement (NDA)
- Partnership Agreement
- Shareholders Agreement
- Franchise Agreement
- Joint Venture Agreement
- Distribution Agreement
- Manufacturing Agreement

### Employment & HR

- Employment Contract
- Consulting Agreement
- Independent Contractor Agreement
- Non-Compete Agreement
- Severance Agreement
- Sales Commission Agreement

### Sales & Services

- Sales Contract
- Service Agreement
- Subscription Agreement
- Maintenance Contract
- Software License Agreement
- SaaS Agreement

### Real Estate

- Residential Lease Agreement
- Commercial Lease Agreement
- Sublease Agreement
- Property Management Agreement
- Real Estate Purchase Agreement

### Financial

- Loan Agreement
- Investment Agreement
- Promissory Note
- Security Agreement
- Personal Guarantee

### Intellectual Property

- IP License Agreement
- Trademark License
- Patent License
- Copyright Transfer
- Technology Transfer Agreement

## Technical Architecture

The application follows a Model-View-Controller (MVC) architecture:

- **Model**: Document templates and generation logic (document_templates.py, document_generator.py)
- **View**: HTML templates and CSS styling
- **Controller**: Flask application routes and request handling (app.py)

Data flow:

1. User selects document type (client-side)
2. Application fetches relevant questions via API
3. User submits form data
4. Server processes data and generates document using AI
5. Formatted document is returned to client and displayed
6. Document can be saved to history for future reference

## Dependencies

The application requires the following Python packages:

- Flask==3.0.2
- openai==1.12.0
- python-dotenv==1.0.1
- httpx==0.27.0
- Werkzeug==3.0.1
- Jinja2==3.1.3
- itsdangerous==2.1.2
- click==8.1.7
- MarkupSafe==2.1.5
- blinker==1.7.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
