# tlgroup-test

Для запуска тестового задания в контейнерах используйте
docker-compose для тестового развёртывания, и docker-compose.prod
для развёртывания на реальном сервере при помощи nginx
Перед этим внесите изменения в файл settings согласно инструкции.
Для тестового задания использовалась база sqllite, но 
подготовлена возможность использовать Postgres на сервере.
В файле view.py app staff создан Endpoint для тестирования 
приложения и наполнения его данными.