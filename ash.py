from colorfinder import ColorFinder
import os

samples = [

	   'Red-Shirt',
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

    cf = ColorFinder('colorchecker')


    samples_path = os.path.join(os.path.dirname(__file__), 'samples')


    for sample in samples:
        fp = open(os.path.join(samples_path, sample))
        a[sample] = cf.find(fp)
        fp.close()

    return a    
