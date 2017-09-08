import json
import os
import os.path


class HBConfigMeta(type):
    class __HBConfigMeta:

        base_dir = "./config/"
        base_fname = "config"

        def __init__(self):
            self.config = self.read_file()

        def read_file(self):
            files = os.listdir(self.base_dir)
            config_files = list(filter(lambda f: f.startswith(self.base_fname + "."), files))

            if len(config_files) == 0:
                raise FileNotFoundError("No such files start filename 'config'")
            else:
                config_file = config_files[0]
                fname, fextension = os.path.splitext(config_file)

                if fextension == ".json":
                    return self.parse_json(config_file)
                elif fextension == ".yml":
                    return self.parse_yaml(config_file)

        def parse_json(self, fname):
            path = os.path.join(self.base_dir + fname)
            with open(path, 'r') as infile:
                return json.loads(infile.read())

        def parse_yaml(self, fname):
            import yaml
            path = os.path.join(self.base_dir + fname)
            with open(path, 'r') as infile:
                return yaml.load(infile.read())

        def __getattr__(self, name):
            config_value = self.config[name]
            if type(config_value) == dict:
                return SubConfig(config_value)
            else:
                return config_value

        def __repr__(self):
            return json.dumps(self.config, indent=4)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__HBConfigMeta()
        return cls.instance


class Config(metaclass=HBConfigMeta):
    pass


class SubConfig:

    def __init__(self, input_dict):
        if type(input_dict) != dict:
            raise TypeError("input_dict must be a dict type")
        self.subconfig = input_dict

    def __getattr__(self, name):
        if name == "get":
            return self.subconfig.get

        config_value = self.subconfig[name]
        if type(config_value) == dict:
            return SubConfig(config_value)
        else:
            return config_value

    def __repr__(self):
        return json.dumps(self.subconfig, indent=4)
