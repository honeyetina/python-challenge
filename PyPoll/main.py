#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:41:21 2021

@author: tinatina
"""
import pandas as pd
election_data = pd.read_csv('./Resources/election_data.csv')
election_data.head()
total_vote_cast = election_data["Voter ID"].count()
print(total_vote_cast)
cv = (election_data["Candidate"]).value_counts()
print(cv)
cv_pct = cv/total_vote_cast
print(cv_pct)
winner = cv.index[0]
print(winner)
result = f'''Election Results
-------------------------
Total Votes: {total_vote_cast}
-------------------------
{cv.index[0]}: {cv_pct.iloc[0]:.3%} ({cv.iloc[0]})
{cv.index[1]}: {cv_pct.iloc[1]:.3%} ({cv.iloc[1]})
{cv.index[2]}: {cv_pct.iloc[2]:.3%} ({cv.iloc[2]})
{cv.index[3]}: {cv_pct.iloc[3]:.3%} ({cv.iloc[3]})
-------------------------
Winner: {winner}
-------------------------'''
print(result)
with open('./analysis/' + "analysis.txt" , "w") as text_file:
    text_file.write(result)