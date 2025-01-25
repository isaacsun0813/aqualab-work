import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

url = os.getenv('URL')
userid = os.getenv('USERID')

headers = { 'Content-Type': 'application/json' } 

#Switzerland first and then Mexico


'''
Swiss Addresses:
{"address": "23.205.89.169", "probes": [1003644, 1007182, 1007670]},
    {"address": "194.247.9.36", "probes": [1009431, 61988, 50269]},
    {"address": "23.65.7.21", "probes": [55532, 1002851, 65331]},
    {"address": "162.23.128.213", "probes": [1004428, 51012, 1003766]},
    {"address": "162.23.129.88", "probes": [1003319, 1005559, 1008093]},
    {"address": "193.223.62.195", "probes": [1008095, 1006346, 53323]},
    {"address": "193.223.22.34", "probes": [1003846, 15430, 24882]},
    {"address": "193.223.22.40", "probes": [1003644, 1007182, 1007670]},
    {"address": "162.23.128.232", "probes": [1009431, 61988, 50269]},
    {"address": "162.23.129.86", "probes": [55532, 1002851, 65331]},
    {"address": "193.26.130.100", "probes": [1004428, 51012, 1003766]},
    {"address": "162.23.128.233", "probes": [1003319, 1005559, 1008093]},
    {"address": "3.167.138.41", "probes": [1008095, 1006346, 53323]},
    {"address": "193.223.22.40", "probes": [1003846, 15430, 24882]},
    {"address": "162.23.128.233", "probes": [1003644, 1007182, 1007670]},
    {"address": "162.23.128.213", "probes": [1009431, 61988, 50269]},
    {"address": "162.23.129.86", "probes": [55532, 1002851, 65331]},
    {"address": "193.223.22.40", "probes": [1004428, 51012, 1003766]},
    {"address": "162.23.128.233", "probes": [1003319, 1005559, 1008093]},
    {"address": "162.23.128.213", "probes": [1008095, 1006346, 53323]},


'''

'''
Mexico Probe

1006632

	1009477

    61873
    
    60714
    
    63001

    64085
    
    25182
    
    27558
    
    7233
    
    35786
'''
addresses_and_probes = [
    {"address": "23.205.89.138", "probes": [1006632, 1009477, 61873]},
    {"address": "187.210.16.12", "probes": [60714, 63001, 64085]},
    {"address": "201.147.98.82", "probes": [25182, 27558, 7233]},
    {"address": "45.60.240.195", "probes": [35786, 1006632, 1009477]},
    {"address": "45.223.137.16", "probes": [61873, 60714, 63001]},
    {"address": "187.217.44.229", "probes": [64085, 25182, 27558]},
    {"address": "45.60.196.160", "probes": [7233, 35786, 1006632]},
    {"address": "200.23.8.5", "probes": [1009477, 61873, 60714]},
    {"address": "108.156.91.27", "probes": [63001, 64085, 25182]},
    {"address": "198.20.86.74", "probes": [27558, 7233, 35786]},
    {"address": "201.98.176.26", "probes": [1006632, 1009477, 61873]},
    {"address": "189.206.56.103", "probes": [60714, 63001, 64085]},
    {"address": "168.255.121.123", "probes": [25182, 27558, 7233]},
    {"address": "200.33.48.100", "probes": [35786, 1006632, 1009477]},
    {"address": "187.141.244.189", "probes": [61873, 60714, 63001]},
    {"address": "45.223.161.189", "probes": [64085, 25182, 27558]},
    {"address": "187.189.139.132", "probes": [7233, 35786, 1006632]},
    {"address": "187.218.29.164", "probes": [1009477, 61873, 60714]},
    {"address": "170.150.163.87", "probes": [63001, 64085, 25182]},
    {"address": "201.134.132.144", "probes": [27558, 7233, 35786]},
]



data = { 'type': 'traceroute', 'addresses_and_probes': addresses_and_probes, 'description': 'For Mexico Gov sites and IPs', 'userid': userid }

response = requests.post(url, data=json.dumps(data), headers=headers)
print('Status code:', response.status_code)
print('Response body:', response.json())