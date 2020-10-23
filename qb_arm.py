#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from PIL import Image

speed = pd.read_csv('week17.csv')

josh_allen = speed[speed.QB == 'Josh Allen']
josh_allen_plot = px.line(josh_allen, x='frame_id', y='speed',
        title='Speed of the Football on Josh Allen Passing Plays - Week 17, 2018')

matthew_stafford = speed[speed.QB == 'Matthew Stafford']
matthew_stafford_plot = px.line(matthew_stafford, x='frame_id', y='speed',
        title='Speed of the Football on Matthew Stafford Passing Plays - Week 17, 2018')

jared_goff = speed[speed.QB == 'Jared Goff']
jared_goff_plot = px.line(jared_goff, x='frame_id', y='speed',
        title='Speed of the Football on Jared Goff Passing Plays - Week 17, 2018')

homepage_image = Image.open('al-soot-c3SY0VqneSg-unsplash.jpg')
josh_allen_image = Image.open('bills.jpg')
matthew_stafford_image = Image.open('josh-garcia-iqa83PdCO1A-unsplash.jpg')
jared_goff_image = Image.open('bp-miller-mu2tDeICLNI-unsplash.jpg')

def main():
    page = st.sidebar.selectbox('Select Quarterback', ('Home Page', 'Josh Allen', 'Matthew Stafford', 'Jared Goff'))

    if page == 'Home Page':
        st.image(homepage_image, use_column_width=True)
        st.title('QB Throwing Power - Week 17, 2018')
        st.write('''
        something,  something  something,  something,  something,  something,  something,  something,  something
        ''')
    elif page == 'Josh Allen':
        st.title('Josh ALlen Throwing Power - Week 17, 2018')
        st.image(josh_allen_image, use_column_width=True)
        st.write('''
                ### How Do I Read This Chart?
                The line chart below tracks the speed (in miles per hour) of the football, frame by frame during a play.
                The data aggregates to the "max" speed of the football at each frame. For example, in week 17 of the
                2018 NFL football season, Josh Allen dropped back to throw the football 28 times. On one play, in the 41st
                frame of the play, the football was moving at 27.36 MPH.
                ''')
        st.write(josh_allen_plot)
    elif page == 'Matthew Stafford':
        st.title('Matthew Stafford Throwing Power - Week 17, 2018')
        st.image(matthew_stafford_image, use_column_width=True)
        st.write('''
                ### How Do I Read This Chart?
                The line chart below tracks the speed (in miles per hour) of the football, frame by frame during a play.
                The data aggregates to the "max" speed of the football at each frame. For example, in week 17 of the
                2018 NFL football season, Matthew Stafford dropped back to throw the football 28 times. On one play, in the 42nd
                frame of the play, the football was moving at 25.12 MPH.
                ''')
        st.write(matthew_stafford_plot)
    elif page == 'Jared Goff':
        st.title('Jared Goff Throwing Power - Week 17, 2018')
        st.image(jared_goff_image, use_column_width=True)
        st.write('''
                ### How Do I Read This Chart?
                The line chart below tracks the speed (in miles per hour) of the football, frame by frame during a play.
                The data aggregates to the "max" speed of the football at each frame. For example, in week 17 of the
                2018 NFL football season, Jared Goff dropped back to throw the football 28 times. On one play, in the 40th
                frame of the play, the football was moving at 25.85 MPH.
                ''')
        st.write(jared_goff_plot)


st.write(main())

