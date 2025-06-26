# Copyright (c) 2025, maddy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServiceBooking(Document):
    def before_save(self):
        if self.workflow_state == "Requested":
            self.status = "Requested"
        elif self.workflow_state == "Approved":
            self.status = "Approved"
        elif self.workflow_state == "Completed":
            self.status = "Completed"

        if (
            self.workflow_state == "Approved"
            and self.status == "Approved"
            and not self.flags.email_sent
        ):
            customer_email = self.get_customer_email_from_address()

            if customer_email:
                frappe.sendmail(
                    recipients=[customer_email],
                    subject="Service Booking Approved",
                    message=f"""Dear {self.customer_name},<br><br>
                    Your service booking for <b>{self.service_type}</b> has been approved.<br><br>
                    Thank you!"""
                )

                self.flags.email_sent = True  

    def get_customer_email_from_address(self):
        address_name = frappe.db.get_value(
            "Dynamic Link", 
            {
                "link_doctype": "Customer",
                "link_name": self.customer_name,
                "parenttype": "Address"
            }, 
            "parent"
        )

        if address_name:
            return frappe.db.get_value("Address", address_name, "email_id")

        return None
