"""
Module containing templates and detailed questions for different types of legal documents.
"""

class DocumentTemplates:
    @staticmethod
    def get_template_questions(document_type):
        """Get the list of questions for a specific document type."""
        templates = {
            "employment_contract": {
                "title": "Employment Contract",
                "questions": [
                    {
                        "id": "employer_name",
                        "label": "Employer's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "e.g., ABC Corporation Ltd."
                    },
                    {
                        "id": "employer_address",
                        "label": "Employer's Complete Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Full registered address including postal code"
                    },
                    {
                        "id": "employee_name",
                        "label": "Employee's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "e.g., John A. Smith"
                    },
                    {
                        "id": "employee_address",
                        "label": "Employee's Complete Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Full residential address including postal code"
                    },
                    {
                        "id": "position_title",
                        "label": "Job Title/Position",
                        "type": "text",
                        "required": True,
                        "placeholder": "e.g., Senior Software Engineer"
                    },
                    {
                        "id": "start_date",
                        "label": "Employment Start Date",
                        "type": "date",
                        "required": True
                    },
                    {
                        "id": "employment_type",
                        "label": "Type of Employment",
                        "type": "select",
                        "options": ["Full-time", "Part-time", "Contract", "Temporary"],
                        "required": True
                    },
                    {
                        "id": "salary",
                        "label": "Base Salary/Wages",
                        "type": "number",
                        "required": True,
                        "placeholder": "Annual salary amount"
                    },
                    {
                        "id": "payment_frequency",
                        "label": "Payment Frequency",
                        "type": "select",
                        "options": ["Weekly", "Bi-weekly", "Monthly"],
                        "required": True
                    },
                    {
                        "id": "working_hours",
                        "label": "Working Hours",
                        "type": "text",
                        "required": True,
                        "placeholder": "e.g., 9:00 AM to 5:00 PM, Monday to Friday"
                    },
                    {
                        "id": "probation_period",
                        "label": "Probation Period (in months)",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 3"
                    },
                    {
                        "id": "vacation_days",
                        "label": "Annual Vacation Days",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 20"
                    },
                    {
                        "id": "benefits",
                        "label": "Benefits Package Details",
                        "type": "textarea",
                        "required": False,
                        "placeholder": "List all benefits (health insurance, retirement plans, etc.)"
                    },
                    {
                        "id": "notice_period",
                        "label": "Notice Period (in weeks)",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 2"
                    }
                ]
            },
            "nda": {
                "title": "Non-Disclosure Agreement",
                "questions": [
                    {
                        "id": "disclosing_party",
                        "label": "Disclosing Party's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "Entity/person disclosing confidential information"
                    },
                    {
                        "id": "disclosing_address",
                        "label": "Disclosing Party's Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Complete address of disclosing party"
                    },
                    {
                        "id": "receiving_party",
                        "label": "Receiving Party's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "Entity/person receiving confidential information"
                    },
                    {
                        "id": "receiving_address",
                        "label": "Receiving Party's Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Complete address of receiving party"
                    },
                    {
                        "id": "purpose",
                        "label": "Purpose of Disclosure",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Describe the business purpose for sharing confidential information"
                    },
                    {
                        "id": "effective_date",
                        "label": "Effective Date",
                        "type": "date",
                        "required": True
                    },
                    {
                        "id": "duration",
                        "label": "Duration of Agreement (in years)",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 2"
                    },
                    {
                        "id": "confidential_info",
                        "label": "Definition of Confidential Information",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Specify what constitutes confidential information"
                    },
                    {
                        "id": "exclusions",
                        "label": "Exclusions from Confidential Information",
                        "type": "textarea",
                        "required": False,
                        "placeholder": "Information that is not considered confidential"
                    },
                    {
                        "id": "return_period",
                        "label": "Return/Destruction Period (in days)",
                        "type": "number",
                        "required": True,
                        "placeholder": "Days to return/destroy confidential information"
                    }
                ]
            },
            "lease_agreement": {
                "title": "Lease Agreement",
                "questions": [
                    {
                        "id": "landlord_name",
                        "label": "Landlord's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "Individual or company name"
                    },
                    {
                        "id": "landlord_address",
                        "label": "Landlord's Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Complete contact address"
                    },
                    {
                        "id": "tenant_name",
                        "label": "Tenant's Full Legal Name",
                        "type": "text",
                        "required": True,
                        "placeholder": "All tenants' names"
                    },
                    {
                        "id": "property_address",
                        "label": "Property Address",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Complete address of rental property"
                    },
                    {
                        "id": "property_type",
                        "label": "Property Type",
                        "type": "select",
                        "options": ["Apartment", "House", "Condo", "Commercial Space"],
                        "required": True
                    },
                    {
                        "id": "lease_start",
                        "label": "Lease Start Date",
                        "type": "date",
                        "required": True
                    },
                    {
                        "id": "lease_end",
                        "label": "Lease End Date",
                        "type": "date",
                        "required": True
                    },
                    {
                        "id": "monthly_rent",
                        "label": "Monthly Rent Amount",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 1500"
                    },
                    {
                        "id": "security_deposit",
                        "label": "Security Deposit Amount",
                        "type": "number",
                        "required": True,
                        "placeholder": "e.g., 1500"
                    },
                    {
                        "id": "utilities_included",
                        "label": "Utilities Included",
                        "type": "checkbox",
                        "options": ["Water", "Electricity", "Gas", "Internet", "Trash"],
                        "required": True
                    },
                    {
                        "id": "pets_allowed",
                        "label": "Pets Allowed",
                        "type": "boolean",
                        "required": True
                    },
                    {
                        "id": "pet_deposit",
                        "label": "Pet Deposit (if applicable)",
                        "type": "number",
                        "required": False,
                        "placeholder": "Additional deposit for pets"
                    },
                    {
                        "id": "maintenance_terms",
                        "label": "Maintenance Responsibilities",
                        "type": "textarea",
                        "required": True,
                        "placeholder": "Specify who is responsible for various maintenance tasks"
                    },
                    {
                        "id": "special_terms",
                        "label": "Special Terms and Conditions",
                        "type": "textarea",
                        "required": False,
                        "placeholder": "Any additional terms or conditions"
                    }
                ]
            }
            # Add more document types here
        }
        
        return templates.get(document_type, {})

    @staticmethod
    def get_document_types():
        """Get the list of available document types."""
        return [
            {
                "id": "employment_contract",
                "name": "Employment Contract",
                "description": "A legal agreement between employer and employee defining terms of employment"
            },
            {
                "id": "nda",
                "name": "Non-Disclosure Agreement",
                "description": "A contract to protect confidential information shared between parties"
            },
            {
                "id": "lease_agreement",
                "name": "Lease Agreement",
                "description": "A contract between landlord and tenant for property rental"
            }
            # Add more document types here
        ] 