class Fila:
    # 
  def __init__(self):
      self.processos = [] 
#Verifica se a fila esta vazia
  def estaVazia(self):
      return self.processos == []
#Inserindo processos na fila
  def enfileirar(self, item):
      self.processos.insert(0,item)
      return item
#Retira o processo da Fila
  def desenfileirar(self):
      return self.processos.pop()
#Retorna o tamanho da fila
  def tamanho(self):
      return len(self.processos)
#Instanciando a classe      
fila=Fila()

print("Entrando na fila: ", fila.enfileirar('Rafael'))
print("Entrando na fila: ", fila.enfileirar('Estela'))
print("Entrando na fila: ", fila.enfileirar('Diogo'))
print("Entrando na fila: ", fila.enfileirar('Yuji'))
print("tamanho: ", fila.tamanho())

#Retira o primeiro processo a entrar na fila
print("Saindo da fila", fila.desenfileirar())
print("tamanho: ", fila.tamanho())