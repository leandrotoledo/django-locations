from django.test import TestCase

from models import *

class PlaceModelsTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(country=u'Brasil', code=u'BR')
        self.region = Region.objects.create(region=u'Sudeste', country=self.country)
        self.state = State.objects.create(state=u'Rio de Janeiro', code=u'RJ', region=self.region)
        self.mesoregion = MesoRegion.objects.create(mesoregion=u'Centro Fluminense', state=self.state)
        self.microregion = MicroRegion.objects.create(microregion=u'Nova Friburgo', mesoregion=self.mesoregion)
        self.municipality = Municipality.objects.create(municipality=u'Bom Jardim', microregion=self.microregion)
        self.district = District.objects.create(district=u'Barra Alegre', municipality=self.municipality)
        self.point = Point.objects.create(postal_code=u'05877330', street_name=u'Rua Renato da Cunha', street_number=u'213')
        self.place = Place.objects.create(city=self.municipality, district=self.district, point=self.point)

    def test_creating_a_new_country_and_saving_it_to_the_database(self):
        all_countries_in_database = Country.objects.all()
        self.assertEquals(len(all_countries_in_database), 1)

        only_country_in_database = Country.objects.get(pk=1)
        self.assertEquals(only_country_in_database, self.country)

    def test_creating_a_new_region_and_saving_it_to_the_database(self):
        all_regions_in_database = Region.objects.all()
        self.assertEquals(len(all_regions_in_database), 1)

        only_region_in_database = Region.objects.get(pk=1)
        self.assertEquals(only_region_in_database, self.region)

        self.assertIsInstance(self.region.country, Country)

    def test_creating_a_new_state_and_saving_it_to_the_database(self):
        all_states_in_database = State.objects.all()
        self.assertEquals(len(all_states_in_database), 1)

        only_state_in_database = State.objects.get(pk=1)
        self.assertEquals(only_state_in_database, self.state)

        self.assertIsInstance(self.state.region, Region)

    def test_creating_a_new_mesoregion_and_saving_it_to_the_database(self):
        all_mesoregions_in_database = MesoRegion.objects.all()
        self.assertEquals(len(all_mesoregions_in_database), 1)

        only_mesoregion_in_database = MesoRegion.objects.get(pk=1)
        self.assertEquals(only_mesoregion_in_database, self.mesoregion)

        self.assertIsInstance(self.mesoregion.state, State)

    def test_creating_a_new_microregion_and_saving_it_to_the_database(self):
        all_microregions_in_database = MicroRegion.objects.all()
        self.assertEquals(len(all_microregions_in_database), 1)

        only_microregion_in_database = MicroRegion.objects.get(pk=1)
        self.assertEquals(only_microregion_in_database, self.microregion)

        self.assertIsInstance(self.microregion.mesoregion, MesoRegion)

    def test_creating_a_new_municipality_and_saving_it_to_the_database(self):
        all_municipalities_in_database = Municipality.objects.all()
        self.assertEquals(len(all_municipalities_in_database), 1)

        only_municipality_in_database = Municipality.objects.get(pk=1)
        self.assertEquals(only_municipality_in_database, self.municipality)

        self.assertIsInstance(self.municipality.microregion, MicroRegion)

    def test_creating_a_new_district_and_saving_it_to_the_database(self):
        all_districts_in_database = District.objects.all()
        self.assertEquals(len(all_districts_in_database), 1)

        only_district_in_database = District.objects.get(pk=1)
        self.assertEquals(only_district_in_database, self.district)

        self.assertIsInstance(self.district.municipality, Municipality)
