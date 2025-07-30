# cinefacil
Descripción del sistema CineFácil
CineFácil es un sistema sencillo de gestión de venta de boletos para funciones de cine. Permite al usuario consultar las funciones disponibles, comprar boletos para una función específica, y consultar las reservas realizadas. Está diseñado para ser fácil de usar, con interacción por consola, facilitando la atención al cliente en la compra de boletos.

Lista de funciones del programa
ver_funciones(): Muestra la lista de funciones (películas) disponibles para compra.

nombre_cliente(): Solicita y valida el nombre del cliente para cada compra.

Atencion_cliente(): Función principal para manejar la compra de boletos; incluye selección de función, ingreso de cantidad de boletos, cálculo del total a pagar, y registro de la reserva.

mostrar_reserva(): Muestra todas las reservas realizadas con detalle del cliente, función, boletos comprados y total a pagar.

menu(): Presenta un menú interactivo que permite navegar entre las opciones del sistema: ver funciones, comprar boletos, mostrar reservas o salir.

Qué hice en la nueva rama y cómo hice el merge
En la rama ver-reservas agregué la función mostrar_reserva(), que permite visualizar de forma clara todas las reservas hechas por los clientes, mostrando datos relevantes como nombre, función, cantidad de boletos y total a pagar.

Para integrar los cambios, realicé un commit con un mensaje claro describiendo la adición de la función, luego hice un push forzado para actualizar la rama remota. Finalmente, abrí un Pull Request en GitHub para hacer el merge de ver-reservas con la rama principal main, asegurando que la función añadida quede disponible en la versión estable del proyecto.

Qué aprendí sobre Git y GitHub
Durante este proceso aprendí:

Cómo crear y trabajar con ramas para desarrollar nuevas funcionalidades sin afectar la rama principal.

La utilidad del comando git commit --amend para modificar mensajes de commits recientes.

La importancia de sincronizar la rama local con el repositorio remoto antes de hacer push.

Cómo usar git push --force para forzar la actualización de ramas remotas cuando el historial local ha cambiado (por ejemplo, tras un amend).

La creación y gestión de Pull Requests en GitHub para integrar cambios de ramas de desarrollo a la rama principal.

A solucionar conflictos y errores comunes relacionados con archivos de bloqueo y estados de repositorios.
