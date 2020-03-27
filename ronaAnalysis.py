#!/usr/bin/env python
# coding: utf-8
import requests
import bs4
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")

def ronaAnalysis():
    #get the url data using requests and beautiful soup
    url = requests.get('https://coda.io/@atc/coronavirus-2019-ncov-updates-resources/country-data-6')
    urlSoup = bs4.BeautifulSoup(url.text, features="lxml")

    #get a list of each column data
    country = urlSoup.select('[data-column-id = "c-E-YMA09Lx_"]')

    lastUpdateDate = urlSoup.select('[data-column-id = "c-cXnlNCXBHV"]')
    confirmedCases = urlSoup.select('[data-column-id = "c-ubb_Gf1NEQ"]')
    doublingRate = urlSoup.select('[data-column-id = "c-WBbk86F0ko"]')
    daysSinceCrossingThreshold = urlSoup.select('[data-column-id = "c-5z5Hfd-vNY"]')

    recovered = urlSoup.select('[data-column-id = "c-i4EEVOMVxQ"]')
    percentRecovered = urlSoup.select('[data-column-id = "c-BYew3BSK4f"]')

    deaths = urlSoup.select('[data-column-id = "c-OduUQXvRBG"]')
    mortalityRate = urlSoup.select('[data-column-id = "c-OduUQXvRBG"]')
    casesPerMillion = urlSoup.select('[data-column-id = "c-36sbn16euR"]')

    totalTests = urlSoup.select('[data-column-id = "c-lYaPEb4xut"]')
    testsPerMillion = urlSoup.select('[data-column-id = "c-_dR2mFoZBb"]')
    positivityRate = urlSoup.select('[data-column-id = "c-qUJQUJGaG6"]')

    #create a list of dictionaries for each row
    data = []
    for i in range(2, len(country)):
        dictionary = {}
        dictionary['Country'] = country[i].getText()
        dictionary['Last Update Date'] = lastUpdateDate[i].getText()
        dictionary['Confirmed Cases'] = confirmedCases[i].getText()
        dictionary['Doubling rate'] = doublingRate[i].getText()
        dictionary['Days since crossing threshold'] = daysSinceCrossingThreshold[i].getText()
        dictionary['Recovered'] = recovered[i].getText()
        dictionary['Recovered %'] = percentRecovered[i].getText()
        dictionary['Deaths'] = deaths[i].getText()
        dictionary['Mortality Rate'] = mortalityRate[i].getText()
        dictionary['Cases per million'] = casesPerMillion[i].getText()
        dictionary['Total tests'] = totalTests[i].getText()
        dictionary['Tests per million'] = testsPerMillion[i].getText()
        dictionary['Positivity rate'] = positivityRate[i].getText()
        
        data.append(dictionary)
    
    #convert list to json
    data_json = json.dumps(data)

    return (data_json)

if __name__ == '__main__':
    app.run(debug=True)

