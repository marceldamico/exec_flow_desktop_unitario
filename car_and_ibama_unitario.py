import requests

from tkinter import *

class RequisicoesFunctions:
    def __init__(self):
        self.url_car = 'https://car.atfunctions.com/api/car/get_by_id/{codigo}/?IAMKEY=sua_chave_aqui'
        self.url_ibama = 'https://ibama.atfunctions.com/api/ibama/get_by_polygon/?IAMKEY=sua_chave_aqui' 
        

    def executa_get(self, url):
        url = url
        try: 
            resposta = requests.get(url, timeout=120)
            retorno = resposta.json()
            if resposta.status_code == 200:
                return retorno
            if resposta.status_code == 401:
                return "Status Code: {}. Message: {}".format(resposta.status_code, retorno["message"])                   
            else:
                return "Status Code: {}".format(resposta.status_code)
        except Exception as e:
            return "ERRO: {}".format(e)

    def executa_post(self, url, body):
        try: 
            resposta = requests.post(url, json = body, timeout=120)
            retorno = resposta.json()
            if resposta.status_code == 200:
                return retorno
            if resposta.status_code == 401:
                return "Status Code: {}. Message: {}".format(resposta.status_code, retorno["message"])                
            else:
                return "Status Code: {}".format(resposta.status_code)
        except Exception as e:
            return "ERRO: {}".format(e)   

    def gera_url_car_get_by_id(self, IAMKEY, id):
        url = self.url_car
        url = url.replace("sua_chave_aqui",IAMKEY)
        valor_para_replace = "{codigo}"
        url = url.replace(valor_para_replace, id)
        return url

    def gera_url_ibama_get_by_polygon(self, IAMKEY):
        url = self.url_ibama
        url = url.replace("sua_chave_aqui",IAMKEY)
        return url        

    def gera_url_ibama_get_by_point(self,IAMKEY, longitude, latitude, consult_date):
        url = self.url_ibama
        url = url.replace("sua_chave_aqui",IAMKEY)
        longitude_to_replace = "{longitude}"
        url = url.replace(longitude_to_replace, str(longitude))
        latitude_to_replace = "{latitude}"
        url = url.replace(latitude_to_replace, str(latitude))
        consult_date_to_replace = "{consult_date}"
        url = url.replace(consult_date_to_replace, consult_date)
        return url        

    def gera_body_ibama_get_by_polygon(self, wkt, epsg, consult_date):
        dicionario_request = {}
        dicionario_request["wkt"] = wkt
        dicionario_request["epsg"] = str(epsg)
        dicionario_request["consult_date"] = consult_date
        return dicionario_request

