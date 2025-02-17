#Пример кода: сохраняем общий контекст для агентов:
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

memory.save_context({"user": "Какой курс доллара?"}, {"response": "1 EUR = 1.08 USD"})

print(memory.load_memory_variables({}))
