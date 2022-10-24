#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:31:47 2022

@author: hocine
"""
import fct_utile as fu

#1- initialize param_file parameter
param_file = 'params.yaml'

#2- read  param_file parameter
params = fu.read_params(param_file)

#3- mow all parameteres are in params
MAX_NBR_COM = params['MAX_NBR_COM']
api_key = params["api_key"]
video_id = params["video_id"]
list_of_videoLinks = params['list_of_videoLinks']


if __name__ == '__main__':
    
    

    response = fu.build_res_req(api_key,video_id,MAX_NBR_COM)  
    
    dict_of_comment = fu.dict_comment_item(response,MAX_NBR_COM)
            
    dict_multi_videoComments = fu.comments_to_json(list_of_videoLinks,response,MAX_NBR_COM)
        
