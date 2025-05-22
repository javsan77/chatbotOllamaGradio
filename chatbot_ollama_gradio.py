import gradio as gr
import requests

# Configura el modelo que estás usando en Ollama
OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/chat"

# Función que llama a Ollama
def conversar_con_ollama(mensaje, historial):
    if historial is None:
        historial = []

    messages = [{"role": "system", "content": "Eres un asistente útil."}]
    for entrada, salida in historial:
        messages.append({"role": "user", "content": entrada})
        messages.append({"role": "assistant", "content": salida})
    messages.append({"role": "user", "content": mensaje})

    response = requests.post(OLLAMA_URL, json={
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False
    })

    if response.status_code == 200:
        respuesta = response.json()["message"]["content"]
        historial.append((mensaje, respuesta))
        return respuesta, historial
    else:
        return "Error al conectar con Ollama", historial

# Interfaz con Gradio
with gr.Blocks() as interfaz:
    gr.Markdown("## 🤖 Chatbot con Ollama + Gradio")
    chatbot = gr.Chatbot()
    mensaje = gr.Textbox(label="Tu mensaje:")
    estado = gr.State([])

    def responder(mensaje_usuario, historial):
        respuesta, historial_actualizado = conversar_con_ollama(mensaje_usuario, historial)
        #return chatbot.update(value=historial_actualizado), historial_actualizado
        return historial_actualizado, historial_actualizado

    enviar = gr.Button("Enviar")
    enviar.click(fn=responder, inputs=[mensaje, estado], outputs=[chatbot, estado])
    mensaje.submit(responder, [mensaje, estado], [chatbot, estado])

# Ejecutar interfaz
interfaz.launch()
