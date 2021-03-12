from struct import unpack

def cursor(path):
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
    return pixel_width, pixel_height