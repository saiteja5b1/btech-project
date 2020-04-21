import psycopg2

class table:
    def __init__(self,conn,username,password,values):
        """ initilization of db instance """
        self.connection=conn
        self.user_name=username
        self.pass_word=password
        self.data=values
        
    # def user_personal_details(self,args): 
    #     """ table for storing user personal details """ 

    #     self.command=""" 
    #     insert into user_personal_details(fullname,age,phonenumber,adress,state,district,mandal,username) values(%s,%s,%s,%s,%s,%s,%s,%s);
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command,(args[0],args[1],args[2],args[3],args[4],args[5],args[6],self.user_name))
    #         self.connection.commit()

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return(error)
    #     finally:
    #         if self.connection is not None:
    #             # self.connection.close()
    #             return("success")

    # def user_login_details(self):
    #     """ table for storing the user credentialls """

    #     self.command="""
    #     insert into user_login_details(username,password) values(%s,%s);
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command,(self.user_name,self.pass_word))
    #         self.connection.commit()


    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return(error)
    #     finally:
    #         if self.connection is not None:
    #             # self.connection.close()
    #             return("success")

    # def user_agro_details(self,args):
    #     """ table for storing user agro details """

    #     self.command="""insert into user_agro_details(username,placeofland,landtype,landarea,crop,kind) values(%s,%s,%s,%s,%s,%s);"""

    #     try:
    #         print(self.connection)
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command,(self.user_name,args[0],args[1],args[2],args[3],args[4]))
    #         self.connection.commit()


    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return(error)
    #     finally:
    #         if self.connection is not None:
    #             # self.connection.close()
    #             return("success")

        
    # def user_crop_details(self,args):
    #     """ table for storing user crop details """

    #     self.command="""insert into user_crop_details(username,crop1,production1,crop2,production2,crop3,production3) values(%s,%s,%s,%s,%s,%s,%s);"""

    #     try:
    #         print(self.connection)
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command,(self.user_name,args[0],args[1],args[2],args[3],args[4],args[5]))
    #         self.connection.commit()


    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             return("success")
        
 

    # def get_details(self):
    #     """ table for storing user agro details """
    #     self.command="""
    #     select type,crop from crops;       
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command)
    #         reult=self.cur.fetchall()

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             print(result)

    # def get_user_login_details(self):
    #     """ table for storing user login details """
    #     self.command="""
    #     select * from user_login_details;       
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command)
    #         self.result=self.cur.fetchall()
    #         print(self.result)

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             # print(result)


    # def get_user_personal_details(self):
    #     """ table for retrieving user personal details """
    #     self.command="""
    #     select * from user_personal_details;       
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command)
    #         self.result=self.cur.fetchall()
    #         print(self.result)

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             # print(result)


    # def get_user_agro_details(self):
    #     """ table for retrieving user agro details """
    #     self.command="""
    #     select * from user_agro_details;       
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command)
    #         self.result=self.cur.fetchall()
    #         print(self.result)

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             # print(result)


    # def get_user_crop_details(self):
    #     """ table for retrieving user crop details """
    #     self.command="""
    #     select * from user_crop_details;       
    #     """
    #     try:
    #         self.cur=self.connection.cursor()
    #         self.cur.execute(self.command)
    #         self.result=self.cur.fetchall()
    #         print(self.result)

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #             # print(result)

    def delete_details(self):
        """ table for retrieving user crop details """
        self.command="""
        delete from user_login_details;       
        """
        self.command1="""
        delete from user_agro_details;       
        """
        self.command2="""
        delete from user_personal_details;       
        """
        self.command3="""
        delete from user_crop_details;       
        """
        try:
            self.cur=self.connection.cursor()
            self.cur.execute(self.command)
            self.connection.commit()
            self.cur.execute(self.command1)
            self.connection.commit()
            self.cur.execute(self.command2)
            self.connection.commit()
            self.cur.execute(self.command3)
            self.connection.commit()
            

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return("success")


    def insert_details(self):
        """ table for storing the user credentialls """

        self.command1="""
        insert into user_login_details(username,password) values(%s,%s);
        """
        self.command2=""" 
        insert into user_personal_details(fullname,age,phonenumber,adress,state,district,mandal,username) values(%s,%s,%s,%s,%s,%s,%s,%s);
        """
        self.command3="""insert into user_agro_details(username,placeofland,landtype,landarea,crop,kind) values(%s,%s,%s,%s,%s,%s);"""
        self.command4="""insert into user_crop_details(username,crop1,production1,crop2,production2,crop3,production3) values(%s,%s,%s,%s,%s,%s,%s);"""
        try:
            self.cur=self.connection.cursor()
            self.cur.execute(self.command1,(self.user_name,self.pass_word))
            self.connection.commit()
            self.cur.execute(self.command2,(self.data[0],self.data[1],self.data[2],self.data[3],'ANDHRA PRADESH',self.data[4],self.data[5],self.user_name))
            print(self.data[0],self.data[1],self.data[2],self.data[3],'ANDHRA PRADESH',self.data[4],self.data[5],self.user_name)
            self.connection.commit()
            self.cur.execute(self.command3,(self.user_name,self.data[6],self.data[1],self.data[8],self.data[9],self.data[10]))
            self.connection.commit()
            print(self.user_name,self.data[6],self.data[1],self.data[8],self.data[9],self.data[10])
            self.cur.execute(self.command4,(self.user_name,self.data[11],self.data[12],self.data[13],self.data[14],self.data[15],self.data[16]))
            self.connection.commit()
            print(self.user_name,self.data[11],self.data[12],self.data[13],self.data[14],self.data[15],self.data[16])


        except (Exception, psycopg2.DatabaseError) as error:
            return(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return("success")