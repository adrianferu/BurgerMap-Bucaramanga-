#Función para extraer coordenadas
#--- The followinf packages are used for geospatial analysis
import requests
import json
import pandas as pd

 # type: ignore

def read_instantDataScrapper(route):
    '''
    This function will read the csv file from the route and return a pandas dataframe.
    The input is the route of the file.
    The output is a pandas dataframe.
    '''
    df = pd.read_csv(route)
    return df

def read_GoogleMapsScrapper(route):
    '''
    This function will read the excel file from the route and return a pandas dataframe.
    The input is the route of the file.
    The output is a pandas dataframe.
    '''
    df = pd.read_excel(route)
    return df


def get_coord(Address,YOUR_API_KEY):
    '''
    This function will return the clean address, latitude and longitude of a given address.
    The input is the address and the API key.
    The output is a list with the clean address, latitude and longitude.
    If the address is not found, the function will return ['NotFound','NA','NA']
        ''' 

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


def get_score_range(score):
    '''
    This function will return the range of the score.
    The input is the score.
    The output is the range of the score.
    '''
    if score >= 4.5:
        result = '4.5-5.0'
    elif score >= 4.0 and score < 4.5:
        result = '4.0-4.5'
    else:
        result = '< 4.0'
    return result