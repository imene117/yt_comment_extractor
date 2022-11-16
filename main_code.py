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

#3- mow all parameteres are in params
MAX_NBR_COM = params['MAX_NBR_COM']
api_key = params["api_key"]
list_of_videoLinks = params['list_of_videoLinks'] # list of videos id 



if __name__ == '__main__':
  
    dict_multi_videoComments = fu.comments_to_json(list_of_videoLinks,MAX_NBR_COM,api_key)
    # Creating a dictionary
    dict_of_dfs = {}
    key_list =  list(dict_multi_videoComments.keys())    
    tables = fu.dict_to_df(key_list,dict_multi_videoComments,dict_of_dfs)
    
    '''
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




'''






















    
    
    
'''
    import pandas as pd
    #exp:
    df = pd.DataFrame({'Job position': [[1], [2, 3, 4], [5],[6,7,8],['f','l','k']], 
                       'Job type': [[11], [22, 33, 44],[55],[66,77,88],['ff','ll','kk']]})
    
    column_headers = list(df.columns.values)
    len_column_headers = len(column_headers)
    df2 = pd.DataFrame(columns=column_headers)
    
    for ch in range(0,len_column_headers,1):
        print(ch)
        
        #column fictive to be append:  explode the lists

        col_fic = df[column_headers[ch]].apply(pd.Series)
        
        #combine the columns
        oneCol = []
        colLength = len(col_fic.columns)
        print('taille de colLength',colLength)
        
        for c in range(0,colLength,1):
            print('val de c:', c)
            oneCol.append(col_fic[c])
            print('end of append')
            combined = pd.concat(oneCol, ignore_index=True)
            print('fin du combined')
        print('end first loop')

        df2[column_headers[ch]] = combined
        
        
        exp from
        #explode the lists
        jobs = df['Job position'].apply(pd.Series)# allow to explode the values of the list (each elt of the list in a colon)

        #combine the columns
        oneCol = []
        colLength = len(jobs)
        for c in range(colLength):
            oneCol.append(jobs[c])
            combined = pd.concat(oneCol, ignore_index=True)
        combined
  '''      
        
        
    
   

        
        
        
        
        
        
        
        
        
        
        
        
        
        