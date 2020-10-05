
from collections import defaultdict


if __name__ == "__main__":

    class Grafo(object):
        """ Implementacaoo basica de um grafo. """

        def __init__(self, arestas, direcionado=False):
            """Inicializa as estruturas base do grafo."""
            self.adj = defaultdict(set)
            self.direcionado = direcionado
            self.adiciona_arestas(arestas)


        def get_vertices(self):
            """ Retorna a lista de vertices do grafo. """
            return list(self.adj.keys())
        
        def vertices_vetor(self):
            """ Retorna a lista de vertices do grafo. """
            return list(self.adj.keys())

        def get_arestas(self):
            """ Retorna a lista de arestas do grafo. """
            return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


        def adiciona_arestas(self, arestas):
            """ Adiciona arestas ao grafo. """
            for u, v in arestas:
                self.adiciona_arco(u, v)


        def adiciona_arco(self, u, v):
            """ Adiciona uma ligacao (arco) entre os nodos 'u' e 'v'. """
            self.adj[u].add(v)
            if not self.direcionado:
                self.adj[v].add(u)


        def existe_aresta(self, u, v):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return u in self.adj and v in self.adj[u]

        def grau(self, u):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return len(self.adj[u])
        
        def verticesAdjacentes(self, u):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return self.adj[u]

        def __len__(self):
            return len(self.adj)


        def __str__(self):
            return '{}({})'.format(self.__class__.__name__, dict(self.adj))


        def __getitem__(self, v):
            return self.adj[v]
    
    
    def leituraArquivo():
        arq = open('arquivo.txt', 'r')  #abre o arquivo
        texto = []  #declaro um vetor
        arestas = [] #declaro um segundo vetor
        matriz2 = [] #declaro um terceiro vetor
        texto = arq.readlines() #quebra as linhas do arquivo em vetores 

        for i in range(len(texto)):        
            arestas.append(texto[i].split())
            
        arq.close()

        return arestas
    
    def questao6():
        arestas = leituraArquivo()
        print("Grafo arestas", arestas)
        vertices = []
        grafo = Grafo(arestas, direcionado=False)
        print(grafo.adj)
        print("vertices:", grafo.get_vertices())
        print("numero de vertices:", len(grafo.get_vertices()))
        x = 1
        while x <= 6:
            opcao = int(input("digite o vertice para saber qual e o grau dele: "))
            print(grafo.grau(str(opcao)))
            x = x + 1
            
    def questao7():
        arestas = leituraArquivo()
        grafo = Grafo(arestas, direcionado=False)
        print(grafo.adj)
        print("vertices:", grafo.get_vertices())
        print("numero de vertices:", len(grafo.get_vertices()))
        x = 1
        while x <= 6:
            opcao = int(input("digite o vertice para saber qual e o seu(s) vertices adjacentes "))
            print(grafo.verticesAdjacentes(str(opcao)))
            x = x + 1

    def questao8():
        vetor = [2,4,5]
        print("Elementos do vetor", vetor)
        resultado = soma_vetor(vetor)
        print("total:", resultado)
        
    def soma_vetor(vetor):
        if len(vetor) == 1:
            return vetor[0]
        else:
            return vetor[0] + soma_vetor(vetor[1:])
    
    
    class Tarefa():
        def __init__(self, nome, descricao, prioridade):
            self.nome = nome
            self.descricao = descricao
            self.prioridade = prioridade

        def criandoTarefa(self, nome, descricao, prioridade):
            self.nome = nome
            self.descricao = descricao
            self.prioridade = prioridade
            
        def getTarefas(self):
            return self.nome, self.descricao, self.prioridade
    
        
    def questao9():
        tamanho = 10
        tarefas = []
        for i in range(tamanho):
            nome = raw_input("digite o nome da tarefa:")
            descricao = raw_input("descreva sobre a tarefa ")
            prioridade = int(input("Digite a ordem a ser executada desta tarefa "))
            tarefas.append(Tarefa(nome,descricao,prioridade))
            
        for tarefa in tarefas:
            print "\"%s\"  %s (%s)" % (tarefa.nome, tarefa.descricao, tarefa.prioridade)
        #Ordena a lista baseada na prioridade do maior para o menor
        prioridade = sorted(tarefas, key=lambda x: x.prioridade,reverse=False)
        print("Descricao da tarefas por ordem")
        for tarefa in prioridade:
            print(tarefa.descricao)
    
    def imprime_matriz(matriz):

        linhas = len(matriz)
        colunas = len(matriz[0])

        for i in range(linhas):
            for j in range(colunas):
                if(j == colunas - 1):
                    print("%d" %matriz[i][j])
                else:
                    print("%d" %matriz[i][j])
        print()
        
    def questao10():

        print("Questao 10")
        print("Quebra Cabeca")
  
        matriz = [] # lista vazia
        tamanho = 3
        valor = 0
        n_linhas = tamanho
        n_colunas = tamanho
        matriz1 = [[1,2,3],[5,0,6],[7,4,8]]
        matriz2 = [[1,0,3],[5,2,6],[7,4,8]]
        matriz3 = [[1,2,3],[5,2,0],[7,4,8]]
        matriz4 = [[1,2,3],[5,4,6],[7,0,8]]
        matriz5 = [[1,2,3],[0,2,6],[7,4,8]]
        
        print("Escolha um estado inicial do quebra cabeca")
        print("Estado inicial 1", imprimirMatriz(matriz1,n_colunas))
        print("Estado inicial 2", imprimirMatriz(matriz2,n_colunas))
        print("Estado inicial 3", imprimirMatriz(matriz3,n_colunas))
        print("Estado inicial 4", imprimirMatriz(matriz4,n_colunas))
        print("Estado inicial 5", imprimirMatriz(matriz5,n_colunas))
        
        opcao = int(input("digite o numero do estado inicial: "))

        if (opcao == 1):
            print("Resultados subsequentes")
            print("Estado  2", imprimirMatriz(matriz2,n_colunas))
            print("Estado  3", imprimirMatriz(matriz3,n_colunas))
            print("Estado  4", imprimirMatriz(matriz4,n_colunas))
            print("Estado  5", imprimirMatriz(matriz5,n_colunas))

        elif(opcao == 2):
            print("Resultados subsequentes")
            print("Estado  1", imprimirMatriz(matriz1,n_colunas))
            print("Estado  3", imprimirMatriz(matriz3,n_colunas))
            print("Estado  4", imprimirMatriz(matriz4,n_colunas))
            print("Estado  5", imprimirMatriz(matriz5,n_colunas))

        elif(opcao == 3 ):
            print("Resultados subsequentes")
            print("Estado  1", imprimirMatriz(matriz1,n_colunas))
            print("Estado  2", imprimirMatriz(matriz2,n_colunas))
            print("Estado  4", imprimirMatriz(matriz4,n_colunas))
            print("Estado  5", imprimirMatriz(matriz5,n_colunas))

        elif(opcao == 4):
            print("Resultados subsequentes")
            print("Estado  1", imprimirMatriz(matriz1,n_colunas))
            print("Estado  2", imprimirMatriz(matriz2,n_colunas))
            print("Estado  3", imprimirMatriz(matriz3,n_colunas))
            print("Estado  5", imprimirMatriz(matriz5,n_colunas))

        elif(opcao == 5):
            print("Estado  1", imprimirMatriz(matriz1,n_colunas))
            print("Estado  2", imprimirMatriz(matriz2,n_colunas))
            print("Estado  3", imprimirMatriz(matriz3,n_colunas))
            print("Estado  4", imprimirMatriz(matriz4,n_colunas))
        else:
            print("Nao tem esse estado")
            Menu()
        
    def imprimirMatriz(matriz,n_colunas):
        for i in range(n_colunas):
            print(matriz[i])

                
 
    def Menu():
        print("Escolha a opcao que deseja")
        print("Escolha 6 para questao 6")
        print("Escolha 7 para questao 7")
        print("Escolha 8 para questao 8")
        print("Escolha 9 para questao 9")
        print("Escolha 10 para questao 10")
        opcao = int(input("digite a opcao: "))

        if (opcao == 6):
            questao6()
        elif(opcao == 7):
            questao7()
        elif(opcao == 8 ):
            questao8()
        elif(opcao == 9):
            questao9()
        elif(opcao == 10):
            questao10()
        else:
            print("Nao tem essa questao")
            Menu()
        
Menu()