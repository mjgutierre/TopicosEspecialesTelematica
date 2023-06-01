from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieRatingsMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae el ID del usuario, el ID de la película y la calificación de la línea
        user_id = fields[0]
        movie_id = fields[1]
        rating = float(fields[2])
        
        # Emite el ID del usuario como clave y una tupla (1, rating) como valor
        yield user_id, (1, rating)

    def reducer(self, user_id, values):
        # Inicializa variables para contar el número de películas y calcular la suma de calificaciones
        movie_count = 0
        rating_sum = 0
        
        # Recorre los valores y realiza la sumatoria de películas y calificaciones
        for value in values:
            movie_count += value[0]
            rating_sum += value[1]
        
        # Calcula el valor promedio de calificación
        average_rating = rating_sum / movie_count
        
        # Emite el ID del usuario junto con el número de películas y el valor promedio de calificación
        yield user_id, (movie_count, average_rating)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MovieRatingsMR.run()
