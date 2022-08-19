DEFAULT_BACKEND = 'duckdb'
import os
import ibis
import pandas as pd


def duckdb_conn():
    conn = ibis.connect('duckdb://:memory:')

    dpath = '/home/patrick/dev/repos/ibis-tutorials/tutorials/farm_data'
    for file in os.listdir(dpath):
        if '.parquet' in file:
            conn.register(os.path.join(dpath, file), file.split('/')[-1].replace('.parquet', ''))
    return conn


def pandas_conn():
    dfs = dict()
    dpath = '/home/patrick/dev/repos/ibis-tutorials/tutorials/farm_data'
    
    for file in os.listdir(dpath):
        if '.parquet' in file:
            dfs[file.replace('.parquet', '')] = pd.read_parquet(os.path.join(dpath, file))

    conn = ibis.pandas.connect(dfs)
    return conn


def postgres_conn():
    return ibis.connect('postgres://ibistutorials@localhost:5432/pg-ibis')


FN_DICT = dict(
    duckdb=duckdb_conn()
    ,pandas=pandas_conn()
    ,postgres=postgres_conn()
)

def connect(backend=DEFAULT_BACKEND):
    return FN_DICT[backend]
