

import os
import shutil
from datetime import datetime

def rotate_log(logfile, max_size_mb=5):
    if os.path.exists(logfile):
        file_size = os.path.getsize(logfile) / (1024 * 1024)
        
        if file_size > max_size_mb:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{logfile}.{timestamp}.bak"
            shutil.copy(logfile, backup_name)
            
            with open(logfile, 'w') as f:
                f.write(f"Log rotated on {datetime.now()}\n")
            
            print(f"Log rotated. Backup created: {backup_name}")
            return True
    return False

def parse_log(logfile, keyword=None):
    try:
        with open(logfile, 'r') as file:
            lines = file.readlines()
            
            print("=" * 50)
            print("LOG FILE PARSING REPORT")
            print("=" * 50)
            print(f"Total entries: {len(lines)}")
            
            error_count = 0
            warning_count = 0
            info_count = 0
            
            for line in lines:
                if 'ERROR' in line.upper():
                    error_count += 1
                elif 'WARNING' in line.upper():
                    warning_count += 1
                elif 'INFO' in line.upper():
                    info_count += 1
            
            print(f"Errors: {error_count}")
            print(f"Warnings: {warning_count}")
            print(f"Info: {info_count}")
            
            if keyword:
                print(f"\nSearching for keyword: '{keyword}'")
                matches = [line for line in lines if keyword.lower() in line.lower()]
                print(f"Matches found: {len(matches)}")
                for match in matches[:5]:
                    print(f"  {match.strip()}")
            
            print("=" * 50)
            
    except FileNotFoundError:
        print(f"Error: Log file '{logfile}' not found")

logfile = input("Enter log filename: ")
rotate_log(logfile, 5)
parse_log(logfile, "error")