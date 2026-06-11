import re

def extract_emails_from_file(filename):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            emails = re.findall(email_pattern, content)
            
            unique_emails = list(set(emails))
            
            print("=" * 50)
            print("EMAIL EXTRACTION REPORT")
            print("=" * 50)
            print(f"File: {filename}")
            print(f"Total emails found: {len(emails)}")
            print(f"Unique emails: {len(unique_emails)}")
            print("\nExtracted emails:")
            print("-" * 50)
            
            for email in sorted(unique_emails):
                print(email)
            
            print("=" * 50)
            
            with open("extracted_emails.txt", "w") as output_file:
                for email in sorted(unique_emails):
                    output_file.write(email + "\n")
            
            print(f"\nEmails saved to: extracted_emails.txt")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

filename = input("Enter filename to extract emails from: ")
extract_emails_from_file(filename)