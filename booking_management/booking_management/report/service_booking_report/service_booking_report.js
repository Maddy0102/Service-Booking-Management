// Copyright (c) 2025, maddy and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking Report"] = {
	"filters": [
		{
			fieldname: "service_type",
			label: "Service Type",
			fieldtype: "Link",
			options: "Service Type",
			reqd: 0
		},
		{
			fieldname: "status",
			label: "Status",
			fieldtype: "Select",
			options: [
				"",
				"Requested",
				"Approved",
				"Completed",
			],
			reqd: 0
		}
	]
};
