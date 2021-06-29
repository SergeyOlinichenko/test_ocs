# Тестовое задание для AQA OCS 

API для работы с файлом users.csv, методы:

**GET /users** - возвращает всех пользователей из users.csv

**GET /users/userid** - возвращает данные пользователя с id = userid
 
**POST /users** - создает новую запись в users.csv, обязательные поля в json: 
  first_name - имя пользователя 
  last_name - фамилия пользователя 
  age - возраст пользователя 
 
**DELETE /users** - принимает json с значением id и удаляет запись с этим id

**DELETE /users/userid** - удаляет запись с id = userid
  
API сделано через flask, требуемые библиотеки в requirements.txt
