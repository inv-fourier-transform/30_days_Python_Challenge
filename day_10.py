import re

def process_file(filename: str) -> tuple[list[int], list[str]]:

    valid_numbers = []
    bad_tokens = []
    
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                # Split line into tokens on whitespace
                tokens = line.strip().split()
                
                for token in tokens:
                    if not token:  # Skip empty tokens
                        continue
                        
                    # Normalize the token
                    normalized = token.replace(' ', '').replace(',', '').replace('_', '').replace('+', '')
                    
                    # Remove letters (but keep negative sign at start if present)
                    if normalized.startswith('-'):
                        normalized = '-' + re.sub(r'[^0-9]', '', normalized[1:])
                    else:
                        normalized = re.sub(r'[^0-9]', '', normalized)
                    
                    # Try to convert to integer
                    if normalized:  # Only try conversion if we have something left
                        try:
                            num = int(normalized)
                            valid_numbers.append(num)
                        except ValueError:
                            bad_tokens.append(token)
                    else:
                        bad_tokens.append(token)
                        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {str(e)}")
        exit(1)
    
    return valid_numbers, bad_tokens


def main():
    filename = input("Enter the path to the numbers file: ")
    valid_numbers, bad_tokens = process_file(filename)
    
    print("\nResults:")
    print("-" * 40)
    print(f"Valid integers: {valid_numbers}")
    print(f"Bad tokens: {bad_tokens}")
    
if __name__ == "__main__":
    main()
