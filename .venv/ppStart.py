import streamlit as st
# 1. Define the pages
home_page = st.Page("ppHome.py", title="Home", icon="🏠")
dbdTrans_page = st.Page("ppDbdTransaction.py", title="Transaction Dashboard", icon="🏠")
AggUser_page = st.Page("ppPages/Aggregated/ppAggUser.py", title="Data_Aggregate_User", icon="📊")
AggTrans_page = st.Page("ppPages/Aggregated/ppAggTransaction.py", title="Data_Aggregate_Transaction", icon="📊")
AggInsur_page = st.Page("ppPages/Aggregated/ppAggInsurance.py", title="Data_Aggregate_Insurance", icon="📊")
MapInsur_page = st.Page("ppPages/Map/ppMapInsurance.py", title="Data_Map_Insurance", icon="📊")
Maptran_page = st.Page("ppPages/Map/ppMapTransaction.py", title="Data_Map_Transaction", icon="📊")
Mapuser_page = st.Page("ppPages/Map/ppMapuser.py", title="Data_Map_user", icon="📊")
TopInsur_page = st.Page("ppPages/Top/ppTopInsurance.py", title="Data_Top_Insurance", icon="📊")
Toptran_page = st.Page("ppPages/Top/ppTopTransaction.py", title="Data_Top_Transaction", icon="📊")
Topuser_page = st.Page("ppPages/Top/ppTopuser.py", title="Data_Top_user", icon="📊")

# 2. Create the navigation menu

pg = st.navigation({"Home":[home_page,dbdTrans_page],"Aggregated":[AggUser_page, AggTrans_page, AggInsur_page],"Map":[MapInsur_page,Maptran_page,Mapuser_page],
                    "Top":[TopInsur_page,Toptran_page,Topuser_page]})
pg.run()

