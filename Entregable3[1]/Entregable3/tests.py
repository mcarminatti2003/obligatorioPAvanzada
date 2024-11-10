import unittest
from APIConsultas import CreadorDeConsultas

class TestCreadorDeConsultas(unittest.TestCase):

    def setUp(self) -> None:
        self.builder: CreadorDeConsultas = CreadorDeConsultas()

    def test_select_simple(self) -> None:
        query = self.builder.select("*").from_table("usuarios").where("edad > 18")
        self.assertEqual(query.to_usql(), "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;")
        self.assertEqual(query.to_sql(), "SELECT * FROM usuarios WHERE edad > 18;")

    def test_insert_simple(self) -> None:
        query = self.builder.insert_into("usuarios", "nombre", "edad").values(" Juan ", 25)
        self.assertEqual(query.to_usql(), "METE EN usuarios (nombre, edad) LOS VALORES (' Juan ', 25);")
        self.assertEqual(query.to_sql(), "INSERT INTO usuarios(nombre,edad) VALUES(' Juan ',25);")

    def test_update_simple(self) -> None:
        query = self.builder.update("empleados").set(salario=3000, puesto="ingeniero")
        self.assertEqual(query.to_usql(), "ACTUALIZA empleados SETEA salario = 3000, puesto = ' ingeniero ';")
        self.assertEqual(query.to_sql(), "UPDATE empleados SET salario = 3000, puesto = 'ingeniero';")

    def test_delete_simple(self) -> None:
        query = self.builder.delete_from("clientes").where("edad > 18")
        self.assertEqual(query.to_usql(), "BORRA DE LA clientes DONDE edad > 18;")
        self.assertEqual(query.to_sql(), "DELETE FROM clientes WHERE edad > 18;")

    def test_alter_table_add_column(self) -> None:
        query = self.builder.alter_table("empleados").add_column("direccion", "VARCHAR(255) NO NULO")
        self.assertEqual(query.to_usql(), "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR (255) NO NULO;")
        self.assertEqual(query.to_sql(), "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NO NULO;")

    def test_alter_table_drop_column(self) -> None:
        query = self.builder.alter_table("empleados").drop_column("direccion")
        self.assertEqual(query.to_usql(), "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;")
        self.assertEqual(query.to_sql(), "ALTER TABLE empleados DROP COLUMN direccion;")

    def test_complex_query_with_group_and_having(self) -> None:
        query = self.builder.select("COUNT(*)").from_table("ventas").group_by("producto").having("COUNT(*) > 5")
        self.assertEqual(query.to_usql(), "TRAEME CONTANDO (TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO (TODO) > 5;")
        self.assertEqual(query.to_sql(), "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;")

    def test_join_query(self) -> None:
        query = self.builder.select("*").from_table("pedidos").join("clientes", "pedidos.cliente_id = clientes.id").where("clientes.ciudad = ' Barcelona '")
        self.assertEqual(query.to_usql(), "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos . cliente_id = clientes . id DONDE clientes . ciudad = ' Barcelona ';")
        self.assertEqual(query.to_sql(), "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = ' Barcelona ';")

    def test_between_query(self) -> None:
        query = self.builder.select("*").from_table("clientes").where("edad BETWEEN 18 AND 25")
        self.assertEqual(query.to_usql(), "TRAEME TODO DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;")
        self.assertEqual(query.to_sql(), "SELECT * FROM clientes WHERE edad BETWEEN 18 AND 25;")

if __name__ == "__main__":
    unittest.main()
