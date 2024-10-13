class Introspection_info:
    def __init__(self, obj):
        self.obj = obj
        self.info = self._get_introspection_info()

    def _get_introspection_info(self):
        # Получаем тип объекта
        object_type = "class" if isinstance(self.obj, type) else type(self.obj).__name__
        attributes = []
        methods = []

        for attr in dir(self.obj):
            if not callable(getattr(self.obj, attr)): # Проверяем на вызов метода
                attributes.append(attr)
            else:
                methods.append(attr)

        info = {
            'type': object_type,
            'attributes': attributes,
            'methods': methods,
            'module': getattr(self.obj, '__module__', 'N/A') # Модуль может быть недоступен
        }

        # Дополнительная информация в зависимости от типа объекта

        if isinstance(self.obj, (int, float, complex)):
            info['real'] = getattr(self.obj, 'real', None)
            info['imag'] = getattr(self.obj, 'imag', None)
        elif isinstance(self.obj, str):
            info['length'] = len(self.obj)
            info['label'] = str(self.obj)
        elif isinstance(self.obj, list):
            info['length'] = len(self.obj)
            info['items'] = self.obj[:]
        elif isinstance(self.obj, dict):
            info['keys'] = list(self.obj.keys())
            info['values'] = list(self.obj.values())


        return info

    def get_info(self):
        return self.info


# Пример работы:
number_info = Introspection_info(42)
print(number_info)

string_info = Introspection_info("Bubba Kastorsky!")
print(string_info)

list_info = Introspection_info([1, 2, 3])
print(list_info)

Class_info = Introspection_info(Introspection_info)
print(Class_info)

func_info = Introspection_info(Introspection_info._get_introspection_info)
print(func_info)
