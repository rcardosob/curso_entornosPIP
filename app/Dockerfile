FROM python:3.9

WORKDIR /app 
#creamos un directorio

COPY requirements.txt /app/requirements.txt 
#buena práctica es copiar la lista de requerimientos.
#al copiar se pone dos veces, izquierda es local - derecha es contenedor
#le especifico que lo quiero en mi directorio app que recién cree arriba

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#le digo que instale mis requerimientos
#le digo que no instale la carpeta cache
#le digo upgrade, pero es solo para el pip

COPY . /app

CMD bash -c "while true; do sleep 1; done"
