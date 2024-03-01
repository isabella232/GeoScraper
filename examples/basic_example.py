import os
from pprint import pprint

from GeoScraper import GeoScraper


XML_FNAME = os.path.join(os.path.dirname(__file__),
                         'map.osm')


if __name__ == '__main__':
    scraper = GeoScraper()
    
    # print('=' * 50)
    # print('Using file:')
    # print('=' * 50)
    # scraper.from_file(XML_FNAME)
    # pprint(scraper.highways()[:3])
    # print('\n')
    
    print('=' * 50)
    print('Using bbox:')
    print('=' * 50)
    scraper.from_bbox(left   = -84.0958000,
                      bottom =  39.7617000,
                      right  = -84.0484000,
                      top    =  39.7823000)
    pprint(scraper.highways()[:3])
    print('\n')
    print('=' * 50)
    print('Done')
    print('=' * 50)