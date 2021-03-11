from convectors.ppm import _PPM
name = 'test-images/test.ppm'

_ppm_converter = _PPM('test')
_ppm_image = _ppm_converter.read(name)
_ppm_image = _ppm_converter.clean(_ppm_image)

image = _ppm_converter.data(_ppm_image)

print(image.width)
print(image.height)
print(image.pixel_map)

