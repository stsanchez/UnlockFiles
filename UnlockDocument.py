import cx_Oracle

try:
    #Connect to the database and execute the query for get the information i need
    file_number = input("Enter your file number: ")
    conn = cx_Oracle.connect('SCHEMA', 'PASSWORD', 'USERNAME')
    c = conn.cursor()
    c.execute('''select * from table.upload_tramite
                where expediente = :exp and pending = 't'
                order by fecha_iniciado desc ''', exp = file_number)
    data = c.fetchone()
    
    #Check if i get information from the last query and update the information with the next query
    if data != None:
        try:
            c = conn.cursor()
            c.execute('''update table.upload_tramite
                    set pending = 'f', fecha_finalizado = sysdate 
                    where id = :id ''', id = data[0])

            print('Expediente destrabado')
            conn.commit()
            conn.close
            
        except:
            conn.rollback
            pass

    #If i dont get information is because everythig is allright
    else:
        print('No esta pendiente')
        pass

except:
    conn.close
    pass


