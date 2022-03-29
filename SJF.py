class Processo:
  def __init__(self, nome, chegada, duracao):
        self.nome = nome
        self.tempo_chegada = chegada
        self.tempo_duracao = duracao
        self.tempo_final = 0
  
  def pegar_tempo_chegada(self):
    return self.tempo_chegada

  def pegar_tempo_duracao(self):
    return self.tempo_duracao

  def __repr__(self):
        return '' + self.nome + ' chegada: ' + str(self.tempo_chegada) + ' duração: ' + str(self.tempo_duracao) + '\n'

class SJF_Não_Preemptivo:
    def __init__(self):
        self.processos = []
        self.tempoFinal = []
        self.tempoInicial = []

    def estaVazia(self):
        return self.processos == []

    def entrada(self, p):
        self.processos.append(p)

    def ordena(self):
      ordenada = []
      ordenada.append(self.processos[0])
      return ordenada + sorted(self.processos[1:], key=Processo.pegar_tempo_duracao)

    def tempo_medio_de_espera(self):
      duracao = 0
      ordenada = []
      aux_media = 0

      ordenada.append(self.processos[0])
      ordenada += sorted(self.processos[1:], key=Processo.pegar_tempo_duracao)

      for i, processo in enumerate(ordenada):
        if i == 0:
          duracao = processo.tempo_duracao
          ordenada[i].tempo_final = duracao
        else:
          duracao += processo.tempo_duracao
          ordenada[i].tempo_final = duracao

      for p in ordenada:
        aux_media += (p.tempo_final - p.tempo_duracao - p.tempo_chegada)

      return duracao/len(ordenada)

    def tamanho(self):
        return len(self.processos)

sjf = SJF_Não_Preemptivo()
sjf.entrada(Processo('p1', 0, 1))
sjf.entrada(Processo('p2', 2, 6))
sjf.entrada(Processo('p3', 4, 1))
sjf.entrada(Processo('p4', 5, 4))

print(sjf.ordena())
print("Tempo médio de espera: ", sjf.tempo_medio_de_espera())

