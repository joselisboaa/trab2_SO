# Leitura x Escrita
### Leitores:
Processos, os quais não são requeridos excluir uns aos outros (entre eles). 

### Escritores:
Processos, os quais são requeridos excluir todos os outros processos, leitores e
escritores. 

### Observações 
- Leitores não podem corromper a seção crítica (pode ter N leitores acessando o mesmo arquivo)
- Escritores devem escrever sob exclusão mútua para garantir a integridade dos dados.
- Não pode haver leitores e escritores simultaneamente

## Soluções propostas:
### 1º)
Os escritores são obrigados a esperar para acessar a região crítica sempre que houver leitores
(pode levar os escritores a esperar indefinidamente pelo acesso).

### 2º)
A possibilidade de espera indefinida dos escritores é resolvida (Quando for solicitado uma ação de 
escrita os leitores param para esperar a escrita ocorrer.