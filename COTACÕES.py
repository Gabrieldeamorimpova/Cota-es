from tkinter import *
import requests
import pandas as pd
def cotações():
    requisição = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisiçao = requisição.json()
    dólar = requisiçao['USDBRL']['bid']
    t_dolar = Label(janela,text='Dólar:{}'.format(dólar))
    t_dolar.grid(column=5,row=0)
    bitcoin = requisiçao['BTCBRL']['bid']
    t_bitcoin = Label(janela,text='Bitcoin:{}'.format(bitcoin))
    t_bitcoin.grid(column=5,row=1)
    euro = requisiçao['EURBRL']['bid']
    t_euro = Label(janela,text='Euro:{}'.format(euro))
    t_euro.grid(column=5,row=2)

janela = Tk()
janela.title('COTAÇÕES DÓLAR,EURO,BITCOIN.')
botão =Button(janela,text='PEGAR COTAÇÕES DÓLAR/EURO/BITCOIN',command=cotações)
botão.grid(column=5,row=6)


mainloop()