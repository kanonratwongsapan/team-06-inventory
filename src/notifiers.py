from typing import Protocol

class Notifier(Protocol):
    """Protocol สำหรับการแจ้งเตือน"""
    def send(self, message: str) -> None: ...

class EmailNotifier:
    """ระบบแจ้งเตือนผ่าน Email"""
    def __init__(self, email: str):
        self.email = email
    def send(self, message: str) -> None:
        """ส่งการแจ้งเตือนออกทาง Email (จำลองด้วย print)"""
        print(f"[Email to {self.email}] {message}")

class SMSNotifier:
    """ระบบแจ้งเตือนผ่าน SMS"""
    def __init__(self, phone: str):
        self.phone = phone
    def send(self, message: str) -> None:
        """ส่งการแจ้งเตือนออกทาง SMS (จำลองด้วย print)"""
        print(f"[SMS to {self.phone}] {message}")

class NotifierFactory:
    """Factory สำหรับสร้าง Notifier"""
    @staticmethod
    def create(channel: str, config: str) -> Notifier:
        """สร้าง Notifier ตามช่องทางที่ระบุ"""
        if channel == "email":
            return EmailNotifier(config)
        elif channel == "sms":
            return SMSNotifier(config)
        raise ValueError(f"Unknown channel: {channel}")