import snowflake.connector as sf
import pandas

ctx = sf.connect(
    user='wassimbrahim',
    password='1Wassim23.',
    account='ga88781.eu-central-1',
    warehouse='compute_wh',
    database='demo_db',
    schema='public'
)

cs = ctx.cursor()
