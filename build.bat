@echo off
setlocal

set "envFile=.env"
set "exampleFile=.env.example"

if exist "%envFile%" (
    echo "%envFile%" exists
    docker compose up --build
) else (
    if exist "%exampleFile%" (
        echo "%envFile%" not found. Copying from "%exampleFile%"...
        copy "%exampleFile%" "%envFile%"
        echo "%envFile%" created by copying from "%exampleFile%".
        docker compose up --build
    ) else (
        echo Error: "%exampleFile%" not found.
    )
)

pause
