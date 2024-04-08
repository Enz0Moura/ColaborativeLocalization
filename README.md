# Sistema de Localização para Trilhas

## Visão Geral

Este projeto simula um sistema de localização destinado a locais de trilha, facilitando a comunicação e o rastreamento de indivíduos por meio de dispositivos wearable (terminais/braceletes), totens distribuídos pela trilha e um servidor central. O sistema visa aumentar a segurança dos trilheiros, permitindo a rápida localização e assistência em caso de necessidade.


## Componentes do Sistema

- **Terminal (Bracelet):** Dispositivo wearable que cada trilheiro leva consigo. Responsável por enviar e receber sinais (registros e beacons) para e de totens, e comunicar-se com o servidor central via totens
- **Totem:** Dispositivos fixos distribuídos ao longo da trilha. Eles recebem dados dos braceletes, armazenam temporariamente essas informações e as transmitem para o servidor.
- **Servidor:** Centraliza a coleta de dados, armazenando as informações de localização de cada bracelete. Utilizado para monitoramento e assistência.

## Fluxo de Dados

1. **Ativação do Bracelete**:
 

    O bracelete é ativado (wake_up) e começa a enviar e escutar beacons a fim de fechar 
    comunicação com totéms próximos ou outros braceletes.

2. **Interação Bracelet-Totem**:

    
    Na ausência de beacons de outros braceletes, o bracelete emite um beacon (emit_beacon).
    O totem recebe o beacon do bracelet e armazena os dados recebidos caso possua memória.
    O bracelet recebe um ACK do totem, indicando que se sua transmissão foi aceita.

3. **Comunicação Totem-Servidor**:

    
    Os totens transmitem periodicamente os dados acumulados para o servidor (send_memory).
    O servidor recebe e armazena esses dados para processamento e monitoramento.

## Esquemas de Mensagem
**Message Schema**: Define a estrutura das mensagens transmitidas entre os componentes. Inclui informações como tipo de mensagem, ID do dispositivo, latitude, longitude, entre outros.

## Estratégias de Simulação
**Simulação de Interação**: Métodos que simulam a lógica de interação entre braceletes e totens, incluindo o envio de beacons, recebimento de ACKs e armazenamento temporário de dados nos totens.

## Utilitários
- **Conversão de Coordenadas**: Funções para converter valores de latitude e longitude para um formato de 24 bits adequado para transmissão, e vice-versa.


## Tecnologias Utilizadas

- Python
- Biblioteca `construct` para estruturas de dados binários
- `pydantic` para validação de esquemas de dados

## Instalação

Para instalar e executar o sistema de localização, siga os passos abaixo:

1. Clone o repositório para sua máquina local:

`git clone https://github.com/Enz0Moura/ColaborativeLocalization`

2. Instale as dependências necessárias:

`pip install -r requirements.txt`

## Uso

Para simular a interação entre os componentes do sistema, execute o script principal:

```bash
python main.py