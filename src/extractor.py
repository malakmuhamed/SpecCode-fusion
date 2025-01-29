import re
import fitz  # PyMuPDF for PDF handling

def load_srs(file_path):
    """Load an external SRS file (supports .txt and .pdf)."""
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        print("Unsupported file format! Please provide a .txt or .pdf file.")
        return None

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def extract_requirements(srs_text):
    """Extract functional requirements using keyword-based NLP."""
    pattern = r"(shall|must|will|should)\s+([^.\n]*)"
    requirements = re.findall(pattern, srs_text, flags=re.IGNORECASE)
    return [req[1].strip() for req in requirements]

# Main logic to run the extractor alone
if __name__ == "__main__":
    # Get file path for the SRS from the user
    srs_file = input("Enter the SRS PDF file path (e.g., C:\\path\\to\\specode.pdf): ").strip()

    # Load the SRS file content
    srs_text = load_srs(srs_file)
    if not srs_text:
        print("Error: Unable to load the SRS file.")
    else:
        print("SRS file loaded successfully.\n")

        # Extract the requirements from the SRS text
        requirements = extract_requirements(srs_text)
        
        if requirements:
            print("\n=== Extracted Requirements ===")
            for req in requirements:
                print(f"- {req}")
        else:
            print("No requirements extracted.")
