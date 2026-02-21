import pandas as pd
import json
import os
import streamlit as st
from sqlalchemy import create_engine
import pymysql

#This is to direct the path to get the data as states

path="pulse/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)

#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quarter':[], 'users_brand':[], 'users_count':[],'users_percentage':[]}

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
                for z in D['data']['usersByDevice']:
                    brand=z['brand']
                    count=z['count']
                    percentage=z['percentage']
                    clm['users_brand'].append(brand)
                    clm['users_count'].append(count)
                    clm['users_percentage'].append(percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Succesfully created a dataframe
Agg_users=pd.DataFrame(clm)
#print(Agg_users)
st.write(Agg_users)
engine = create_engine("mysql+pymysql://root:admin@localhost/dbproject")
Agg_users.to_sql('aggregated_user', engine, if_exists='append', index=False)