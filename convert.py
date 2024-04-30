import os
import subprocess

# Define the parent folder path
parent_folder = 'data_band'

methods = ['PACKBITS', 'DEFLATE', 'LZW', 'LZMA', 'ZSTD']

# Iterate through each child folder in the parent folder
for child_folder in os.listdir(parent_folder):
    # Construct the full path of the child folder
    child_folder_path = os.path.join(parent_folder, child_folder)
    
    # Check if the path is a directory
    if os.path.isdir(child_folder_path):
        # Create a text file to store the reduction percentage for each method
        with open(os.path.join(child_folder_path, 'reduction_percentage.txt'), 'w') as f:
            # Iterate through each file in the child folder
            for file_name in os.listdir(child_folder_path):
                os.makedirs(os.path.join(child_folder_path, 'compressed'), exist_ok=True)

                # Check if the file is a .tif file
                if file_name.lower().endswith('.tif'):
                    # Construct the full path of the .tif file
                    tif_file = os.path.join(child_folder_path, file_name)
                    original_size = os.path.getsize(tif_file)
                    
                    # Iterate through each compression method
                    for method in methods:
                        output_file = os.path.join(child_folder_path, "compressed" , f'{file_name[:-4]}_{method}.TIF')
                        
                        # Define the GDAL command
                        gdal_command = f'gdal_translate -co COMPRESS={method} -co ZLEVEL=9 -co NUM_THREADS=ALL_CPUS -co TILED=YES {tif_file} {output_file}'
                        
                        # Run the GDAL command
                        try:
                            subprocess.run(gdal_command, shell=True, check=True)
                            compressed_size = os.path.getsize(output_file)
                            reduction_percentage = ((original_size - compressed_size) / original_size) * 100
                            f.write(f"File: {file_name}, Method: {method}, Reduction: {reduction_percentage:.2f}%\n")
                            print(f"Size reduction for {tif_file} with method {method}: {reduction_percentage:.2f}%")
                        except subprocess.CalledProcessError as e:
                            print(f"Error executing GDAL command on {tif_file} for method {method}: {e}")
