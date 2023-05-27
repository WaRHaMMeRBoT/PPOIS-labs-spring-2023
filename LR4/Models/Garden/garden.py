from Models.Weather.weather import Weather

class BaseGarden:
    WEATHER = Weather()

    def __init__(self, fields):
        self._fields = fields

    def next_day(self):
        health_impact = self.WEATHER.is_sunny
        hydro_impact = 2
        for field in self.fields:
            if field.plant:
                field.plant.get_hydrated(hydro_impact)
                field.plant.health += health_impact
            field.grow()
            if hasattr(field.plant, 'ready_plant'):
                if field.plant.ready_plant:
                    field.plant = field.plant.ready_plant

        self.WEATHER.next_day()

    @property
    def fields(self):
        return self._fields
