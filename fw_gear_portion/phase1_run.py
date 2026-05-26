import os
import requests
from flywheel_gear_toolkit import GearToolkitContext

def main():
    # Initialize the gear context to parse inputs
    context = GearToolkitContext()
    
    # Locate the dummy file path just to prove we "ran on a file"
    file_path = context.get_input_path("dummy_file")
    print(file_path)
    print(f"[INFO] Found input file at: {file_path}. Proceeding to API call...")

    # Target your local machine from inside Docker
    # Note: If testing on Linux, you might need http://172.17.0.1:8000 instead
    url = "http://host.docker.internal:8000/status"
    
    try:
        print(f"[INFO] Sending request to {url}...")
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"[SUCCESS] Response from host: {response.json()}")
        else:
            print(f"[ERROR] Server responded with code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[FAILURE] Could not connect to the local API. Error: {e}")

if __name__ == "__main__":
    main()
