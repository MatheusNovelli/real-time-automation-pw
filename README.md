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

--------------------------------------------------------------------------------------------------------------------------------

# Final Practical Project

## Project Description
An electrical testing company has a bank of 30 motors that it uses for various tests and training sessions. However, for safety reasons, only 12 of them can be powered on simultaneously. Additionally, two motors in sequence cannot operate at the same time.

## File Structure
The project is divided into files by threads, in addition to having files for global variables and the main function.

**-> control_thread:**  
Control thread, responsible for selecting and starting the motors, as well as controlling the voltage and speed of each one. It also establishes socket communication with the synoptic process to transmit the current speed values of each motor.

**-> engine_thread:**  
Motor thread, where each motor, once started, is responsible for its own speed and torque increase.

**-> interface_thread:**  
Interface thread, responsible for capturing user input from the keyboard to set the speed of each motor randomly chosen by the controller.

**-> logger_thread:**  
Logger thread, responsible for storing the speed values of the motors every second, along with a timestamp, in a log file (`log.txt`).

**-> sypnotic_process:**  
Process that communicates with the control thread via socket and is responsible for storing the motor speed values in a historian file. It is recommended to delete the file after each execution of the process since it can become very large due to the high data flow reaching it.

**-> timer:**  
Device responsible for repeating tasks. It receives the repetition time and the callback function (the task to be repeated) as arguments.

**-> global_variables:**  
File containing global variables and their locks (mutex).

**-> main:**  
Main process, responsible for initializing and terminating threads and processes.

## Running the Project
To run the project, simply enter the command `python main.py runserver 8081`. If this port is already in use on your computer, you can run it on the next available port, which in this case would be 8082.

Once this is done, the program will prompt you to enter a list of motor speeds, requiring a list of 12 numerical elements. To do this, it is recommended to follow the example values displayed in the terminal.

`[55.2, 40, 87, 45.7, 92.1, 20, 35, 76, 86, 86, 15.2, 42]`

Since we were unable to implement the loop, after the control operates for 1 minute, due to anomalies it generated in the speed convergence, we decided to terminate the program after this minute. Therefore, after the control has completed its task, you need to restart the project.

## Libraries Used
No external libraries were used, so no installation is required. The most notable libraries used include `threading`, `socket`, and `time`. 



