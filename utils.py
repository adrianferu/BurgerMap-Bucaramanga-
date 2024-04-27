#Función para extraer coordenadas
#--- The followinf packages are used for geospatial analysis
import requests
import json

 # type: ignore

def get_coord(Address,YOUR_API_KEY): 

    api_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={Address}&key={YOUR_API_KEY}'
    try:
        j = requests.get(api_url).json()
        CleanAddress = str(j['results'][0]['formatted_address']).upper()
        LAT = j['results'][0]['geometry']['location']['lat']
        LON = j['results'][0]['geometry']['location']['lng']
        results = [CleanAddress,round(LAT,7),round(LON,7)]
    except:
        results = ['NotFound','NA','NA']
    return results 


#We will create a function based on the score column. The syntax will be the following:
#if score >= 4.5, then result will be '45.-5.0'
#if score >=4.0 and <4.5, then result will be '4.0-4.5'
#if score <4.0. then result will be '< 4.0'
def get_score_range(score):
    if score >= 4.5:
        result = '4.5-5.0'
    elif score >= 4.0 and score < 4.5:
        result = '4.0-4.5'
    else:
        result = '< 4.0'
    return result