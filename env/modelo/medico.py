from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

medico = Table("medico", meta,
              Column("id",Integer, primary_key=True),
              Column("nombre", String(255), nullable=False),
              Column("apellido", String(255), nullable=False),
              Column("especialidad", String(255), nullable=False),
              Column("cedula", String(255), nullable=False),
              Column("telefono", String(255), nullable=False))
              
    
meta.create_all(engine)