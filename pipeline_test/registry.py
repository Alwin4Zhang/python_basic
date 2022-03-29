import utils
from components import Component
from tokenizer import JiebaTokenizer
from regex_featurizer import RegexFeaturizer

component_classes = [
    JiebaTokenizer, RegexFeaturizer
]

registered_components = {c.name: c for c in component_classes}

registered_pipeline_templates = {}


def get_component_class(component_name):
    if component_name not in registered_components:
        try:
            return utils.class_from_module_path(component_name)
        except Exception:
            raise Exception("Component {} not found".format(component_name))
    return registered_components[component_name]


# print(get_component_class("tokenizer_jieba"))
