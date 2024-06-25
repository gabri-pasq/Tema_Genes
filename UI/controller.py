import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.btnstaz.disabled = False
        self._view.btncammino.disabled = False
        self._model.creaGrafo()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Nodi: {self._model.getnodi()}, Archi: {self._model.getarchi()}"))

        for i in self._model.grafo.nodes:
            self._view.drop.options.append(ft.dropdown.Option(i))

        self._view.update_page()

    def handle_stat(self, e):
        if self._view.drop.value is None:
            self._view.create_alert("Selezionare un nodo")
            return
        lista = self._model.statistiche(self._view.drop.value)
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a: {self._view.drop.value}"))
        for nodo,peso in lista:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}: {peso}"))

        self._view.update_page()



    def handle_cammino(self, e):
        lista, peso = self._model.percorso(self._view.drop.value)
        self._view.txt_result.controls.append(ft.Text(f'Peso percorso: {peso}'))
        for i in range(0,len(lista)-1):
            self._view.txt_result.controls.append(ft.Text(f'{lista[i]} -> {lista[i+1]}'))
        self._view.update_page()