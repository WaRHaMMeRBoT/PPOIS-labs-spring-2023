from unittest import TestCase

from main import Garden, Weed, Sun


class TestGarden(TestCase):
    def setUp(self) -> None:
        self.g = Garden()

    def test_new_bed(self):
        self.g.new_bed()
        assert self.g.bed is not None

    def test_new_seed(self):
        self.g.new_seed()
        counter: int = 0
        for seed in self.g.bed.place:
            if seed is not None:
                counter += 1
        assert counter == 1

    def test_new_fruit_tree(self):
        self.g.new_fruit_tree()
        assert len(self.g.trees) == 1

    def test_fertile_garden(self):
        self.g.new_seed()
        previous_fertility: int = 0
        new_fertility: int = 0
        for seed in self.g.bed.place:
            if seed is not None:
                previous_fertility = seed.get_immunity_info()
                self.g.fertile_garden()
                new_fertility = seed.get_immunity_info()
                break
        assert new_fertility > previous_fertility

    def test_love_garden(self):
        self.g.new_seed()
        previous_damage: int = 0
        new_damage: int = 0
        for seed in self.g.bed.place:
            if seed is not None:
                previous_damage = seed.get_damage_info()
                self.g.love_garden()
                new_damage = seed.get_damage_info()
                break
        assert new_damage > previous_damage

    def test_weeding_garden(self):
        self.g.misery.weed = Weed()
        self.g.misery.weed.capture_bed(self.g.bed)
        for weed in self.g.bed.place:
            if isinstance(weed, Weed):
                assert True
                return
        assert False

    def test_sun(self):
        self.g.new_bed()
        self.g.new_fruit_tree()
        sun = Sun()
        previous_sun: int = 0
        new_sun: int = 0
        for tree in self.g.trees:
            if tree is not None:
                previous_sun = tree.get_sun_info()
                sun.shine_trees(self.g.trees)
                new_sun = tree.get_sun_info()
                break
        assert new_sun > previous_sun
