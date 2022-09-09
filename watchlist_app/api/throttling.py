from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'reveiw-create'
    
    
class ReviewListThrottle(UserRateThrottle):
    scope = 'reveiw-list'
    

