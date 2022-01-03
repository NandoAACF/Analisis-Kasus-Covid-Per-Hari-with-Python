import requests
import pandas as pd
import json
import matplotlib.dates as mdates
import numpy as np

resp = requests.get('https://data.covid19.go.id/public/api/update.json')
resp

resp.headers

cov_id_raw = resp.json()

print("====================================================")
print('Length of cov_id_raw : %d.' %len(cov_id_raw))
print('Komponen cov_id_raw  : %s.' %cov_id_raw.keys())
cov_id_update = cov_id_raw['update']
print("====================================================")
print("Tanggal pembaruan penambahan kasus: ", cov_id_update['penambahan']['tanggal'])
print("Jumlah penambahan kasus sembuh: ", cov_id_update['penambahan']['jumlah_sembuh'])
print("Jumlah penambahan kasus meninggal: ", cov_id_update['penambahan']['jumlah_meninggal'])
print("Jumlah penambahan kasus positif: ", cov_id_update['penambahan']['jumlah_positif'])
print("Jumlah total kasus meninggal hingga saat ini: ", cov_id_update['total']["jumlah_meninggal"])
print("====================================================")