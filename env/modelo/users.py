from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine


users = Table("users", meta,
              Column("id",Integer, primary_key=True),
              Column("nombre", String(255), nullable=False),
              Column("apellido", String(255), nullable=False),
              Column("usuario", String(255), nullable=False),
              Column("contraseña", String(255), nullable=False),
              Column("cedula", String(255), nullable=False),
              Column("telefono", String(255), nullable=False),
              Column("direccion", String(255), nullable=False),
              Column("correo", String(255), nullable=False))


    
meta.create_all(engine)
