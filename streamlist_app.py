import streamlit
import pandas

streamlit.title(' ":heart:" My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3')
streamlit.text('Kale')
streamlit.text('Hard Boiled')
streamlit.header('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
# display table
streamlit.dataframe(my_fruit_list)

