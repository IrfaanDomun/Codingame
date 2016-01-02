import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def distance(longitude, latitude):
    x = (longitude - lon)*math.cos((lat+latitude)/2)
    y =(latitude - lat)
    return math.sqrt(x**2+y**2)*6371
    
lon = raw_input()
lat = raw_input()
#print  >> sys.stderr, lon,lat,type(lon)
lon = float(lon.replace(",","."))
lat= float(lat.replace(",","."))
n = int(raw_input())
dict= {}
for i in xrange(n):
    defib = raw_input().split(";")
#    print >> sys.stderr, defib#.split(";")
    lon_temp = float(defib[-2].replace(",","."))
    lat_temp = float(defib[-1].replace(",","."))
    dict[defib[1]] = distance(lon_temp,lat_temp)
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr,min(dict,key=dict.get),dict[min(dict,key=dict.get)]

print min(dict,key=dict.get)
