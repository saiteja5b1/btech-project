from db_tables import table
from db_connect import connect
from db_username_generator import create_username
from werkzeug.security import generate_password_hash,check_password_hash
from db_insert import insert_details,delete_details


def user_details(data):
    """ user details process in db"""
    conn=connect()
    user_name=create_username(data['Name'],data['PhNo'])
    pass_word=generate_password_hash(data['PhNo'])
    # c=check_password_hash(password,data['PhNo'])

    values=list(data.values())

    # # process1
    user=table(conn,user_name,pass_word)
    user.user_login_details()
    user.user_personal_details(values[0:6])
    user.user_agro_details(values[6:12])
    user.user_crop_details(values[12:21])   

    # procss2
    # user=table(conn,user_name,pass_word,values)
    # user.insert_details()
    # user.delete_details()

    # process3
    # insert_details(conn,user_name,pass_word,values)
    # delete_details(conn)


if __name__=="__main__":
    # data={'Name': 'sai teja yaragani', 'Age': 21, 'PhNo': '9848643914', 'Address': 'kankipadu', 'District': 'krishna', 'Mandal': 'kankipadu', 'place': 'kankipadu', 'identity': 'ownland','landarea':30,'culture':'Monoculture','cropkind':'cash', 'crop_select': 'Banana', 'date1': '16/04/2020', 'crop1': 'tobacco', 'pro1': 40, 'date2': '17/04/2020', 'crop2': 'ragi', 'Pro2': 30, 'date3': '18/04/2020', 'crop3': 'wheat', 'pro3': 20}
    user_details(data)