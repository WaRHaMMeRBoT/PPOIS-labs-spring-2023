from plant import Plant
import my_enums
from typing import List, NoReturn
import random


class Urut(Plant):

    _life_median = my_enums.LifeMedian.URUT_LM.value
    _max_hp = my_enums.MaxHP.URUT_MHP.value
    _start_hp = my_enums.StartHP.URUT_START_HP.value
    _hp_reduction = my_enums.PlantHPReduction.URUT_HPR.value
    _offspring_dispersion = my_enums.PlantOffspringDispersion.URUT_OD.value
    _offspring_nutritional_value = my_enums.NutritionalValue.URUT_OFFSPRING_NV.value
    _start_shrub_nutritional_value = my_enums.NutritionalValue.START_URUT_SNV.value
    _shrub_reduction = my_enums.PlantShrubReduction.URUT_SR.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.URUT_RAI.value
    _id_counter = 0

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Urut._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Urut._id_counter})")
        Urut._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Urut._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Urut._id_counter += 1
            return
        self._age = 0
        self._hp = self._start_hp
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(my_enums.PersonalPowerCoefficientParameters.URUT_PPCP)
        self._id = my_enums.IdPrefix.URUT_PREF.value + str(self._id_counter)
        Urut._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        start_power = my_enums.StartPower.URUT_SP.value
        k_func_coefficient = my_enums.PowerFunctionCoefficient.SEDGE_PFC.value
        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        else:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))

    def produce_eatable_offspring(self) -> NoReturn:
        min_amount, max_amount = my_enums.PlantEatableOffspringPossibleAmount.URUT_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = my_enums.ChanceToProduceKids.URUT_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce == 1:
            min_amount, max_amount = my_enums.PossibleKidsAmount.URUT_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Urut() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value) -> int:
        if nutritional_value > self._nutritional_value:
            self._nutritional_value = 0
            self.get_hearted(int(0.5 * (nutritional_value - self._nutritional_value)))
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(int(nutritional_value * my_enums.UnprotectedDamageMultiplier.URUT_UDM.value))
        return nutritional_value

    def stats(self) -> str:
        return """ Kingdom: Plant
 Kind: Urut
    """ + super().stats()