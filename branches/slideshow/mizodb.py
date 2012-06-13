# -*- coding: utf-8 -*-
from ZEO.ClientStorage import ClientStorage
from ZODB import  DB
from BTrees.OOBTree import OOBTree
from persistent.list import PersistentList
import transaction as trans
import web
from operator import attrgetter

class MiZODB(object):
	def __init__(self, server="localhost", port=8090):
		#Recibe como parametro, el servidor al cual se conectara
		#por defecto se conectara a localhost en el puerto 8090
		#es importante asignar el blob_dir para poder contar con soporte de blobs
		#de manera correcta
		self.storage =  ClientStorage((server,port), blob_dir="./blobcache")
		self.db = DB(self.storage)
		self.cnx = self.db.open()
		self.raiz = self.cnx.root()
		#inicializamos la base de datos, esto es bueno en caso de realizar cambios
		#en la estructura
		self.init()

	def init(self):
		#variable que lleva la cuenta de si hubo alguna modificacion
		cambiado = False
		#Crea el contenedor de usuarios
		#Usaremos un oobtree para poder acceder al usuario mediante una clave
		if 'users' not in self.raiz:
			self.raiz['users'] = OOBTree()
			cambiado =True

		#Crea la lista de threads, utiliza un persistentList por simplicidad
		if 'threads' not in self.raiz:
			self.raiz['threads'] = PersistentList()
			cambiado =True
		#Crea la lista de proyectos
		if 'projects' not in self.raiz:
			#Usa un OOBtree para acceder mediante claves
			self.raiz['projects'] = OOBTree()
			#crea una variable donde llevar la cuenta del ultimo id generado
			self.raiz['projects_id'] = 0
			cambiado =True

		#Lista de proyectos completos
		if 'complete_projects' not in self.raiz:
			self.raiz['complete_projects'] = OOBTree()
			cambiado =True

		if cambiado:
			self.commit("sys", "inicializacion")

		#Asigna los objetos a variables para un uso sencillo
		self.users = self.raiz['users']
		self.threads = self.raiz['threads']
		self.sections = self.raiz['sections']
		self.projects = self.raiz['projects']
		self.ranks = self.raiz['ranks']
		self.complete_projects = self.raiz['complete_projects']

	def commit(self, user=None, note=None):
		#Esta funcion permite realizar un commit
		#recibe como parametros el nombre de usuario y una nota
		#las que se guardan con el commit
		if user:
			trans.get().setUser(user)
		if note:
			trans.get().note(note)
		trans.commit()

	def abort(self):
		trans.abort()

	def close(self):
		self.cnx.close()
		self.db.close()
		self.storage.close()

	def usersForJob(self, job=""):
		#Devuelve una lista con todos los usuarios que ralizan el mismo trabajo
		return [''] + [u for u in zodb.users.values() if u.job == job]

#zodb singleton para la base de datos
#zodb = MiZODB()
zodb=None
def currentUser():
	#Esta funcion devuelve el usuario actual (dada la naturaleza de las aplicaciones web)
	#Puede ser llamada desde los metodos que responden una peticion ya que
	#si el usuario no esta logueado, redireccionara a la pagina principal
	#si no hay sesion activa redirecciona
	if not hasattr(web.config, '_session'):
		raise web.seeother("/")
	#si el usuario no esta logueado, redirecciona
	u = web.config._session.user
	if not u or u=='anonymous':
		raise web.seeother("/")

	#obtiene el usuario segun su nombre
	user = zodb.users[web.config._session.user]

	#verifica que el usuario no este baneado
	if user.banned:
		#si esta baneado, elimina la sesion y redirecciona
		web.config._session.kill()
		raise web.seeother('/')
	return user

def lastConnected():
	#Esta funcion devuelve la lista de los ultimos usuarios conectados
	#demuestra algunos comandos basicos de python que suelen utilizarse en sql
	#zodb.users.values() devuelve una lista de los elementos en users (sin importar las claves)
	#SORT ordena una lista y devuelve la lista ordenada,
	#reverse=True hace que la lista sea ordenada
	#keygetter= utiliza el campo "last_login" para ordenar
	#[:5] es un slice de python, significa que tomará solo los primeros 5 elementos de la lista
	susers = sorted(zodb.users.values(), reverse=True, key=attrgetter('last_login'))[:5]
	#list comprehension: devuelve los links de cada uno de los usuarios en la lista
	return [u.getViewLink() for u in susers]

#singleton para renderizar templates, utiliza un template base
#y dispone de varias variables globales para ser utilizadas dentro de los templates
render = web.template.render('templates/', base='base', globals={'utils':web.utils,
		'currentUser':currentUser, 'zodb':zodb, 'lastConnected':lastConnected})
#singleton para renderizar templates sin el template base
#ya que dicho template verifica el currentUser por lo tanto debe estar logueado o redireccionara
plain_render = web.template.render("templates/")
#simple string para casos inesperados
not_allowed =u"ò_ó!!?"



