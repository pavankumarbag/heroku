import streamlit as st

st.write("""
# Subtracton of two numbers
This app finds the difference between two numbers
""")
#Get Input

st.header('Input Parameters')


number_1 = st.number_input('Enter first number')
number_2 = st.number_input('Enter second number')
#number_3 = st.number_input('Enter third number')
    

data = {'First_Number': number_1,
        'Second_Number': number_2,
        }


st.subheader('User Input parameters')
st.write(data)

#Getting largest

numbers = [data['First_Number'],data['Second_Number']]
#numbers.sort()

#Output

st.subheader('Subtraction of two nos is:')
st.write(numbers[0]-numbers[1])
