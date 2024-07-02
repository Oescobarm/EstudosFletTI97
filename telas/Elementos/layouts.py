from flet import *


def main(page:Page):
    page.title="Estudando Cards"

    produto=Card(

    margin=10,
        content=Container(

            border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=10, bottom_right=10),
            bgcolor=colors.WHITE,
            content=Column(
                controls=[
                    Row(controls=[Image(src="lanche2.png")],alignment=MainAxisAlignment.CENTER),
                    Container(content=Row(controls=[
                        Text("Lanche  Vegano", color=colors.RED, weight=FontWeight.BOLD),
                                  ], alignment=MainAxisAlignment.CENTER),
                            border=border.only(bottom=BorderSide(2, color=colors.RED))
                    ),

                    Row(controls=[Icon(cupertino_icons.CHEVRON_RIGHT),Text(" Proteina Vegetal",max_lines=3)],
                        alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        Icon(cupertino_icons.HEART, color=colors.RED),
                        Row(controls=[Text("R$ 45,90", size=18,color=colors.RED )]),
                        IconButton(icon=icons.SHOPPING_CART, icon_color=colors.GREEN)
                    ], alignment=MainAxisAlignment.SPACE_AROUND)

                ],

            ),

        width=200,
            shadow=BoxShadow(
                spread_radius=0,  # bordinha branca antes da sombra
                blur_radius=25,  # desfoque
                color=colors.BLUE_GREY_300,
                offset=Offset(0, 0),  # trabalha nos X e Y
                blur_style=ShadowBlurStyle.OUTER,  # o tipo de shadow
            )

        )

    )

    page.add(produto)


if __name__ == '__main__':
    app(target=main)