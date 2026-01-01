class ActionResult:
    def __init__(self, success, data=None, error=None):
        self.success = success
        self.data = data
        self.error = error

class Action:
    async def run(self, **kwargs):
        raise NotImplementedError
