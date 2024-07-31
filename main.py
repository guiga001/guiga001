from browser import document, html
import random

class DressUpGame:
    def __init__(self):
        self.outfits = ["Vestido vermelho", "Calça jeans e camiseta", "Saia e blusa", "Macacão", "Conjunto de esporte"]
        self.accessories = ["Chapéu", "Óculos de sol", "Bolsa", "Colar", "Pulseiras"]
        self.shoes = ["Tênis", "Sandálias", "Botas", "Sapatilhas", "Saltos altos"]
        self.selected_outfit = None
        self.selected_accessory = None
        self.selected_shoes = None

    def choose_outfit(self, event):
        self.selected_outfit = random.choice(self.outfits)
        document["game"] <= html.P(f"Você escolheu: {self.selected_outfit}")

    def choose_accessory(self, event):
        self.selected_accessory = random.choice(self.accessories)
        document["game"] <= html.P(f"Você escolheu: {self.selected_accessory}")

    def choose_shoes(self, event):
        self.selected_shoes = random.choice(self.shoes)
        document["game"] <= html.P(f"Você escolheu: {self.selected_shoes}")

    def show_selection(self, event):
        document["game"] <= html.H3("Sua personagem está vestida com:")
        document["game"] <= html.P(f"Roupa: {self.selected_outfit}")
        document["game"] <= html.P(f"Acessório: {self.selected_accessory}")
        document["game"] <= html.P(f"Sapatos: {self.selected_shoes}")

def main():
    game = DressUpGame()

    btn_outfit = html.BUTTON("Escolher Roupa")
    btn_outfit.bind("click", game.choose_outfit)

    btn_accessory = html.BUTTON("Escolher Acessório")
    btn_accessory.bind("click", game.choose_accessory)

    btn_shoes = html.BUTTON("Escolher Sapatos")
    btn_shoes.bind("click", game.choose_shoes)

    btn_show = html.BUTTON("Mostrar Seleção")
    btn_show.bind("click", game.show_selection)

    document["game"] <= btn_outfit
    document["game"] <= html.BR()
    document["game"] <= btn_accessory
    document["game"] <= html.BR()
    document["game"] <= btn
