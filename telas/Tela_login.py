from flet import *

colorPrimary="#5d305f"
secondecolor="#77457a"
colorBar="#0A0A0D"
fontColor="#ffffff"
colorTeste="#734636"
backgroundColor="#ffffff"


def main(page:Page):
    page.title="Login"
    page.window_min_width=360
    page.window_center()
    page.bgcolor=backgroundColor
    imageLogin=Image(src="img_login.png",width=200,height=200)

    t_field_login=TextField(label="Login",icon=icons.LOGIN_SHARP)
    t_field_passWord=TextField(label="PassWord",icon=icons.PASSWORD,password=True)
    btn_enter=ElevatedButton(text="Enter",
                                    width=300,
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(radius=0),
                                        bgcolor={
                                            MaterialState.DEFAULT:secondecolor,
                                            MaterialState.HOVERED:colorPrimary
                                        },
                                        color=fontColor

                                    )
                                    )

    lineImg=Row(controls=[imageLogin],alignment=MainAxisAlignment.CENTER)
    line1=Row(controls=[t_field_login],alignment=MainAxisAlignment.CENTER)
    line2=Row(controls=[t_field_passWord],alignment=MainAxisAlignment.CENTER)
    line3=Row(controls=[btn_enter],alignment=MainAxisAlignment.CENTER)

    # o controls do column tem que ser uma lista
    coluna=Column(controls=[lineImg,line1,line2,line3])


    # controls permite que eu trabalhe com mais de um container
    # page.add(t_field_login,t_field_passWord,btn_enter)

    page.add(coluna)
    page.update()

if __name__ == '__main__':
    app(target=main)