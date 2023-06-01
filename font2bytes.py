from PIL import Image, ImageDraw, ImageFont
from numpy import asarray, ceil, array, sum, concatenate

filename = 'FontReg36'              #<----- select new font name
fontname = 'Roboto-Regular.ttf'     #<----- specify the font the you intend to use. Place any font into the fonts folder
height = 36                     #<----- new font height
width = 22                       #<----- new fonr width
THRESHOLD = 190                  #<----- image intensity threshold for binary conversion. It changes the contrast of the final font


font_offset = 4  # recommended to be at least 4
binary_byte = array([128, 64, 32, 16, 8, 4, 2, 1])

def createTMPimage(ASCII):

    # TODO better center the position of the letter within the image

    image = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(f"./fonts/{fontname}", height - font_offset)
    draw.text((0, 0), chr(ASCII), font=font)
    image.save(f'./tmp/{ASCII}.bmp')


def readImage2Binary(ASCII):

    image = Image.open(f'./tmp/{ASCII}.bmp')
    data = asarray(image)
    binary_map = data[:, :, 0]
    return binary_map


def convertMap2Hex(binary_map):

    hex_map = []
    for line in range(binary_map.shape[0]):
        for bit_chunks in range(int(ceil(width/8))):
            tmp = binary_map[line][bit_chunks*8:(min((bit_chunks+1)*8, width))]
            tmp = array(list(map(lambda x: int(x > THRESHOLD), tmp)))
            tmp = concatenate((array([0] * (8 - len(tmp))), tmp))  # padding with zeros
            binary_value = int(sum(tmp * binary_byte))
            hex_map.append(f"{binary_value:#0{4}x}")

    return hex_map


def write_file_intro(f):

    f.write('/* Includes ------------------------------------------------------------------*/\n')
    f.write('#include "fonts.h"\n')
    f.write(f'const uint8_t Font{height}_Table [] = \n')
    f.write('{\n')


def write_file_closure(f):

    f.write('};\n\n')
    f.write(f'sFONT Font{height} = {{\n')
    f.write(f'\tFont{height}_Table,\n')
    f.write(f'\t{width}, /* Width */\n')
    f.write(f'\t{height}, /* Height */\n')
    f.write('};\n\n')


def write_letter(hex_map):

    f.write(f'\t// ASCII: {ASCII} "{chr(ASCII)}" ({width} pixels wide)\n')

    count = 0
    f.write('\t')

    for item in hex_map:
        f.write(f'{item}, ')
        count += 1
        if count == 3:
            count = 0
            f.write('\n\t')

    f.write('\n')




if __name__ == "__main__":

    with open(f'./output/{filename}.cpp', 'w') as f:
        write_file_intro(f)

        for ASCII in range(32, 127):
            print(f'working on ASCII: {ASCII}: {chr(ASCII)}')

            createTMPimage(ASCII)
            binary_map = readImage2Binary(ASCII)
            hex_map = convertMap2Hex(binary_map)
            write_letter(hex_map)

        write_file_closure(f)










