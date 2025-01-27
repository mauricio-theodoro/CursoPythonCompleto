"""
Decoradores (Decorators)

O que são decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram os seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

|-----------------------------------|
|       Function Decorator          |
|-----------------------------------|

 -----------------------------------
| |-------------------------------| |
| |        Função decorada        | |
| |-------------------------------| |
 -----------------------------------
"""
"""
# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Loja Virtual!')

# Testando 1

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('Eu te odeio!!')

raiva_educada = seja_educado(raiva)

raiva_educada()
"""

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()

"""
|-------------------------------------------------------------|
|    Home ---- Serviços ---- Produtos ---- Adiministrativo    |
| ------------------------------------------------------------|

https://www.seusite.com.br/home
https://www.seusite.com.br/servicos
https://www.seusite.com.br/produtos
https://www.seusite.com.br/admin

# OBS: Não é funcional (Que funcione) é apenas um exemplo

def checa_login(request):
    if not request.usuario:
        redirect('https://www.seusite.com.br')
        
def home(request):
    return 'Pode aessar home'
    
def servicos(request):
    return 'Pode aessar serviços'
    
def produtos(request):
    return 'Pode aessar produtos'

@checa_login    
def admin(request):
    return 'Pode aessar admin'
    

"""

# OBS: Não confunda Decorator com Decorator Function
