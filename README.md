# Trabalho Prático Final

## Descrição do projeto
Uma empresa de ensaios elétricos possui um banco com 30 motores que utiliza para diversos
testes e treinamentos. Mas apesar da quantidade, e por questões de segurança, apenas 12 deles
podem ser ligados simultaneamente. Além disso, dois motores em sequência não podem operar
ao mesmo tempo.

## Estrutura de arquivos
O projeto está separado em arquivos por threads, além de contar com arquivos de variáveis globais
e função main.

**-> control_thread:**
Thread de controle, responsável pela escolha e inicialização dos motores e também pelo controle de tensão
e velocidade de cada um deles, além de estabelecer uma comunicação via socket com o processo sinóptico
para que fossem passados os valores das velocidades atuais de cada motor.

**-> engine_thread:**
Thread de motor, assim que inicializado cada motor é responsável pelo seu próprio aumento de velocidade
e torque.

**-> interface_thread:**
Thread de interface, responsável por capturar um Input do teclado do usuário para estabelecer a velocidade
de cada motor escolhido aleatoriamente pelo controlador.

**-> logger_thread:**
Thread Logger, responsável por armazenar os valores das velocidades dos motores a cada 1s, junto com um timestamp,
em um arquivo log.txt.

**-> sypnotic_process:**
Processo que se comunica com a thread de controle via socket, responsável por armazenar os valores de velocidades dos
motores em um arquivo historiador. É recomendado a deleção do arquivo depois de cada vez que o processo é rodadado. Pois este
pode ficar com um tamanho muito grande, devido ao grande fluxo de dados que chegam até ele.

**-> timer:**
Dispositivo responsável pela repetição de tarefas, recebe como argumentos o tempo dessa repetição e a função de callback,
que seria a tarefa a ser repetida.

**-> global_variables:**
Arquivo que contém as variáveis globais e seus locks(mutex).

**-> main:**
Processo principal, responsável por inicializar e encerrar thread e processos.

## Rodando o projeto
Para rodar o projeto, basta inserir o comando `python main.py runserver 8081`, caso
esta porta esteja ocupada em seu computador, pode rodar na porta seguinte, que neste 
caso seria a 8082.
Feito isso, o programa irá pedir para inserir uma lista de velocidades dos motores, sendo preciso inserir uma lista de 12
elementos numéricos. Para isto, é recomendado seguir o valor de exemplo que é exibido no terminal.
[55.2, 40, 87, 45.7, 92.1, 20, 35, 76, 86, 86, 15.2, 42]
Como não conseguimos realizar a implementação do loop, após o controle funcionar por 1 minuto, devido a anormalidades que isso gerava na convergência das velocidades,
decidimos encerrar o programa após esse minuto. Portanto, depois do controle realizar seu trabalho, é preciso inicializar novamente o projeto.

## Bibliotecas utilizadas
Nenhuma biblioteca externa foi utilizada, portanto não é necessário realizar nenhuma instalação, dentre as bibliotecas utilizadas
se destacam a threading, socket e time.

