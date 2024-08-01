def loginUsuario(perfil):
    usuarios = perfil[0]
    for e in perfil:
        if e == 'admin':
            print('Bem-vindo, Administrador')
        else:
            print('Bem-vindo, Usuário')
    return usuarios

listaDeUsuarios = [x.lower() for x in ['Admin','admin','User','usuario','uSuario','aDMIN']]
users = loginUsuario(listaDeUsuarios)
print('A'.lower())
