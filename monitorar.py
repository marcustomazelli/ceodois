
from flask import Blueprint, render_template, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
print(f'MAP_KEY: {API_KEY}')


monitorar_app = Blueprint('monitorar_app', __name__)

@monitorar_app.route('/monitorar')
def qualidade_ar():
    return render_template('monitorar.html')

# now let's check how many transactions we have
import pandas as pd

url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=%s' % API_KEY
try:
  df = pd.read_json(url,  typ='series')
  print(df)
except:
  # possible error, wrong MAP_KEY value, check for extra quotes, missing letters
  print ("There is an issue with the query. \nTry in your browser: %s" % url)

# Rota para pegar os dados da API FIRMS
@monitorar_app.route('/api/queimadas', methods=['GET'])
def queimadas():
    # URL da API FIRMS para os últimos 2 dias de dados MODIS para o Brasil
    brazil_url = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/%s/VIIRS_NOAA21_NRT/BRA/2' % API_KEY

    df_brazil = pd.read_csv(brazil_url)

    json_brazil = df_brazil.to_dict(orient='records')  # Transforma diretamente em lista de dicionários 
    
    # Retornar os dados como resposta JSON
    return jsonify(json_brazil)
