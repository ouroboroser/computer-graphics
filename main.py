from converters.ppm import _PPM
from converters.bmp import _BMP
from converters.png import _PNG

_ppm_converter = _PPM('test-ppm')
# bmp_name = 'test-images/bmp/test5.bmp'
print('Input .bmp file name')
bmp_name = input()

try:
    _bmp_converter = _BMP('test-bmp')
    _bmp_image = _bmp_converter.read(bmp_name)
    _to_P3 = _ppm_converter.write_from_bmp(_bmp_image)
except FileNotFoundError:
    print("Couldn't find the .bmp file specified. Invalid input data.")
except:
    print("Invalid file format")

# png_name = 'test-images/png/test1.png'
print('Input .png file name')
png_name = input()

try:
    _png_converter = _PNG('test-png')
    _png_image = _png_converter.read(png_name)
    _to_P3 = _ppm_converter.write_from_png(_png_image)
except FileNotFoundError:
    print("Couldn't find the .png file specified. Invalid input data.")
except:
    print("Invalid file format")