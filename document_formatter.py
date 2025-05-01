"""
Module for handling legal document formatting and structure.
"""

class LegalDocumentFormatter:
    def __init__(self):
        self.default_margins = {
            'top': '1in',
            'bottom': '1in',
            'left': '1in',
            'right': '1in'
        }
        self.default_indent = '0.5in'
        self.line_spacing = 2

    def format_document(self, content, document_type):
        """Format the document with proper styling and structure."""
        
        formatted_content = f"""
        <div class="document-content">
            <div class="legal-document">
                {content}
            </div>
        </div>
        """
        
        return formatted_content

    def _format_sections(self, content):
        """Format document sections with proper spacing and structure."""
        lines = content.split('\n')
        formatted_lines = []
        in_section = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect and format section headers
            if line.isupper() and not line.endswith(':'):
                formatted_lines.append(f'<div class="section-header">{line}</div>')
                in_section = True
            # Format subsections
            elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                formatted_lines.append(f'<div class="subsection">{line}</div>')
            # Format signature blocks
            elif 'SIGNED' in line.upper() or 'WITNESS' in line.upper():
                formatted_lines.append(self._format_signature_block(line))
            # Format regular paragraphs
            else:
                formatted_lines.append(f'<p>{line}</p>')

        return '\n'.join(formatted_lines)

    def _format_signature_block(self, content):
        """Format signature blocks with proper spacing and structure."""
        return f'''
        <div class="signature-block">
            <div class="signature-line"></div>
            <div class="signature-name">{content}</div>
            <div class="signature-date">Date: _____________________</div>
        </div>
        '''

    def _wrap_in_html(self, title, body):
        """Wrap the formatted content in proper HTML structure."""
        return f'''
        <div class="legal-document">
            <div class="document-title">
                {title}
            </div>
            <div class="document-body">
                {body}
            </div>
        </div>
        '''

    def format_date(self, date_str):
        """Format dates in proper legal style."""
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj.strftime('%dst day of %B, %Y').replace('1st', self._get_day_suffix(date_obj.day))
        except ValueError:
            return date_str

    def _get_day_suffix(self, day):
        """Get the proper suffix for the day (1st, 2nd, 3rd, etc.)."""
        if 10 <= day % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return f"{day}{suffix}"

    def get_document_css(self):
        """Return the CSS styles for legal documents."""
        return '''
        .legal-document {
            font-family: "Times New Roman", Times, serif;
            font-size: 12pt;
            line-height: 2;
            margin: 1in;
            color: black;
            background-color: white;
        }

        .document-title {
            text-align: center;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }

        .document-body {
            text-align: justify;
        }

        .section-header {
            font-weight: bold;
            text-transform: uppercase;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }

        .subsection {
            margin-left: 0.5in;
            margin-bottom: 1rem;
        }

        p {
            text-indent: 0.5in;
            margin-bottom: 1rem;
        }

        .signature-block {
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        .signature-line {
            border-top: 1px solid black;
            width: 200px;
            margin-top: 2rem;
        }

        .signature-name {
            margin-top: 0.5rem;
        }

        .signature-date {
            margin-top: 1rem;
        }
        ''' 