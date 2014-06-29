class meal(object):
	meat = 'none'
	veg = 'none'
	type = 'curry'

today = meal()
today.meat='chicken'
today.veg = 'radishes'
#today.type = 'whelk stew'

tomorrow = meal()
tomorrow.meat = "human flesh"
tomorrow.veg = "terri scheipo"
tomorrow.type = "zombie"


print today.meat, today.veg, today.type