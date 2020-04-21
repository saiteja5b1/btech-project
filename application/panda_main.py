from panda_data import data
import panda_average_crops
# import panda_yearly_crops
import panda_average_crops_districts
import pandas as pd

def main():

    """ main data manipulation entry for the application """

    crop_data=data() 
    average_crops=panda_average_crops.main(crop_data)
    average_crops_districtwise=panda_average_crops_districts.main(crop_data)
    # yearly_crops=panda_yearly_crops.main(crop_data)

    average_production=crop_data['production']/crop_data['area']
    average=pd.Series(average_production,name='per(1acre)')
    crop_data=pd.concat([crop_data,average],axis=1)
    label1=pd.Series(name="districtwise",dtype=int)
    label2=pd.Series(name="statewise",dtype=int)
    crop_data=pd.concat([crop_data,label1,label2],axis=1)
    
    rows=crop_data.shape[0]
    districts=crop_data['district_name'].unique()
    indices=average_crops_districtwise.index
    
    # for i in range(rows):
    #     crop_data[i,'districtwise']=i
    
    # count=0
    # for i in range(rows):
    #     value=tuple(crop_data.xs(i)[['season','district_name','crop']])
    #     if tuple(value) in indices:
    #         if crop_data.xs(i)['per(1acre)'] >= average_crops_districtwise.xs(value)['per(1acre)']:
    #             crop_data.xs(i)['districtwise']=1
    #         else:
    #             crop_data.xs(i)['districtwise']=0
                # print(count)
                # count=count+1
    # # print(crop_data)
    # for i in range(rows):
    #     if tuple(crop_data.xs(i)[['season','district_name','crop']]) in indices:
            
           
    # print(crop_data,average_crops,sep='\n')
    return(crop_data[['crop','per(1acre)']])

    
    # print(average_crops_districtwise.xs(indices[1])['per(1acre)'])


    # print(average_crops_districtwise,crop_data,sep='\n')

if __name__=="__main__":
    main()