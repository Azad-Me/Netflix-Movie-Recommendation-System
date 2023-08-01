# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import streamlit as st
import pandas
import pickle
import bz2

data1 = pickle.load(open('data_new.pkl','rb'))
data = data1.iloc[:2500,:]
with bz2.BZ2File('final_compressed_data.pkl', 'rb') as f:
    similarities = pickle.load(f)


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://pixabay.com/get/g3ad6aae6a5c46e43ea6ee422570620bf9e1762384056a34d0c4d95303ef347068d3800318ebd1fc0e80f85025ed4eb63.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

def movies_recommendation(movie_nme):

  print('Hey!! Gyus, Checkout these Amazing Movies')
  print(' ')
  index = data[data['title']== movie_nme].index[0]
  similar_content = sorted(list(enumerate(similarities[index])),reverse = True , key = lambda x: x[-1])

  recommend_movies =[]
  for i,j in similar_content[1:6]:
    recommend_movies.append(data['title'][i])
        
  return (recommend_movies)
    

def poster_file(movie_name):
    url = "https://streaming-availability.p.rapidapi.com/v2/search/title"
    
    querystring = {"title":movie_name,"country":"us"}
    
    headers = {
    	"X-RapidAPI-Key": "8a00eb7337mshf8a2d52e86cf87cp12435fjsnc093d6aa0f8f",
    	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    
    output= response.json()
    
    poster = output['result'][0]['posterURLs']['original']
    #for i in (output['result']):
      #if i['title']== movie_name :
        #poster.append(i['posterURLs']['original'])
        #break
    return poster


#st.title(':white[Netflix Movies Recommendation System]')
st.markdown("<h1 style='color: white;'>Netflix Movies Recommendation System</h1>", unsafe_allow_html=True)
#st.write("<span style='color: white;'>Movie List</span>", unsafe_allow_html=True)

option = st.selectbox(      
        'Movies List',
        data['title'].unique())
    
    
if st.button('Recommend'):
        recommendation = movies_recommendation(option)
        for i in recommendation :
            st.write(i)
            #image = Image.open(poster_file(i))
            st.image(poster_file(i))

