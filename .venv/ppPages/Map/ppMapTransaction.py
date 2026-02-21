import pandas as pd
import json
import os
import streamlit as st
from sqlalchemy import create_engine
import pymysql

#This is to direct the path to get the data as states

path="pulse/data/map/transaction/hover/country/india/state/"
Map_state_list=os.listdir(path)
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quarter':[], 'Tran_name':[],'Tran_type':[], 'Tran_count':[],'Tran_amount':[]}

for i in Map_state_list:
    p_i=path+i+"/"
    Map_yr=os.listdir(p_i)
    for j in Map_yr:
        p_j=p_i+j+"/"
        Map_yr_list=os.listdir(p_j)
        for k in Map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['hoverDataList']:
                    Name=z['name']
                    type=z['metric'][0]['type']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    clm['Tran_name'].append(Name)
                    clm['Tran_type'].append(type)
                    clm['Tran_count'].append(count)
                    clm['Tran_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Succesfully created a dataframe
Map_tran=pd.DataFrame(clm)
#print(Agg_users)
st.write(Map_tran)
#engine=create_engine('postgresql://postgres:admin@localhost:5432/DSProject1')
#postgresql://dsserverinstance_user:cQ8pF4SOLlmo4rmyWxIzCFsU2bO7558l@dpg-d5h4i594tr6s739bmadg-a.virginia-postgres.render.com/dsserverinstanc
# Insert DataFrame into PostgreSQL table
#Mysql Connection
# 1. Establish the connection
# 1. Establish the connection
#connection = pymysql.connect(
#    host='localhost',
#    user='root',
#    password='admin',
#    database='dbproject'
#)

# Create engine
engine = create_engine("mysql+pymysql://root:admin@localhost/dbproject")
Map_tran.to_sql('map_transaction', engine, if_exists='replace', index=False)