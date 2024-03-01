import os
from pprint import pprint

from GeoScraper import GeoScraper


USE_BBOX  = True
USE_FILE  = True
USE_URL   = True

XML_FNAME = os.path.join(os.path.dirname(__file__), 'map.osm') # YOU MAY NEED TO CHANGE THIS LINE!
BBOX = [-84.0958000, # left
         39.7617000, # bottom
        -84.0484000, # right
         39.7823000] # top
URL = r'https://api.openstreetmap.org/api/0.6/map?bbox=-84.0958000,39.7617000,-84.0484000,39.7823000'


if __name__ == '__main__':
    scraper = GeoScraper()
    
    if USE_FILE:
        print('=' * 50)
        print('Using file:')
        print('=' * 50)
        scraper.from_file(XML_FNAME)
        pprint(scraper.highways()[:3])
        print('\n')
    
    if USE_BBOX:
        print('=' * 50)
        print('Using bbox:')
        print('=' * 50)
        scraper.from_bbox(left   = BBOX[0],
                          bottom = BBOX[1],
                          right  = BBOX[2],
                          top    = BBOX[3])
        pprint(scraper.highways()[:3])
        print('\n')
        print('=' * 50)
        print('Done')
        print('=' * 50)
    
    if USE_URL:
        print('=' * 50)
        print('Using url:')
        print('=' * 50)
        scraper.from_url(URL)
        pprint(scraper.highways()[:3])
        print('\n')
        print('=' * 50)
        print('Done')
        print('=' * 50)