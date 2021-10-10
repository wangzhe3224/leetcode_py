from typing import Dict

class Logger:
    
    def __init__(self) -> None:
        self._status: Dict[str, int] = {}
        self._limit = 10
    
    def shouldPrintMessage(self, ts: int, msg: str) -> bool:
        last = self._status.get(msg, -self._limit)
        if ts - last >= self._limit:
            self._status[msg] = ts
            return True
        else:
            return False