

def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = 0
            char_count = 0
            
            for line in lines:
                words = line.split()
                word_count += len(words)
                char_count += len(line)
            
            print("=" * 40)
            print("FILE ANALYSIS REPORT")
            print("=" * 40)
            print(f"Filename: {filename}")
            print(f"Total lines: {line_count}")
            print(f"Total words: {word_count}")
            print(f"Total characters: {char_count}")
            print(f"Average words per line: {word_count/line_count:.2f}")
            print("=" * 40)
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

filename = input("Enter filename to analyze: ")
analyze_file(filename)