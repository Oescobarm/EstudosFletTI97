import flet as ft     #biblioteca

#vou usar essa função para criar o layout da pagina
def main(page:ft.Page):
    page.title="Qualquer coisa"
    #toda vez que eu alterar minha pagina eu devo dar um update
    tf_nome=ft.TextField(label="Digite seu nome")
    btn_cadastrar=ft.ElevatedButton(text="Cadastrar")
    page.add(tf_nome)
    page.add(btn_cadastrar)

    #criando o evento
    def enviarNome(e):
        print(tf_nome.value)

    btn_cadastrar.on_click=enviarNome

    page.update()

ft.app(main)

