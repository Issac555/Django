
@echo off
echo ==========================
echo   MIGRACIONES DE DJANGO
echo ==========================

cd sistema
python manage.py makemigrations
if errorlevel 1 goto error

python manage.py migrate
if errorlevel 1 goto error

echo ==========================
echo   INICIANDO SERVIDOR
echo ==========================

python manage.py runserver
goto fin

:error
echo ERROR: No se pudo completar el proceso.
pause

:fin
