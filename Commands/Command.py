class Command:

    @staticmethod
    def get_command_prefix():
        return "Test"

    def __init__(self):
        self._pattern = "{-1} {0}, {1}, {2} command"
        self._params = []
        self.__params_data = None
        self.string = None

    def add_param(self, param: str, index: int = -1):
        self._params.insert(index, param)

    def replace_param(self, new_param: str, index: int):
        self._params.remove(self._params[index])
        self._params.insert(index, new_param)

    def init(self):
        self.__params_data = self.__parse_param_pattern()

    def prepare(self):
        self.string = self._pattern[::]
        self._params.insert(0, self.get_command_prefix())
        for start_index, end_index, num in self.__params_data:
            self.string = self.string[:start_index] + self._params[num] + self.string[end_index:]

    def get_string(self) -> str:
        if self.string is None:
            self.prepare()
        return self.string

    # получение списка индексов (начало и конец) параметров
    def __parse_param_pattern(self):
        params_data = []
        start_ = None
        num = ""
        for index, i in enumerate(self._pattern):
            if i == "{":
                start_ = index
            elif i == "}":
                params_data.append((start_, index, int(num)))
                start_ = None
                num = ""
            else:
                num += i
        return params_data
