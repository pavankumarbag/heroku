import streamlit as st

st.write("""
# Finding largest of 3 given numbers

This app finds the value greater than other two numbers
""")
#Get Input

st.header('Input Parameters')


number_1 = st.number_input('Enter first number')
number_2 = st.number_input('Enter second number')
number_3 = st.number_input('Enter third number')
    

data = {'First_Number': number_1,
        'Second_Number': number_2,
        'Third_Number': number_3
        }


st.subheader('User Input parameters')
st.write(data)

#Getting largest

list1 = [number_1,number_2,number_3]
list1 = list1.sort()
output1=list1[-1]

#Output

st.subheader('Greatest number among the given inputs is:')
st.write(output1)
