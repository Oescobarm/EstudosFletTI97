from flet import *

def main(page:Page):
    page.title="Estudando Cards"
    produto=Card(
        content=Container(
            content=Column(
                controls=[
                    Image(src="hack men.jpg"),
                    Text(),
                    Text()
                ]
            )
        )
    )