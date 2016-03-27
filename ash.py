from colorfinder import ColorFinder
import os

samples = ['Shirt1R', 'Shirt2R', 'Shirt3R',
           'Shirt1G', 'Shirt2G', 'Shirt3G',
           'Shirt1B', 'Shirt2B', 'Shirt3B',

           'Skirt1R', 'Skirt2R', 'Skirt3R',
           'Skirt1G', 'Skirt2G', 'Skirt3G',
           'Skirt1B', 'Skirt2B', 'Skirt3B',

           'Short1R', 'Short2R', 'Short3R',
           'Short1G', 'Short2G', 'Short3G',
           'Short1B', 'Short2B', 'Short3B',

           'Jeans1R', 'Jeans2R', 'Jeans3R',
           'Jeans1G', 'Jeans2G', 'Jeans3G',
           'Jeans1B', 'Jeans2B', 'Jeans3B'
           ]



def generateMetaData():


    samples_path = os.path.join(os.path.dirname(__file__), 'samples')

    a = {}

    for sample in samples:
        fp = open(os.path.join(samples_path, sample))
        ColorFinder().find(fp, color_space='Adobe', html_output=os.path.join(samples_path, "colors_%s.html" % sample))
        fp.close()
        a[sample] =
