# Candlestick Charts to CSV

This package converts stock market candlestick charts to CSV.
In brief, this is how the whole procedure will be look like:

1- Download (or screenshot) the candlestick charts and save them all in one folder. The image types that their pixel values have been manipulated (such as .jpg) are not suitable. .png and .bmp are the best options.
2- The name of the files should have a number which represents the date order of the images. For example, the image showing the results from 01-01-2009 to 01-04-2009 is named img-1 , the one showing 01-04-2009 to 01-07-2009 is named img-2, and so on. The time overlaps between the adjacent images does not matter, the code will handle it.
3- Run the code and it reads all the images and then outputs one .csv file including data for the whole time span of images.

Note that the code needs to be calibrated, mostly based on the RGB colors used in the image. So if you go to another stock market broker the code needs to be changed slightly. You can adjust the appropriate RGB colors in line 143 of the code.
Obviously, the numerical results of the code is not 100% accurate. The deviation depends on the size of the images. For 1366x615 pixel images the deviation is less than 0.02%.

Any customization is available based on different requirement. For example modifying the code to read and include the volumes, or populating the database with the results.

Kian.

Copy this into your command line to install: "pip install git+https://github.com/KianML/candlestick_to_csv#egg=candlestick_to_csv"
