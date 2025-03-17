from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
import litellm

litellm.drop_params=True

class AppAgent():
    
    def __init__(self, ia_client):
        
        self.agent = create_csv_agent(
                ia_client.chat,
                "./data/cohorte_alergias.csv",
                verbose=True,
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                allow_dangerous_code=True
            )
    
    def ask_agent(self, msg):
        res = self.agent.invoke(msg)
        return res  # 🔹 Debes retornar la respuesta
            #()es el mensaje que le llega a la ia