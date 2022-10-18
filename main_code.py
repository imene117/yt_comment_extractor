#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:31:47 2022

@author: hocine
"""

import fct_utile as fu
from googleapiclient.discovery import build


#1- initialize param_file parameter
param_file = "params.yaml"
#2- read  param_file parameter
params = fu.read_params(param_file)

#3- mow all parameteres are in params
MAX_NBR_COM = params["MAX_NBR_COM"]

if __name__ == '__main__':
    
    api_key = params["api_key"]
    video_id = params["video_id"]
    '''
    response = fu.build_res_req(api_key,video_id,MAX_NBR_COM)    
   
    comment = fu.df_comments(MAX_NBR_COM,response)
    '''
    
    
    
    
    
    
    def build_res_req(api_key,video_id,MAX_NBR_COM):
        #build a resource for youtube
        resource = build('youtube', 'v3', developerKey=api_key)
        #create a request to get 20 comments on the video
        request = resource.commentThreads().list(
                                    part="snippet,replies",
                                    videoId=video_id,
                                    maxResults= MAX_NBR_COM,   #get 20 comments
                                    order="orderUnspecified")  #top comments.
        #execute the request
        response =request.execute()
        return response
    
    response = build_res_req(api_key,video_id,MAX_NBR_COM)    
    
    #initialize the dictionnary of comments_information
    dict_of_comment = dict()
    ##initialize a dict first
    dict_of_comment['author'] = []
    dict_of_comment['comment'] = []
    dict_of_comment['reply'] = []
    dict_of_comment['date_time'] = []
    dict_of_comment['nbr_likes'] = []
         
 
    #get first 10 items from 20 comments 
    items = response["items"][:min(len(response["items"]),MAX_NBR_COM)]
    
    
    for item in items:
        #the top level comment can have sub reply comments
        item_info = item["snippet"]  
        topLevelComment = item_info["topLevelComment"]
        comment_info = topLevelComment["snippet"]
        
        
        comment_info_rep = dict()
        comment_info_rep['textDisplay'] = ''
        
        if "replies" in item.keys():
            item_info_rep = item["replies"]############
            comment_rep = item_info_rep["comments"]
            
            for x in comment_rep:
                if 'snippet' in x.keys():
                    comment_info_rep = x['snippet']
                    break
        
        
        #the top level comment can have sub reply comments

        
        dict_of_comment['author'].append(comment_info['authorDisplayName'])
        dict_of_comment['comment'].append(comment_info['textDisplay'])
        dict_of_comment['reply'].append(comment_info_rep['textDisplay'])############
        dict_of_comment['date_time'].append(comment_info["likeCount"])
        dict_of_comment['nbr_likes'].append(comment_info['publishedAt'])
    
                     
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 