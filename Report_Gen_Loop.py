import pandas as pd
import numpy as np
import sys, os
import Report_Generator_v1 as RepGen

pd.set_option('display.max_colwidth',None)
base_path = r'C:\Users\Laf User\Downloads\Reports_Round_1'
positions = os.listdir(base_path)
files_to_eval = pd.DataFrame(columns = ["Reports Found"])
for p in positions:
    path2 = os.path.join(base_path,p)
    list2 = os.listdir(path2)
    for n in list2:
        path3 = os.path.join(path2,n)
        list3 = os.listdir(path3)
        for AD in list3:
            path4 = os.path.join(path3,AD)
            list4 = os.listdir(path4)
            for line in list4:
                report_name_string = "PotCaptureReport"+str(p)+"_"+str(n)+"_"+str(AD)+"_"+str(line)
                finalpath = os.path.join(path4,line)
                finalpath = os.path.join(finalpath,"report.csv")
                
                files_to_eval = pd.concat([files_to_eval,new_file_to_eval])
                # raw_data = pd.read_csv(finalpath,sep='delimiter', header=None,names=["1", "2", "3", "4", "5", "6", "7","8","9", "10", "11", "12", "13", "14","15", "16", "17", "18","19"])
                
                raw_data = pd.read_csv(finalpath,skiprows=3,header=None)
                new_header = raw_data.iloc[0]
                raw_data = raw_data[1:]
                raw_data.columns = new_header
                raw_data.to_csv("report_test.csv")
                print(files_to_eval)
                print(raw_data.columns)
                print(len(raw_data.columns))
                #RUN ANALYSIS & TESTS
                # print(RepGen.GenResults(raw_data))   
                #             
                new_file_to_eval = pd.DataFrame(columns= ["Reports Found"], data = [[finalpath]])
#formation