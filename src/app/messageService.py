

# Use full import paths
from src.app.llmService import LLMService
from src.app.messagesUtil import MessagesUtil


class MessageService:
    def __init__(self):
        self.messageUtil = MessagesUtil()
        self.llmService = LLMService()

    def process_message(self, message):
        if self.messageUtil.isBankSms(message):
            return self.llmService.runLLM(message)
        else:
            return None
