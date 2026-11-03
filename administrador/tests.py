from django.test import TestCase
from django.urls import reverse


class AdministradorViewsTests(TestCase):
	def test_panel_carga(self):
		response = self.client.get(reverse('index_admin'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Registro de Actividad Reciente')
