SELECT xmlelement(
	name warehouses,
	xmlagg(
		xmlelement(
			name warehouse,
			xmlelement(name id, w.w_id),
			xmlelement(name name, w.w_name),
			xmlelement(
				name address,
				xmlelement(name street, w.w_street),
				xmlelement(name city, w.w_city),
				xmlelement(name country, w.w_country)
			),
			xmlelement(
				name items,
				(
					SELECT xmlagg(
						xmlelement(
							name item,
							xmlelement(name id, i.i_id),
							xmlelement(name im_id, i.i_im_id),
							xmlelement(name name, i.i_name),
							xmlelement(name price, i.i_price),
							xmlelement(name qty, s.s_qty)
						)
					)
					FROM stock s, item i
					WHERE s.w_id = w.w_id
					AND s.i_id = i.i_id
				)
			)
		)
		ORDER BY w.w_id ASC
	)
)
FROM warehouse w