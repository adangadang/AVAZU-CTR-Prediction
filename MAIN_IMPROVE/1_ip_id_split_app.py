# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:52:53 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'other/train_df_app.csv'               # path to training file
test = 'other/test_df_app.csv' 

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('other/train_df_app_split.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,app_id,app_domain,app_domain_hf,app_category,device_id,device_ip,device_id_2,device_ip_2,device_model,device_type,device_conn_type,C14,img_size,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        hour = row['hour']

        C1 = row['C1']
        if (C1 in ['']):
            C1 = '1005'

        banner_pos = row['banner_pos']
        if (banner_pos in ['']):
            banner_pos = '0'

        app_id = row['app_id']
        if (app_id in ['']):
            app_id = '92f5800b'

        app_domain = row['app_domain']
        if (app_domain in ['']):
            app_domain = '2347f47a'
        app_domain_hf = app_domain[0:2] + app_domain[6:8]

        app_category = row['app_category']
        if (app_category in ['']):
            app_category = '0f2161f8'

        device_id = row['device_id']
        if (device_id in ['']):
            device_id = 'a99f214a'

        device_ip = row['device_ip']
        if (device_ip in ['']):
            device_ip = '6b9769f2'

        device_id_2 = row['device_id'][0:4]
        device_ip_2 = row['device_ip'][0:4]

        device_model = row['device_model']
        if (device_model in ['']):
            device_model = '1f0bc64f'

        device_type = row['device_type']
        if (device_type in ['']):
            device_type = '1'

        device_conn_type = row['device_conn_type']
        if (device_conn_type in ['']):
            device_conn_type = '0'

        C14 = row['C14']
        if (C14 in ['']):
            C14 = '21611'

        img_size = row['C15'] + '*' + row['C16']
        if (img_size in ['320*480', '480*320']):
            img_size = '480*320'
        if (img_size in ['768*1024', '1024*768']):
            img_size = '1024*768'

        C17 = row['C17']
        if (C17 in ['']):
            C17 = '2424'

        C18 = row['C18']
        if (C18 in ['']):
            C18 = '3'

        C19 = row['C19']
        if (C19 in ['']):
            C19 = '35'

        C20 = row['C20']
        if (C20 in ['']):
            C20 = '-1'

        C21 = row['C21']
        if (C21 in ['']):
            C21 = '23'
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_domain_hf),str(app_category),str(device_id),str(device_ip),str(device_id_2),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(img_size),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
 # -- test data -- #
start = datetime.now()
with open('other/test_df_app_split.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_domain_hf,app_category,device_id,device_ip,device_id_2,device_ip_2,device_model,device_type,device_conn_type,C14,img_size,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        hour = row['hour']
        
        C1 = row['C1']
        if (C1 in ['']):
            C1 = '1005'

        banner_pos = row['banner_pos']
        if (banner_pos in ['']):
            banner_pos = '0'

        app_id = row['app_id']
        if (app_id in ['']):
            app_id = '92f5800b'

        app_domain = row['app_domain']
        if (app_domain in ['']):
            app_domain = '2347f47a'
        app_domain_hf = app_domain[0:2] + app_domain[6:8]

        app_category = row['app_category']
        if (app_category in ['']):
            app_category = '0f2161f8'

        device_id = row['device_id']
        if (device_id in ['']):
            device_id = 'a99f214a'

        device_ip = row['device_ip']
        if (device_ip in ['']):
            device_ip = '6b9769f2'

        device_id_2 = row['device_id'][0:4]
        device_ip_2 = row['device_ip'][0:4]

        device_model = row['device_model']
        if (device_model in ['']):
            device_model = '1f0bc64f'

        device_type = row['device_type']
        if (device_type in ['']):
            device_type = '1'

        device_conn_type = row['device_conn_type']
        if (device_conn_type in ['']):
            device_conn_type = '0'

        C14 = row['C14']
        if (C14 in ['']):
            C14 = '21611'

        img_size = row['C15'] + '*' + row['C16']
        if (img_size in ['320*480', '480*320']):
            img_size = '480*320'
        if (img_size in ['768*1024', '1024*768']):
            img_size = '1024*768'

        C17 = row['C17']
        if (C17 in ['']):
            C17 = '2424'

        C18 = row['C18']
        if (C18 in ['']):
            C18 = '3'

        C19 = row['C19']
        if (C19 in ['']):
            C19 = '35'

        C20 = row['C20']
        if (C20 in ['']):
            C20 = '-1'

        C21 = row['C21']
        if (C21 in ['']):
            C21 = '23'
        
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_domain_hf),str(app_category),str(device_id),str(device_ip),str(device_id_2),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(img_size),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
