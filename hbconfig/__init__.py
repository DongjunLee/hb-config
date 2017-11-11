import json
import os
import os.path



class HBConfigMeta(type):
    class __HBConfigMeta:

        base_dir = "./config/"
        base_fname = "config"

        def __init__(self, is_new=False):
            self.is_new = is_new
            self.config = None

            if is_new is False:
                self.config = self.read_file(self.base_fname)

        def __call__(self, fname):
            self.is_new = False
            if fname is None:
                self.config = self.read_file(self.base_fname)
            else:
                self.config = self.read_file(fname)

        def read_file(self, fname):
            if not os.path.isdir(fname) and os.path.exists(fname):
                path = fname
                fname, fextension = os.path.splitext(path)
                self.read_fname = fname

                return self._read_file(path, fextension)

            files = os.listdir(self.base_dir)
            config_files = list(filter(lambda f: f.startswith(fname + "."), files))

            if len(config_files) == 0 and self.is_new is False:
                raise FileNotFoundError(f"No such files start filename '{fname}'")
            else:
                config_file = config_files[0]
                fname, fextension = os.path.splitext(config_file)
                self.read_fname = self.base_dir + fname

                path = os.path.join(self.base_dir, config_file)
                return self._read_file(path, fextension)

        def _read_file(self, path, fextension):
            if fextension == ".json":
                return self.parse_json(path)
            elif fextension == ".yml":
                return self.parse_yaml(path)

        def parse_json(self, path):
            with open(path, 'r') as infile:
                return json.loads(infile.read())

        def parse_yaml(self, path):
            import yaml
            path = os.path.join(path)
            with open(path, 'r') as infile:
                return yaml.load(infile.read())

        def to_dict(self):
            return self.config

        def get(self, name, default=None):
            try:
                return self.__getattr__(name)
            except KeyError as ke:
                return default

        def __getattr__(self, name):
            self._set_config()

            config_value = self.config[name]
            if type(config_value) == dict:
                return SubConfig(config_value, get_tag=name)
            else:
                return config_value

        def __repr__(self):
            if self.config is None:
                raise FileNotFoundError(f"No such files start filename '{self.base_fname}'")
            else:
                return f"Read config file name: {self.read_fname}\n" + json.dumps(self.config, indent=4)

        def _set_config(self):
            if self.config is None:
                self.is_new = False
                self.config = self.read_file(self.base_fname)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__HBConfigMeta(is_new=True)
        return cls.instance


class Config(metaclass=HBConfigMeta):
    pass


class SubConfig:

    def __init__(self, *args, get_tag=None):
        self.get_tag = get_tag
        self.__dict__ = dict(*args)

    def __getattr__(self, name):
        if name in self.__dict__["__dict__"]:
            item = self.__dict__["__dict__"][name]
            if type(item) == dict:
                return SubConfig(item, get_tag=self.get_tag+"."+name)
            else:
                return item
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name != "get" and name != "__dict__":
            origin_config = Config.config
            gets = self.get_tag.split(".")
            for get in gets:
                origin_config = origin_config[get]

            origin_config[name] = value

    def get(self, name, default=None):
        return self.__dict__["__dict__"].get(name, default)

    def to_dict(self):
        return self.__dict__["__dict__"]

    def __repr__(self):
        return json.dumps(self.__dict__["__dict__"], indent=4)
