from datetime import date

filename = 'accounts.txt'

def has_file(filename):
  try:
    file = open(filename, 'rt')
    file.close()
  except FileNotFoundError:
    return False
  
  return True

def create_file(filename):
  try:
    file = open(filename, 'wt+')
  except:
    print('Algum erro ocorreu com o método create_file')
  finally:
    file.close()

  print(f'Arquivo {filename} criado com sucesso!')

def write_lines(filename, lines):
  try:
    file = open(filename, 'w')
    file.writelines(lines)
  except:
    print('Algum erro ocorreu com o método write_lines')
  finally:
    file.close()

accounts = []

def update_accounts(account):
  accounts.append(account)

  lines = []
  for acc in accounts:
    lines.append(str(acc) + '\n')

  write_lines(filename, lines)

def load():
  if not has_file(filename):
    create_file(filename)

  try:
    file = open(filename, 'r')

    for line in file.readlines():
      accounts.append(eval(line.strip()))
  except:
    print('Algum erro ocorreu com o método load')
  finally:
    file.close()

load()

def has_account(login):
  for account in accounts:
    if account['login'] == login:
      return account
  
  return None

def register():
  name = input('Digite seu nome completo: ').strip()
  login = input('Digite seu login: ').strip()

  if has_account(login) is None:
    password = input('Digite sua senha: ').strip()
    email = input('Digite seu e-mail: ').strip()
    birthday = input('Digite sua data de nascimento (dd/mm/yyyy): ').strip()
    phone = input('Digite seu telefone: ').strip()
    address = input('Digite seu endereço (rua, número, complemento, bairro, cidade, CEP, ponto de referencia): ').strip().split(',')

    print('Cliente registrado!')

    return {
      'name': name,
      'login': login,
      'password': password,
      'email': email,
      'birthday': birthday,
      'phone': phone,
      'address': {
        'street': address[0],
        'number': address[1],
        'complement': address[2],
        'district': address[3],
        'city': address[4],
        'zip': address[5],
        'reference': address[6]
      }
    }
  else:
    print('Esta conta já está registrada!')

def get_costumer_data(login):
  account = has_account(login)
  if account is None:
    return None
  else:
    return f'Informações do cliente {login}\n\nNome: {account["name"]}\nLogin: {account["login"]}\nSenha: {account["password"]}\nE-mail: {account["email"]}\nData de nascimento: {account["birthday"]}\nCelular: {account["phone"]}\nRua: {account["address"]["street"]}\nNúmero: {account["address"]["number"]}\nComplemento: {account["address"]["complement"]}\nBairro: {account["address"]["district"]}\nCidade: {account["address"]["city"]}\nCEP: {account["address"]["zip"]}\nPonto de referência: {account["address"]["reference"]}'

def get_costumers():
  costumers = ''

  for account in accounts:
    costumers += f'{account["login"]}\n'

  return costumers.strip()

def report_generator():
  if not has_file('report.txt'):
    create_file('report.txt')
    
  lines = [f"Ata de Clientes\n\nA loja Marquinhos's Store possui {len(accounts)} clientes que seguem listados abaixo:\n"]

  for i in range(len(accounts)):
    lines.append(f'\n{i + 1}. {accounts[i]["name"]}')

  time = date.today()
  lines.append(f'\n\nRussas, {time.strftime("%d/%m/%Y")}')
  
  write_lines('report.txt', lines)

  print('Relatória gerado!')

while True:
  print('[1] Cadastrar cliente\n[2] Mostrar dados do cliente\n[3] Mostrar clientes registrados\n[4] Gerar relatório dos clientes\n[0] Sair')

  value = input('Opção: ')

  if value == '0':
    break
  elif value == '1':
    account = register()

    if account is None:
      print('Algo não ocorreu como esperado ao criar uma conta. Tente novamente!')
    else:
      update_accounts(account)  
  elif value == '2':
    costumer_login = input('Digite o login do cliente que você deseja ver: ')
    costumer_account = get_costumer_data(costumer_login)

    if costumer_account is None:
      print('Este cliente não está registrado!')
    else:
      print(costumer_account)
  elif value == '3':
    costumers = get_costumers()
    print(costumers)
  elif value == '4':
    report_generator()
  else:
    print('Opção inválida!')