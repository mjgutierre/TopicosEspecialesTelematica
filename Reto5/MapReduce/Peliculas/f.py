from mrjob.job import MRJob
from mrjob.step import MRStep

class BestRatingDayMR(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae la fecha y el rating de la línea
        date = fields[4]
        rating = float(fields[2])
        
        yield date, rating # Emite la fecha como clave y el rating como valor
    
    def reducer(self, date, ratings):
        rating_sum = 0 #rating promedio 
        rating_count = 0
        
        # Recorre los ratings y realiza la sumatoria y el conteo
        for rating in ratings:
            rating_sum += rating
            rating_count += 1
        
        # Calcula el rating promedio
        average_rating = rating_sum / rating_count
        
        # Emite el rating promedio junto con la fecha
        yield average_rating, date

    def steps(self):
            return [
                MRStep(mapper=self.mapper, reducer=self.reducer)
            ]

if __name__ == '__main__':
    BestRatingDayMR.run()
