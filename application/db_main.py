from db_connect import connect
import random,json
import pandas as pd

c=connect()
with open('datasets/dat.json','r') as f:
    mand_list=json.load(f)
dist_list=list(mand_list.keys()) 
# print(mand_list['Krishna'])

with open('datasets/crops.json','r') as g:
    crops=json.load(g)
# print(dist)
# print(random.choice(list(crops.keys())))

data=pd.DataFrame(columns=['name','crop','district','mandal'])
print(data)

def main():
    for i in range(1000):
        name='xxxxx'+str(i).zfill(5)
        crop=random.choice(list(crops.keys()))
        district=random.choice(dist_list)
        mandal=random.choice(mand_list[district])
        data=data.append({'name':name,'crop':crop,'district':district,'mandal':mandal},ignore_index = True)
    # print(data)
    print(data.groupby('crop')['crop'].count())

if __name__==if __name__ == "__main__":
    main()