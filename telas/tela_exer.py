#Criar uma aplicação que vai pegar o nome e o endereço da pessoa, pegue a rua, numero, bairro, cep separados, e vai mostrar na tela em dois elementos Text:Nome:
#Nome: Carlos
#Endereço: Rua srrsrrs Numero srsr CEP:00000

from  flet import Page,TextField,ElevatedButton,app,Text

def main(pagina:Page):
    # esse parametro vai ter tudo que uma Page faz e tem
    pagina.title="Tela 3"
    # usando o window_max, quer dizer que você so pode abrir ate essa medida
    pagina.window_max_width=600
    pagina.window_max_height=700
    # essa é a largura real dela
    pagina.window_width=600
    pagina.window_height=700
    # Definindo o tamanho minimo
    pagina.window_min_width=400
    pagina.window_min_height=550
# posso carregar o meu projeto no centro da tela
    pagina.window_center()
    pagina.bgcolor="#FFFAF0"
    #Colocando elementos na tela
    # vai me pertimir pegar dados da tela
    t_field_nome=TextField(label="Digite o seu nome")
    t_field_cep=TextField(label="Digite o seu CEP")
    t_field_numero=TextField(label="Digite o numero")
    t_field_rua=TextField(label="Digite a rua")
    t_field_bairro=TextField(label="Digite o bairro")
    # o text é o texto que aparece dentro do botão
    btn_calcular=ElevatedButton(text="Cadastrar")
    def cadastrando(e):
        # eu posso pegar o valor de dentro do TextField usando o atributo value
        txt_resposta.value=(f"Nome: {t_field_nome.value}")
        txt_respostaa.value=(f"Rua {t_field_rua.value} numero {t_field_numero.value} do CEP {t_field_cep.value}")
        # Limpando os campos ja digitados
        t_field_nome.value=""
        t_field_nome.update()
        t_field_cep.value=""
        t_field_cep.update()
        t_field_rua.value=""
        t_field_rua.update()
        t_field_numero.value=""
        t_field_numero.update()
        t_field_bairro.value=""
        t_field_bairro.update()
        txt_resposta.update()
        txt_respostaa.update()

# todo evento é construido dentro de uma função
    btn_calcular.on_click=cadastrando

    # o value vai ser o valor inicial do nosso texto
    # o size vai modificar o tamanho do texto
    txt_resposta=Text(value="Resposta",size=30)
    txt_respostaa=Text(value="Resposta",size=30)

    # estou usando o add para adicionar elementos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_cep)
    pagina.add(t_field_numero)
    pagina.add(t_field_bairro)
    pagina.add(t_field_rua)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)
    pagina.add(txt_respostaa)

# ela carrega a nossa pagina, ou no nosso projeto
 # ela é resposavel de determinar se vai ser uma aplicação local ou web
app(target=main)