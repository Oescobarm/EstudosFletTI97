from flet import *

def main(page:Page):
    page.title="Trabalhando com Container"
    container1=Container(content=Column(controls=[
            Text( "LA MAQUINA",size=23,weight=FontWeight.W_600,color="#000000"),
            Text("zummmmmmmm",color="orange")
        ]),
#sei la
        width=200,
        height=200,
        margin=margin.all(20),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=10),
        image_src="uno.jpg",
        shadow=BoxShadow(
            spread_radius=10,  # bordinha branca antes da sombra
            blur_radius=25,  # desfoque
            offset=Offset(0, 0),  # trabalha nos X e Y
            blur_style=ShadowBlurStyle.OUTER,  # o tipo de shadow
        ),
        alignment=Alignment(0,0)  # ( x, y) o centro do valor é sempre o 0


    )

    container2=Container(content=Column(controls=[
        Row(controls=[Image(src="uno.jpg")], alignment=MainAxisAlignment.CENTER),
        Row(controls=[Text("LA MAQUINA", size=20)], alignment=MainAxisAlignment.CENTER),
        Row(controls=[Text("zummmmmmmmmmmmmmmmmmmm""zummmmmmmmmmm""zummm", width=200,
                           text_align=TextAlign.JUSTIFY)]
            )],
        horizontal_alignment="center"),
        width=200,
        height=200,
        margin=margin.all(20),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=10),
        shadow=BoxShadow(
            spread_radius=10,  # bordinha branca antes da sombra
            blur_radius=25,  # desfoque
            offset=Offset(0, 0),  # trabalha nos X e Y
            blur_style=ShadowBlurStyle.OUTER,  # o tipo de shadow
        )

    )

    container3 = Container(content=Column(controls=[
        Row(controls=[Image(src="img_bee.png")], alignment=MainAxisAlignment.CENTER),
        Row(controls=[Text("ABELHO", size=20)], alignment=MainAxisAlignment.CENTER),
        Row(controls=[Text("zummmmmmmmmmmmmmmmmmmm""zummmmmmmmmmm""zummm", width=200,
                           text_align=TextAlign.JUSTIFY)]
            )],
        horizontal_alignment="center"),
        width=300,
        height=300,
        margin=margin.all(20),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=10),
        shadow=BoxShadow(
            spread_radius=10,  # bordinha branca antes da sombra
            blur_radius=25,  # desfoque
            offset=Offset(0, 0),  # trabalha nos X e Y
            blur_style=ShadowBlurStyle.OUTER,  # o tipo de shadow
        )

    )


    linha = Row(controls=[container1,container2,container3])
    page.add(linha)
    page.update()

if __name__ == '__main__':
    app(target=main)
