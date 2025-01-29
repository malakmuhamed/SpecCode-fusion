def match_requirements_to_functions(requirements, functions):
    """Match extracted requirements to function names from uploaded files."""
    matches = {req: [] for req in requirements}
    for req in requirements:
        for func in functions:
            if any(word in func.lower() for word in req.lower().split()):
                matches[req].append(func)
    return matches

if __name__ == "__main__":
    from extractor import load_srs, extract_requirements
    from parser import extract_functions

    srs_file = input("Enter the SRS file path (e.g., uploads/sample_srs.txt): ").strip()
    code_file = input("Enter the source code file path (e.g., uploads/sample_code.py): ").strip()

    srs_text = load_srs(srs_file)
    functions = extract_functions(code_file)

    if srs_text and functions:
        requirements = extract_requirements(srs_text)
        matches = match_requirements_to_functions(requirements, functions)
        print("Matches:", matches)
