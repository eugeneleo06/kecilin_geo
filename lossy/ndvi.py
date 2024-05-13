import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the GeoTIFF file
file_path_red = 'lossy/input_band4.TIF'
file_path_nir = 'lossy/input_band5.TIF'
with rasterio.open(file_path_red) as red:
    # Step 2: Read data from the red band
    red_data = red.read(1).astype('float64')  # Ensure data is in float64 to avoid data type issues

with rasterio.open(file_path_nir) as nir:
    # Read data from the NIR band
    nir_data = nir.read(1).astype('float64')

# Step 3: Calculate NDVI
ndvi = (nir_data - red_data) / (nir_data + red_data)

# Handle division by zero
ndvi[np.isnan(ndvi)] = 0

# Step 4: Visualize NDVI
plt.figure(figsize=(10, 6))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()
plt.title('NDVI Image')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
plt.show()
