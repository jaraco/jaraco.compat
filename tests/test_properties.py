from py27compat import properties


def test_AutoBindingMethod():
	class Example(object):
		@properties.simplemethod
		def method(self):
			return 'called with {self!r}'.format(self=self)

	ex = Example()
	assert ex.method().startswith('called with {ex!r}'.format(ex=ex))

	assert Example.method('some value') == "called with 'some value'"
