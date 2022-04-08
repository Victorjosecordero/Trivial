import imp
import os
from telnetlib import Telnet
from bottle import route,run,TEMPLATE_PATH,jinja2_view,static_file,request,redirect
import sqlite3

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__), 'templates'))
BASE_DATOS = os.path.join(os.path.dirname(__file__),'base_datos.db')

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static')

@route('/')
@jinja2_view('home.html')
def hola():
    cnx = sqlite3.connect(BASE_DATOS)
    consulta = """SELECT p.id, p.nombre,p.apelllidos ,p.dni ,to2.descripcion,tn.descripcion 
                from persona p left join T_ocupacion to2 
                on p.id_ocupacion =to2.id left join T_numero tn on tn.id=p.id_numero """
    cursor = cnx.execute(consulta)
    filas = cursor.fetchall()
    cnx.close()
    return {"datos": filas}