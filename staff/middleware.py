from atserver import settings

XS_SHARING_ALLOWED_ORIGINS = settings.XS_SHARING_ALLOWED_ORIGINS
XS_SHARING_ALLOWED_HEADERS = settings.XS_SHARING_ALLOWED_HEADERS


class XsSharing(object):
    def process_response(self, request, response):
        if not response.has_header('Access-Control-Allow-Origin'):
            response['Access-Control-Allow-Origin']  = XS_SHARING_ALLOWED_ORIGINS 
            
        if not response.has_header('Access-Control-Allow-Headers'):
            response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
 
        return response