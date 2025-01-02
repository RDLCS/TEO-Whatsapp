from typing import List,DefaultDict,Dict,Tuple,Set,Optional,NamedTuple
from datetime import date,time,timedelta,datetime
import csv

Mensaje = NamedTuple('Mensaje', [('fecha', date), ('hora', time), ('usuario', str), ('texto', str)])

def lee_mensajes(ruta:str)->List[Mensaje]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f,delimiter='*')
        for entero in iter:
            if entero!=[]:
                separado=entero[0].split(' - ')
                fecha_hora=parseo_fecha_hora(separado[0])
                usuario_texto=parseo_usuario_texto(separado[1])
                lista.append(Mensaje(fecha_hora[0],fecha_hora[1],usuario_texto[0],usuario_texto[1]))
    return lista

def parseo_fecha_hora(txt:str)->Tuple[date,time]:
    lista=txt.split(', ')
    fecha=datetime.strptime(lista[0],'%d/%m/%y').date()
    hora=datetime.strptime(lista[1],'%H:%M').time()
    return (fecha,hora)

def parseo_usuario_texto(txt:str)->Tuple[str,str]:
    lista=txt.split(': ')
    return (lista[0],lista[1])

def calcula_usuarios(mensajes:List[Mensaje])->List[str]:
    conjunto=set()
    for m in mensajes:
        conjunto.add(m.usuario)
    return sorted(conjunto)

def cuenta_mensajes_por_usuario(mensajes:List[Mensaje])->Dict[str,int]:
    dicc=DefaultDict(int)
    for m in mensajes:
        dicc[m.usuario]+=1
    return dicc

def cuenta_mensajes_por_meses(mensajes:List[Mensaje])->Dict[str,int]:
    dicc=DefaultDict(int)
    for m in mensajes:
        mes=m.fecha.month
        año=m.fecha.year
        fecha=str(mes)+'/'+str(año)
        dicc[fecha]+=1
    return dicc

def cuenta_mensajes_por_dia_semana(mensajes:List[Mensaje])->Dict[str,int]:
    dicc=DefaultDict(int)
    for m in mensajes:
        dicc[m.fecha.weekday()]+=1
    return dicc

def cuenta_mensajes_por_momento_del_dia(mensajes:List[Mensaje])->Dict[str,int]:
    dicc=DefaultDict(int)
    for m in mensajes:
        momento=parseo_momento_dia(m.hora.hour)
        dicc[momento]+=1
    return dicc

def parseo_momento_dia(hora:int)->str:
    if 7<=hora<=13:
        return 'MAÑANA'
    elif 13<hora<=20:
        return 'TARDE'
    elif 20<hora or hora<7:
        return 'NOCHE'
    
def calcula_media_horas_entre_mensajes(mensajes:List[Mensaje])->float:
    lista=list()
    nueva=list()
    for m in mensajes:
        final=datetime.combine(m.fecha,m.hora)
        lista.append(final)
    for h1,h2 in zip(lista[0:],lista[1:]):
        dif=(h2-h1).total_seconds()/3600
        nueva.append(dif)
    return sum(nueva)/(len(nueva)-1)

def genera_conteos_palabra_usuario_y_resto(mensajes:List[Mensaje],usuario:str)->Tuple[Dict[str,int],Dict[str,int]]:
    dicc=DefaultDict(int)
    dicc2=DefaultDict(int)
    for m in mensajes:
        if m.usuario==usuario:
            palabras=m.texto.split(' ')
            for p in palabras:
                dicc[p]+=1
        else:
            palabras=m.texto.split(' ')
            for p in palabras:
                dicc2[p]+=1
    return dicc ,dicc2

def genera_palabras_caracteristicas_usuario(mensajes:List[Mensaje])->Dict[str,float]: