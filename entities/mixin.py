class Mixin:    # essa é uma classe do tipo mixin. Não tem funcionalidade própria, serve para fornecer funcionalidade a outras classes.
    def create_fields(self, local_variables_dict) -> None:   # essa implementação está muuuuito mais elegante
        variables = [parameter for parameter in self.__init__.__code__.co_varnames if parameter != "self"]
        for variable in variables:
                value = local_variables_dict[variable]
                if value != None:
                    self.__dict__[variable] = value
    
    def set_version(self, version: str) -> None:
        self.version = version
