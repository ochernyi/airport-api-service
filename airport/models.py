from django.db import models

from users.models import User


class Airport(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    closest_big_city = models.CharField(max_length=255, null=False, blank=False)


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="source_routes")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination_routes")
    distance = models.IntegerField()


class Crew(models.Model):
    first_name = models.CharField(max_length=65, null=False, blank=False)
    last_name = models.CharField(max_length=65, null=False, blank=False)


class AirplaneType(models.Model):
    name = models.CharField(max_length=112, null=False, blank=False)


class Airplane(models.Model):
    name = models.CharField(max_length=112, null=False, blank=False)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE, related_name="airplanes")


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Order(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_orders")


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_tickets")
