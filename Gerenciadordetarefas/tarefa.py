class Tarefa:
    counter = 1
    
    def __init__(self, titulo, descricao):
        self.id = Tarefa.counter
        self.__titulo = titulo
        self.__descricao = descricao
        self.concluida = False
        Tarefa.counter += 1
    
    def definir_conclusao(self, confirmacao):
        if confirmacao == 'y':
            self.concluida = True
        elif confirmacao == 'n':
            self.concluida = False
                

    def __str__(self):
            status = "✔️ Concluída" if self.concluida else "❌ Pendente"
            return f"[{self.id}] {self.__titulo} - {status}\n  {self.__descricao}\n"
        