# def analise(id, consult_date):
def analise():
    mytext.insert('end', str("Iniciando o processamento") + '\n')
    frame2.update()     
    r = RequisicoesFunctions()
    id = e1.get()
    consult_date = e2.get()
    IAMKEY = e3.get()
    mytext.insert('end', str("Iniciando a consulta ao CAR") + '\n')
    frame2.update()  
    url_car = r.gera_url_car_get_by_id(IAMKEY, id)
    response_car = r.executa_get(url_car)
    mytext.insert('end', str("Concluída a consulta ao CAR") + '\n')
    frame2.update()     
    wkt = response_car['objectResult']['geom']
    url_ibama = r.gera_url_ibama_get_by_polygon(IAMKEY)
    epsg = 4326
    mytext.insert('end', str("Iniciada a consulta aos dados de Embargo do IBAMA") + '\n')
    frame2.update()    
    body_ibama = r.gera_body_ibama_get_by_polygon(wkt, epsg, consult_date)
    response_ibama = r.executa_post(url_ibama, body_ibama)
    mytext.insert('end', str("Concluída a consulta aos dados de Embargo do IBAMA") + '\n')
    frame2.update()      
    objectResult = response_ibama['objectResult']
    quantidade_de_registros = len(objectResult)
    registro = 1
    linha1 = "Quantidade de registros encontrados: {} ".format(str(quantidade_de_registros))
    mytext.insert('end', str(linha1) + '\n' + '\n')
    frame2.update()
    for object in objectResult:
        linha_1_loop1 = "Registro: {} ".format(str(registro))
        mytext.insert('end', str(linha_1_loop1) + '\n')
        frame2.update()
        linha_2_loop1 = "Status: {} ".format(str(object['status']))
        mytext.insert('end', str(linha_2_loop1) + '\n')
        frame2.update()
        item_embargo = 1
        if object['status'] != "APTO":
            for embargo in object['embargoedList']:
                linha_1_loop2 = "Embargo: {} ".format(str(item_embargo))
                mytext.insert('end', str(linha_1_loop2) + '\n')
                frame2.update()

                nom_pessoa = "nom_pessoa: {} ".format(str(embargo['nom_pessoa']))
                mytext.insert('end', str(nom_pessoa) + '\n')
                frame2.update()

                processo_t = "processo_t: {} ".format(str(embargo['processo_t']))
                mytext.insert('end', str(processo_t) + '\n')
                frame2.update()            
                
                cpf_cnpj_s = "cpf_cnpj_s: {} ".format(str(embargo['cpf_cnpj_s']))
                mytext.insert('end', str(cpf_cnpj_s) + '\n')
                frame2.update()

                end_pessoa = "end_pessoa: {} ".format(str(embargo['end_pessoa']))
                mytext.insert('end', str(end_pessoa) + '\n')
                frame2.update()

                processo_t = "processo_t: {} ".format(str(embargo['processo_t']))
                mytext.insert('end', str(processo_t) + '\n')
                frame2.update()

                des_bairro = "des_bairro: {} ".format(str(embargo['des_bairro']))
                mytext.insert('end', str(des_bairro) + '\n')
                frame2.update()

                numero_tad = "numero_tad: {} ".format(str(embargo['numero_tad']))
                mytext.insert('end', str(numero_tad) + '\n')
                frame2.update()            

                num_auto_i = "num_auto_i: {} ".format(str(embargo['num_auto_i']))
                mytext.insert('end', str(num_auto_i) + '\n')
                frame2.update()            

                tipo_termo = "tipo_termo: {} ".format(str(embargo['tipo_termo']))
                mytext.insert('end', str(tipo_termo) + '\n')
                frame2.update()            

                data_tad = "data_tad: {} ".format(str(embargo['data_tad']))
                mytext.insert('end', str(data_tad) + '\n')
                frame2.update()            

                dat_altera = "dat_altera: {} ".format(str(embargo['dat_altera']))
                mytext.insert('end', str(dat_altera) + '\n')
                frame2.update()            

                sig_uf = "sig_uf: {} ".format(str(embargo['sig_uf']))
                mytext.insert('end', str(sig_uf) + '\n')
                frame2.update()            

                nom_munici = "nom_munici: {} ".format(str(embargo['nom_munici']))
                mytext.insert('end', str(nom_munici) + '\n')
                frame2.update()            

                area_ibama = "area_ibama: {} ".format(str(embargo['area_ibama']))
                mytext.insert('end', str(area_ibama) + '\n')
                frame2.update()            

                area_geom = "area_geom: {} ".format(str(embargo['area_geom']))
                mytext.insert('end', str(area_geom) + '\n' + '\n')
                frame2.update()            

                item_embargo+=1

        registro+=1
 
#Criando uma interface
root = Tk()
root.title("Executar Análise Socioambiental")
# root.geometry('600x300')
root.state('zoomed')

frame1=Frame(root)
frame1.pack()

frame2=Frame(root)
lab1f2 = Label(frame2, text="Resultados").pack()
frame2.pack()

Label(frame1, text="Número do CAR").grid(row=0) 
e1 = Entry(frame1)
e1.grid(row=0, column=1)

Label(frame1, text="Data a analisar").grid(row=1) 
e2 = Entry(frame1)
e2.grid(row=1, column=1)

Label(frame1, text="IAMKEY").grid(row=2) 
e3 = Entry(frame1)
e3.grid(row=2, column=1)

Button(frame1, text='Processar', command=analise).grid(row=3, column=1, sticky=W, pady=4) 

# mytext=Text(frame2).pack()
mytext=Text(frame2)
mytext.pack(padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()

# if __name__=="__main__":
#     IAMKEY = 'BEF3CAD78C638977BA4813F17CB7885CBC690E108F022A5998480DAC2DC2EB82'
#     id = "RR-1400233-FE38F60765D149AD98FDA9EBD30ADC71"
#     consult_date = '2021-06-22'
#     analise(id, consult_date)
    

