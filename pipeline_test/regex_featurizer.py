import numpy as np

from components import Component

REGEX_FEATURIZER_FILE_NAME = "regex_featurizer.json"


class Featurizer(Component):
    @staticmethod
    def _combine_with_existing_text_features(message, additional_features):
        if message.get("text_features") is not None:
            return np.hstack((message.get("text_features"),
                              additional_features))
        else:
            return additional_features


class RegexFeaturizer(Featurizer):
    name = "intent_entity_featurizer_regex"
    providers = ["text_features"]
    requires = ["tokens"]

    def __init__(self, known_patterns=False):
        super(RegexFeaturizer, self).__init__()
        self.known_patterns = known_patterns if known_patterns else []

    def process(self, message, **kwargs):
        updated = self._text_features_with_regex(message)
        message.set("text_features", updated)

    def _text_features_with_regex(self, message):
        if self.known_patterns is not None:
            extras = self.features_for_patterns(message)
            return self._combine_with_existing_text_features(message, extras)
        else:
            return message.get("text_features")

    def features_for_patterns(self, message):
        found = []
        for i, exp in enumerate(self.known_patterns):
            match = res.search(exp['pattern'], message.text)
            if match is not None:
                for t in message.get("tokens", []):
                    if t.offset < match.end() and t.end > match.start():
                        t.set("pattern", i)
                        found.append(1.0)
                    else:
                        found.append(0.0)
        return np.array(found)
