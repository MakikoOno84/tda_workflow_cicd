import os, sys
# os.system(f"{sys.executable} -m pip install --upgrade pytd==1.4.0")

def get_abandoned(database_name, table_name):
  os.system(f"{sys.executable} -m pip install requests")
  os.system(f"{sys.executable} -m pip install --upgrade pytd")

  import pandas as pd
  import requests
  import pytd
  import json 
  from pandas.io.json import json_normalize

  sc_apikey  = os.environ.get("SC_API_KEY")
  sc_passwd  = os.environ.get("SC_API_PASSWD")
  sc_server  = os.environ.get("SC_SERVER")
  apikey     = os.environ.get("TD_API_KEY")
  apiserver  = os.environ.get("TD_API_SERVER")

  res = requests.get(sc_server,headers={"Accept":"application/json"},auth=requests.auth.HTTPBasicAuth(sc_apikey, sc_passwd))

  print(f"statusCode:{res.status_code}")
  items = []
  if (res.status_code == 200 ):
    # res_dict = res.json()
    # print('****************res_dict output from here******************')
    # print(res_dict)
    # for key in res_dict:
    #   print(f"{key}: {res_dict[key]}")
    #   items.append((key, res_dict[key]))
    # json_dict = json.loads(res.text)
    # df = json_normalize(json_dict['items'])

    # print('****************df output from here******************')
    # print(df)
  

    # client = pytd.Client(apikey=apikey, endpoint=apiserver, database=database_name)    

    # client.create_database_if_not_exists(database_name)
    # client.load_table_from_dataframe(
    #   df, f"{database_name}.{table_name}", if_exists="append", fmt='msgpack'
    # )

    print(f"statusCode: {res.status_code}")
    items = []
    if (res.status_code == 200):
      json_dict = json.loads(res.text)
      df_json = json_normalize(json_dict['items'])

      ## Debug
      print("*****df_json from here******")
      print(df_json)

      # df_test = pd.DataFrame(data={"col1": [1, 2, 4], "col2": [1.0, 2.0, 3.0]})

      client = pytd.Client(apikey=apikey, endpoint=apiserver, database=database_name)
      client.create_database_if_not_exists(database_name)
      client.load_table_from_dataframe(df_json, f"{database_name}.{table_name}", if_exists="append")

