from db_tables import table
from db_connect import connect
from db_username_generator import create_username
from werkzeug.security import generate_password_hash,check_password_hash


def user_details(data):
    """ user details process in db"""
    conn=connect()
    user_name=create_username(data['Name'],data['PhNo'])
    password=generate_password_hash(data['PhNo'])

    values=list(data.values())

    # c=check_password_hash(password,data['PhNo'])
    user=table(conn,user_name,password,values)

    user.insert_details()
    # print(user.delete_details())
    # print(len(values),values[0:6],values[6:11],values[11:17],sep='\n')
    # print(values)


if __name__=="__main__":
    data={'Name': 'yesu babu', 'Age': '21', 'PhNo': '9849643914', 'Address': 'kankipadu', 'District': 'krishna', 'Mandal': 'kankipadu', 'place': 'kankipadu', 'identity': 'ownland','landarea':'30','cropkind':'cash', 'crop_select': 'Banana', 'crop1': 'tobacco', 'pro1': '40','crop2': 'ragi', 'Pro2': '30', 'crop3': 'wheat', 'pro3': '20'}
    user_details(data)