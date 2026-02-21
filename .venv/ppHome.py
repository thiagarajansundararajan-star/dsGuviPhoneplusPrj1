import pandas as pd
import plotly.express as px
import streamlit as st
import requests

from sqlalchemy import create_engine

#df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
df = pd.read_csv("Insurance.csv")
@st.cache_data
def load_data():
    conn_str = "mysql+pymysql://root:admin@localhost/dbproject"

    # 2. Create the engine
    engine = create_engine(conn_str)

    # 3. Use read_sql to load the query directly into a DataFrame
    query = "select State,Year,Quarter, CONCAT(Year,' Q', Quarter) Year_Quarter,Insurance_name,Insurance_count,Insurance_amount from dbproject.Aggregated_Insurance"
    df = pd.read_sql(query, con=engine)
    return df

df = load_data()
#st.write(df)
# 3. Sidebar Filter
st.sidebar.header("Filter Options")
selected_q = st.sidebar.selectbox("Select Quarter", options=df['Year_Quarter'].unique())

# Filter the dataframe based on selection
filtered_df = df[df['Year_Quarter'] == selected_q]

# 4. Dashboard Title
st.title(f"Insurance Analysis - {selected_q}")

# 5. Key Metrics (Total and Average)
total_insurance = filtered_df['Insurance_amount'].sum()
avg_insurance = filtered_df['Insurance_amount'].mean()
count_insurance = len(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Total Insurance", f"₹{total_insurance:,.2f}")
col2.metric("Average Insurance", f"₹{avg_insurance:,.2f}")
col3.metric("Insurance Count", count_insurance)

# 6. Category-wise Analysis
st.subheader("State-wise Insurance Count")

# Group data by category
cat_df = filtered_df.groupby('State')['Insurance_count'].sum().reset_index()

st.write(cat_df)
# 2. Fetch the GeoJSON from the URL
url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
repo = requests.get(url).json()

# 3. Convert the 'ST_NM' property to lowercase inside the GeoJSON object
for feature in repo['features']:
    feature['properties']['ST_NM'] = feature['properties']['ST_NM'].lower()

fig = px.choropleth(
    cat_df,
    geojson=repo,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Insurance_count',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

#fig.show()
st.plotly_chart(fig,width='stretch')