from connect_sf import cs
try:
    cs.execute("SELECT * FROM demo_db.public.CLEAN_CLUSTER_FACILITY;")
    df = cs.fetch_pandas_all()
    df.info()
    print(df.to_string())
finally:
    cs.close()
# ctx.close()
