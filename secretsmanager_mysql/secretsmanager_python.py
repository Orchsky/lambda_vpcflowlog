import mysql.connector
import boto3 
import json

sm_client = boto3.client('secretsmanager')

response = sm_client.get_secret_value(
    SecretId = "dev/orchsky/mysql"
)

secret_dict = json.loads(response['SecretString'])


mydb = mysql.connector.connect(
    host = secret_dict.get("host"),
    user = secret_dict.get("username"),
    password = secret_dict.get("password"),
    database = secret_dict.get("dbname")
)

mycursor = mydb.cursor()

sql = "INSERT INTO Orchsky (id, name) VALUES (%s, %s)"
val = (2, "Orchsky2")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted...")