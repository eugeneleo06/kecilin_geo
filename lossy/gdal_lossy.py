import os

quality = [95,90,85,80,75]
for q in quality:
    os.system(f'gdal_translate -of JPEG -co "QUALITY={q}" lossy/input.TIF lossy/output_{q}.jpg')
    os.system(f'gdal_translate -of JP2OpenJPEG -co "QUALITY={q}" lossy/input.TIF lossy/output_{q}.jp2')
    os.system(f'gdal_translate -of WEBP -co "QUALITY={q}" lossy/input.TIF lossy/output_{q}.webp')
