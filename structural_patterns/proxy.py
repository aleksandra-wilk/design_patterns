from abc import ABC, abstractmethod


class Subject(ABC):
    
    @abstractmethod
    def request(self):
        pass
    

class RealSubject(Subject):
    
    def request(self):
        print("Real Subject performing operation")
        
    
class Proxy(Subject):
    
    def __init__(self, user):
        self.real_subject = RealSubject()
        self.user = user
        
    def check_access(self):
        print(f"Checking the access for '{self.user}' user")
        return self.user == 'admin'
            
    def request(self):
        if self.check_access():
            self.real_subject.request()
        else:
            print("Permission denied")
            

if __name__ == "__main__":
    
    proxy_user = Proxy('user')
    proxy_user.request()
    proxy_admin = Proxy('admin')
    proxy_admin.request()
    