from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, delete
import sys


engine = create_engine('sqlite:////home/johnathan/Documents/Projetos/feirinha/db.sqlite3', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)


class Produto(Base):
    __table__ = Base.metadata.tables['hortifruti_produto']


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
    if len(sys.argv) > 1:
        csvpath = sys.argv[1]
    else:
        folderpath = "/home/johnathan/Documents/Projetos/hortifruti_scrapping/"
        filepath = "output/20210605_hortifrutiestrela.csv"
        csvpath = f'{folderpath}{filepath}'
    inserttable(Produto, engine, csvpath)          
