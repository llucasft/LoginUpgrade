import pyodbc


def connector():
    data_conn = (
        "Driver={SQL Server};"
        "Server=DESKTOP-G90E8IG\SQLSERVER;"
        "Database=all_data;"
        "Trusted_Connection=Yes"
    )

    conn = pyodbc.connect(data_conn)

    cursor = conn.cursor()
    return cursor


def register():
    cursor = connector()
    usuario = dict()
    usuario['nome'] = input('Digite seu nome: ')
    usuario['nick'] = input('Digite seu nick: ')

    registered = verifier(usuario['nick'])

    if registered:
        print('Usuário já cadastrado. ')
        return

    usuario['senha'] = input('Digite sua senha: ')

    command = f"""INSERT INTO usuarios(nome, nick, senha)
    VALUES ('{usuario["nome"]}', '{usuario["nick"]}', '{usuario["senha"]}')"""

    cursor.execute(command)
    cursor.commit()


def verifier(user):
    registered = False
    cursor = connector()
    string_sql = """
            SELECT * FROM usuarios;
        """
    cursor.execute(string_sql)
    lines = cursor.fetchall()

    for line in lines:

        if user == line[1]:
            registered = True
            break

    return registered


def login():
    cursor = connector()

    string_sql = """
        SELECT * FROM usuarios;
    """
    cursor.execute(string_sql)
    lines = cursor.fetchall()

    logged = {}
    online = False
    nick = input('Digite seu nick: ')

    for line in lines:

        if nick == line[1]:
            logged['nome'] = line[0]
            logged['nick'] = line[1]
            logged['senha'] = line[2]
            online = True
            break

    if not online:
        print('Usuário não cadastrado. ')
        return

    senha = input('Digite sua senha: ')

    if senha != logged['senha']:
        print('Usuário ou senha incorreto. ')
        return

    print(f'Bem vindo(a) {logged["nome"]}')


def main():
    opcao = int(input(
        "Digite a opção:\n* 1 - Login\n* 2 - Cadastro\n* 3 - Sair\n-> "
    ))

    if opcao == 1:
        login()
        main()

    elif opcao == 2:
        register()
        main()

    else:
        print("Saindo!")


if __name__ == '__main__':
    main()
