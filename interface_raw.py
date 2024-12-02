"""
Conceito de interface em orientação a objetos. 
Embora Python não tenha uma estrutura de dados chamada interface, podemos usar a biblioteca abc para obter funcionalidades semelhantes. 
Vou criar uma classe chamada NotificationSender e usá-la como uma classe abstrata. 
Em seguida, vou criar uma classe chamada emailNotificationSender que herda da classe NotificationSender e implementa o método sendNotification. 
Vou mostrar como essa classe abstrata obriga outras classes a implementarem o mesmo método. Isso é conhecido como injeção de dependência e é uma prática comum na programação orientada a objetos.
"""

from abc import ABC, abstractmethod

class NotificationSender(ABC):
    
    @abstractmethod
    def send_notification(self, message: str) -> None: pass
    
class EmailNotificationSender(NotificationSender):
    
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")
        
class SMSNotificationSender(NotificationSender):
    
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")
        
class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender
        
    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)
        
obj = Notificator(SMSNotificationSender())
obj.send("Hello, world!")