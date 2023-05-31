from mrjob.job import MRJob
from mrjob.step import MRStep

class BlackDayMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae el nombre de la empresa, el precio y la fecha de la línea
        company = fields[0]
        price = float(fields[1])
        date = fields[2]
        
        # día como clave y una tupla (empresa, precio) como valor
        yield date, (company, price)

    def reducer(self, date, values):
        # Inicializa una lista para almacenar las acciones con el menor valor de acción
        min_price_companies = []
        min_price = float('inf')
        
        # Encuentra el valor de acción más bajo para cada día y guarda las acciones correspondientes
        for company, price in values:
            if price < min_price:
                min_price = price
                min_price_companies = [company]
            elif price == min_price:
                min_price_companies.append(company)
        
        yield date, min_price_companies

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    BlackDayMR.run()
