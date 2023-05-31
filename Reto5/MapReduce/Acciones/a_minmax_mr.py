from mrjob.job import MRJob
from mrjob.step import MRStep

class valorStockMR(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        # nombre de la compañía como clave y  tupla (precio, fecha) como valor
        yield company, (float(price), date)

    def reducer(self, company, values):
        # Encuentra el día de menor y mayor valor para cada compañía
        min_price = None
        max_price = None
        min_date = None
        max_date = None
        
        for price, date in values:
            if min_price is None or price < min_price:
                min_price = price
                min_date = date
            if max_price is None or price > max_price:
                max_price = price
                max_date = date
        
        # Emite el nombre de la compañía, el día de menor valor y el día de mayor valor como resultado final
        yield company, (min_price, min_date, max_price, max_date)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    valorStockMR.run()
