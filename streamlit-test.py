import streamlit as st
import pandas as pd
import numpy as np

st.title('Sourcing Misinformation')

# st.write('Text goes here in Markdown')

DATA_URL = ('data/tweets_cluster_output_15000.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['created_on']= pd.to_datetime(data['created_on'])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = load_data(150)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

data.dtypes


# Load clusters CSV
df_clusters = pd.read_csv('data/tweets_cluster_keywords.csv', index_col=0)

st.subheader('Explore clusters')
df_clusters

# User selection of cluster
cluster_choice = st.selectbox(
    'Which cluster would you like to explore further?',
    df_clusters.columns)

st.write('You selected:', cluster_choice)

st.subheader('Explore tweets')

# Reorganize tweet data
data2 = data[["clusters", "tweet_text", "user", "user_follower_count", "hashtags"]]

# Filter based on cluster choice input
st.write(data2[data2["clusters"] == int(cluster_choice[-1])])


# Create a time series of tweets

"""data_timeindex = data.set_index('created_on')
data_timeindex = data_timeindex[["tweet_text", "clusters"]]
data_timeindex

st.line_chart(data_timeindex)"""

# Show full dataframe on user request
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)