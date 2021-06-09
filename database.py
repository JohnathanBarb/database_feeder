from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, delete
import sys
import argparse


def deletetable(table, engine):
    stmt = delete(table)
    with engine.begin() as conn:
        conn.execute(stmt)


def inserttable(table, engine, csv):
    with open(csv, 'r') as _file:
        _file.readline()
        deletetable(table, engine)
        cont = 1
        stmts = []
        while True:
            linha = _file.readline()
            if not linha:
                break
            infos = str(linha).strip().split(';')
            ref = infos[0]
            descricao = infos[1]
            preco = infos[2].replace(',', '.')
            stmts.append( (
                insert(table).
                values(id=cont, ref_code=ref, descricao=descricao, preco=preco)
            ))
            cont += 1
        with engine.begin() as conn:
            for stmt in stmts:
                conn.execute(stmt)


if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="Feed a database using csv files.")
    parser.add_argument('--file', help="csv file")
    parser.add_argument('--database', help="database url")
    args = parser.parse_args()
    if args.database:
        urldatabase = args.database
    else:
        urldatabase = 'sqlite:////home/johnathan/Documents/Projetos/feirinha/db.sqlite3'
    engine = create_engine(urldatabase, echo=True)
    Base = declarative_base()
    Base.metadata.reflect(engine)

    class Produto(Base):
        __table__ = Base.metadata.tables['hortifruti_produto']

    if args.file:
        csvpath = args.file
    else:
        folderpath = "/home/johnathan/Documents/Projetos/hortifruti_scrapping/"
        filepath = "output/20210605_hortifrutiestrela.csv"
        csvpath = f'{folderpath}{filepath}'
    inserttable(Produto, engine, csvpath)         
