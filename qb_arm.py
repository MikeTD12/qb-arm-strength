#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from PIL import Image

tracking = pd.read_csv('week17.csv')

# Creating a unique key for every play in every game.
tracking['gameId'] = tracking['gameId'].astype('str')
tracking['playId'] = tracking['playId'].astype('str')
tracking['unique_playId'] = tracking.gameId+''+tracking.playId

# Creating a table of QB names and their uniuqe_playId.
qb = tracking[tracking.position == 'QB'][['unique_playId', 'displayName', 'frameId']]

# Creating a table of football tracking metrics.
football = tracking[tracking.displayName == 'Football']

# Merging the two tables so I can analyze the football tracking associated with each QB.
fb_speed = pd.merge(qb, football, on=['unique_playId', 'frameId'])

speed = fb_speed.groupby(['displayName_x', 'frameId']).agg({
    's': 'max',
    'a': 'max'
}
).reset_index()

speed.rename(columns={'displayName_x': 'QB', 'frameId': 'frame_id',
                      's': 'speed', 'a': 'acceleration'}, inplace=True)


josh_allen = speed[speed.QB == 'Josh Allen']
josh_allen_plot = px.line(josh_allen, x='frame_id', y='speed',
        title='Speed of the Football on Josh Allen Passing Plays - Week 17, 2018')

matthew_stafford = speed[speed.QB == 'Matthew Stafford']
matthew_stafford_plot = px.line(matthew_stafford, x='frame_id', y='speed',
        title='Speed of the Football on Matthew Stafford Passing Plays - Week 17, 2018')

jared_goff = speed[speed.QB == 'Jared Goff']
jared_goff_plot = px.line(jared_goff, x='frame_id', y='speed',
        title='Speed of the Football on Jared Goff Passing Plays - Week 17, 2018')


image = Image.open('al-soot-c3SY0VqneSg-unsplash.jpg')
st.image(image, use_column_width=True)

def get_qb(name):
    if name =='Josh Allen':
        st.write(josh_allen_plot)
    elif name == 'Matthew Stafford':
        st.write(matthew_stafford_plot)
    elif name == 'Jared Goff':
        st.write(jared_goff_plot)
    return select_qb

select_qb = st.sidebar.selectbox('Select Quarterback', ('Josh Allen', 'Matthew Stafford', 'Jared Goff'))


st.title('QB Throwing Power - Week 17, 2018')
st.write('''
### How Do I Read This Chart?
The line chart below tracks the speed (in miles per hour) of the football, frame by frame during a play.
The data aggregates to the "max" speed of the football at each frame. For example, in week 17 of the
2018 NFL football season, Josh Allen dropped back to throw the football 28 times. On one play, in the 41st
frame of the play, the football was moving at 27.36 MPH.
''')
st.write(get_qb(select_qb))

