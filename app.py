import streamlit as st
import pickle
import pandas as pd
import numpy as np

import string
st.set_page_config(
     page_title="BOOK RECOMMENDER SYSTEM",
     page_icon=":book:",
     layout="wide"
 )
books_genre = pickle.load(open('books_title.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(book):
    listbk = []
    index = books_genre[books_genre['Title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances:
        if(i[1]>0.9):
            listbk.append(books_genre.iloc[i[0]].Title)
        else:
            break
    return listbk
st.title('BOOK RECOMMENDER SYSTEM')
books = pickle.load(open('books.pkl','rb'))
st.write("Hi!, Welcome")
answer = st.radio(
     "What do you want to do?",
     ('Recommend books based on some input book', 'Filter books based on genre'))
if answer=='Filter books based on genre':

    option = st.selectbox('Select Genre',('All','Fiction','Non Fiction','Philosophy','Science','Tech'))


    dataGS=pickle.load(open('dataGS.pkl','rb'))
    dataGTitle = pickle.load(open('dataGTitle.pkl','rb'))
    if option == 'All':
        st.table(books)

    if option == 'Fiction':
        option2 = st.selectbox('Select SubGenre',(['All']+ dataGS['fiction']))
        bf = books.loc[dataGTitle['fiction']]
        if(option2=='All'):
            st.table(bf)
        else:
            data = bf.loc[bf['SubGenre']==option2]
            st.table(data)


    if option == 'Non Fiction':
        option2 = st.selectbox('Select SubGenre', (['All'] + dataGS['nonfiction']))
        bf = books.loc[dataGTitle['nonfiction']]
        if (option2 == 'All'):
            st.table(bf)
        else:
            data = bf.loc[bf['SubGenre'] == option2]
            st.table(data)


    if option == 'Philosophy':
        option2 = st.selectbox('Select SubGenre', (['All'] + dataGS['philosophy']))
        bf = books.loc[dataGTitle['philosophy']]
        if (option2 == 'All'):
            st.table(bf)
        else:
            data = bf.loc[bf['SubGenre'] == option2]
            st.table(data)


    if option == 'Science':
        option2 = st.selectbox('Select SubGenre', (['All'] + dataGS['science']))
        bf = books.loc[dataGTitle['science']]
        if (option2 == 'All'):
            st.table(bf)
        else:
            data = bf.loc[bf['SubGenre'] == option2]
            st.table(data)


    if option == 'Tech':
        option2 = st.selectbox('Select SubGenre', (['All'] + dataGS['tech']))
        bf = books.loc[dataGTitle['tech']]
        if (option2 == 'All'):
            st.table(bf)
        else:
            data = bf.loc[bf['SubGenre'] == option2]
            st.table(data)

else:
    option = st.selectbox('Select the book', books.index.tolist())
    listbk = recommend(option)
    data = books.loc[listbk]
    st.table(data)



