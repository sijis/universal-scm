"""Common Methods."""


def dynamic_dir(self):
    """Dynamically generate attributes and methods based on endpoints."""
    self_keys = list(self.__dict__.keys())
    menu_keys = list(self.api_map.keys())
    return self_keys + menu_keys
