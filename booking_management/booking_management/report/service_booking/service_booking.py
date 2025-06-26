# Copyright (c) 2025, maddy and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
        {"label": "Booking ID", "fieldname": "name", "fieldtype": "Link", "options": "Service Booking", "width": 120},
        {"label": "Customer", "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": "Date/Time", "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 180},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100}
    ]
 
	conditions = []
	if filters.get("service_type"):
		conditions.append("service_type = %(service_type)s")
	if filters.get("status"):
		conditions.append("status = %(status)s")

	where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

	data = frappe.db.sql(f"""
        SELECT
            name, customer_name, service_type, preferred_datetime, status
        FROM
            `tabService Booking`
        {where_clause}
        ORDER BY preferred_datetime DESC
    """, filters, as_dict=True)
	return columns, data
