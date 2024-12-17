@echo off
setlocal

set "envFile=.env"
set "exampleFile=.env.example"

if exist "%envFile%" (
    echo Файл "%envFile%" уже существует.
) else (
    if exist "%exampleFile%" (
        echo Файл "%envFile%" не найден. Копирую содержимое из "%exampleFile%"...
        copy "%exampleFile%" "%envFile%"
        echo Файл "%envFile%" успешно создан из "%exampleFile%".
    ) else (
        echo Ошибка: Файл "%exampleFile%" не найден. Не удалось создать "%envFile%".
    )
)
docker compose up --build

pause
