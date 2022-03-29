import jieba

from components import Component
from message import Message


class Tokenizer(object):
    pass


class Token(object):
    def __init__(self, text, offset, data=None):
        self.offset = offset
        self.text = text
        self.end = offset + len(text)
        self.data = data if data else {}

    def set(self, prop, info):
        self.data[prop] = info

    def get(self, prop, default=None):
        return self.data.get(prop, default)


class JiebaTokenizer(Tokenizer, Component):
    name = "tokenizer_jieba"
    provides = ["tokens"]
    language_list = ["zh"]

    def __init__(self, tokenizer=None):
        super(JiebaTokenizer, self).__init__()
        self.tokenizer = tokenizer if tokenizer else jieba

    def process(self, message, **kwargs):
        message.set("tokens", self.tokenize(message.text))

    def tokenize(self, text):
        return [Token(word, start) for i, (word, start, end) in enumerate(self.tokenizer.tokenize(text))]

# message = Message("测试")
# tokenizer = JiebaTokenizer()
#
# tokenizer.process(message)
# print(message.as_dict())


# text = "测试你好"
# res = [Token(word, start) for i, (word, start, end) in enumerate(jieba.tokenize(text))]
# print(res)
