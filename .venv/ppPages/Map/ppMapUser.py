import pandas as pd
import json
import os
import streamlit as st
from sqlalchemy import create_engine
import pymysql

#This is to direct the path to get the data as states

path="pulse/data/map/user/hover/country/india/state/"
Map_state_list=os.listdir(path)

#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quarter':[], 'user_state':[], 'user_reguser':[],'user_appopens':[]}

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
                #for z in D['data']['hoverData']:
                z=D['data']['hoverData']
                for state_name, details in z.items():
                    # state_name = "puducherry"
                    # details = {"registeredUsers": 49318, "appOpens": 0}
                    name = state_name
                    #st.write(state_name)
                    registeredUsers = details['registeredUsers']
                    appOpens = details['appOpens']
                    clm['user_state'].append(name)
                    clm['user_reguser'].append(registeredUsers)
                    clm['user_appopens'].append(appOpens)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

#Succesfully created a dataframe
Map_users=pd.DataFrame(clm)
#print(Agg_users)
st.write(Map_users)
engine = create_engine("mysql+pymysql://root:admin@localhost/dbproject")
Map_users.to_sql('map_user', engine, if_exists='append', index=False)