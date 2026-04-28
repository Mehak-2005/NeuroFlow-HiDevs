class RoutingCriteria:
    def __init__(self, task_type, require_vision=False, require_long_context=False):
        self.task_type = task_type
        self.require_vision = require_vision
        self.require_long_context = require_long_context

class ModelRouter:

    def route(self, criteria):
        if criteria.require_long_context:
            return "anthropic"
        return "openai"