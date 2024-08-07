# font2bytes

Python script to create new fonts for WaveShare epaper / e-ink [EPS32 module]

Rational
-------------------

I am super happy of my e-ink display from Waveshare, but their library only offers basic fonts types, and only 5 fonts sizes (font8, font12, font16, font20 and font24). This is unfortunately very limiting :(

This python script is inspired by the waveshare blogpost [this](https://wavesharejfs.blogspot.com/2018/08/make-new-larger-font-for-waveshare-spi.html). But they do not provide any code to use...

On the other hand the font2bytes from [Dominik Kapusta](https://github.com/ayoy/font2bytes/tree/master) is available but requires C++ compilers.

This is my version made in python.
At this moment it only recreates ASCII caracters, but you can use any font and specify any size.
(just make sure that it will fit your epaper display)


Requirements
-------------------
* Python 3
* [Pillow](https://pillow.readthedocs.io/en/stable/index.html#) library  (NOTE: Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.)
* [numpy](https://numpy.org/install/) library


Use
-------------------
1. drop any font you want to use (.tff) within the ./fonts folder within the font2bytes.py

2. specify a new name for the font to create

3. specify the font name that you want to use (default is roboto-Regular)

4. specify the height and the width of the new font. 

5. run the python script


The python script will generate the new .cpp file within the ./output folder with the desired name

within the waveshare library source folder (Arduino\libraries\esp32-waveshare-epd\src)

6. add the new .cpp font file

7. open the fonts.h and

8. add a new "extern" line with the name of the new font

    E.g.: extern sFONT FontBold40;

9. [OPTIONAL] make sure that the defined MAX_HEIGHT_FONT and MAX_WIDTH_FONT are equal or smaller that the new font size. Update the values if required

10. Use the new font in your script and enjoy!

    E.g. Paint_DrawString_EN(5, 0, "waveshare Electronics", &FontBold40, BLACK, WHITE);


Examples
-------------------
within the ./output folder there are already a couple of .cpp files that can be used without running the oython code.
Just follow the instructions from the 6th step


Author
-------------------
TheHeXstyle

License
-------------------
LGPL v3.0, see LICENSE for details.
