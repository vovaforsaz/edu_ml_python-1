import psycopg2
import pandas as pd
import pandas.io.sql as psql
from log import all_logs
from psycopg2 import OperationalError
log = all_logs()

class Bd_pg():

    def create_connection(self,db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            log.info_log("Connection to PostgreSQL DB successful", 'bd')
        except OperationalError as e:
            log.error_logs(f"The error '{e}' occurred", 'bd')
        return connection

    def Get_the_result(self,connect,script):
        log.info_log(f"Get_the_result connect '{connect}' and '{script}'", "bd")
        cursor = connect.cursor()
        log.info_log(f"Get_the_result cursor '{cursor}", "bd")
        cursor.execute(script)
        record = cursor.fetchone()
        log.info_log(f"Get_the_result record '{record}", "bd")
        return record

    def Get_the_result_two(self,script,connect):
        log.info_log(f"Get_the_result_two connect '{connect}' and '{script}'", "bd")
        search = pd.read_sql(script, connect)
        log.info_log(f"Get_the_result_two search '{search}'", "bd")
        return search

    def update(self,script,connect):
        log.info_log(f"update connect '{connect}' and '{script}'", "bd")
        cursor = connect.cursor()
        cursor.execute(script)
        connect.commit()
        count = cursor.rowcount
        log.info_log(f"update count - '{count}'", "bd")
        return count