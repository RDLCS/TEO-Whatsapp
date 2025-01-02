from whatsapp import*

def test_lee_mensajes(mensajes:List[Mensaje])->None:
    print(len(mensajes))
    print(mensajes[0])

def test_calcula_usuarios(mensajes:List[Mensaje])->None:
    lista=calcula_usuarios(mensajes)
    print(f"Los usuarios de log son: {lista}")

def test_cuenta_mensajes_por_usuario(mensajes:List[Mensaje])->None:
    dicc=cuenta_mensajes_por_usuario(mensajes)
    for c,v in dicc.items():
        print(f"{c}: {v}")

def test_cuenta_mensajes_por_meses(mensajes:List[Mensaje])->None:
    dicc=cuenta_mensajes_por_meses(mensajes)
    for c,v in dicc.items():
        print(f'{c}: {v}')

def test_cuenta_mensajes_por_dia_semana(mensajes:List[Mensaje])->None:
    dias=['L','M','X','J','V','S','D']
    dicc=cuenta_mensajes_por_dia_semana(mensajes)
    nueva=sorted(dicc.items())
    for c,v in nueva:
        print(f'{dias[c]}: {v}')

def test_cuenta_mensajes_por_momento_del_dia(mensajes:List[Mensaje])->None:
    dicc=cuenta_mensajes_por_momento_del_dia(mensajes)
    for c,v in dicc.items():
        print(f'{c}: {v}')

def test_calcula_media_horas_entre_mensajes(mensajes:List[Mensaje])->None:
    media=calcula_media_horas_entre_mensajes(mensajes)
    print(f"La media entre los mensajes consecutivos es: {media}")

def test_genera_conteos_palabra_usuario_y_resto(mensajes:List[Mensaje],usuario:str)->None:
    dicc,dicc2=genera_conteos_palabra_usuario_y_resto(mensajes,usuario)
    for c,v in dicc.items():
        print(f"La palabra \"{c}\" fue usada")
        print(f"\t\t {v} por {usuario} y")
        print(f"\t\t {dicc2[c]} por el resto.")

if __name__=='__main__':
    whatsapp=lee_mensajes('data/bigbangtheory_es.txt')
    #test_lee_mensajes(whatsapp)
    #print('Test de calcula_usuarios')
    #test_calcula_usuarios(whatsapp)
    #print('Test de cuenta_mensajes_por_usuario')
    #test_cuenta_mensajes_por_usuario(whatsapp)
    #print('Test de cuenta_mensajes_por_meses')
    #test_cuenta_mensajes_por_meses(whatsapp)
    #print('Test de cuenta_mensajes_por_dia_semana')
    #test_cuenta_mensajes_por_dia_semana(whatsapp)
    #print('Test de cuenta_mensajes_por_momento_del_dia')
    #test_cuenta_mensajes_por_momento_del_dia(whatsapp)
    #print('Test de calcula_media_horas_entre_mensajes')
    #test_calcula_media_horas_entre_mensajes(whatsapp)
    print('Test de genera_conteos_palabras_usuario_y_resto')
    test_genera_conteos_palabra_usuario_y_resto(whatsapp,'Sheldon')