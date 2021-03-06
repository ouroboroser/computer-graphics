from struct import unpack
from formats.image import _IMAGE

class _BMP:
    def read(self, path):
        f = open(path, "rb")
        offset = 0

        signature = unpack('<h', f.read(2))
        file_size = unpack('<i', f.read(4))

        reserved = unpack('<h', f.read(2))
        reserved = unpack('<h', f.read(2))

        bitmap_location = unpack('<i', f.read(4))

        dib_header = unpack('<i', f.read(4))
        pixel_width = unpack('<i', f.read(4))[0]
        pixel_height = unpack('<i', f.read(4))[0]
        colour_planes = unpack('<h', f.read(2))
        bytes_per_pixel = unpack('<h', f.read(2))
        compression = unpack('<i', f.read(4))

        img_size = unpack('<i', f.read(4))
        horz_resolution = unpack('<i', f.read(4))
        vert_resolution = unpack('<i', f.read(4))
        number_of_colors = unpack('<i', f.read(4))
        i_number_of_colors = unpack('<i', f.read(4))

        pixels = []
        padding = 4 - (3 * pixel_width) % 4
        if padding == 4:
            padding = 0
        for i in reversed(range(pixel_height)):
            for j in range(pixel_width):
                b = unpack('<B', f.read(1))[0]
                g = unpack('<B', f.read(1))[0]
                r = unpack('<B', f.read(1))[0]
                pixels.append([r, g, b])
            for p in range(padding):
               junk = unpack('<B', f.read(1))[0]

        image_data = _IMAGE(
            pixel_width,
            pixel_height,
            pixels
        )
        return image_data