import streamlit as st

import pandas as pd
import numpy as np



st.title('Yelp map trial')


file_uload = st.file_uploader('yelp_business.json')

@st.cache
def load_data():
    data = pd.read_json(file_uload,lines=True)
    selected = data.get('name')
    return selected

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Map')

def load_data_map():
    data = pd.read_json(file_uload,lines=True)
    selected = data[['latitude','longitude','state']]
    return selected

data_load_state = st.text('Loading data...')
map_data = load_data_map()
data_load_state.text('Loading data...done!')

st.map(map_data)




state_option = st.selectbox(
    'Choose a state:',
     ('AB', 'MO', 'TN','CA','IN','ID','FL'))

filtered_data = map_data[map_data['state'] == state_option]


st.subheader(f'Bussiness in {state_option}:')
st.map(filtered_data)
