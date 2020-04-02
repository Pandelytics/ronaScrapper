import pandas as pd
import html5lib
import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route("/")


def ronaAnalysis():
    totalCases = pd.read_html('http://covid19.ncdc.gov.ng/', attrs = {'id': 'custom1'})
    totalCases = totalCases[0]
    totalCases = totalCases.set_index(0)


    stateCases = pd.read_html('http://covid19.ncdc.gov.ng/', attrs = {'id': 'custom3'})
    stateCases = stateCases[0]

    stateCasesA = stateCases[["States.1", "Numbers.1"]]
    stateCasesA.rename(columns = {'States.1':'States', 'Numbers.1':'Numbers'}, inplace=True)
    stateCasesB = stateCases[["States", "Numbers"]]

    allStateCases = stateCasesB.merge(stateCasesA, how='outer', sort=True)
    allStateCases = allStateCases.set_index('States')
    allStateCases = allStateCases.drop(np.nan)

    allStateCases_json = allStateCases.to_json(orient = 'index')
    return (allStateCases_json)

if __name__ == '__main__':
	app.run(debug=True)