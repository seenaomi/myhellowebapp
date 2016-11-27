from registration.backends.simple.views import RegistrationView

# my new reg view, subclassing RegisttationView from the plugin
class MyRegistrationView(RegistrationView):
	def get_success_url(self, request, user):
		# the named URL that we want to redirect to after
		# successful registration
		return ('registration_create_post')