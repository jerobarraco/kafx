# -*- coding: utf-8 -*-
"""
May 2012
@author: MoonGate
"""
#Incluimos todo lo necesario
#el modulo web pertenece al proyecto web.py es necesario para todo lo que tiene que ver con web
import web
#datetime es una clase de python para el manejo del tiempo
import datetime
#clases creadas en este proyecto
#urls es una tupla, conteniendo una secuencia de urls y la clase manejadora que corresponde
urls = (
	'/', 'main',
	'/logout/', 'logout',
	'/register/', 'user.Register',
	'/thread/', 'fthread.fthread',
	'/thread/list/', 'fthread.tList',
	'/thread/edit/', 'fthread.tEdit',
	'/thread/delete/', 'fthread.tDelete',
	'/post/edit/', 'post.post',
	'/user/edit/', 'user.Edit',
	'/user/avatar/', 'user.Avatar',
	'/user/view/', 'user.View',
	'/user/list/', 'user.List',
	'/user/ban', 'user.Ban',
	'/project/edit/', 'project.Edit',
	'/project/delete/', 'project.Delete',
	'/project/list/', 'project.List',
	'/project/list/published/', 'project.ListPublished',
	'/project/publish/', 'project.Publish'
)
session = None
#crea la instancia de la aplicacion con la urls y las variables cargadas

from mizodb import render, plain_render
#crea el objeto sesion
from web import form
import gdata
import gdata.photos.service
import gdata.media
import gdata.geo
try:
	import cStringIO as StringIo
except:
	import StringIO

gd_client = gdata.photos.service.PhotosService()
def GoogleLogin():
	callback = 'http://nande.kicks-ass.org:8080'
	scope = 'https://picasaweb.google.com/data/'
	secure = False
	session = True

	return gd_client.GenerateAuthSubURL(callback, scope, secure, session)

#clase principal
class main:
	def GET(self):
		input = web.input(token=None, auth_sub_scope=None)
		token = input.token
		auth_sub_scope = input.auth_sub_scope
		#si el usuario esta logueado, muestra la pagina principal
		#si no lo esta, le muestra el formulario de login
		if token:
			#if token.startswith("1/"): token = token[2:]
			gd_client.auth_sub_scope = input.auth_sub_scope
			gd_client.auth_token = token
			gd_client.UpgradeToSessionToken()

			session['tkn'] = token
			albums = gd_client.GetUserFeed(user='default')
			out = StringIO.StringIO()
			for album in albums.entry:
				out.write( 'title: %s, number of photos: %s, id: %s' % (album.title.text,  album.numphotos.text, album.gphoto_id.text))
			return str("Logged in , token:", token)

		if not ('access_token' in session):
			return plain_render.login(GoogleLogin())
		else:
			return "logged?"

#Esta clase maneja el deslogueo
class logout:
	def GET(self):
		#vacia la sesion
		session.kill()
		#redirije al /
		raise web.seeother('/')

if __name__ == "__main__":
	#si se intento ejecutar este script y no importarlo,
	app = web.application(urls, globals())
	session = web.session.Session(app, web.session.DiskStore('sessions'),
		initializer={'user': 'anonymous'})
	web.config._session = session
	#ejecuta la instancia de la aplicacion
	app.run()
