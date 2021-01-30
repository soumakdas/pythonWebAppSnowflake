from snowflake import connector

def sfconnect():
    cnx = connector.connect(
        account='ur36139.us-central1.gcp',
        user='soumak',
        password='Soumak94',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC',
        role='ACCOUNTADMIN')
    return cnx