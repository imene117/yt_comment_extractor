#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:31:47 2022

@author: hocine
"""
import fct_utile as fu

#must be deleted after
import pandas as pd

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
    dict_of_dfs = {}
    key_list =  list(dict_multi_videoComments.keys())    
    tables = fu.dict_to_df(key_list,dict_multi_videoComments,dict_of_dfs)
    
    