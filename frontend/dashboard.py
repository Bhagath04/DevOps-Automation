import streamlit as st
import pandas as pd

# Title of the dashboard
st.title('Real-Time Dashboard')

# Current Date and Time
st.write('Current Date and Time (UTC):', pd.to_datetime('now', utc=True).strftime('%Y-%m-%d %H:%M:%S'))

# Text input widget
name = st.text_input('Enter your name:')

# Number input widget
age = st.number_input('Enter your age:', min_value=0, max_value=120)

# Selectbox widget
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])

# Checkbox widget
agree = st.checkbox('I agree')

# Button widget
if st.button('Submit'):
    st.write(f'Hello, {name}. You are {age} years old. You selected {option}.')
    if agree:
        st.write('Thank you for agreeing!')

# Displaying a line chart
data = pd.DataFrame({'x': range(10), 'y': range(10, 20)})
st.line_chart(data.set_index('x'))
