import json
import os
import os.path


class HBConfigMeta(type):
    class __HBConfigMeta:

        base_dir = "./config/"
        base_fname = "config"

        def __init__(self):
            self.config = self.read_file(self.base_fname)

        def __call__(self, fname):
            self.config = self.read_file(fname)

        def read_file(self, fname):
            files = os.listdir(self.base_dir)
            config_files = list(filter(lambda f: f.startswith(fname + "."), files))

            if len(config_files) == 0:
                raise FileNotFoundError(f"No such files start filename '{fname}'")
            else:
                config_file = config_files[0]
                fname, fextension = os.path.splitext(config_file)

                if fextension == ".json":
                    return self.parse_json(config_file)
                elif fextension == ".yml":
                    return self.parse_yaml(config_file)

        def parse_json(self, fname):
            self.read_fname = fname
            path = os.path.join(self.base_dir + fname)
            with open(path, 'r') as infile:
                return json.loads(infile.read())

        def parse_yaml(self, fname):
            self.read_fname = fname

            import yaml
            path = os.path.join(self.base_dir + fname)
            with open(path, 'r') as infile:
                return yaml.load(infile.read())

        def __getattr__(self, name):
            config_value = self.config[name]
            if type(config_value) == dict:
                return SubConfig(config_value, get=name)
            else:
                return config_value

        def __repr__(self):
            return f"Read config file name: {self.read_fname}\n" + json.dumps(self.config, indent=4)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__HBConfigMeta()
        return cls.instance


class Config(metaclass=HBConfigMeta):
    pass


class SubConfig:

    def __init__(self, *args, get=None):
        self.get = get
        self.__dict__ = dict(*args)

    def __getattr__(self, name):
        if name in self.__dict__["__dict__"]:
            item = self.__dict__["__dict__"][name]
            if type(item) == dict:
                return SubConfig(item, get=self.get+"."+name)
            else:
                return item
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name != "get" and name != "__dict__":
            origin_config = Config.config
            gets = self.get.split(".")
            for get in gets:
                origin_config = origin_config[get]

            origin_config[name] = value

    def __repr__(self):
        return json.dumps(self.__dict__["__dict__"], indent=4)
