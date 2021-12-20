from wsgiref import simple_server

from composites.service_api import create_app


# Написать отдельные эндпоинты для message и user
# Добавить сериализацию/десериализацию для них
# Создание/удаление/изменение данных только через эндпоинты


app = create_app()
httpd = simple_server.make_server('0.0.0.0', 1234, app)
httpd.serve_forever()
