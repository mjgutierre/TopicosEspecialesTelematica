from mrjob.job import MRJob
from mrjob.step import MRStep

class WorstRatingDayMR(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae la fecha y el rating de la línea
        date = fields[4]
        rating = float(fields[2])
        
        yield date, rating # Emite la fecha como clave y el rating como valor

    def reducer(self, date, ratings):
        rating_sum = 0
        rating_count = 0
        
        # Recorre los ratings y realiza la sumatoria y el conteo
        for rating in ratings:
            rating_sum += rating
            rating_count += 1
        
        average_rating = rating_sum / rating_count # Calcula el rating promedio
        
        yield average_rating, date # Emite el rating promedio junto con la fecha

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    WorstRatingDayMR.run()

