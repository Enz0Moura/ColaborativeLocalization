# Sistema de Localização para Trilhas

## Visão Geral

Este projeto implementa um sistema de localização destinado a locais de trilha, utilizando dispositivos wearable (bracelets), totens distribuídos ao longo das trilhas, e um servidor central. O objetivo é aumentar a segurança dos trilheiros, permitindo a rápida localização e assistência em caso de necessidade.

## Componentes do Sistema

- **Terminal (Bracelet):** Dispositivo wearable que cada trilheiro leva consigo.
- **Totem:** Dispositivos fixos distribuídos pela trilha para comunicação com os bracelets.
- **Servidor:** Centraliza a coleta de dados de localização e monitoramento.

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