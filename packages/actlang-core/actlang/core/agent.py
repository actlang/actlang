class Agent:
    def __init__(self, actions):
        self.actions = actions

    async def run(self):
        context = {}
        for action in self.actions:
            result = await action.run(**context)
            if not result.success:
                return result
            context.update(result.data or {})
        return result
