from colorfinder import ColorFinder
import os

samples = ['Red-Shirt',
           'Green-tshirt',
           'Blue-Tshirt',

           'Red-Skirt',
           'Green-Skirt',
           'Blue-Skirt',

           'Red-Short',
           'Green-Short',
           'Blue-Short',

           'Red-Jeans',
           'Green-Jeans',
           'Blue-Jeans'
           ]



def generateMetaData():


    samples_path = os.path.join(os.path.dirname(__file__), 'samples')

    a = {}

    for sample in samples:
        fp = open(os.path.join(samples_path, sample))
        ColorFinder().find(fp, color_space='Adobe', html_output=os.path.join(samples_path, "colors_%s.html" % sample))
        fp.close()
        a[sample] =
