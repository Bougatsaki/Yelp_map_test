import streamlit as st
import s3fs
import pandas as pd
import numpy as np

fs = s3fs.S3FileSystem(anon=False)

st.title('Yelp map trial')


DATA_URL = ('https://cmpt732-no-error.s3.us-west-2.amazonaws.com/yelp_business.json')

@st.cache
@st.experimental_memo(ttl=600)
def load_data():
    data = pd.read_json(DATA_URL)
    selected = data.select('name','state','star')
    return selected

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Map')



state_option = st.selectbox(
    'Choose a state:',
    ('CA', 'MO', 'TN'))

filtered_data = data[data.state == state_option]

st.subheader(f'Bussiness in {state_option}:')
st.map(filtered_data)
