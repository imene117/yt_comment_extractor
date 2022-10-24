#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:36:07 2022

@author: hocine
"""
import pandas as pd
import yaml
from googleapiclient.discovery import build
import json

        


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

    
# function extracting the object items, and returning a dictionnary dict_of_comment
def dict_comment_item(response,MAX_NBR_COM):
    #initialize the dictionnary of comments_information
    dict_of_comment = dict()

    dict_of_comment['comment'] = {'text':[],
                                  'nbr_likes':[],
                                  'author': [],
                                  'totalReplyCount':[],
                                  'reply':{'id_rep':[],
                                           'text':[]
                                           }
                                  }
 
    #get first 10 items from 20 comments 
    items = response["items"][:min(len(response["items"]),MAX_NBR_COM)]
    
    for item in items:
        #getting the comments from snippet
        item_info = item["snippet"]  
        topLevelComment = item_info["topLevelComment"]
        comment_info = topLevelComment["snippet"]
        
        #getting the replies
        comment_info_rep = dict()
        comment_info_rep['textDisplay'] = ''
        comment_info_rep['parentId'] = ''
        
        nbr_of_replies = item_info["totalReplyCount"]#########
        rep =[]
        #In case we have a replies
        #n = nbr_of_replies
        
        if "replies" in item.keys():
            n = len(item["replies"]['comments'])
            for rc in range(0,n,1):
                item_info_rep = item["replies"]
                #comment_rep = item_info_rep["comments"]
                var_pb = item_info_rep["comments"][rc]['snippet']['textDisplay']
                rep.append(var_pb)
        
        #the top level comment can have sub reply comments
        dict_of_comment['comment']['text'].append(comment_info['textDisplay'])
        dict_of_comment['comment']['nbr_likes'].append(comment_info['likeCount'])
        dict_of_comment['comment']['author'].append(comment_info['authorDisplayName'])
        dict_of_comment['comment']['totalReplyCount'].append(nbr_of_replies)

        #reply
        dict_of_comment['comment']['reply']['id_rep'].append(comment_info_rep['parentId'])
        dict_of_comment['comment']['reply']['text'].append(rep)


    return dict_of_comment

def comments_to_json(list_of_videoLinks,response,MAX_NBR_COM):
    dict_multi_videoComments = dict()
    n = len(list_of_videoLinks)
    for l in range(0,n,1):
        dict_multi_videoComments[list_of_videoLinks[l]] =  dict_comment_item(response,MAX_NBR_COM)
    
    #json file to check the structur of comments vs replies B
    fDump = open('file.json', 'w')
    json.dump(response, fDump)
    fDump.close()
        
    return dict_multi_videoComments

    
    
 
def read_params(param_file):
    with open(param_file,'r') as f:
        params = yaml.safe_load(f)
    return params





































