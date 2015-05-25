from py27compat import properties


def test_AutoBindingMethod():
	class Example(object):
		@properties.simplemethod
		def method(self):
			return 'called with {!r}'.format(self)

	ex = Example()
	assert ex.method().startswith('called with {!r}'.format(ex))

	assert Example.method('some value') == "called with 'some value'"
