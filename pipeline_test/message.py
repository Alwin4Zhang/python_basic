class Message(object):
    def __init__(self, text, data=None, time=None):
        self.text = text
        self.data = data if data else {}
        self.time = time

    def set(self, prop, info):
        self.data[prop] = info

    def get(self, prop):
        return self.data.get(prop)

    def as_dict(self):
        return dict(self.data, text=self.text)
