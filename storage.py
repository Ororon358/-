import uuid
from typing import Dict

class URLStorage:
    def __init__(self):
        self.storage: Dict[str, str] = {}

    def create_short_url(self, original_url: str) -> str:
        short_id = str(uuid.uuid4())[:8]  # 8-символьный ID
        self.storage[short_id] = original_url
        return short_id

    def get_original_url(self, short_id: str) -> str:
        return self.storage.get(short_id, None)
