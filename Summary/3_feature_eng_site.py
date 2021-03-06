# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:52:53 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'other/train_df_site.csv'               # path to training file
test = 'other/test_df_site.csv' 

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('other/train_df_site_split.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_ip_2,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']

        site_id = row['site_id']
        site_domain = row['site_domain']
        site_category = row['site_category']

        device_id = row['device_id']
        device_ip = row['device_ip']
        device_ip_2 = device_id[0:4]
        device_model = row['device_model']
        device_type = row['device_type']
        device_conn_type = row['device_conn_type']
        C14 = row['C14']
        C15 = row['C15']
        C16 = row['C16']
        C17 = row['C17']
        C18 = row['C18']
        C19 = row['C19']
        C20 = row['C20']
        C21 = row['C21']
        '''
        if C1 in ['']:
            C1 = 'other'
        if banner_pos in ['']:
            banner_pos = 'other'
        if site_id in ['']:
            site_id = 'other'
        if site_domain in ['']:
            site_domain = 'other'
        if site_category in ['']:
            site_category = 'other'
        if device_id in ['']:
            device_id = 'other'
        if device_ip in ['']:
            device_ip = 'other'
        if device_ip_2 in ['']:
            device_ip_2 = 'other'
        if device_model in ['']:
            device_model = 'other'
        if device_type in ['']:
            device_type = 'other'
        if device_conn_type in ['']:
            device_conn_type = 'other'
        if C14 in ['']:
            C14 = 'other'    
        if C15 in ['']:
            C15 = 'other'
        if C16 in ['']:
            C16 = 'other'
        if C17 in ['']:
            C17 = 'other'
        if C18 in ['']:
            C18 = 'other'
        if C19 in ['']:
            C19 = 'other'
        if C20 in ['']:
            C20 = 'other'
        if C21 in ['']:
            C21 = 'other'   
        '''
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
        
 # -- test data -- #
start = datetime.now()
with open('other/test_df_site_split.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_ip_2,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        
        site_id = row['site_id']
        site_domain = row['site_domain']
        site_category = row['site_category']
        
        device_id = row['device_id']
        device_ip = row['device_ip']
        device_ip_2 = device_id[0:4]
        device_model = row['device_model']
        device_type = row['device_type']
        device_conn_type = row['device_conn_type']
        C14 = row['C14']
        C15 = row['C15']
        C16 = row['C16']
        C17 = row['C17']
        C18 = row['C18']
        C19 = row['C19']
        C20 = row['C20']
        C21 = row['C21']
        '''
        if C1 in ['']:
            C1 = 'other'
        if banner_pos in ['']:
            banner_pos = 'other'
        if site_id in ['']:
            site_id = 'other'
        if site_domain in ['']:
            site_domain = 'other'
        if site_category in ['']:
            site_category = 'other'
        if device_id in ['']:
            device_id = 'other'
        if device_ip in ['']:
            device_ip = 'other'
        if device_ip_2 in ['']:
            device_ip_2 = 'other'
        if device_model in ['']:
            device_model = 'other'
        if device_type in ['']:
            device_type = 'other'
        if device_conn_type in ['']:
            device_conn_type = 'other'
        if C14 in ['']:
            C14 = 'other'    
        if C15 in ['']:
            C15 = 'other'
        if C16 in ['']:
            C16 = 'other'
        if C17 in ['']:
            C17 = 'other'
        if C18 in ['']:
            C18 = 'other'
        if C19 in ['']:
            C19 = 'other'
        if C20 in ['']:
            C20 = 'other'
        if C21 in ['']:
            C21 = 'other'  
        '''    
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
