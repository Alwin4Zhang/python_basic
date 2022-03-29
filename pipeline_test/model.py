from message import Message
from registry import get_component_class


class Interperter(object):
    @staticmethod
    def default_output_attributes():
        return {"intent": {"name": "", "confidence": 0.0}, "entities": []}

    def __init__(self, pipeline, context=None):
        self.pipeline = pipeline
        self.context = context if context is not None else {}

    def parse(self, text, time=None):
        if not text:
            output = self.default_output_attributes()
            output["text"] = ""
            return output
        message = Message(text, time=time)
        for component in self.pipeline:
            component_name = component.get("name")
            component = get_component_class(component_name)()
            component.process(message)
        output = self.default_output_attributes()
        output.update(message.as_dict())
        return output


from pprint import pprint
from utils import read_yaml_file

path = "config.yml"
text = "我想要查询我的账户余额"
pipeline = read_yaml_file(path).get("pipeline", [])
interperter = Interperter(pipeline)
output = interperter.parse(text)
pprint(output)
