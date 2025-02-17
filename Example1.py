#Пример кода: создаём систему, где агенты работают последовательно:
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool

# Создаём агентов с разными настройками
expert = ChatOpenAI(model="gpt-4o", temperature=0.3)
executor = ChatOpenAI(model="gpt-4o", temperature=0.7)
editor = ChatOpenAI(model="gpt-4", temperature=0.2)

# Определяем функции агентов
def analyze_query(query):
    return f"Определяю суть запроса: {query}"

def generate_response(analysis):
    return f"Ответ на основе анализа: {analysis}"

def refine_response(response):
    return f"Отредактированный ответ: {response}"

# Объединяем агентов в систему
tools = [
    Tool(name="Анализ запроса", func=analyze_query, description="Определяет смысл запроса"),
    Tool(name="Генерация ответа", func=generate_response, description="Создаёт ответ"),
    Tool(name="Редактирование ответа", func=refine_response, description="Улучшает текст")
]

agent = initialize_agent(
    tools, expert, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

response = agent.run("Какой курс евро сегодня?")
print(response)
