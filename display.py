# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
from concurrent import futures
import grpc
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 160
PIXEL_WIDTH = 16
PIXEL_HEIGHT = 10

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

display = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
           [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17],
           [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
           [64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49],
           [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
           [96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],
           [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
           [128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113],
           [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
           [160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145]]

colors = [[Adafruit_WS2801.RGB_to_color(255, 255, 255) for y in range(PIXEL_HEIGHT)] for x in range(PIXEL_WIDTH)]


def main():
    initialisation(pixels, display, colors)


def initialisation(pixels, display, colors):
    # Clear all the pixels to turn them off.
    pixels.clear()
    for y in range(PIXEL_HEIGHT):
        for x in range(PIXEL_WIDTH):
            pixels.set_pixel(display[y][x] - 1, colors[x][y])
            # print "Display wert: {}".format(display[y][x] - 1 )
            # print "DisplayColor wert: {}".format(colors[x][y])
    pixels.show()  # Make sure to call show() after changing any pixels!


if __name__ == "__main__":
    main()
