# Mouse Steering for F1 & Sim Racing — Virtual Wheel with FreePIE + vJoy

<div align="center">
  <video src="https://github.com/user-attachments/assets/cc9cd84f-8275-41fa-8746-4e03e328260b" width="100%" controls></video>
  <p><b>Visualizing the script in action!</b></p>
</div>

[English description below] | [Descrição em português abaixo]

---

## English Version

### Description
This project provides a Python script for **FreePIE** that translates mouse movement into a virtual steering wheel axis via **vJoy**. It was specifically refined for F1 simulation, offering a professional feel with audio feedback and on-the-fly adjustments.

### New Features (v1.3)
* **Toggle Switch with Audio:** Press 'C' to enable/disable. You will hear a high-pitched beep for ON and a low-pitched beep for OFF.
* **On-the-fly Sensitivity:** Use the **Mouse Wheel** to increase or decrease sensitivity while driving.
* **Quick Reset:** Click the **Middle Mouse Button** (Scroll Click) to instantly reset to your default sensitivity.
* **F1 Style Feedback:** Beep frequencies are inspired by F1 steering wheel systems for better immersion.

### How to use
1. Install [vJoy](http://vjoystick.sourceforge.net/) and [FreePIE](https://andersmalmgren.github.io/FreePIE/).
2. Open **vJoy Conf** and ensure **Device 1** is enabled with the **X Axis** set to at least 8 buttons (optional).
3. Copy the code from `script.py` into FreePIE.
4. Run the script and press **'C'** to activate.
5. **Mapping Tip:** If the game doesn't recognize the axis during setup, scroll up to increase sensitivity to **1000**, map the control in-game, and then click the scroll button to reset to **1.5**.

---

## Versão em Português

### Descrição
Este projeto fornece um script em Python para o **FreePIE** que traduz o movimento do mouse em um eixo de volante virtual utilizando o **vJoy**. Foi refinado especificamente para simuladores de F1, oferecendo uma sensação profissional com feedback de áudio e ajustes em tempo real.

### Novas Funcionalidades (v1.3)
* **Ativação com Áudio:** Aperte 'C' para ligar/desligar. Você ouvirá um bipe agudo para LIGADO e um bipe grave para DESLIGADO.
* **Sensibilidade em Tempo Real:** Use a **Rodinha do Mouse (Scroll)** para aumentar ou diminuir a sensibilidade enquanto dirige.
* **Reset Rápido:** Clique com o **Botão do Meio do Mouse** (Clique do Scroll) para resetar instantaneamente para a sensibilidade padrão.
* **Imersão F1:** As frequências dos bipes são inspiradas nos sistemas reais de volante da F1.

### Como usar
1. Instale o [vJoy](http://vjoystick.sourceforge.net/) e o [FreePIE](https://andersmalmgren.github.io/FreePIE/).
2. Abra o **vJoy Conf** e verifique se o **Device 1** está ativo com o **Eixo X**.
3. Cole o código do arquivo `script.py` no FreePIE.
4. Rode o script e aperte **'C'** para ativar.
5. **Dica de Mapeamento:** Se o jogo não reconhecer o eixo na configuração, gire o scroll para aumentar a sensibilidade para **1000**, mapeie o controle no jogo e depois clique no botão do scroll para resetar para **1.5**.

---

## Troubleshooting (Common Errors)

### 🇺🇸 DLL Version Mismatch (Error 218/219)
If you see the error: `"vJoy version of Driver (219) does NOT match DLL Version (218)"`:
1. Go to `C:\Program Files\vJoy\x86`.
2. Copy `vJoyInterface.dll`.
3. Paste it into `C:\Program Files (x86)\FreePIE`, replacing the old one.

### 🇧🇷 Erro de Versão da DLL (Erro 218/219)
Se aparecer o erro: `"vJoy version of Driver (219) does NOT match DLL Version (218)"`:
1. Vá até `C:\Program Files\vJoy\x86`.
2. Copie o arquivo `vJoyInterface.dll`.
3. Cole na pasta do FreePIE (`C:\Program Files (x86)\FreePIE`), substituindo o arquivo existente.

---

*Developed by Emanuel (sousa7tz) - Systems Development Student (M-TEC)*
