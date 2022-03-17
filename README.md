# TestManager
API для составления и прохождения тестов


## API
Авторизация
```
/auth/users/ - Создание пользователя

/auth/jwt/create - Генерация токенов
/auth/jwt/refresh - Обновление токена
```


```
/testapp/tests/ - Все тесты
/testapp/tests/<int:id>/ - Вопросы к тесту
    
/testapp/tests/question/<int:id>/ - Информация о вопросе
/testapp/tests/question/<int:id>/choices/ - Варианты ответа
            
/testapp/tests/answer/ - Ответить на вопрос
            
{
    "selected_answer": id варианта ответа,
    "text": "Ответ на текстовый вопрос"
}
            
            
/testapp/tests/passed/ - Пройденные тесты пользователя
/testapp/tests/passed/add - Добавить тест в пройденные
/testapp/tests/<int:test_id>/answers/ - Ответы пользователя на тест

/testapp/tests/passed/filters/user=id_пользователя&test=id_теста
```

Некоторые права доступа временно изменены для упрощения.
