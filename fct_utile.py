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

'''
def build_video_req(api_key,video_id,MAX_NBR_COM):
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet",
        id="XTjtPc0uiG8"
        )
    response = request.execute()
    return response
'''    


def comments_to_json(list_of_videoLinks,MAX_NBR_COM,api_key):
    dict_multi_videoComments = dict()
    n = len(list_of_videoLinks)
    for l in range(0,n,1):
        video_id = list_of_videoLinks[l]
        res = build_res_req(api_key,video_id,MAX_NBR_COM)
        dict_multi_videoComments[list_of_videoLinks[l]] =  dict_comment_item(res,MAX_NBR_COM,video_id)
    fDump = open('file.json', 'w')
    json.dump(res, fDump)
    fDump.close()
        
    return dict_multi_videoComments  
    
 
    
 
def read_params(param_file):
    with open(param_file,'r') as f:
        params = yaml.safe_load(f)
    return params
  

#####New dict
# function extracting the object items, and returning a dictionnary dict_of_comment
def dict_comment_item(response,MAX_NBR_COM,video_id):
    #initialize the dictionnary of comments_information
    dict_of_comment = {'video_id':[],
                       'author_comm': [],
                       'text_comm':[],
                       'id_comm':[],
                       'nbr_likes':[],
                       'date_and_time':[],
                       'totalReplyCount':[],
                       'reply':{'author_rep':[],
                                'text_rep':[],
                                'id_rep':[],
                                'parent_id':[],
                                'date_and_time':[]
                               }
                      }
 
    items = response['items'][:min(len(response['items']),MAX_NBR_COM)]

    for item in items:
        #getting the id comment 'id_comm'
        comment_item_id = item['id']
        
        #getting comments from snippet
        item_info = item['snippet']  
        topLevelComment = item_info['topLevelComment']
        comment_info = topLevelComment['snippet']
        
        #getting the replies
        author_rep = []
        id_rep = []
        parent_id = []#############
        publishedAt = []
        rep =[]
        
        
        #In case we have a replies
        #n = nbr_of_replies
        
        if 'replies' in item.keys():
            n = len(item['replies']['comments'])
            for rc in range(0,n,1):
                item_info_rep = item['replies']
                
                aut_rep = item_info_rep['comments'][rc]['snippet']['authorDisplayName']
                id_reply = item_info_rep['comments'][rc]['id']
                text_rep = item_info_rep['comments'][rc]['snippet']['textDisplay']
                parent_com = item_info_rep['comments'][rc]['snippet']['parentId']
                date_published = item_info_rep['comments'][rc]['snippet']['publishedAt']

                
                author_rep.append(aut_rep)
                id_rep.append(id_reply)
                rep.append(text_rep)
                parent_id.append(parent_com)
                publishedAt.append(date_published)



                
        # Filling dict_of_comment
        #comment
        dict_of_comment['video_id'].append(video_id)
        dict_of_comment['author_comm'].append(comment_info['authorDisplayName'])
        dict_of_comment['text_comm'].append(comment_info['textDisplay'])
        dict_of_comment['id_comm'].append(comment_item_id)
        dict_of_comment['nbr_likes'].append(comment_info['likeCount'])
        dict_of_comment['date_and_time'].append(comment_info['publishedAt'])
        
        #reply
        dict_of_comment['reply']['author_rep'].append(author_rep)
        dict_of_comment['reply']['text_rep'].append(rep)
        dict_of_comment['reply']['id_rep'].append(id_rep)
        dict_of_comment['reply']['parent_id'].append(parent_id)
        dict_of_comment['reply']['date_and_time'].append(publishedAt)

    taille = len(dict_of_comment['author_comm'])
    return dict_of_comment


#fct to that return a dict to a df

def dict_to_df(key_list,dict_multi_videoComments,dict_of_dfs):

    for vi in key_list:
        
        result = pd.DataFrame(columns=['video_id','author_of_comment','comment','comment_id','parent_id'])
        vid_id = vi
        
        result_lev_1 = result.copy()   
        # comments
        result_lev_1['video_id'] = dict_multi_videoComments[vid_id]['video_id']
        result_lev_1['author_of_comment'] = dict_multi_videoComments[vid_id]['author_comm']
        result_lev_1['comment'] = dict_multi_videoComments[vid_id]['text_comm']
        result_lev_1['comment_id'] = dict_multi_videoComments[vid_id]['id_comm']
        
        # Replies
        result_lev_2 = result.copy()   
        reply = dict_multi_videoComments[vid_id]['reply']
        
        d = 0
        
        while d < len(reply['author_rep']):
       
            verif_empty_list = list(reply.values())[0][d]   
            if verif_empty_list == []:   
                d = d + 1
            else:
                df_temporary = pd.DataFrame()
                
                #get the columns
                vid_id = []
                author_of_comment = reply['author_rep'][d]
                comment = reply['text_rep'][d]
                comment_id = reply['id_rep'][d]
                parent_id = reply['parent_id'][d]
                
                #concatenat the columns
                df_temporary = pd.concat([pd.Series(vid_id),pd.Series(author_of_comment),pd.Series(comment),pd.Series(comment_id),pd.Series(parent_id)], axis =1)
                print('df_temporary', df_temporary)
                print('df_temporary col =',df_temporary.columns )
                df_temporary.columns = ['video_id', 'author_of_comment', 'comment', 'comment_id', 'parent_id']
    
                #concat with result_lev_2 df
                result_lev_2 = pd.concat([result_lev_2,df_temporary],  ignore_index=True)
                
                d = d + 1
    
        result = pd.concat([result_lev_1,result_lev_2],  ignore_index=True)
        dict_of_dfs[vi] = result
        
        return dict_of_dfs
    
    
    






'''
lenght_comm_df = len(dict_multi_videoComments[i]['author_comm'])# nbr of comment
lenght_rep_df = len(dict_multi_videoComments[i]['reply']['author_rep'])# nbr of replies
print('ceci est length rep df:',lenght_rep_df)
'''







