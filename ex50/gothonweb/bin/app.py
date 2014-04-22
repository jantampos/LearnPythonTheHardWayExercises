import web

urls = (
 	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Jan Aubrey Tomada Tampos"
		return render.foo(greeting = None)

if __name__ == "__main__":
	app.run()

