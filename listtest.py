import os
import re


def is_image_file(filename):
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def write_formatted_filenames_to_txt(folder_path):
    folder_name = os.path.basename(folder_path)
    parent_folder_name = os.path.basename(os.path.dirname(folder_path))
    
    output_file_path = os.path.join(os.path.dirname(folder_path), 'test.txt')
    
    try:
        filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and is_image_file(f)]
        
        formatted_filenames = [f"{folder_name}/{filename}" for filename in filenames]
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for formatted_filename in formatted_filenames:
                file.write(f"{formatted_filename}\n")
        
        print(f"save:{output_file_path}")
    except FileNotFoundError:
        print("no path")
    except PermissionError:
        print("error")

folder_path ='./data/test/test'
write_formatted_filenames_to_txt(folder_path)
