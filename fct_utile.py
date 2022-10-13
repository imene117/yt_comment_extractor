#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:36:07 2022

@author: hocine
"""
import pandas as pd
import yaml
from googleapiclient.discovery import build


def df_append(df,df_line):
    df = pd.concat([df, df_line], ignore_index=True, sort=False)
    return df


 
def extract_info_comment(item):
    item_info = item["snippet"]
    
    #the top level comment can have sub reply comments
    topLevelComment = item_info["topLevelComment"]
    comment_info = topLevelComment["snippet"]
    df_line = pd.DataFrame({'author':comment_info["authorDisplayName"],
                            'comment':comment_info["textDisplay"],
                            'date_time':comment_info["likeCount"],
                            'nbr_likes':comment_info['publishedAt']},index=[0])
    return df_line
    

def read_params(param_file):
    with open(param_file,'r') as f:
        params = yaml.safe_load(f)
    return params

def build_res_req(api_key,video_id,MAX_NBR_COM):
    #build a resource for youtube
    resource = build('youtube', 'v3', developerKey=api_key)
    #create a request to get 20 comments on the video
    request = resource.commentThreads().list(
                                part="snippet",
                                videoId=video_id,
                                maxResults= MAX_NBR_COM,   #get 20 comments
                                order="orderUnspecified")  #top comments.
    #execute the request
    response =request.execute()
    return response


def df_comments(MAX_NBR_COM,response):
    #get first 10 items from 20 comments 
    items = response["items"][:min(len(response["items"]),MAX_NBR_COM)]
     
    #Data frame containing author, comment, ...
    channel_data = pd.DataFrame(columns=['author','comment','date_time','nbr_likes'])
    ####
    
    for item in items:
        #the top level comment can have sub reply comments
        item_info = item["snippet"]
        topLevelComment = item_info["topLevelComment"]
        comment_info = topLevelComment["snippet"]
        
        df_line = extract_info_comment(item)
        
        channel_data = df_append(channel_data,df_line)
        
    return channel_data
        
        
        
        
        
        
        
        
