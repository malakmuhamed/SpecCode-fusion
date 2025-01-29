import os
import re
import fitz  # PyMuPDF for PDF handling
from extractor import load_srs, extract_requirements  # Assuming extractor is in another file

def main():
    # Get the SRS file path from the user
    srs_file = input("Enter the SRS PDF file path (e.g., C:\\path\\to\\specode.pdf): ").strip()

    # Load the SRS file
    srs_text = load_srs(srs_file)
    if not srs_text:
        print("Error: Unable to load SRS file.")
        return

    print("SRS file loaded successfully.\n")

    # Extract requirements from the SRS text
    requirements = extract_requirements(srs_text)

    if requirements:
        print("\n=== Extracted Requirements ===")
        for req in requirements:
            print(f"- {req}")

        # Ensure the 'data' folder exists
        output_folder = "data"
        os.makedirs(output_folder, exist_ok=True)

        # Save requirements to a file
        output_file = os.path.join(output_folder, "extracted_requirements.txt")
        with open(output_file, "w") as file:
            file.write("\n".join(requirements))

        print(f"\nExtracted requirements saved to: {output_file}")
    else:
        print("No requirements extracted.")

if __name__ == "__main__":
    main()
