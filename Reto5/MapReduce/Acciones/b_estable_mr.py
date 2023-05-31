from mrjob.job import MRJob
from mrjob.step import MRStep

class EstableAltoStock(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae el nombre de la empresa y el precio de la línea
        company = fields[0]
        price = float(fields[1])
        
        # nombre de la empresa como clave y precio como valor
        yield company, price

    def reducer(self, company, prices):
        price_list = list(prices)
        
        # Verifica si los precios siempre han subido o se han mantenido estables
        if all(price_list[i] <= price_list[i+1] for i in range(len(price_list)-1)):
            # Emite el nombre de la empresa como resultado final
            yield company, None

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    EstableAltoStock.run()
