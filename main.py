import threading


class Monitor:
    def __init__(self):
        # Mutex
        self.reader = threading.Semaphore(1)
        # DB
        self.writer = threading.Semaphore(1)
        self.readers_count = 0

    def start_write(self):
        with self.writer:
            # Check if critical section is available (semaphore = 0)
            self.writer.acquire()

            # Write the data

    def start_read(self):

        while True:
            # Allow to reader be allocated (semaphore = 0)
            self.reader.acquire()
            self.readers_count += 1
            # writer can write
            if self.readers_count == 1: self.writer.acquire()
            self.reader.release()
            # read

    def end_read(self):
        # read
        self.reader.acquire()
        self.readers_count -= 1
        # writer cannot write
        if self.readers_count == 0: self.writer.release()
        self.reader.release()

    def end_write(self):
        # Write the data

        # up semaphore to 1
        self.writer.release()

    # def read(self):
    #     self.start_read()
    #
    #     while (True):
    #         up(semaphore)
    #         down(mutex)
    #         readers_count =+ 1
    #         # writer can write
    #         if readers_count == 1:
    #         up(mutex)
    #         # read
    #         down(mutex)
    #         readers_count =- 1
    #         # writer cannot write
    #         if readers_count == 0: down(semaphore)
    #         up(mutex)
    #

recurso_compartilhado = []
leitores_escritores = Monitor()

def leitor(id):
    leitores_escritores.start_read()
    print(f"Leitor {id} lendo o recurso: {recurso_compartilhado}")
    leitores_escritores.end_read()

def escritor(id):
    leitores_escritores.start_write()
    print(f"Escritor {id} escrevendo no recurso")
    recurso_compartilhado.append(f"Dados escritos pelo escritor {id}")
    leitores_escritores.end_write()

threads = []

for i in range(3):
    leitor_thread = threading.Thread(target=leitor, args=(i,))
    threads.append(leitor_thread)

for i in range(2):
    escritor_thread = threading.Thread(target=escritor, args=(i,))
    threads.append(escritor_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Todas as threads terminaram.")
