# Core Components
dcc.Dropdown(
	options=[
		{'label': 'New York City', 'value': 'NYC'},
		{'label': u'Montréal', 'value': 'MTL'},
		{'label': 'San Francisco', 'value': 'SF'}
	],
	value='MTL'
)

html.Label('Multi-Select Dropdown'),
	dcc.Dropdown(
		options=[
			{'label': 'New York City', 'value': 'NYC'},
			{'label': u'Montréal', 'value': 'MTL'},
			{'label': 'San Francisco', 'value': 'SF'}
		],
		value=['MTL', 'SF'],
		multi=True
	)

html.Label('Radio Items'),
	dcc.RadioItems(
		options=[
			{'label': 'New York City', 'value': 'NYC'},
			{'label': u'Montréal', 'value': 'MTL'},
			{'label': 'San Francisco', 'value': 'SF'}
		],
		value='MTL'
	)

html.Label('Checkboxes'),
	dcc.Checklist(
		options=[
			{'label': 'New York City', 'value': 'NYC'},
			{'label': u'Montréal', 'value': 'MTL'},
			{'label': 'San Francisco', 'value': 'SF'}
		],
		values=['MTL', 'SF']
	)

html.Label('Text Box'),
	dcc.Input(value='MTL', type='text')


# Calling help
help(dcc.Input)