# Mouse Steering Script for F1 (FreePIE + vJoy)

[English description below] | [Descrição em português abaixo]

---

## 🇺🇸 English Version

### Description
This project provides a simple Python script for **FreePIE** that translates mouse movement into a virtual steering wheel axis using **vJoy**. It was designed to enhance the gameplay experience in simulation games like F1, and others that not accept mouse steering nativetly.

### Features
* **Toggle Switch (Simple Settable Key):** Press 'C' to enable/disable the mouse control.
* **Mouse Lock:** Automatically locks the cursor to the game window to prevent focus loss.
* **Precise Centering:** Uses an offset logic to ensure the wheel returns to a perfect 0° position.
* **Customizable:** Easy to adjust sensitivity, key and limits.

### How to use
1.  Install [vJoy](http://vjoystick.sourceforge.net/) and [FreePIE](https://andersmalmgren.github.io/FreePIE/).
2.  Open **vJoy Conf** and ensure **Device 1** is enabled with the **X Axis**.
3.  Copy the code from `script.py` into FreePIE.
4.  Run the script and press **'C'** to activate. (Remembering: You can reconfigure this key on archive)
5.  **Important Tip:** If the game doesn't recognize the axis, increase the `sensitivity` to **1000** during mapping, then set it back to **1.5**, or whatever you want.

---

## 🇧🇷 Versão em Português

### Descrição
Este projeto fornece um script simples em Python para o **FreePIE** que traduz o movimento do mouse em um eixo de volante virtual utilizando o **vJoy**. Desenvolvido para melhorar a experiência em simuladores como F1, e outros não aceitam mouse como controle nativamente.

### Funcionalidades
* **Ativação por Tecla (Configuração Simples de Tecla):** Aperte 'C' para ligar/desligar o controle pelo mouse.
* **Trava de Cursor:** Trava o mouse na tela automaticamente para evitar que ele saia do jogo.
* **Centralização Precisa:** Utiliza lógica de *offset* para garantir que o volante volte à posição 0° perfeitamente.
* **Customizável:** Fácil ajuste de sensibilidade, tecla e limites.

### Como usar
1.  Instale o [vJoy](http://vjoystick.sourceforge.net/) e o [FreePIE](https://andersmalmgren.github.io/FreePIE/).
2.  Abra o **vJoy Conf** e verifique se o **Device 1** está ativo com o **Eixo X**.
3.  Cole o código do arquivo `script.py` no FreePIE.
4.  Rode o script e aperte **'C'** para ativar. (Lembrando: Você pode reconfigurar essa tecla no arquivo)
5.  **Dica Importante:** Se o jogo não reconhecer o eixo, aumente a `sensitivity` para **1000** durante o mapeamento e depois volte para **1.5**, ou qual você quiser.

---

*Developed by Emanuel - Systems Development Student (M-TEC)*
