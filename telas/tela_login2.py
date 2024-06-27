from flet import *

def main(page:Page):
    page.title="Login"
    page.bgcolor = "#FFDE59"
    imageLogin=Image(src="img_bee.png",width=200,height=200)
    imageGmail=Image(src="img_gmail.png",width=200,height=200)

    t_field_login = TextField(label="Login", icon=icons.EMOJI_NATURE)
    t_field_passWord = TextField(label="PassWord",color="white", icon=icons.PASSWORD, password=True)
    btn_enter = ElevatedButton(text="Entrar", icon=icons.EMOJI_EMOTIONS_OUTLINED,color="black")
    t_field_esqueci = TextButton(text="Esqueci minha senha")


    lineImg=Row(controls=[imageLogin],alignment=MainAxisAlignment.CENTER)
    line1 = Row(controls=[t_field_login], alignment=MainAxisAlignment.CENTER)
    line2 = Row(controls=[t_field_passWord], alignment=MainAxisAlignment.CENTER)
    line3 = Row(controls=[btn_enter], alignment=MainAxisAlignment.CENTER)
    line4 = Row(controls=[t_field_esqueci],alignment=MainAxisAlignment.CENTER)
    lineImg2 = Row(controls=[imageGmail], alignment=MainAxisAlignment.CENTER)

    coluna = Column(controls=[lineImg,line1, line2, line3,line4,lineImg2])

    page.add(coluna)
    page.update()

if __name__ == '__main__':
    app(target=main)
