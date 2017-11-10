import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from optparse import OptionParser

def connect_to_stream():

    """
    Environment                 Description 
    fxTrade (Live)              The live (real money) environment 
    fxTrade Practice (Demo)     The demo (simulated money) environment 
    """

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domainDict = { 'live' : 'stream-fxtrade.oanda.com',
               'demo' : 'stream-fxpractice.oanda.com' }
               
    # Replace the following variables with your personal values 
    environment = "demo" # Replace this 'live' if you wish to connect to the live environment 
    domain = domainDict[environment] 
    access_token = os.getenv('OANDA_TOKEN')
    account_id = os.getenv('OANDA_ACCOUNT')
    instruments = 'USD_JPY,EUR_USD,AUD_USD,EUR_GBP,USD_CAD,USD_CHF,USD_MXN,USD_TRY,USD_CNH,NZD_USD' 

    try:
        s = requests.Session()
        url = "https://api-fxtrade.oanda.com/v1/accounts"
        headers = {'Authorization' : 'Bearer ' + access_token,
                   # 'X-Accept-Datetime-Format' : 'unix'
                  }
        req = requests.Request('GET', url, headers = headers)
        pre = req.prepare()
        pretty_print_POST(pre)
    except Exception as e:
        s.close()
        print("Caught exception when connecting to stream\n" + str(e)) 

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def main():
    connect_to_stream()

if __name__ == "__main__":
    main()