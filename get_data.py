import pymongo
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
MONGO_USER = os.getenv('MONGO_USER', '_')
MONGO_PASS = os.getenv('MONGO_PASS', '_')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER', '_')

# Get Data ====================================
MONGO_URL=f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/home-info?retryWrites=true&w=majority&appName=clsFalcon'
MONGO_CLIENT = pymongo.MongoClient(MONGO_URL)
MONGO_DB = MONGO_CLIENT['home-info']
MONGO_COLLETION = MONGO_DB['dailies']

def get_data():
  data = list(MONGO_COLLETION.find())

  df = pd.DataFrame(data)

  df['date_time'] = pd.to_datetime(df['date_time'])
  df['date'] = df['date_time'].dt.date
  df['time'] = df['date_time'].dt.time
  
  return df   


