import datetime 

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.Verifica(*args)

    def Verifica(self, *args): # Função que retorna o valor após convertido
        for l in args:
            ll = self.Modifica(l)
            if ll is not None:
                self.datas.append(ll)

    def Modifica(self, data): # Função que Modifica as datas recebidas como String para o tipo Date
        if isinstance(data, datetime.date):
            return data
        try:
            new_value = datetime.datetime.strptime(data, '%d/%m/%Y').date()
            return new_value
        except (ValueError, TypeError):
            return None

    def add_holiday(self, *dates): 
        self.Verifica(*dates)
        local_datas = set(self.datas)
        self.datas = list(local_datas)

    def check_holiday(self, dt):
        l = self.Modifica(dt)
        if l is not None and l in self.datas:
            return True
        else:
            return False
