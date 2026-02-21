import pandas as pd
import json
import os
import streamlit as st
from sqlalchemy import create_engine
import pymysql

#This is to direct the path to get the data as states

path="pulse/data/aggregated/insurance/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quarter':[], 'insurance_name':[], 'insurance_count':[],'insurance_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['insurance_name'].append(Name)
                    clm['insurance_count'].append(count)
                    clm['insurance_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Succesfully created a dataframe
Agg_insurance=pd.DataFrame(clm)
#print(Agg_users)
st.write(Agg_insurance)
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
Agg_insurance.to_sql('aggregated_insurance', engine, if_exists='append', index=False)