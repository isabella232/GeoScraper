import os

from simplekml import Kml, Color
from GeoScraper import GeoScraper


if __name__ == '__main__':
    scraper = GeoScraper()
    scraper.from_bbox(left   = -84.0958000,
                      bottom =  39.7617000,
                      right  = -84.0484000,
                      top    =  39.7823000)
    
    KML_FNAME = r'osm_example.kml'
    
    kml = Kml(name=KML_FNAME, open=1)
    
    kml_roads        = kml.newmultigeometry(name='roads')
    kml_power_lines  = kml.newmultigeometry(name='power_lines')
    kml_sub_stations = kml.newmultigeometry(name='sub_stations')
    
    for road in scraper.highways():
        kml_roads.newlinestring(coords=road['coords'])
    
    for power in scraper.power_locations():
        if 'line' in power['tag_vals']:
            kml_power_lines.newlinestring(coords=power['coords'])
            
        elif 'substation' in power['tag_vals']:
            kml_sub_stations.newpolygon(outerboundaryis=power['coords'])
    
    kml_roads.style.linestyle.color        = Color.black
    kml_roads.style.linestyle.width        = 2
    kml_power_lines.style.linestyle.color  = Color.red
    kml_power_lines.style.linestyle.width  = 2
    kml_sub_stations.style.polystyle.color = Color.orange
    
    kml.save(KML_FNAME)
    os.system(KML_FNAME)