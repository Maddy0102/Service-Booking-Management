import frappe
from frappe.model.document import Document
import json

@frappe.whitelist(allow_guest=True)
def create_service_booking(data):
    data = json.loads(data)

    customer_name = data.get("customer_name")
    email = data.get("email")
    phone = data.get("phone")
    address_line1 = data.get("address_line1")
    address_line2 = data.get("address_line2")
    service_type = data.get("service_type")
    preferred_datetime = data.get("preferred_datetime")
    is_existing_customer = data.get("is_existing_customer")

    if not is_existing_customer:
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_name,
            "customer_type": "Individual",
            "territory": "India"
        }).insert(ignore_permissions=True)

        customer_name = customer.name

        address = frappe.get_doc({
            "doctype": "Address",
            "address_title": customer_name,
            "address_type": "Billing",
            "address_line1": address_line1,
            "city": address_line2,
            "phone": phone,
            "email_id": email,
            "links": [{
                "link_doctype": "Customer",
                "link_name": customer_name
            }]
        }).insert(ignore_permissions=True)

    booking = frappe.get_doc({
        "doctype": "Service Booking",
        "customer_name": customer_name,
        "service_type": service_type,
        "preferred_datetime": preferred_datetime,
        "status": "Requested"
    }).insert(ignore_permissions=True)

    return {
        "message": "Booking requested successfully!",
        "booking_id": booking.name
    }

@frappe.whitelist(allow_guest=True)
def get_customer_address(customer_name):
    link = frappe.db.get_all(
        "Dynamic Link",
        filters={
            "link_doctype": "Customer",
            "link_name": customer_name,
            "parenttype": "Address"
        },
        fields=["parent"],
        limit=1
    )

    if not link:
        return {}

    address_doc = frappe.get_doc("Address", link[0]["parent"])
    return {
        "address_line1": address_doc.address_line1,
        "address_line2": address_doc.city,
        "email": address_doc.email_id,
        "phone": address_doc.phone
    }
