from db_connect import connect
from db_get import get_details

conn=connect()


def farmer_search(range1=None,range2=None,district=None,mandal=None,crops=None):
    if range1 and range2 and district and mandal:
        pass
    elif district and mandal:
        print(get_details(conn,district,mandal))
    elif range1 and range2:
        pass
    elif crops:
        pass
    


if __name__=="__main__":
    farmer_search(range1=1,range2=2,district="Krishna",mandal="Kankipadu")