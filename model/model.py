import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.percorsoFinale = []
        self.pesoMassimo = 0


    def creaGrafo(self):
        nodi = DAO.getNodi()
        self.grafo.add_nodes_from(nodi)

        for n1 in self.grafo.nodes:
            for n2 in self.grafo.nodes:
                if n1 != n2 and not self.grafo.has_edge(n1,n2) and not self.grafo.has_edge(n2,n1):
                    peso = DAO.peso(n1,n2)
                    if peso > 0:
                        self.grafo.add_edge(n1,n2,weight=peso)

    def statistiche(self,nodo):
        listina=[]
        for i in self.grafo.neighbors(nodo):
            listina.append((i,self.grafo[nodo][i]['weight']))
        return listina



    def getnodi(self):
        return len(self.grafo.nodes)

    def getarchi(self):
        return len(self.grafo.edges)

    def percorso(self,start):
        self.percorsoFinale = []
        self.pesoMassimo = 0

        self.ricorsione([start])
        print('hgfjghfdfhkgfiyhtgdfiytdiytdiytdiytdyutd')
        return self.percorsoFinale, self.pesoMassimo

    def ricorsione(self, parziale):
        for nodo in self.grafo.neighbors(parziale[-1]):
            if self.controlli(parziale,nodo):
                parziale.append(nodo)
                pp = self.pesoP(parziale)
                if pp > self.pesoMassimo:
                    self.pesoMassimo = pp
                    self.percorsoFinale = copy.deepcopy(parziale)
                    print(self.percorsoFinale, self.pesoMassimo)
                self.ricorsione(parziale)
                parziale.pop()

    def controlli(self,parziale,nodo):
        for i in range(0,len(parziale)-1):
            if (parziale[i] == parziale[-1] and parziale[i+1] == nodo) or (parziale[i] == nodo and parziale[i+1] == parziale[-1]):
                return False
        return True

    def pesoP(self, lista):
        peso = 0
        for i in range(0, len(lista) - 1):
            peso += self.grafo[lista[i]][lista[i + 1]]['weight']
        return peso

