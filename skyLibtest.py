from skyfield.api import Star, load
from astropy.coordinates import SkyCoord
from astropy import units as u
from skyfield.data import hipparcos
import math

#the coordinates are in degrees
def starToXYZCoords(ra, dec, distToearh):
    R=distToearh

    #convert to radians
    ra=math.radians(ra)
    dec=math.radians(dec)

    x=R*math.cos(ra)*math.cos(dec)
    y=R*math.sin(ra)*math.cos(dec)
    z=R*math.sin(dec)
    return x,y,z

def distanceBetweenTwoStars(ra1,ra2,dec1,dec2, dte1,dte2):
    x1,y1,z1=starToXYZCoords(ra1,dec1, dte1)
    x2,y2,z2=starToXYZCoords(ra2,dec2, dte2)
    D=math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(z2-z1,2)
    res=math.sqrt(D)
    return res


def angulardistanceTwoStars(ra1, ra2, dec1, dec2):
    ra1 = math.radians(ra1)
    dec1 = math.radians(dec1)
    ra2 = math.radians(ra2)
    dec2 = math.radians(dec2)

    a=math.sin(dec1)*math.sin(dec2)+math.cos(dec1)*math.cos(dec2)*math.cos(ra1-ra2)

    res=math.acos(a)
    res=math.degrees(res)
    return res

with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)
    df = df[df['ra_degrees'].notnull()]
    df = df[df['magnitude'] <= 5]
    #df=df[df['ra_degrees']<15]
    #df = df[df['ra_degrees'] >10 ]

    print('After filtering, there are {} stars'.format(len(df)))


ts = load.timescale()
t = ts.now()
planets = load('de421.bsp')
earth = planets['earth']

#betelguice
#betelguice_star = Star.from_dataframe(df.loc[27989])

#vega
#vega_star = Star.from_dataframe(df.loc[91262])
#astrometric = earth.at(t).observe(vega_star)

#c = SkyCoord('00 42 30 +41 12 00', unit=(u.hourangle, u.deg))

# ra, dec, distance = astrometric.radec()
# print(ra.hours)
# print("vega", ra.hours*15, dec.degrees, distance)

stars_ra=[]
stars_dec=[]
#big bear constellation
#Dubhe
d_star = Star.from_dataframe(df.loc[54061])
a1 = earth.at(t).observe(d_star)
ra, dec, distance = a1.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)

#Merek
me_star = Star.from_dataframe(df.loc[53910])
a2 = earth.at(t).observe(me_star)
ra, dec, distance = a2.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)

#Phecda
ph_star = Star.from_dataframe(df.loc[58001])
a3 = earth.at(t).observe(ph_star)
ra, dec, distance = a3.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)


#uma
uma_star = Star.from_dataframe(df.loc[59774])
a4 = earth.at(t).observe(uma_star)
ra, dec, distance = a4.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)

#kochab
ko_star = Star.from_dataframe(df.loc[72607])
a5 = earth.at(t).observe(ko_star)
ra, dec, distance = a5.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)

#Alioth
al_star = Star.from_dataframe(df.loc[62956])
a6 = earth.at(t).observe(al_star)
ra, dec, distance = a6.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)

#Mizar
mi_star = Star.from_dataframe(df.loc[65378])
a7 = earth.at(t).observe(mi_star)
ra, dec, distance = a7.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)


#Alkaid
alk_star = Star.from_dataframe(df.loc[67301])
a8 = earth.at(t).observe(alk_star)
ra, dec, distance = a8.radec()
stars_ra.append(ra.hours*15)
stars_dec.append(dec.degrees)


bright_stars = Star.from_dataframe(df)
#
# t = ts.utc(2018, 9, 3)
#astrometric = earth.at(t).observe(bright_stars)
#ra, dec, distance = astrometric.radec()
#
# print('There are {} right ascensions'.format(len(ra.hours)))
# print('and {} declinations'.format(len(dec.degrees)))

sirius=[101.2870833,-16.7161111]
#print(101.2870833/15)
#vega=[279.2345833,38.7836111, 25.3]

# print(distance.au)
# vega=[ra.hours*15, dec.degrees]

#sirius_vega_d=distanceBetweenTwoStars(sirius[0], vega[0],sirius[1], vega[1],sirius[2],vega[2])
#sirius_vega_d=angulardistanceTwoStars(sirius[0], vega[0],sirius[1], vega[1])
#print(math.degrees(sirius_vega_d))

#print(starToXYZCoords(sirius[0],sirius[1]))
#print(starToXYZCoords(vega[0],vega[1]))
#print(sirius_vega_d)


from matplotlib import pyplot as plt
#plt.scatter(ra.hours, dec.degrees,8- df['magnitude'], 'k')
plt.scatter(stars_ra, stars_dec,8- df['magnitude'], 'k')
#plt.xlim(50, 65)
#plt.ylim(30, 70)
#plt.savefig('bright_stars.png')
plt.show()

for i in range(8):
    for j in range(i+1,8):
        d= angulardistanceTwoStars(stars_ra[i], stars_ra[j], stars_dec[i], stars_dec[j])
        print(d)


for i in range(len(stars_ra)):
    print(stars_ra[i], stars_dec[i])