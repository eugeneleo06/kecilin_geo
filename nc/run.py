import netCDF4 as nc

# Path to the original NetCDF file
original_file_path = 'nc/ESRL-GMD-AEROSOL_v1.0_HOUR_BRW_s20150101T000000Z_e20160101T000000Z_c20170926T205812Z.nc'
# Path to the compressed NetCDF file
compressed_file_path = 'nc/data.nc'

# Open the original NetCDF file
with nc.Dataset(original_file_path, 'r') as src:
    # Create a new NetCDF file for the compressed output
    with nc.Dataset(compressed_file_path, 'w', format='NETCDF4') as dst:
        # Copy global attributes from source to destination
        dst.setncatts(src.__dict__)
        
        # Copy dimensions
        for name, dimension in src.dimensions.items():
            dst.createDimension(
                name, (len(dimension) if not dimension.isunlimited() else None))
        
        # Copy and compress variables
        for name, variable in src.variables.items():
            # Create the variable in the destination file
            # Compression settings: zlib=True, complevel=4, shuffle=True
            new_var = dst.createVariable(name, variable.datatype, variable.dimensions,
                                         zlib=True, complevel=4, shuffle=True)
            # Copy variable attributes
            new_var.setncatts(variable.__dict__)
            # Copy the data into the new variable
            new_var[:] = variable[:]

print(f"Compressed file created at {compressed_file_path}")
