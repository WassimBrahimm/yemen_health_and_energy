import snowflake.connector as sf
import pandas

ctx = sf.connect(
    user='wassimbraa',
    password='1Wassim23.',
    account='de08234.eu-central-1',
    warehouse='compute_wh',
    database='demo_db',
    schema='public'
)

cs = ctx.cursor()
