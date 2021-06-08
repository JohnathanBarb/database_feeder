from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert, delete

engine = create_engine('sqlite:////home/johnathan/Documents/Projetos/feirinha/db.sqlite3', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)

class Produto(Base):
    __table__ = Base.metadata.tables['hortifruti_produto']


if __name__ == "__main__":
    table = Produto
    stmt = delete(table)
    with engine.begin() as conn:
        conn.execute(stmt)
    path = "/home/johnathan/Documents/Projetos/hortifruti_scrapping/output/""20210606_hortifrutiestrela.csv"
    with open(path, 'r') as _file:
        _file.readline()
        cont = 1
        while True:
            linha = _file.readline()            
            if not linha:
                break
            infos = str(linha).strip().split(';')
            ref = infos[0]
            descricao = infos[1]
            preco = infos[2].replace(',', '.')
            stmt = (
                insert(table).
                values(id=cont, ref_code=ref, descricao=descricao, preco=preco)
            )
            with engine.begin() as conn:
                conn.execute(stmt)
            cont += 1
