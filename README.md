# Sprint_7
### API тесты на сервис по аренде самокатов https://qa-scooter.praktikum-services.ru/

### Описание тестов
## test_create_courier тесты создания курьера 
* test_create_courier_success - Успешная регистрация
* test_create_identical_couriers - Попытка повторной регистрации(учетная запись уже сущетсвует)
* test_create_courier_without_name_not_successful - Регистрация прошла успешно, заполнены только обязательные поля
* test_create_courier_without_login_or_pass_not_successful - Регистрация не прошла , не заполнены обязательные поля

## test_create_order тесты создания заказа
* test_create_order - Заказ самоката с различными цветами прошел успешно

## test_login_courier - тесты на авторизацию
* test_login_courier_success - При успешной авторизации возвращается id
* test_login_courier_incorrect_log_or_pass - Авторизация не проходит , неверный логин или пароль
* test_login_courier_empty_login_field - Авторизация не проходит , не передан логин
* test_login_courier_empty_pass_field - Авторизация не проходит, не передан пароль
* test_login_not_found_courier - Авторизация не проходит, пользователь не существует

## test_order_list - тест списка заказов
* test_order_list - Возврат списка заказов в тело ответа

