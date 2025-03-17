from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from ai_controller.controller_client import IAClient
from ai_controller.agent import AppAgent
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Cargar variables de entorno
load_dotenv()

# Configuración inicial de la IA
ai_client = IAClient()
agent = AppAgent(ai_client)

# Crear la aplicación FastAPI
app = FastAPI()

# Servir archivos estáticos desde la carpeta 'static'
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definir el modelo de datos para el mensaje
class MessageRequest(BaseModel):
    mensaje: str

# Ruta para manejar las solicitudes POST desde el HTML
@app.post("/ask")
async def ask_agent(message: MessageRequest):
    try:
        # Obtener la respuesta de la IA
        resp = agent.ask_agent(message.mensaje)
        print(f"Respuesta de la IA: {resp}")  # Imprime la respuesta de la IA en la consola del servidor

        # Asegúrate de devolver solo el texto de la respuesta
        if isinstance(resp, dict) and 'output' in resp:
            return {"respuesta": resp['output']}  # Si la IA devuelve un diccionario, usa la clave 'output'
        else:
            return {"respuesta": resp}  # Si la IA devuelve una cadena de texto directamente
    except Exception as e:
        print(f"Error: {str(e)}")  # Imprime el error para depuración
        raise HTTPException(status_code=500, detail="La IA no devolvió una respuesta válida.")




# Ruta raíz (opcional, solo si deseas devolver algo inicial)
@app.get("/")
async def root():
    resp = agent.ask_agent("Cuales son las alergias mas comunes?")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes de cualquier origen (puedes limitarlo)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todas las cabeceras
)
