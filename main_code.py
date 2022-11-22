#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:31:47 2022

@author: hocine
"""
import fct_utile as fu

#must be deleted after
import pandas as pd
import os
import shutil

#1- initialize param_file parameter
param_file = 'params.yaml'

#2- read  param_file parameter
params = fu.read_params(param_file)

#3- all parameteres are in params
MAX_NBR_COM = params['MAX_NBR_COM']
api_key = params["api_key"]
list_of_videoLinks = params['list_of_videoLinks'] # list of videos id 



if __name__ == '__main__':
  
    dict_multi_videoComments = fu.comments_to_json(list_of_videoLinks,MAX_NBR_COM,api_key)
    key_list =  list(dict_multi_videoComments.keys())    
    dict_of_dfs = dict.fromkeys(key_list, None) # initialize a dictionnary with its keys
    
    tables = fu.dict_to_df(key_list,dict_multi_videoComments,dict_of_dfs)
    
    #source = '/Users/hocine/yt_comment_extractor/tab1.csv'
    #
    
        
    fileName = 'tab1.csv'
    destination = '/Users/hocine/yt_comment_extractor/tabs_csv/'
        
    test1 = tables['gqS1ov4lSI0']
    test1.to_csv(destination + fileName, index=False)
    #
    
    fileName = 'tab2.csv'
    destination = '/Users/hocine/yt_comment_extractor/tabs_csv/'
        
    test2 = tables['1RrHbtJA6V0']
    test2.to_csv(destination + fileName, index=False)
    
    #
    
    fileName = 'tab3.csv'
    destination = '/Users/hocine/yt_comment_extractor/tabs_csv/'
        
    test3 = tables['TTHazQeM8v8']
    test3.to_csv(destination + fileName, index=False)

    #
    
    fileName = 'tab4.csv'
    destination = '/Users/hocine/yt_comment_extractor/tabs_csv/'
        
    test4 = tables['tzQC3uYL67U']
    test4.to_csv(destination + fileName, index=False)
    
    





