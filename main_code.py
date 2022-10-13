#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:31:47 2022

@author: hocine
"""

import fct_utile as fu


#1- initialize param_file parameter
param_file = "params.yaml"
#2- read  param_file parameter
params = fu.read_params(param_file)

#3- mow all parameteres are in params
MAX_NBR_COM = params["MAX_NBR_COM"]

if __name__ == '__main__':
        
    api_key = params["api_key"]
    video_id = params["video_id"]
    
    response = fu.build_res_req(api_key,video_id,MAX_NBR_COM)    
   
    comment = fu.df_comments(MAX_NBR_COM,response)
  
    



















