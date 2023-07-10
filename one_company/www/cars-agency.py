import frappe

def get_context(context):
    cars = frappe.get_list(
        "cars",
        filters={"is_published": 1},
        filters=["name", "make", "model", "cars_image"],
        order_by="make desc"
    )
    context.cars = cars    