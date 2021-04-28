import streamlit as st
import pandas as pd
import numpy as np

st.title('Sourcing Misinformation')

# st.write('Text goes here in Markdown')

DATA_URL = ('data/tweets_cluster_output_15000.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

df_clusters = pd.read_csv('data/tweets_cluster_keywords.csv', index_col=0)

df_clusters

cluster_choice = st.selectbox(
    'Which cluster would you like to see?',
    df_clusters.columns)

st.write('You selected:', cluster_choice)

st.subheader('Raw data')
st.write(data[data["clusters"] == int(cluster_choice[-1])])






""" 
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...") """