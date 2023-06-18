import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

host = config['mysql']['host']
root_user = config['mysql']['root_user']
password = config['mysql']['password']
database = config['mysql']['database']

#================= ok ===================
def CreateDatabase():
    try:
        strsql="CREATE SCHEMA IF NOT EXISTS `tsetmc_2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;"
        conn = mysql.connector.connect(
                host=host,
                user=root_user,
                password=password
            )
        cursor= conn.cursor()
        cursor.execute(strsql)
        cursor.close()
        createTable()

        return True
    except :
        return False    
    
#================= ok ===================

def test_mysql_connection():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=root_user,
            password=password,
            database=database
        )
        # Check if connection was successful
        if conn.is_connected():
            print(f"Connected to MySQL database {database}")
            with open("log.txt","a") as f:
                f.writelines(f"Connected to MySQL database {database} \n " )
            conn.close()
            return True
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        with open("log.txt","a") as f:
                f.writelines(f"Error connecting to MySQL database: {e} \n ")
        return False

def get_mysql_connection():
    connection = mysql.connector.connect(
        host=host,
        user=root_user,
        password=password,
        database=database,
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
    )
    return connection


def createTable():
    db =get_mysql_connection()
    # Create table if it doesn't exist
    cursor = db.cursor()
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS `symbol` (
                            `symbol_id` bigint NOT NULL,
                            `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                            `symbol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                            PRIMARY KEY (`symbol_id`)
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
                       """)
                            
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS `shenase_symbol` (
                        `id` bigint NOT NULL AUTO_INCREMENT,
                        `symbol_id` bigint NOT NULL,
                        `f1` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد 12 رقمی نماد',
                        `f2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد 5 رقمی نماد',
                        `f3` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'نام لاتین شرکت',
                        `f4` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد 4 رقمی شرکت',
                        `f5` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'نام شرکت',
                        `f6` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'نماد فارسی',
                        `f7` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'نماد 30 رقمی فارسی	',
                        `f8` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد 12 رقمی شرکت',
                        `f9` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'بازار',
                        `f10` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد تابلو',
                        `f11` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد گروه صنعت',
                        `f12` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'گروه صنعت',
                        `f13` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'کد زیر گروه صنعت	',
                        `f14` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'زیر گروه صنعت',
                        `avg_1` decimal(10,2) DEFAULT NULL COMMENT 'میانگین حجم ماه',
                        `avg_symbol` varchar(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'نماد میانگین حجم ماه',
                        `time` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `date` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        PRIMARY KEY (`id`),
                        KEY `ss_idx` (`symbol_id`),
                        CONSTRAINT `fkey_symbol_id` FOREIGN KEY (`symbol_id`) REFERENCES `symbol` (`symbol_id`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
                    """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS `symbol_daily` (
                        `id` bigint NOT NULL AUTO_INCREMENT,
                        `symbol_id` bigint DEFAULT NULL,
                        `f1` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f2` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f3` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f4` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f5` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f6` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f7` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f8` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f9` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f10` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f11` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f12` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f13` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f14` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f15` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f16` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f17` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f18` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f19` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f20` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f21` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f22` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f23` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f24` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f25` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f26` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f27` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f28` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f29` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f30` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f31` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f32` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f33` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f34` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f35` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f36` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f37` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f38` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f39` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f40` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f41` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f42` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `f43` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `time` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        `date` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                        PRIMARY KEY (`id`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=775125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
                   """)
"""
def InsertIntoTable(mydata, table_name):
    try:
        db = get_mysql_connection()
        cursor = db.cursor()

        placeholders = ', '.join(['%s'] * len(mydata[0]))
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"

        if table_name == "symbol":
            sql =f"INSERT INTO {table_name} (symbol_id,name) VALUES ({placeholders})" + " ON DUPLICATE KEY UPDATE name = VALUES(name)"

        print(sql, placeholders)
        
        cursor.executemany(sql, mydata)
        db.commit()
        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        print(f"Failed to insert into MySQL table {table_name}: {error}")

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("Database connection closed.")
"""
def InsertIntoTable(mydata,table_name):
    try:
        db=get_mysql_connection()
        cursor = db.cursor()    
        if table_name=="symbol":
            strins ="INSERT INTO  symbol (symbol_id,name) VALUES (%s,%s)  ON DUPLICATE KEY UPDATE name = VALUES(name)"
        elif table_name=="shenase_symbol":
            #strins="(symbol_id, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14,avg_1,avg_n,time,date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
            strins="INSERT INTO  shenase_symbol(symbol_id, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14,time,date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
            str1=""
        elif table_name=="symbol_daily":
            strins=""" INSERT INTO symbol_daily (symbol_id, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14,f15,f16,f17, f18, f19, f20, f21, f22,
                    f23, f24, f25, f26, f27, f28,f29, f30, f31, f32, f33, f34, f35, f36, f37,f38, f39, f40,f41, f42,f43,time,date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)
                            """
                    
            str1=""
        else:
            strins=""
            str1=""
        #sql = "INSERT INTO " + table_name  
        print(strins)
        cursor.executemany(strins, mydata )
        with open("log.txt","a") as f:
            f.writelines(f"INSERT INTO {table_name} \n " )
        db.commit()
        cursor.close()
        db.close()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        with open("log.txt","a") as f:
            f.writelines("Failed to insert into MySQL table {0} {1} \n ".format(table_name,error))
    
    finally:
            # Close database connection
            if db.is_connected():
                cursor.close()
                db.close()
                print("Database connection closed.")
#== ===============================================

