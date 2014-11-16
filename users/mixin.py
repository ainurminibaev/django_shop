from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect


class AuthorizedMixin(object):
    user_check_failure_path = reverse_lazy('index')

    def check_user(self, request):
        return request.user.is_authenticated()

    def user_auth_handler(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('index'))

    def dispatch(self, request, *args, **kwargs):
        if self.check_user(request):
            return self.user_auth_handler(request, *args, **kwargs)
        return super(AuthorizedMixin, self).dispatch(request, *args, **kwargs)
