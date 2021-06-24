import time


class StatsMiddleware:
    '''Middleware to inject pagload time in ms into context'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''This thing is broken. No way this is accurate. Need to figure out. Driving me crazzy'''
        try:
            request_start = request.start  # if it exists do nothing (__call__ gets called more than once)
        except AttributeError:
            request.start = time.time() #  record the time before the response is processed

        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        duration = time.time() - request.start  # calculate duration
        response.context_data["pageload"] = int(duration * 1000)  # add to context
        return response


class GetNextMiddleware:
    '''Middleware that pulls the next link from request and injects it into context'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if request.method == 'GET':
            next_link = request.GET.get('next', '/')
            response.context_data["next_link"] = next_link
        return response
