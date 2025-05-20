
# FarmTech Solutions - Entrega 1

## 🌱 Simulador de Sistema de Irrigação com ESP32

Este projeto simula sensores agrícolas utilizando a plataforma Wokwi e um ESP32 para controlar uma bomba de irrigação.

### 🔌 Sensores Simulados:
- **Fósforo (P):** Botão físico (pressionado = presença).
- **Potássio (K):** Botão físico (pressionado = presença).
- **pH do Solo:** Sensor LDR simula valor analógico convertido para escala 0-14.
- **Umidade do Solo:** Sensor DHT22.

### ⚙️ Lógica de Controle:
A irrigação é ativada **somente se**:
- P e K estiverem presentes;
- pH entre **5.5 e 7.5**;
- Umidade < **40%**.

### 💡 Indicador:
- **LED** ligado = irrigação ativada.

### 🧪 Resultado:
Os dados são impressos no monitor serial a cada 2 segundos.

## 🔧 Circuito Wokwi

(Adicionar imagem circuito.png aqui)

## 📁 Arquivo principal

- **main.cpp:** Código-fonte em C++ com a lógica comentada.
