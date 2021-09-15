from connect_sf import cs
try:
    cs.execute("select * from demo_db.public.raw_facilities;")
    df = cs.fetch_pandas_all()
    df.info()
    print(df.to_string())
finally:
    cs.close()
ctx.close()
