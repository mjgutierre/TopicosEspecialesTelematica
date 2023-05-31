from mrjob.job import MRJob
from mrjob.step import MRStep

class SalaryAverageEmployeeMR(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        # Extrae el ID del empleado y el salario de la línea
        employee_id = fields[0]
        salary = int(fields[2])
        # Emite el ID del empleado y el salario como clave-valor
        yield employee_id, salary

    def reducer(self, employee_id, salaries):
        # Calcula el salario promedio para cada empleado
        total_salary = 0
        num_salaries = 0
        for salary in salaries:
            total_salary += salary
            num_salaries += 1
        
        avg_salary = total_salary / num_salaries
        
        # Emite el ID del empleado y el salario promedio como resultado final
        yield employee_id, avg_salary

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    SalaryAverageEmployeeMR.run()
