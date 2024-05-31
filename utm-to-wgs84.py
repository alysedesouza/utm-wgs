from pyproj import Transformer
import sys
import json

def convert_utm_to_wgs84(zone, easting, northing):
    source_crs = 7800 + zone
    destination_crs = 4326

    transformer = Transformer.from_crs(source_crs, destination_crs)
    transformed_point = transformer.transform(easting, northing)
    
    return transformed_point

if __name__ == "__main__":
    zone = int(sys.argv[1])
    easting = float(sys.argv[2])
    northing = float(sys.argv[3])

    latitude, longitude = convert_utm_to_wgs84(zone, easting, northing)
    result = {'latitude': latitude, 'longitude': longitude}
    print(json.dumps(result))
