import streamlit as st
import pandas as pd
import numpy as np
import matplotlib_inline as plt

# load the files into a dataframe
groups = pd.read_csv('Fifa_Worldcup_2022_Groups.csv')
matches = pd.read_csv('international_matches.csv')
player_ratings = pd.read_csv('FIFA22_official_data.csv')

groups['Group'] = groups['Group'].replace(['A1','A2','A3','A4'],"A")
groups['Group'] = groups['Group'].replace(['B1','B2','B3','B4'],"B")
groups['Group'] = groups['Group'].replace(['C1','C2','C3','C4'],"C")
groups['Group'] = groups['Group'].replace(['D1','D2','D3','D4'],"D")
groups['Group'] = groups['Group'].replace(['E1','E2','E3','E4'],"E")
groups['Group'] = groups['Group'].replace(['F1','F2','F3','F4'],"F")
groups['Group'] = groups['Group'].replace(['G1','G2','G3','G4'],"G")
groups['Group'] = groups['Group'].replace(['H1','H2','H3','H4'],"H")

st.dataframe(groups)