from cesma_library_database.apps.estudiantes.models import Estudiantes
from cesma_library_database.apps.libros.models import Libros
from django.core.management.base import BaseCommand

def insert_data():
	Libros(nombre = 'apocalipsis', ISBN = '', codigo = '9788821170287', editorial = 'planeta', autor = 'Mario Mendoza', stock = '1', portada  = 'img/libros/images.jpg').save()
	Libros(nombre = 'El manuscrito encontrado en Accra', ISBN = '', codigo = '978-958-8789-06-4', editorial = 'Grijalbo', autor = 'Paulo Coehlo', stock = '1', portada  = '').save()
	Estudiantes(nombre_y_apellido = 'paula valentina barrero lopez', codigo = '3862', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Juan Pablo Barrios Suarez', codigo = '3617', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Juan Diego Ávila Cruz', codigo = '3744', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Daniela Arteaga Mendez', codigo = '3534', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Fransua Natalia Barrios Angulo', codigo = '3666', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Laura Nallely Carrillo Rodriguez', codigo = '3610', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Maria Jose Castañeda Peña', codigo = '3641', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Maria Alejandra Cerquera Gonzales', codigo = '3811', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Johan Sebastian Contreras Garcia', codigo = '3751', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Karen Nicol Galvez Uricohechea', codigo = '3631', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Sergio Gutierrez Tavera', codigo = '3885', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Estefania Guzman Quintero', codigo = '3715', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Mariana Ladino Valdes', codigo = '3661', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Juan Fernando Longas Romero', codigo = '3632', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Valentina Martinez Charry', codigo = '4478', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Juan Jose Murcia Rojas', codigo = '4531', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Alexandra Nuñez Esquivel', codigo = '4437', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Johan Sebastian Puentes Garcia', codigo = '4385', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Jaime Andres Rivera Triana', codigo = '4756', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Javier Alejandro Perez Montaña', codigo = '4772', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Lina Tatiana Patiño Infante', codigo = '4519', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Giselle Daniela Endo Sanmiguel', codigo = '3649', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Maria Fernanda Hinestroza Velasco', codigo = '3909', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Gabriela Valderrama Granados', codigo = '4678', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Luisa Fernanda Urrego Villalba', codigo = '4045', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Mike Alejandro Rodriguez Salguero', codigo = '4682', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Paula Andrea Peñuela Bohorquez', codigo = '4798', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Angie Vanessa Torres Casilimas', codigo = '4741', grado = '11A').save()
	Estudiantes(nombre_y_apellido = 'Lizeth Geraldine Acosta Duran', codigo = '4787', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Diana Camila Asmaza Romero', codigo = '4321', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Maria Paula Barrero Sierra', codigo = '4658', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Andres Felipe Possos Lozano', codigo = '4123', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Omar Yesid Carvajal Pulgarín', codigo = '4533', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Maria Alejandra Calderon Herrera', codigo = '4711', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Nataly Lorena Barrios Roldan', codigo = '4320', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Lina Maria Rojas Orjuela', codigo = '4189', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Julian Humberto Rojas Molina', codigo = '4142', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Isis Sofia Rodriguez Nieto', codigo = '4375', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Laura Sofia Parga Garcia', codigo = '4204', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Andres Felipe Pirban Lucumi', codigo = '4464', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Carlos Andres Ramirez Vanegas', codigo = '4613', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Nicolas Avila Galeano', codigo = '4306', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Maria Alejandra Calderon Herrera', codigo = '4711', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Paula Andrea Garcia Mogollón', codigo = '4418', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Estefania Labrador Sanchez', codigo = '4600', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Maria Alejandra Gonzales Gomez', codigo = '4806', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Laura Valentina Lopez Gonzalez', codigo = '4379', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Javier Steven Osuna Osuna', codigo = '4382', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Silvia Juliana Palma Sotelo', codigo = '4112', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Laura Andrea Palacios Fandiño', codigo = '4651', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Angela Maria Garcia Tovar', codigo = '4431', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Fabian Manuel Gil Camacho', codigo = '4604', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Laura Isabel Gomez Doncel', codigo = '4310', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Sharoon Sty´l Fierro Bautista', codigo = '4232', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Julieth Magaly Castro Gutierrez', codigo = '4367', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Yulian Lorenzo Castillo Calderon', codigo = '4712', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Vanessa Alexandra Bojaca Carrillo', codigo = '4212', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'David Andres Bustamante Arteaga', codigo = '4633', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Mayerli Cardozo Rodriguez', codigo = '4177', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Eduardo Carvajal Gomez', codigo = '4162', grado = '11B').save()
	Estudiantes(nombre_y_apellido = 'Paula Tatiana Godoy Barragan', codigo = '4179', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Santiago Arturo Hernandez Lizarazo', codigo = '4165', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Leidy Katherine Izquierdo Amaya', codigo = '4271', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Paula Andrea Izquierdo Amaya', codigo = '4272', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Chistofer Manzanera Cordoba', codigo = '4096', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Sollangie Valentina Manzanera Cordoba', codigo = '4097', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Juan Sebastian Media Roa', codigo = '4424', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Karen Vanessa Gutierrez Ricaurte', codigo = '4627', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Alejandro Gonzalez Alvaréz', codigo = '4070', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Jhon David Prieto Castro', codigo = '4318', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Lizbeth Tatiana Pinzon Leal', codigo = '4068', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Luisa Fernanda Ospina Moreno', codigo = '4199', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Andres Santiago Ordoñez Santos', codigo = '4520', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Gisel Karina Ñustes Arteaga', codigo = '4140', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Jose Daniel Murillo Barrios', codigo = '4414', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Olga Valentina Prieto Castro', codigo = '4317', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Juan Pablo Sea Urrea', codigo = '4194', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Julian David Vera Guzman', codigo = '4427', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Juan David Vargas Tafur', codigo = '4152', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Miguel Angel Torres Gomez', codigo = '4716', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Juan Sebastian Sosa Caro', codigo = '4276', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Santiago Santos Aleman', codigo = '4075', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Diego Alberto Santamaría Pachon', codigo = '4159', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Angelly Tatiana Sanabria Sandoval', codigo = '4190', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Alejandra Rojas Herran', codigo = '4158', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Jhon Kevin Rodriguez Vaquero', codigo = '4447', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Valentina Rincon Medallo', codigo = '4322', grado = '10A').save()
	Estudiantes(nombre_y_apellido = 'Miguel David Benitez Hernandez', codigo = '4044', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Juan Esteban Barbosa Villabon', codigo = '4680', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Maria Camila Aragon Serrano', codigo = '4704', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Estefania Bernal Perez', codigo = '4521', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Kevin Fernando Canencio Martinez', codigo = '4309', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Carlos Andres Cotes Cuchubo', codigo = '4336', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Angel De Dios Feria Prado', codigo = '4253', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Crlos Stiven Gomez Parra', codigo = '4720', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Anderson Estiven Herrera Ordoñez', codigo = '4120', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Juan Esteban Lopez Trujillo', codigo = '4754', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Maria Alejandra Jimenez Oviedo', codigo = '4803', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Angelly Vanessa Herrera Rojas', codigo = '4074', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Nicole Natalia Lozano Alvis', codigo = '4327', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Kenner David Miranda Serrano', codigo = '4636', grado = '10B').save()
	Estudiantes(nombre_y_apellido = 'Dallyz Janneth Mora Moreno', codigo = '4778', grado = '10B').save()

class Command(BaseCommand):
	def handle(self, **options):
		insert_data()