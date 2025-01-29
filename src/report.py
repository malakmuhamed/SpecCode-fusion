import matplotlib.pyplot as plt

def visualize_compatibility(matches):
    """Visualize matched vs unmatched requirements from uploaded files."""
    matched = sum(1 for funcs in matches.values() if funcs)
    unmatched = len(matches) - matched
    labels = ['Matched', 'Unmatched']
    sizes = [matched, unmatched]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Requirement Compatibility')
    plt.show()

if __name__ == "__main__":
    from matcher import match_requirements_to_functions
    from extractor import load_srs, extract_requirements
    from parser import extract_functions

    srs_file = input("Enter the SRS file path (e.g., uploads/sample_srs.txt): ").strip()
    code_file = input("Enter the source code file path (e.g., uploads/sample_code.py): ").strip()

    srs_text = load_srs(srs_file)
    functions = extract_functions(code_file)

    if srs_text and functions:
        requirements = extract_requirements(srs_text)
        matches = match_requirements_to_functions(requirements, functions)
        visualize_compatibility(matches)
