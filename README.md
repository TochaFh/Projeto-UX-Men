# Projeto UX-Men 🎮✨

Bem-vindo ao repositório do Projeto UX-Men, um projeto de Interface Humano-Computador (IHC) desenvolvido como parte de uma disciplina acadêmica. A ideia central é criar um sistema interativo que auxilie jogos de cartas físicos com o apoio de um "árbitro digital".
## 👥 Integrantes (ID 12)

- Caique Pinheiro Andrade            – RA: 204677
- Lucas Rodrigues de Mendonça        - RA: 236800
- Thiago Augusto de Tulio Nascimento - RA: 252937
- Rafael Campideli Hoyos             – RA: 175100  
- Lucas Palacio Almeida              – RA: 236380

## 📁 Estrutura do Repositório
```bash

./
├── 📑 documentos/                    # Documentação e diagramas
│   ├── 🗺️ Magic_States.drawio          # Fluxo de estados do Magic
│   ├── 📝 script_partida_magic_sistema.txt   # Roteiro da interação com o sistema
│   └── 📝 script_partida_magic.txt          # Roteiro da partida física
│
├── 📄 estrutura.txt                   # Esboço inicial da estrutura do projeto
├── 🐍 main.py                         # Ponto de entrada geral (protótipo inicial)
│
├── 🍓 Raspberry/                      # Código específico para o Raspberry Pi + RFID
│   ├── 🖼️ Captura de tela 2025-06-09 010212.png  # Screenshot do ambiente físico
│   ├── 📂 main_rasp/                  # Código de leitura RFID
│   │   ├── 🐍 main.py
│   │   └── 🐍 mfrc522.py              # Biblioteca para o leitor MFRC522
│   └── 📂 projeto_blink/              # Teste de GPIO (ex: blink de LED)
│       └── 🐍 main.py
│
├── 📄 README.md                       # Este arquivo de documentação
│
├── 🧙 UX_Magic/                       # Lógica do jogo Magic (protótipo)
│   ├── 🃏 cartas_demo.py              # Cartas de demonstração
│   ├── 📂 magic_logic/                # Núcleo de regras do Magic
│   │   ├── ⚔️ batalha.py
│   │   ├── 🧾 carta_magic.py
│   │   ├── 📋 exemplo_cartamagic.py
│   │   └── 👤 jogador.py
│   ├── 🖥️ magic_ui.py                 # Integração da UI com o jogo
│   └── 🐍 main_magic.py               # Execução principal do protótipo Magic
│
├── 🖧 UX_System/                      # Módulo central de comunicação física ↔️ digital
│   ├── 🧲 carta_fisica_virtual.py      # Tradução de RFID para objetos virtuais
│   ├── 📡 comunica_rasp.py            # Comunicação entre Raspberry e o sistema
│   └── 🧠 uxsystem.py                 # Lógica geral do sistema árbitro
│
└── 🖼️ UX_UI/                          # Interface gráfica (Tkinter)
    ├── 🖼️ images/                     # Recursos visuais
    │   ├── 🌅 fundo.png
    │   ├── 🖥️ logo_ux_system.png
    │   └── 🎴 magic_BG.png
    ├── 🖥️ interface2.py               # Versão alternativa da UI
    ├── 🖥️ interface.py                # Interface principal
    ├── 🗂️ menu_ux.py                   # Menu inicial
    └── 🧪 teste_UI.py                 # Testes da interface

``` 

  
📌 Visão Geral

O sistema usa um Raspberry Pi acoplado a um sensor RFID para identificar cartas físicas. Cada carta possui um tag RFID que é lido pelo sistema, permitindo que ele entenda as jogadas que estão acontecendo em tempo real.

Além da leitura física, o sistema inclui uma interface gráfica feita com Tkinter, exibida em uma tela conectada ao Raspberry, funcionando como um painel digital de acompanhamento e mediação das partidas.

Atualmente, o protótipo inicial foi implementado com algumas regras e cartas inspiradas no jogo Magic: The Gathering, mas o foco futuro é expandir para um sistema genérico capaz de entender e validar qualquer jogo de cartas físico.

🎯 Objetivos do Projeto

✅ Proporcionar uma experiência híbrida entre o físico e o digital em jogos de cartas.  
✅ Ajudar jogadores a seguirem corretamente as regras, com validações automáticas.   
✅ Evitar erros durante partidas presenciais com auxílio de um árbitro digital.  
✅ Explorar conceitos de usabilidade e interação homem-máquina em um ambiente lúdico.  

🖥️ Tecnologias Usadas

    🐍 Python

    🖱️ Tkinter (para a interface gráfica)

    🍓 Raspberry Pi

    📡 Sensor RFID (Leitura de tags das cartas)

🚩 Estado Atual do Projeto

O projeto está em fase de protótipo funcional:

    Leitura de cartas com RFID ✅

    Interface gráfica com informações da partida ✅

    Regras básicas de um jogo de Magic implementadas de forma hard-coded ✅

    Integração inicial entre hardware e software ✅

📷 Imagens do Projeto


🚀 Próximos Passos

    Tornar o sistema modular para permitir diferentes jogos além de Magic.

    Implementar um parser de regras genérico.

    Melhorar a experiência da interface gráfica.

    Testes com usuários para avaliação de usabilidade.

    Melhor integração visual e feedback físico (LEDs, sons, etc).



