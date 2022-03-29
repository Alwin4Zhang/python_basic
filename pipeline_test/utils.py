import os
import io
import json
import yaml
import importlib


def write_to_file(filename, text):
    # type: (Text, Text) -> None
    """Write a text to a file."""

    with io.open(filename, 'w', encoding="utf-8") as f:
        f.write(str(text))


def read_file(filename, encoding="utf-8-sig"):
    """Read text from a file."""
    with io.open(filename, encoding=encoding) as f:
        return f.read()


def json_to_string(obj, **kwargs):
    indent = kwargs.pop("indent", 2)
    ensure_ascii = kwargs.pop("ensure_ascii", False)
    return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii, **kwargs)


def write_json_to_file(filename, obj, **kwargs):
    # type: (Text, Any) -> None
    """Write an object as a json string to a file."""

    write_to_file(filename, json_to_string(obj, **kwargs))


def class_from_module_path(module_path):
    if '.' in module_path:
        module_name, _, class_name = module_path.rpartition('.')
        m = importlib.import_module(module_name)
        # get the class,will raise AttributeError if class does not exist
        return getattr(m, class_name)
    else:
        return globals()[module_path]


def module_path_from_object(o):
    """Returns the fully qualified class path of the instantiated object."""
    return o.__class__.__module__ + "." + o.__class__.__name__


def fix_yaml_loader():
    """Ensure that any string read by yaml is represented as unicode."""
    from yaml import Loader, SafeLoader

    def construct_yaml_str(self, node):
        # Override the default string handling function
        # to always return unicode objects
        return self.construct_scalar(node)

    Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)
    SafeLoader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)


def read_yaml_file(filename):
    fix_yaml_loader()
    return yaml.load(read_file(filename, 'utf-8'))
