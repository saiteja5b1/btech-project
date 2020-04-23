from db_connect import connect
from db_get import get_details
import json

conn=connect()

def send_details(args):
    start=args['start']
    end=args['end']
    district=args['district']
    mandal=args['mandal']
    crops=json.loads(args['crops'])
    if start==''or start=='0':
        start=None
    if end=='' or end=='0':
        end=None
    if district=='':
        district=None
    if len(crops)==0:
        crops=None
    result=farmer_search(start,end,district,mandal,crops)
    # print(start,end,district,mandal,crops)
    return(result)


def farmer_search(range1=None,range2=None,district=None,mandal=None,crops=None):
    if range1 and range2 and district and mandal and crops:
        print('hai')
        pass
    elif district and mandal and crops:
        pass
    elif range1 and range2:
        pass
    elif district and mandal:
        result=get_details(conn,district,mandal)
        return(result)
    elif crops:
        pass
    else:
        pass
    


if __name__=="__main__":
    farmer_search(range1=1,range2=2,district="Krishna",mandal="Kankipadu")