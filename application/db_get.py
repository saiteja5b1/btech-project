import psycopg2

def get_details(connection,*arg):
    """ table for storing user agro details """
    command="""
    select fullname,district,mandal from user_personal_details where district=%s and mandal=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(arg[0],arg[1],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)