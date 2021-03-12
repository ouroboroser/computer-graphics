from convectors.ppm import _PPM
from convectors.bmp import _BMP

ppm_name = 'test-images/test.ppm'

_ppm_converter = _PPM('test-ppm')
_ppm_image = _ppm_converter.read(ppm_name)
_ppm_image = _ppm_converter.clean(_ppm_image)

image = _ppm_converter.data(_ppm_image)

#print(image.width)
#print(image.height)
#print(image.pixel_map)

bmp_name = 'test-images/bmp/test2.bmp'

_bmp_converter = _BMP('test-bmp')
_bmp_image = _bmp_converter.read(bmp_name)

#print(_bmp_image.width)
#print(_bmp_image.height)

#print(_bmp_image.pixel_map)

#for row in _bmp_image.pixel_map:
#    print(row)

_to_P3 = _ppm_converter.write(_bmp_image)