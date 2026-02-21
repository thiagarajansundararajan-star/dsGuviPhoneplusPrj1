import streamlit as st
import pandas as pd
import plotly.express as px

from sqlalchemy import create_engine

# 1. Setup Page Config
st.set_page_config(page_title="Transaction Dashboard", layout="wide")

# 2. Sample Data Generation (Replace this with your pd.read_csv or SQL data)
@st.cache_data
def load_data():
    conn_str = "mysql+pymysql://root:admin@localhost/dbproject"

    # 2. Create the engine
    engine = create_engine(conn_str)

    # 3. Use read_sql to load the query directly into a DataFrame
    query = "select State,Year,Quarter, CONCAT(Year,' Q', Quarter) Year_Quarter,Transacion_type,Transacion_count,Transacion_amount from Aggregated_transaction"
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
st.title(f"Transaction Analysis - {selected_q}")

# 5. Key Metrics (Total and Average)
total_trans = filtered_df['Transacion_amount'].sum()
avg_trans = filtered_df['Transacion_amount'].mean()
count_trans = len(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", f"₹{total_trans:,.2f}")
col2.metric("Average Transaction", f"₹{avg_trans:,.2f}")
col3.metric("Transaction Count", count_trans)

st.markdown("---")

# 6. Category-wise Analysis
st.subheader("Category-wise Transactions")

# Group data by category
cat_df = filtered_df.groupby('Transacion_type')['Transacion_amount'].sum().reset_index()

# Visualization using Plotly
fig = px.bar(
    cat_df, 
    x='Transacion_type', 
    y='Transacion_amount', 
    text_auto='.2s',
    title=f"Spending by Category in {selected_q}",
    color='Transacion_type',
    color_continuous_scale='Reds'
)

# Show plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# 7. Data Table View
with st.expander("View Filtered Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)