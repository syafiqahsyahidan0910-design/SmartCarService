# vehicle_module.py

# =========================
# CLASS VEHICLE
# =========================

class Vehicle:
    def __init__(self, customer_name, vehicle_no, vehicle_model):
        self.customer_name = customer_name
        self.vehicle_no = vehicle_no
        self.vehicle_model = vehicle_model

    def calculate_charge(self, service_charges, discount=0):
        total = sum(service_charges)
        return total - (total * discount / 100)

    def __str__(self):
        return (
            f"Customer Name: {self.customer_name}\n"
            f"Vehicle Number: {self.vehicle_no}\n"
            f"Vehicle Model: {self.vehicle_model}"
        )

    def __add__(self, other):
        return len(self.vehicle_no) + len(other.vehicle_no)


# =========================
# SUBCLASS PREMIUM VEHICLE
# =========================

class PremiumVehicle(Vehicle):

    def __init__(self, customer_name, vehicle_no, vehicle_model, membership="Premium"):
        super().__init__(customer_name, vehicle_no, vehicle_model)
        self.membership = membership

    def calculate_charge(self, service_charges, discount=10):
        total = sum(service_charges)
        return total - (total * discount / 100)

    def __str__(self):
        return (
            f"Customer Name: {self.customer_name}\n"
            f"Vehicle Number: {self.vehicle_no}\n"
            f"Vehicle Model: {self.vehicle_model}\n"
            f"Membership: {self.membership}"
        )


# =========================
# FUNCTION 1
# REGISTER CUSTOMER & VEHICLE
# =========================

def register_customer(name, vehicle_no, vehicle_model, vehicle_type):
    if vehicle_type == "Premium":
        vehicle = PremiumVehicle(
            name,
            vehicle_no,
            vehicle_model
        )
    else:
        vehicle = Vehicle(
            name,
            vehicle_no,
            vehicle_model
        )

    return vehicle


# =========================
# FUNCTION 2
# CALCULATE SERVICE CHARGE
# =========================

def calculate_service_charge(services, service_list):
    charges = []

    for service in services:
        charges.append(service_list[service])

    return charges


# =========================
# FUNCTION 3
# DISPLAY INFORMATION
# =========================

def display_information(vehicle, services, charges, total):
    information = str(vehicle)

    service_info = "\nSelected Services:\n"

    for service, charge in zip(services, charges):
        service_info += f"{service}: RM{charge:.2f}\n"

    service_info += f"\nTotal Charge: RM{total:.2f}"

    return information + service_info