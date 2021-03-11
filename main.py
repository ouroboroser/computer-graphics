from convectors.ppm import _PPM
from convectors.image import _IMAGE

name = 'test-images/test.ppm'

_ppm_converter = _PPM('test')
_ppm_image = _ppm_converter.read(name)
_ppm_image = _ppm_converter.clean(_ppm_image)

#size = _ppm_converter.get_header(_ppm_image)

#print('size: ', size)

for row in _ppm_image:
    print(row)

