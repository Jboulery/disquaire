from django.core.urlresolvers import reverse
from django.test import TestCase

from store.models import Album, Artist, Booking, Contact


#Index page
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


#DetailPage
class DetailPageTestCase(TestCase):
    def setUp(self):
        impossible = Album.objects.create(title='Transmission Impossible')
        self.album = Album.objects.get(title='Transmission Impossible')

    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:detail', args=(album_id, )))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self):
        album_id = self.album.id + 1
        response = self.client.get(reverse('store:detail', args=(album_id, )))
        self.assertEqual(response.status_code, 404)


#BookingPage
class BookingPageTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(name='Freddie', email='fred@example.com')
        impossible = Album.objects.create(title='Transmission Impossible')
        journey = Artist.objects.create(name='Journey')
        impossible.artists.add(journey)
        self.contact = Contact.objects.get(name='Freddie')
        self.album = Album.objects.get(title='Transmission Impossible')

    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id, )), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings + 1)
