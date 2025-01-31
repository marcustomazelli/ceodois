
#importações flask: classe principal p criar aplicação/ request: para receber requisições/ jsonify: para retornar json/ render_template: para renderizar páginas html
from flask import Blueprint, request, jsonify, render_template

calculadora_app = Blueprint('calculadora_app', __name__)

# Rota para renderizar a página da calculadora
@calculadora_app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

# Função para calcular a emissão de CO2
def calcular_emissao_co2(litros_combustivel, energia_gasta, gas, etanol, diesels10, diesels500,onibus):
    co2_por_litro = 2.3
    co2_por_kwh = 0.233
    co2_por_gaskg = 2.5  
    co2_por_etanol = 1.51
    co2_por_diesels10 = 2.68
    co2_por_diesels500 = 2.68
    co2_km_onibus = 1.3 
   
    
    emissao_combustivel = litros_combustivel * co2_por_litro
    emissao_energia = energia_gasta * co2_por_kwh
    emissao_gas = gas * co2_por_gaskg
    emissao_etanol = etanol * co2_por_etanol
    emissao_diesels10 = diesels10 * co2_por_diesels10
    emissao_diesels500 = diesels500 * co2_por_diesels500
    emissao_onibus = onibus * 30 * (co2_km_onibus / 25) #Usuário anda x km por dia de ônibus (lotação média: 25 passageiros) * 30 dias


    emissao_total = emissao_combustivel + emissao_energia + emissao_gas + emissao_etanol + emissao_diesels10 + emissao_diesels500 + emissao_onibus 
    return emissao_total

# Função para calcular a quantidade de árvores necessárias para compensar a emissão de CO2
def calcular_arvores_necessarias(emissao):
    co2_por_arvore = 25 / 12
    arvores_necessarias = emissao / co2_por_arvore
    return arvores_necessarias

# Função para calcular o derretimento polar
def calcular_derretimento_polar(emissao):
    gelo_derretido_mcubico = emissao/1000 * 0.00034 #Um estudo de 2019 da Nature Communications estimou que para cada tonelada de CO₂ emitida, aproximadamente 0,00034 metros quadrados de gelo
    gelo_derretido_litros = gelo_derretido_mcubico * 1000
    gelo_derretido_litros = gelo_derretido_litros * 12 #12 meses

    return gelo_derretido_litros

def calcular_km_percorrido(emissao):
    co2_por_litro_gasolina = 2.3  # kg de CO2 por litro de gasolina
    eficiencia_carro = 12  # km por litro carro economico

    litros_gasolina_equivalentes = emissao / co2_por_litro_gasolina
    km_equivalentes = litros_gasolina_equivalentes * eficiencia_carro

    return km_equivalentes

def calcular_desmatamento(emissao):
    kgm2_desmatado = 65 # 65kg de CO2 equivale a 1m2 de desmatamento
    desmatamento = emissao / kgm2_desmatado

    return desmatamento

# Rota para calcular a emissão de CO2
@calculadora_app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Captura o JSON enviado pelo cliente
        data = request.get_json()
        print(f"Dados recebidos: {data}")  # Log para depuração

        # Validação e conversão de dados
        litros_combustivel = float(data.get('litros_combustivel', 0))
        energia_gasta = float(data.get('energia_gasta', 0))
        gas = float(data.get('gas', 0))
        etanol = float(data.get('etanol', 0))
        diesels10 = float(data.get('diesels10', 0))
        diesels500 = float(data.get('diesels500', 0))
        onibus = float(data.get('onibus', 0))


        # Calcula a emissão total de CO2
        emissao = calcular_emissao_co2(litros_combustivel, energia_gasta, gas, etanol, diesels10, diesels500, onibus)
        print(f"Emissão calculada: {emissao} kg")  # Log para depuração

        # Função para calcular a quantidade de árvores necessárias para compensar a emissão de CO2
        arvores = calcular_arvores_necessarias(emissao)

        # Função para calcular o derretimento polar
        derretimento = calcular_derretimento_polar(emissao)
        
        # Função para calcular a quantidade de km percorridos
        km = calcular_km_percorrido(emissao)

        desmatamento = calcular_desmatamento(emissao)

        # Log para depuração
        print(f"Retornando: emissao={round(emissao, 2)}, arvores={round(arvores, 2)}, derretimento={round(derretimento, 2)}, km={round(km, 2)}, desmatamento={round(desmatamento, 2)}")

        # Retorna o resultado como JSON
        return jsonify({'emissao': round(emissao, 2), 'arvores': round(arvores, 0), 'derretimento': round(derretimento, 2), 'km': round(km, 0), 'desmatamento': round(desmatamento, 2)})

    except ValueError as ve:
        print(f"Erro de conversão de valores: {ve}")
        return jsonify({'error': 'Os dados enviados devem ser números válidos.'}), 400

    except Exception as e:
        print(f"Erro geral: {e}")
        return jsonify({'error': 'Erro ao processar a solicitação.'}), 500
