from PIL import Image
import os
import shutil

# Assign directory
directory = 'source'
compressed_directory = 'resized'
compression_ratio = 1

# Ensure the compressed directory exists
if not os.path.exists(compressed_directory):
    os.makedirs(compressed_directory)

def is_image(file_path):
    try:
        # Try to open the file with Pillow
        Image.open(file_path)
        return True
    except IOError:
        # If an error occurs, it's likely not an image
        return False

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # Check if it is a file
    if os.path.isfile(f) and is_image(f): 
        try:
            im = Image.open(f)
            filename_without_ext = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1]
            
            # Resize the image
            resized_im = im.resize((round(im.size[0]*compression_ratio), round(im.size[1]*compression_ratio)))
            
            # Save the resized image
            resized_im.save(os.path.join(compressed_directory, f"{filename_without_ext}{ext}"))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
