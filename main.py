import os 
import numpy as np 
import sys 
import json 
from geojson import Feature, Point, FeatureCollection 

def toGEOJSON(data):
    featureColl = []
    for d in data:
        props = {}
        for k, v in d.iteritems():
            if k != 'Lat' and k != 'Long':
                props[k] = v
        featureColl.append(Feature(
            geometry = Point((
                d['Long'], d['Lat']
            )),
            properties = props
        ))
    return FeatureCollection(featureColl) 

def writeGEOJSON(data):
    with open('public/geojson/data.geojson', 'w') as f:
        json.dump(data, f, indent=2)

def main():
    with open('public/json/data.json', 'rb') as f:
        dataDict = json.load(f)
    geoData = toGEOJSON(dataDict)
    writeGEOJSON(geoData)

    

if __name__ == '__main__':
    main()