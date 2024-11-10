from __future__ import annotations
from Traductor import Traductor
from typing import List, Any, Union

class CreadorDeConsultas:
    def __init__(self) -> None:
        self.query_parts: List[str] = []
        self.translator: Traductor = Traductor()

    def select(self, *columns: str) -> CreadorDeConsultas:
        cols = ', '.join(columns) if columns else "*"
        self.query_parts.append(f"SELECT {cols}")
        return self

    def from_table(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"FROM {table_name}")
        return self

    def where(self, condition: str) -> CreadorDeConsultas:
        self.query_parts.append(f"WHERE {condition}")
        return self

    def group_by(self, *columns: str) -> CreadorDeConsultas:
        cols = ', '.join(columns)
        self.query_parts.append(f"GROUP BY {cols}")
        return self

    def order_by(self, *columns: str) -> CreadorDeConsultas:
        cols = ', '.join(columns)
        self.query_parts.append(f"ORDER BY {cols}")
        return self

    def having(self, condition: str) -> CreadorDeConsultas:
        self.query_parts.append(f"HAVING {condition}")
        return self

    def limit(self, limit_value: int) -> CreadorDeConsultas:
        self.query_parts.append(f"LIMIT {limit_value}")
        return self

    def update(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"UPDATE {table_name}")
        return self

    def delete_from(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"DELETE FROM {table_name}")
        return self

    def between(self, column: str, value1: Union[str, int, float], value2: Union[str, int, float]) -> CreadorDeConsultas:
        if "WHERE" in self.query_parts[-1]:
            self.query_parts[-1] += f" BETWEEN {value1} AND {value2}"
        else:
            self.query_parts.append(f"{column} BETWEEN {value1} AND {value2}")
        return self

    def alter_table(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"ALTER TABLE {table_name}")
        return self

    def drop_column(self, column_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"DROP COLUMN {column_name}")
        return self

    def create_table(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"CREATE TABLE {table_name}")
        return self

    def drop_table(self, table_name: str) -> CreadorDeConsultas:
        self.query_parts.append(f"DROP TABLE {table_name}")
        return self

    def to_sql(self) -> str:
        return ' '.join(self.query_parts) + ";"

    def to_usql(self) -> str:
        sql_query = self.to_sql()
        return self.translator.translate(sql_query, direction='sql_to_usql')

    def insert_into(self, table_name: str, *columns: str) -> CreadorDeConsultas:
        cols = ','.join(columns)
        self.query_parts.append(f"INSERT INTO {table_name}({cols})")
        return self

    def values(self, *values: Any) -> CreadorDeConsultas:
        vals = ','.join([f"'{v}'" if isinstance(v, str) else str(v) for v in values])
        self.query_parts.append(f"VALUES({vals})")
        return self

    def set(self, **values: Any) -> CreadorDeConsultas:
        set_values = ', '.join([
            f"{k} = {v}" if not isinstance(v, str) else f"{k} = '{v}'"
            for k, v in values.items()
        ])
        self.query_parts.append(f"SET {set_values}")
        return self

    def add_column(self, column_name: str, column_type: str) -> CreadorDeConsultas:
        self.query_parts.append(f"ADD COLUMN {column_name} {column_type}")
        return self

    def join(self, table_name: str, condition: str) -> CreadorDeConsultas:
        self.query_parts.append(f"JOIN {table_name} ON {condition}")
        return self

# Ejemplos de uso

query = CreadorDeConsultas().select("*").from_table("usuarios").where("edad > 18")
print(query.to_usql())
print(query.to_sql())

query = CreadorDeConsultas().insert_into("usuarios", "nombre", "edad").values("Juan", 25)
print(query.to_usql())
print(query.to_sql())

query = CreadorDeConsultas().update("empleados").set(salario=3000).where("puesto = 'ingeniero'")
print(query.to_usql())
print(query.to_sql())

query = CreadorDeConsultas().alter_table("empleados").add_column("direccion", "VARCHAR(255) NOT NULL")
print(query.to_usql())
print(query.to_sql())

query = CreadorDeConsultas().alter_table("empleados").drop_column("direccion")
print(query.to_usql())
print(query.to_sql())
