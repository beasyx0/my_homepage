import time


class StatsMiddleware:
    '''Middleware to inject pagload time in ms into context'''
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = time.time()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        duration = round(time.time() - self.start_time, 2)
        response.context_data["pageload"] = duration
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
