from django.db import models

# Class par user se connectant au site
class FtUser(models.Model):
	user_id 			= models.IntegerField(unique=True) # unique=True: jamais 2 fois le meme utilisateur
	user_login 			= models.CharField(max_length=50)
	user_email 			= models.EmailField()
	user_first_name		= models.CharField(max_length=100)
	user_last_name		= models.CharField(max_length=100)
	user_image_url		= models.URLField(blank=True) # blank: le champ peut être vide
	user_created_at		= models.DateTimeField(auto_now_add=True)
	user_updated_at		= models.DateTimeField(auto_now=True)
	user_kind			= models.CharField(max_length=50, default='')


	# Surcharge operator<<
	def	__str__(self):
		return self.user_login

	# Revoi un dict des valeur de la class
	def to_dict(self):
		return {
			'user_id': self.user_id,
			'user_login': self.user_login,
			'user_email': self.user_email,
			'user_first_name': self.user_first_name,
			'user_last_name': self.user_last_name,
			'user_image_url': self.user_image_url,
			'user_kind': self.user_kind,
		}

# Class Whitelist
class WhitelistUser(models.Model):
	wl_login = models.CharField(max_length=50, unique=True)

	# Surcharge operator<<
	def	__str__(self):
		return self.wl_login

# Class Picsineux
class Profil(models.Model):
	profil_id = models.IntegerField(unique=True)
	profil_login = models.CharField(max_length=50)
	profil_email = models.EmailField()
	profil_first_name = models.CharField(max_length=100)
	profil_last_name = models.CharField(max_length=100)
	profil_image_url = models.URLField(blank=True)
	profil_pool_year = models.CharField(max_length=4)
	profil_pool_month = models.CharField(max_length=20)
	profil_lvl = models.FloatField(null=True)

	def __str__(self):
		return self.profil_login

	def to_dict(self):
		projects = []
		for p in self.project_set.all():
			projects.append(p.to_dict())
		return {
			'id': self.profil_id,
			'login': self.profil_login,
			'email': self.profil_email,
			'first_name': self.profil_first_name,
			'last_name': self.profil_last_name,
			'image_url': self.profil_image_url,
			'pool_year': self.profil_pool_year,
			'pool_month': self.profil_pool_month,
			'lvl': self.profil_lvl,
			'projects': projects,
		}



# Class pur les projets
class Project(models.Model):
	profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	valid = models.BooleanField(default=False)
	note = models.IntegerField(null=True)

	def to_dict(self):
		return {
			'name': self.name,
			'slug': self.slug,
			'valid': self.valid,
			'note': self.note,
		}