from django_faker import Faker
# this Populator is only a function thats return a django_faker.populator.Populator instance
# correctly initialized with a faker.generator.Generator instance, configured as above
populator = Faker.getPopulator()

from .models import Student, Course
populator.addEntity(Student, 5, {
    'student_id': lambda x: populator.generator.randomInt(10000001, 19999999),
    'group': lambda x: int('1' + str(populator.generator.randomInt(100, 999)) + str(populator.generator.randomInt(1, 4)))
})
populator.addEntity(Course,10, {
    'mark': lambda x: populator.generator.randomInt(1,10),
    'name': lambda x: populator.generator.choise(['AOIS', 'PPOIS', 'INFBEZ', 'LOIS', 'MAIOS'])
})

insertedPks = populator.execute()