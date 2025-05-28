import json
import os

def update_json_image_paths(directory_path):
    """
    Updates the 'image' URL in JSON files within the specified directory.
    The URL is modified to ensure 'v2/' is present after '/refs/heads/main/'.
    """
    base_path_segment = "/refs/heads/main/"
    required_prefix_after_base = "v2/"
    updated_files_count = 0
    checked_files_count = 0

    print(f"Scanning directory: {directory_path}")

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            checked_files_count += 1
            file_path = os.path.join(directory_path, filename)
            
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                if "image" in data and isinstance(data["image"], str):
                    original_url = data["image"]
                    
                    if base_path_segment in original_url:
                        parts = original_url.split(base_path_segment, 1)
                        # parts[0] is everything before base_path_segment
                        # parts[1] is everything after base_path_segment
                        
                        path_after_main = parts[1]
                        
                        if not path_after_main.startswith(required_prefix_after_base):
                            # Construct the new URL
                            new_url = parts[0] + base_path_segment + required_prefix_after_base + path_after_main
                            data["image"] = new_url
                            
                            with open(file_path, 'w') as f:
                                json.dump(data, f, indent=2) # Using indent=2 for consistency if original had it
                            print(f"Updated image URL in {filename}:")
                            print(f"  Old: {original_url}")
                            print(f"  New: {new_url}")
                            updated_files_count += 1
                        else:
                            print(f"Image URL in {filename} already correct: {original_url}")
                    else:
                        print(f"Skipping {filename}: Image URL does not contain '{base_path_segment}'. URL: {original_url}")
                else:
                    print(f"Skipping {filename}: 'image' key not found or its value is not a string.")
            
            except json.JSONDecodeError:
                print(f"Error decoding JSON from {filename}. Skipping.")
            except Exception as e:
                print(f"An error occurred with {filename}: {e}. Skipping.")
    
    print(f"\nScript finished. Checked {checked_files_count} JSON files. Updated {updated_files_count} files.")

if __name__ == "__main__":
    # This path is relative to where you run the script.
    # If your script is in the workspace root, this should be correct.
    target_directory = "v2/metadata/insignia" 
    
    if os.path.isdir(target_directory):
        update_json_image_paths(target_directory)
    else:
        print(f"Directory not found: {target_directory}")
        print("Please ensure the script is in the correct location or update the 'target_directory' variable in the script.")
