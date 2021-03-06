# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
from concurrent import futures
import grpc
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

import display_server_pb2
import display_server_pb2_grpc

# Configure the count of pixels:
PIXEL_COUNT = 160
PIXEL_WIDTH = 16
PIXEL_HEIGHT = 10

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

updateDisplay = 0

# colors
white = Adafruit_WS2801.RGB_to_color(255, 255, 255)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

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

colors = [[white for y in range(PIXEL_WIDTH)] for x in range(PIXEL_HEIGHT)]

class GRPC_Server(display_server_pb2_grpc.WS2801_DisplayServicer):



    def DISPLAY_CHANGE(self, request, context):

        global updateDisplay

        print "Received DISPLAY Change."
        print "Versionsnummer: {}".format(request.version)
        print "Typ: {}".format(request.typ)
        print "Dimension X: {}".format(request.dim_x)
        print "Dimension Y: {}".format(request.dim_y)

        #print request.pixel_list
        pixel_color = request.pixel_list.split(", ")
	    print "DISPLAY_CHANGE() - pixel_color: " + str(pixel_color)

        for x in range(PIXEL_COUNT):
            #print pixel_color[x]
            pixel_color[x]=int(pixel_color[x])

            green = pixel_color[x] & 255
            blue = pixel_color[x] >> 8 & 255
            red = pixel_color[x] >> 16 & 255

	    print "(" + str(green) + ", " + str(blue) + ", " + str(red) + ")"

            pixel_color[x] = Adafruit_WS2801.RGB_to_color(red,blue,green)
	    print "pixel_color after Adafruit conv: " + str(pixel_color)

        for y in range(PIXEL_HEIGHT):
            for x in range(PIXEL_WIDTH):
		print "x: " + str(x) + ", y:" + str(y)
                colors[y][x] = pixel_color[x + (y * PIXEL_WIDTH)]

        print "DISPLAY_CHANGE() - colors:"
	print colors
        updateDisplay = 1

	update(pixels, display, colors)

        ###### Handle msg into display
        return display_server_pb2.DISPLAY_RESPONSE()

def main():
    initialisation(pixels, display, colors)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    display_server_pb2_grpc.add_WS2801_DisplayServicer_to_server(GRPC_Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(5)
#            if updateDisplay is 1:
#               update(pixels, display, colors)
            print "Tick"
    except KeyboardInterrupt:
        server.stop(0)


def initialisation(pixels, display, colors):
    # Clear all the pixels to turn them off.
    pixels.clear()
    #for y in range(PIXEL_HEIGHT):
    #    for x in range(PIXEL_WIDTH):
    #        pixels.set_pixel(display[y][x] - 1, colors[x][y])
            # print "Display wert: {}".format(display[y][x] - 1 )
            # print "DisplayColor wert: {}".format(colors[x][y])
    pixels.show()  # Make sure to call show() after changing any pixels!

def update(pixels, display, colors):
    print "update() - colors: " #+ colors
    print colors

    for y in range(PIXEL_HEIGHT):
	for x in range(PIXEL_WIDTH):
		pixels.set_pixel(display[y][x] - 1, colors[y][x])

    print "update() - pixels:"
    print pixels
    pixels.show()

if __name__ == "__main__":
    main()
