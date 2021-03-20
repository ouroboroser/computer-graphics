from converters.image import _IMAGE
import zlib
import struct


class _PNG:
    def __init__(self, name):
        self.name = name

    def read(self, path):
        f = open(path, 'rb')

        signature = b'\x89PNG\r\n\x1a\n'
        if f.read(len(signature)) != signature:
            raise Exception('Invalid signature!')

        def read_chunk(f):
            chunk_length, chunk_type = struct.unpack('>I4s', f.read(8))
            chunk_data = f.read(chunk_length)
            chunk_expected_crc, = struct.unpack('>I', f.read(4))
            chunk_actual_crc = zlib.crc32(chunk_data, zlib.crc32(struct.pack('>4s', chunk_type)))
            if chunk_expected_crc != chunk_actual_crc:
                raise Exception('Checksum fail!')
            return chunk_type, chunk_data

        chunks = []
        while True:
            chunk_type, chunk_data = read_chunk(f)
            chunks.append((chunk_type, chunk_data))
            if chunk_type == b'IEND':
                break

        _, IHDR_data = chunks[0]
        width, height, bitd, colort, compm, filterm, interlacem = struct.unpack('>IIBBBBB', IHDR_data)
        if compm != 0:
            raise Exception('Invalid compression method!')
        if filterm != 0:
            raise Exception('Invalid filter method!')
        if colort != 6:
            raise Exception('Only support truecolor with alpha is supported')
        if bitd != 8:
            raise Exception('The only bit depth supported is 8')
        if interlacem != 0:
            raise Exception('Interlacing is not supported')

        IDAT_data = b''.join(chunk_data for chunk_type, chunk_data in chunks if chunk_type == b'IDAT')
        IDAT_data = zlib.decompress(IDAT_data)

        def paeth_predictor(a, b, c):
            p = a + b - c
            pa = abs(p - a)
            pb = abs(p - b)
            pc = abs(p - c)
            if pa <= pb and pa <= pc:
                pr = a
            elif pb <= pc:
                pr = b
            else:
                pr = c
            return pr

        recon = []
        bytes_per_pxl = 4
        stride = width * bytes_per_pxl

        def recon_a(r, c):
            return recon[r * stride + c - bytes_per_pxl] if c >= bytes_per_pxl else 0

        def recon_b(r, c):
            return recon[(r - 1) * stride + c] if r > 0 else 0

        def recon_c(r, c):
            return recon[(r - 1) * stride + c - bytes_per_pxl] if r > 0 and c >= bytes_per_pxl else 0

        i = 0
        for r in range(height):
            filter_type = IDAT_data[i]
            i += 1
            for c in range(stride):
                filt_x = IDAT_data[i]
                i += 1
                if filter_type == 0:
                    recon_x = filt_x
                elif filter_type == 1:
                    recon_x = filt_x + recon_a(r, c)
                elif filter_type == 2:
                    recon_x = filt_x + recon_b(r, c)
                elif filter_type == 3:
                    recon_x = filt_x + (recon_a(r, c) + recon_b(r, c)) // 2
                elif filter_type == 4:
                    recon_x = filt_x + paeth_predictor(recon_a(r, c), recon_b(r, c), recon_c(r, c))
                else:
                    raise Exception('Unknown filter type: ' + str(filter_type))
                recon.append(recon_x & 0xff)

        pixels = recon
        del pixels[3::4]
        image_data = _IMAGE(
            width,
            height,
            pixels
        )
        return image_data
