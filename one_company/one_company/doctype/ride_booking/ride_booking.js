// Copyright (c) 2023, ali jafer and contributors
// For license information, please see license.txt

frappe.ui.form.on('ride booking', {
	 refresh(frm) {
		frm.add_custom_button("Create A Ride", () => {
			let dialog = new frappe.ui.dialog({
				title: "Select Driver",
				fields: [
					{
						fieldtype: "link",
						fieldname: "driver",
						label: "driver",
						option: "driver",
					},
				],
				primary_action_label:"create ride",
				primary_action: (data) => {
					console.log(data);
					let{driver} = data;


					frappe.new_doc("ride", {
						cars: frm.doc.cars,
						driver: driver,
					});
				},
			});
			dialog.show();
		});
	 },
	});
 