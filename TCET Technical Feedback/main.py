import os
import webapp2
import jinja2
from google.appengine.ext import db
from random import randint

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
#start of database

class Survey(db.Model):
    vam_id = db.StringProperty()
    name = db.StringProperty()
    clas = db.StringProperty()
    roll_no = db.IntegerProperty()
    semester = db.IntegerProperty()
    q1 = db.IntegerProperty()
    q2 = db.IntegerProperty()
    q3 = db.IntegerProperty()
    q4 = db.IntegerProperty()
    q5 = db.IntegerProperty()
    q6 = db.IntegerProperty()
    q7 = db.IntegerProperty()
    q8 = db.IntegerProperty()
    q9 = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    
class Latest(db.Model):
    vam_id = db.StringProperty()
    name = db.StringProperty()
    clas = db.StringProperty()
    roll_no = db.IntegerProperty()
    semester = db.IntegerProperty()
    q1sea = db.FloatProperty()    
    q1seb = db.FloatProperty()    
    q1tea = db.FloatProperty()    
    q1teb = db.FloatProperty()    
    q1bea = db.FloatProperty()    
    q1beb = db.FloatProperty()
    q2sea = db.FloatProperty()    
    q2seb = db.FloatProperty()    
    q2tea = db.FloatProperty()    
    q2teb = db.FloatProperty()    
    q2bea = db.FloatProperty()    
    q2beb = db.FloatProperty()     
    q3sea = db.FloatProperty()    
    q3seb = db.FloatProperty()    
    q3tea = db.FloatProperty()    
    q3teb = db.FloatProperty()    
    q3bea = db.FloatProperty()    
    q3beb = db.FloatProperty()  
    q4sea = db.FloatProperty()    
    q4seb = db.FloatProperty()    
    q4tea = db.FloatProperty()    
    q4teb = db.FloatProperty()    
    q4bea = db.FloatProperty()    
    q4beb = db.FloatProperty() 
    q5sea = db.FloatProperty()    
    q5seb = db.FloatProperty()    
    q5tea = db.FloatProperty()    
    q5teb = db.FloatProperty()    
    q5bea = db.FloatProperty()    
    q5beb = db.FloatProperty() 
    q6sea = db.FloatProperty()    
    q6seb = db.FloatProperty()    
    q6tea = db.FloatProperty()    
    q6teb = db.FloatProperty()    
    q6bea = db.FloatProperty()    
    q6beb = db.FloatProperty() 
    q7sea = db.FloatProperty()    
    q7seb = db.FloatProperty()    
    q7tea = db.FloatProperty()    
    q7teb = db.FloatProperty()    
    q7bea = db.FloatProperty()    
    q7beb = db.FloatProperty() 
    q8sea = db.FloatProperty()    
    q8seb = db.FloatProperty()    
    q8tea = db.FloatProperty()    
    q8teb = db.FloatProperty()    
    q8bea = db.FloatProperty()    
    q8beb = db.FloatProperty() 
    q9sea = db.FloatProperty()    
    q9seb = db.FloatProperty()    
    q9tea = db.FloatProperty()    
    q9teb = db.FloatProperty()    
    q9bea = db.FloatProperty()    
    q9beb = db.FloatProperty()
    sea = db.FloatProperty()    
    seb = db.FloatProperty()    
    tea = db.FloatProperty()    
    teb = db.FloatProperty()   
    bea = db.FloatProperty()    
    beb = db.FloatProperty()
    psea = db.FloatProperty()    
    pseb = db.FloatProperty()    
    ptea = db.FloatProperty()    
    pteb = db.FloatProperty()   
    pbea = db.FloatProperty()    
    pbeb = db.FloatProperty()    
    datey = db.DateTimeProperty(auto_now_add = True)    
#end of database        

class MainPage(Handler):
    def get(self):
        self.render("indexab.html")
    def post(self):
        vam_id = str(randint(1, 5000)) 
        name = self.request.get("name")
        clas = self.request.get("clas")
        roll_no = int(self.request.get("roll_no"))
        semester = int(self.request.get("semester"))
        q1 = int(self.request.get("1"))
        q2 = int(self.request.get("2"))
        q3 = int(self.request.get("3"))
        q4 = int(self.request.get("4"))
        q5 = int(self.request.get("5"))
        q6 = int(self.request.get("6"))
        q7 = int(self.request.get("7"))
        q8 = int(self.request.get("8"))
        q9 = int(self.request.get("9"))
        
        total_sea = Survey.all().filter("clas = ", "SE-A").count()
        total_seb = Survey.all().filter("clas = ", "SE-B").count()
        total_tea = Survey.all().filter("clas = ", "TE-A").count()
        total_teb = Survey.all().filter("clas = ", "TE-B").count()
        total_bea = Survey.all().filter("clas = ", "BE-A").count()
        total_beb = Survey.all().filter("clas = ", "BE-B").count()
        
        q1sea2 = Survey.all().filter("clas = ","SE-A").filter("q1 = ", 12).count()
        q1sea4 = Survey.all().filter("clas = ","SE-A").filter("q1 = ", 14).count()
        q1sea6 = Survey.all().filter("clas = ","SE-A").filter("q1 = ", 16).count()
        q1sea8 = Survey.all().filter("clas = ","SE-A").filter("q1 = ", 18).count()
        q1sea0 = Survey.all().filter("clas = ","SE-A").filter("q1 = ", 10).count()
        if(total_sea != 0):
            q1sea = round(float((q1sea2*2 + q1sea4*4 + q1sea6*6 + q1sea8*8 + q1sea0*10))/float(total_sea), 2)
        else:
            q1sea = 0.0
            
        q1seb2 = Survey.all().filter("clas = ","SE-B").filter("q1 = ", 12).count()
        q1seb4 = Survey.all().filter("clas = ","SE-B").filter("q1 = ", 14).count()
        q1seb6 = Survey.all().filter("clas = ","SE-B").filter("q1 = ", 16).count()
        q1seb8 = Survey.all().filter("clas = ","SE-B").filter("q1 = ", 18).count()
        q1seb0 = Survey.all().filter("clas = ","SE-B").filter("q1 = ", 10).count()
        if(total_seb != 0):
            q1seb = round(float((q1seb2*2 + q1seb4*4 + q1seb6*6 + q1seb8*8 + q1seb0*10))/float(total_seb), 2)
        else:
            q1seb = 0.0
        
        q1tea2 = Survey.all().filter("clas = ","TE-A").filter("q1 = ", 12).count()
        q1tea4 = Survey.all().filter("clas = ","TE-A").filter("q1 = ", 14).count()
        q1tea6 = Survey.all().filter("clas = ","TE-A").filter("q1 = ", 16).count()
        q1tea8 = Survey.all().filter("clas = ","TE-A").filter("q1 = ", 18).count()
        q1tea0 = Survey.all().filter("clas = ","TE-A").filter("q1 = ", 10).count()
        if(total_tea != 0):
            q1tea = round(float((q1tea2*2 + q1tea4*4 + q1tea6*6 + q1tea8*8 + q1tea0*10))/float(total_tea), 2)
        else:
            q1tea = 0.0
        q1teb2 = Survey.all().filter("clas = ","TE-B").filter("q1 = ", 12).count()
        q1teb4 = Survey.all().filter("clas = ","TE-B").filter("q1 = ", 14).count()
        q1teb6 = Survey.all().filter("clas = ","TE-B").filter("q1 = ", 16).count()
        q1teb8 = Survey.all().filter("clas = ","TE-B").filter("q1 = ", 18).count()
        q1teb0 = Survey.all().filter("clas = ","TE-B").filter("q1 = ", 10).count()
        if(total_teb != 0):
            q1teb = round(float((q1teb2*2 + q1teb4*4 + q1teb6*6 + q1teb8*8 + q1teb0*10))/float(total_teb), 2)
        else:
            q1teb = 0.0
        q1bea2 = Survey.all().filter("clas = ","BE-A").filter("q1 = ", 12).count()
        q1bea4 = Survey.all().filter("clas = ","BE-A").filter("q1 = ", 14).count()
        q1bea6 = Survey.all().filter("clas = ","BE-A").filter("q1 = ", 16).count()
        q1bea8 = Survey.all().filter("clas = ","BE-A").filter("q1 = ", 18).count()
        q1bea0 = Survey.all().filter("clas = ","BE-A").filter("q1 = ", 10).count()
        if(total_bea != 0):
            q1bea = round(float((q1bea2*2 + q1bea4*4 + q1bea6*6 + q1bea8*8 + q1bea0*10))/float(total_bea), 2)
        else:
            q1bea = 0.0
        q1beb2 = Survey.all().filter("clas = ","BE-B").filter("q1 = ", 12).count()
        q1beb4 = Survey.all().filter("clas = ","BE-B").filter("q1 = ", 14).count()
        q1beb6 = Survey.all().filter("clas = ","BE-B").filter("q1 = ", 16).count()
        q1beb8 = Survey.all().filter("clas = ","BE-B").filter("q1 = ", 18).count()
        q1beb0 = Survey.all().filter("clas = ","BE-B").filter("q1 = ", 10).count()
        if(total_beb != 0):
            q1beb = round(float((q1beb2*2 + q1beb4*4 + q1beb6*6 + q1beb8*8 + q1beb0*10))/float(total_beb), 2)
        else:
            q1beb = 0.0
        #QUESTION 2
        
        q2sea2 = Survey.all().filter("clas = ","SE-A").filter("q2 = ", 22).count()
        q2sea4 = Survey.all().filter("clas = ","SE-A").filter("q2 = ", 24).count()
        q2sea6 = Survey.all().filter("clas = ","SE-A").filter("q2 = ", 26).count()
        q2sea8 = Survey.all().filter("clas = ","SE-A").filter("q2 = ", 28).count()
        q2sea0 = Survey.all().filter("clas = ","SE-A").filter("q2 = ", 20).count()
        if(total_sea != 0):
            q2sea = round(float((q2sea2*2 + q2sea4*4 + q2sea6*6 + q2sea8*8 + q2sea0*10))/float(total_sea), 2)
        else:
            q2sea = 0.0
        
        q2seb2 = Survey.all().filter("clas = ","SE-B").filter("q2 = ", 22).count()
        q2seb4 = Survey.all().filter("clas = ","SE-B").filter("q2 = ", 24).count()
        q2seb6 = Survey.all().filter("clas = ","SE-B").filter("q2 = ", 26).count()
        q2seb8 = Survey.all().filter("clas = ","SE-B").filter("q2 = ", 28).count()
        q2seb0 = Survey.all().filter("clas = ","SE-B").filter("q2 = ", 20).count()
        if(total_seb != 0):
            q2seb = round(float((q2seb2*2 + q2seb4*4 + q2seb6*6 + q2seb8*8 + q2seb0*10))/float(total_seb), 2)
        else:
            q2seb = 0.0
        
        q2tea2 = Survey.all().filter("clas = ","TE-A").filter("q2 = ", 22).count()
        q2tea4 = Survey.all().filter("clas = ","TE-A").filter("q2 = ", 24).count()
        q2tea6 = Survey.all().filter("clas = ","TE-A").filter("q2 = ", 26).count()
        q2tea8 = Survey.all().filter("clas = ","TE-A").filter("q2 = ", 28).count()
        q2tea0 = Survey.all().filter("clas = ","TE-A").filter("q2 = ", 20).count()
        if(total_tea != 0):
            q2tea = round(float((q2tea2*2 + q2tea4*4 + q2tea6*6 + q2tea8*8 + q2tea0*10))/float(total_tea), 2)
        else:
            q2tea = 0.0
        
        q2teb2 = Survey.all().filter("clas = ","TE-B").filter("q2 = ", 22).count()
        q2teb4 = Survey.all().filter("clas = ","TE-B").filter("q2 = ", 24).count()
        q2teb6 = Survey.all().filter("clas = ","TE-B").filter("q2 = ", 26).count()
        q2teb8 = Survey.all().filter("clas = ","TE-B").filter("q2 = ", 28).count()
        q2teb0 = Survey.all().filter("clas = ","TE-B").filter("q2 = ", 20).count()
        if(total_teb != 0):
            q2teb = round(float((q2teb2*2 + q2teb4*4 + q2teb6*6 + q2teb8*8 + q2teb0*10))/float(total_teb), 2)
        else:
            q2teb = 0.0
        
        q2bea2 = Survey.all().filter("clas = ","BE-A").filter("q2 = ", 22).count()
        q2bea4 = Survey.all().filter("clas = ","BE-A").filter("q2 = ", 24).count()
        q2bea6 = Survey.all().filter("clas = ","BE-A").filter("q2 = ", 26).count()
        q2bea8 = Survey.all().filter("clas = ","BE-A").filter("q2 = ", 28).count()
        q2bea0 = Survey.all().filter("clas = ","BE-A").filter("q2 = ", 20).count()
        if(total_bea != 0):
            q2bea = round(float((q2bea2*2 + q2bea4*4 + q2bea6*6 + q2bea8*8 + q2bea0*10))/float(total_bea), 2)
        else:
            q2bea = 0.0
        
        q2beb2 = Survey.all().filter("clas = ","BE-B").filter("q2 = ", 22).count()
        q2beb4 = Survey.all().filter("clas = ","BE-B").filter("q2 = ", 24).count()
        q2beb6 = Survey.all().filter("clas = ","BE-B").filter("q2 = ", 26).count()
        q2beb8 = Survey.all().filter("clas = ","BE-B").filter("q2 = ", 28).count()
        q2beb0 = Survey.all().filter("clas = ","BE-B").filter("q2 = ", 20).count()
        if(total_beb != 0):
            q2beb = round(float((q2beb2*2 + q2beb4*4 + q2beb6*6 + q2beb8*8 + q2beb0*10))/float(total_beb), 2)
        else:
            q2beb = 0.0
        
        #QUESTION 3
        
        q3sea2 = Survey.all().filter("clas = ","SE-A").filter("q3 = ", 32).count()
        q3sea4 = Survey.all().filter("clas = ","SE-A").filter("q3 = ", 34).count()
        q3sea6 = Survey.all().filter("clas = ","SE-A").filter("q3 = ", 36).count()
        q3sea8 = Survey.all().filter("clas = ","SE-A").filter("q3 = ", 38).count()
        q3sea0 = Survey.all().filter("clas = ","SE-A").filter("q3 = ", 30).count()
        if(total_sea != 0):
            q3sea = round(float((q3sea2*2 + q3sea4*4 + q3sea6*6 + q3sea8*8 + q3sea0*10))/float(total_sea), 2)
        else:
            q3sea = 0.0
        
        q3seb2 = Survey.all().filter("clas = ","SE-B").filter("q3 = ", 32).count()
        q3seb4 = Survey.all().filter("clas = ","SE-B").filter("q3 = ", 34).count()
        q3seb6 = Survey.all().filter("clas = ","SE-B").filter("q3 = ", 36).count()
        q3seb8 = Survey.all().filter("clas = ","SE-B").filter("q3 = ", 38).count()
        q3seb0 = Survey.all().filter("clas = ","SE-B").filter("q3 = ", 30).count()
        if(total_seb != 0):
            q3seb = round(float((q3seb2*2 + q3seb4*4 + q3seb6*6 + q3seb8*8 + q3seb0*10))/float(total_seb), 2)
        else:
            q3seb = 0.0
        
        q3tea2 = Survey.all().filter("clas = ","TE-A").filter("q3 = ", 32).count()
        q3tea4 = Survey.all().filter("clas = ","TE-A").filter("q3 = ", 34).count()
        q3tea6 = Survey.all().filter("clas = ","TE-A").filter("q3 = ", 36).count()
        q3tea8 = Survey.all().filter("clas = ","TE-A").filter("q3 = ", 38).count()
        q3tea0 = Survey.all().filter("clas = ","TE-A").filter("q3 = ", 30).count()
        if(total_tea != 0):
            q3tea = round(float((q3tea2*2 + q3tea4*4 + q3tea6*6 + q3tea8*8 + q3tea0*10))/float(total_tea), 2)
        else:
            q3tea = 0.0
        
        q3teb2 = Survey.all().filter("clas = ","TE-B").filter("q3 = ", 32).count()
        q3teb4 = Survey.all().filter("clas = ","TE-B").filter("q3 = ", 34).count()
        q3teb6 = Survey.all().filter("clas = ","TE-B").filter("q3 = ", 36).count()
        q3teb8 = Survey.all().filter("clas = ","TE-B").filter("q3 = ", 38).count()
        q3teb0 = Survey.all().filter("clas = ","TE-B").filter("q3 = ", 30).count()
        if(total_teb != 0):
            q3teb = round(float((q3teb2*2 + q3teb4*4 + q3teb6*6 + q3teb8*8 + q3teb0*10))/float(total_teb), 2)
        else:
            q3teb = 0.0
        
        q3bea2 = Survey.all().filter("clas = ","BE-A").filter("q3 = ", 32).count()
        q3bea4 = Survey.all().filter("clas = ","BE-A").filter("q3 = ", 34).count()
        q3bea6 = Survey.all().filter("clas = ","BE-A").filter("q3 = ", 36).count()
        q3bea8 = Survey.all().filter("clas = ","BE-A").filter("q3 = ", 38).count()
        q3bea0 = Survey.all().filter("clas = ","BE-A").filter("q3 = ", 30).count()
        if(total_bea != 0):
            q3bea = round(float((q3bea2*2 + q3bea4*4 + q3bea6*6 + q3bea8*8 + q3bea0*10))/float(total_bea), 2)
        else:
            q3bea = 0.0
        
        q3beb2 = Survey.all().filter("clas = ","BE-B").filter("q3 = ", 32).count()
        q3beb4 = Survey.all().filter("clas = ","BE-B").filter("q3 = ", 34).count()
        q3beb6 = Survey.all().filter("clas = ","BE-B").filter("q3 = ", 36).count()
        q3beb8 = Survey.all().filter("clas = ","BE-B").filter("q3 = ", 38).count()
        q3beb0 = Survey.all().filter("clas = ","BE-B").filter("q3 = ", 30).count()
        if(total_beb != 0):
            q3beb = round(float((q3beb2*2 + q3beb4*4 + q3beb6*6 + q3beb8*8 + q3beb0*10))/float(total_beb), 2)
        else:
            q3beb = 0.0
        
        #QUESTION 4
        
        q4sea2 = Survey.all().filter("clas = ","SE-A").filter("q4 = ", 42).count()
        q4sea4 = Survey.all().filter("clas = ","SE-A").filter("q4 = ", 44).count()
        q4sea6 = Survey.all().filter("clas = ","SE-A").filter("q4 = ", 46).count()
        q4sea8 = Survey.all().filter("clas = ","SE-A").filter("q4 = ", 48).count()
        q4sea0 = Survey.all().filter("clas = ","SE-A").filter("q4 = ", 40).count()
        if(total_sea != 0):
            q4sea = round(float((q4sea2*2 + q4sea4*4 + q4sea6*6 + q4sea8*8 + q4sea0*10))/float(total_sea), 2)
        else:
            q4sea = 0.0
        
        q4seb2 = Survey.all().filter("clas = ","SE-B").filter("q4 = ", 42).count()
        q4seb4 = Survey.all().filter("clas = ","SE-B").filter("q4 = ", 44).count()
        q4seb6 = Survey.all().filter("clas = ","SE-B").filter("q4 = ", 46).count()
        q4seb8 = Survey.all().filter("clas = ","SE-B").filter("q4 = ", 48).count()
        q4seb0 = Survey.all().filter("clas = ","SE-B").filter("q4 = ", 40).count()
        if(total_seb != 0):
            q4seb = round(float((q4seb2*2 + q4seb4*4 + q4seb6*6 + q4seb8*8 + q4seb0*10))/float(total_seb), 2)
        else:
            q4seb = 0.0
        
        q4tea2 = Survey.all().filter("clas = ","TE-A").filter("q4 = ", 42).count()
        q4tea4 = Survey.all().filter("clas = ","TE-A").filter("q4 = ", 44).count()
        q4tea6 = Survey.all().filter("clas = ","TE-A").filter("q4 = ", 46).count()
        q4tea8 = Survey.all().filter("clas = ","TE-A").filter("q4 = ", 48).count()
        q4tea0 = Survey.all().filter("clas = ","TE-A").filter("q4 = ", 40).count()
        if(total_tea != 0):
            q4tea = round(float((q4tea2*2 + q4tea4*4 + q4tea6*6 + q4tea8*8 + q4tea0*10))/float(total_tea), 2)
        else:
            q4tea = 0.0
        
        q4teb2 = Survey.all().filter("clas = ","TE-B").filter("q4 = ", 42).count()
        q4teb4 = Survey.all().filter("clas = ","TE-B").filter("q4 = ", 44).count()
        q4teb6 = Survey.all().filter("clas = ","TE-B").filter("q4 = ", 46).count()
        q4teb8 = Survey.all().filter("clas = ","TE-B").filter("q4 = ", 48).count()
        q4teb0 = Survey.all().filter("clas = ","TE-B").filter("q4 = ", 40).count()
        if(total_teb != 0):
            q4teb = round(float((q4teb2*2 + q4teb4*4 + q4teb6*6 + q4teb8*8 + q4teb0*10))/float(total_teb), 2)
        else:
            q4teb = 0.0
        
        q4bea2 = Survey.all().filter("clas = ","BE-A").filter("q4 = ", 42).count()
        q4bea4 = Survey.all().filter("clas = ","BE-A").filter("q4 = ", 44).count()
        q4bea6 = Survey.all().filter("clas = ","BE-A").filter("q4 = ", 46).count()
        q4bea8 = Survey.all().filter("clas = ","BE-A").filter("q4 = ", 48).count()
        q4bea0 = Survey.all().filter("clas = ","BE-A").filter("q4 = ", 40).count()
        if(total_bea != 0):
            q4bea = round(float((q4bea2*2 + q4bea4*4 + q4bea6*6 + q4bea8*8 + q4bea0*10))/float(total_bea), 2)
        else:
            q4bea = 0.0
        
        q4beb2 = Survey.all().filter("clas = ","BE-B").filter("q4 = ", 42).count()
        q4beb4 = Survey.all().filter("clas = ","BE-B").filter("q4 = ", 44).count()
        q4beb6 = Survey.all().filter("clas = ","BE-B").filter("q4 = ", 46).count()
        q4beb8 = Survey.all().filter("clas = ","BE-B").filter("q4 = ", 48).count()
        q4beb0 = Survey.all().filter("clas = ","BE-B").filter("q4 = ", 40).count()
        if(total_beb != 0):
            q4beb = round(float((q4beb2*2 + q4beb4*4 + q4beb6*6 + q4beb8*8 + q4beb0*10))/float(total_beb), 2)
        else:
            q4beb = 0.0
        
        #QUESTION 5
        
        q5sea2 = Survey.all().filter("clas = ","SE-A").filter("q5 = ", 52).count()
        q5sea4 = Survey.all().filter("clas = ","SE-A").filter("q5 = ", 54).count()
        q5sea6 = Survey.all().filter("clas = ","SE-A").filter("q5 = ", 56).count()
        q5sea8 = Survey.all().filter("clas = ","SE-A").filter("q5 = ", 58).count()
        q5sea0 = Survey.all().filter("clas = ","SE-A").filter("q5 = ", 50).count()
        if(total_sea != 0):
            q5sea = round(float((q5sea2*2 + q5sea4*4 + q5sea6*6 + q5sea8*8 + q5sea0*10))/float(total_sea), 2)
        else:
            q5sea = 0.0
        
        q5seb2 = Survey.all().filter("clas = ","SE-B").filter("q5 = ", 52).count()
        q5seb4 = Survey.all().filter("clas = ","SE-B").filter("q5 = ", 54).count()
        q5seb6 = Survey.all().filter("clas = ","SE-B").filter("q5 = ", 56).count()
        q5seb8 = Survey.all().filter("clas = ","SE-B").filter("q5 = ", 58).count()
        q5seb0 = Survey.all().filter("clas = ","SE-B").filter("q5 = ", 50).count()
        if(total_seb != 0):
            q5seb = round(float((q5seb2*2 + q5seb4*4 + q5seb6*6 + q5seb8*8 + q5seb0*10))/float(total_seb), 2)
        else:
            q5seb = 0.0
        
        q5tea2 = Survey.all().filter("clas = ","TE-A").filter("q5 = ", 52).count()
        q5tea4 = Survey.all().filter("clas = ","TE-A").filter("q5 = ", 54).count()
        q5tea6 = Survey.all().filter("clas = ","TE-A").filter("q5 = ", 56).count()
        q5tea8 = Survey.all().filter("clas = ","TE-A").filter("q5 = ", 58).count()
        q5tea0 = Survey.all().filter("clas = ","TE-A").filter("q5 = ", 50).count()
        if(total_tea != 0):
            q5tea = round(float((q5tea2*2 + q5tea4*4 + q5tea6*6 + q5tea8*8 + q5tea0*10))/float(total_tea), 2)
        else:
            q5tea = 0.0
        
        q5teb2 = Survey.all().filter("clas = ","TE-B").filter("q5 = ", 52).count()
        q5teb4 = Survey.all().filter("clas = ","TE-B").filter("q5 = ", 54).count()
        q5teb6 = Survey.all().filter("clas = ","TE-B").filter("q5 = ", 56).count()
        q5teb8 = Survey.all().filter("clas = ","TE-B").filter("q5 = ", 58).count()
        q5teb0 = Survey.all().filter("clas = ","TE-B").filter("q5 = ", 50).count()
        if(total_teb != 0):
            q5teb = round(float((q5teb2*2 + q5teb4*4 + q5teb6*6 + q5teb8*8 + q5teb0*10))/float(total_teb), 2)
        else:
            q5teb = 0.0
        
        q5bea2 = Survey.all().filter("clas = ","BE-A").filter("q5 = ", 52).count()
        q5bea4 = Survey.all().filter("clas = ","BE-A").filter("q5 = ", 54).count()
        q5bea6 = Survey.all().filter("clas = ","BE-A").filter("q5 = ", 56).count()
        q5bea8 = Survey.all().filter("clas = ","BE-A").filter("q5 = ", 58).count()
        q5bea0 = Survey.all().filter("clas = ","BE-A").filter("q5 = ", 50).count()
        if(total_bea != 0):
            q5bea = round(float((q5bea2*2 + q5bea4*4 + q5bea6*6 + q5bea8*8 + q5bea0*10))/float(total_bea), 2)
        else:
            q5bea = 0.0
        
        q5beb2 = Survey.all().filter("clas = ","BE-B").filter("q5 = ", 52).count()
        q5beb4 = Survey.all().filter("clas = ","BE-B").filter("q5 = ", 54).count()
        q5beb6 = Survey.all().filter("clas = ","BE-B").filter("q5 = ", 56).count()
        q5beb8 = Survey.all().filter("clas = ","BE-B").filter("q5 = ", 58).count()
        q5beb0 = Survey.all().filter("clas = ","BE-B").filter("q5 = ", 50).count()
        if(total_beb != 0):
            q5beb = round(float((q5beb2*2 + q5beb4*4 + q5beb6*6 + q5beb8*8 + q5beb0*10))/float(total_beb), 2)
        else:
            q5beb = 0.0
        
        #QUESTION 6
        
        q6sea2 = Survey.all().filter("clas = ","SE-A").filter("q6 = ", 62).count()
        q6sea4 = Survey.all().filter("clas = ","SE-A").filter("q6 = ", 64).count()
        q6sea6 = Survey.all().filter("clas = ","SE-A").filter("q6 = ", 66).count()
        q6sea8 = Survey.all().filter("clas = ","SE-A").filter("q6 = ", 68).count()
        q6sea0 = Survey.all().filter("clas = ","SE-A").filter("q6 = ", 60).count()
        if(total_sea != 0):
            q6sea = round(float((q6sea2*2 + q6sea4*4 + q6sea6*6 + q6sea8*8 + q6sea0*10))/float(total_sea), 2)
        else:
            q6sea = 0.0
        
        q6seb2 = Survey.all().filter("clas = ","SE-B").filter("q6 = ", 62).count()
        q6seb4 = Survey.all().filter("clas = ","SE-B").filter("q6 = ", 64).count()
        q6seb6 = Survey.all().filter("clas = ","SE-B").filter("q6 = ", 66).count()
        q6seb8 = Survey.all().filter("clas = ","SE-B").filter("q6 = ", 68).count()
        q6seb0 = Survey.all().filter("clas = ","SE-B").filter("q6 = ", 60).count()
        if(total_seb != 0):
            q6seb = round(float((q6seb2*2 + q6seb4*4 + q6seb6*6 + q6seb8*8 + q6seb0*10))/float(total_seb), 2)
        else:
            q6seb = 0.0
        
        q6tea2 = Survey.all().filter("clas = ","TE-A").filter("q6 = ", 62).count()
        q6tea4 = Survey.all().filter("clas = ","TE-A").filter("q6 = ", 64).count()
        q6tea6 = Survey.all().filter("clas = ","TE-A").filter("q6 = ", 66).count()
        q6tea8 = Survey.all().filter("clas = ","TE-A").filter("q6 = ", 68).count()
        q6tea0 = Survey.all().filter("clas = ","TE-A").filter("q6 = ", 60).count()
        if(total_tea != 0):
            q6tea = round(float((q6tea2*2 + q6tea4*4 + q6tea6*6 + q6tea8*8 + q6tea0*10))/float(total_tea), 2)
        else:
            q6tea = 0.0
        
        q6teb2 = Survey.all().filter("clas = ","TE-B").filter("q6 = ", 62).count()
        q6teb4 = Survey.all().filter("clas = ","TE-B").filter("q6 = ", 64).count()
        q6teb6 = Survey.all().filter("clas = ","TE-B").filter("q6 = ", 66).count()
        q6teb8 = Survey.all().filter("clas = ","TE-B").filter("q6 = ", 68).count()
        q6teb0 = Survey.all().filter("clas = ","TE-B").filter("q6 = ", 60).count()
        if(total_teb != 0):
            q6teb = round(float((q6teb2*2 + q6teb4*4 + q6teb6*6 + q6teb8*8 + q6teb0*10))/float(total_teb), 2)
        else:
            q6teb = 0.0
        
        q6bea2 = Survey.all().filter("clas = ","BE-A").filter("q6 = ", 62).count()
        q6bea4 = Survey.all().filter("clas = ","BE-A").filter("q6 = ", 64).count()
        q6bea6 = Survey.all().filter("clas = ","BE-A").filter("q6 = ", 66).count()
        q6bea8 = Survey.all().filter("clas = ","BE-A").filter("q6 = ", 68).count()
        q6bea0 = Survey.all().filter("clas = ","BE-A").filter("q6 = ", 60).count()
        if(total_bea != 0):
            q6bea = round(float((q6bea2*2 + q6bea4*4 + q6bea6*6 + q6bea8*8 + q6bea0*10))/float(total_bea), 2)
        else:
            q6bea = 0.0
        
        q6beb2 = Survey.all().filter("clas = ","BE-B").filter("q6 = ", 62).count()
        q6beb4 = Survey.all().filter("clas = ","BE-B").filter("q6 = ", 64).count()
        q6beb6 = Survey.all().filter("clas = ","BE-B").filter("q6 = ", 66).count()
        q6beb8 = Survey.all().filter("clas = ","BE-B").filter("q6 = ", 68).count()
        q6beb0 = Survey.all().filter("clas = ","BE-B").filter("q6 = ", 60).count()
        if(total_beb != 0):
            q6beb = round(float((q6beb2*2 + q6beb4*4 + q6beb6*6 + q6beb8*8 + q6beb0*10))/float(total_beb), 2)
        else:
            q6beb = 0.0
        
        #QUESTION 7
        
        q7sea2 = Survey.all().filter("clas = ","SE-A").filter("q7 = ", 72).count()
        q7sea4 = Survey.all().filter("clas = ","SE-A").filter("q7 = ", 74).count()
        q7sea6 = Survey.all().filter("clas = ","SE-A").filter("q7 = ", 76).count()
        q7sea8 = Survey.all().filter("clas = ","SE-A").filter("q7 = ", 78).count()
        q7sea0 = Survey.all().filter("clas = ","SE-A").filter("q7 = ", 70).count()
        if(total_sea != 0):
            q7sea = round(float((q7sea2*2 + q7sea4*4 + q7sea6*6 + q7sea8*8 + q7sea0*10))/float(total_sea), 2)
        else:
            q7sea = 0.0
        
        q7seb2 = Survey.all().filter("clas = ","SE-B").filter("q7 = ", 72).count()
        q7seb4 = Survey.all().filter("clas = ","SE-B").filter("q7 = ", 74).count()
        q7seb6 = Survey.all().filter("clas = ","SE-B").filter("q7 = ", 76).count()
        q7seb8 = Survey.all().filter("clas = ","SE-B").filter("q7 = ", 78).count()
        q7seb0 = Survey.all().filter("clas = ","SE-B").filter("q7 = ", 70).count()
        if(total_seb != 0):
            q7seb = round(float((q7seb2*2 + q7seb4*4 + q7seb6*6 + q7seb8*8 + q7seb0*10))/float(total_seb), 2)
        else:
            q7seb = 0.0
        
        q7tea2 = Survey.all().filter("clas = ","TE-A").filter("q7 = ", 72).count()
        q7tea4 = Survey.all().filter("clas = ","TE-A").filter("q7 = ", 74).count()
        q7tea6 = Survey.all().filter("clas = ","TE-A").filter("q7 = ", 76).count()
        q7tea8 = Survey.all().filter("clas = ","TE-A").filter("q7 = ", 78).count()
        q7tea0 = Survey.all().filter("clas = ","TE-A").filter("q7 = ", 70).count()
        if(total_tea != 0):
            q7tea = round(float((q7tea2*2 + q7tea4*4 + q7tea6*6 + q7tea8*8 + q7tea0*10))/float(total_tea), 2)
        else:
            q7tea = 0.0
        
        q7teb2 = Survey.all().filter("clas = ","TE-B").filter("q7 = ", 72).count()
        q7teb4 = Survey.all().filter("clas = ","TE-B").filter("q7 = ", 74).count()
        q7teb6 = Survey.all().filter("clas = ","TE-B").filter("q7 = ", 76).count()
        q7teb8 = Survey.all().filter("clas = ","TE-B").filter("q7 = ", 78).count()
        q7teb0 = Survey.all().filter("clas = ","TE-B").filter("q7 = ", 70).count()
        if(total_teb != 0):
            q7teb = round(float((q7teb2*2 + q7teb4*4 + q7teb6*6 + q7teb8*8 + q7teb0*10))/float(total_teb), 2)
        else:
            q7teb = 0.0
        
        q7bea2 = Survey.all().filter("clas = ","BE-A").filter("q7 = ", 72).count()
        q7bea4 = Survey.all().filter("clas = ","BE-A").filter("q7 = ", 74).count()
        q7bea6 = Survey.all().filter("clas = ","BE-A").filter("q7 = ", 76).count()
        q7bea8 = Survey.all().filter("clas = ","BE-A").filter("q7 = ", 78).count()
        q7bea0 = Survey.all().filter("clas = ","BE-A").filter("q7 = ", 70).count()
        if(total_bea != 0):
            q7bea = round(float((q7bea2*2 + q7bea4*4 + q7bea6*6 + q7bea8*8 + q7bea0*10))/float(total_bea), 2)
        else:
            q7bea = 0.0
        
        q7beb2 = Survey.all().filter("clas = ","BE-B").filter("q7 = ", 72).count()
        q7beb4 = Survey.all().filter("clas = ","BE-B").filter("q7 = ", 74).count()
        q7beb6 = Survey.all().filter("clas = ","BE-B").filter("q7 = ", 76).count()
        q7beb8 = Survey.all().filter("clas = ","BE-B").filter("q7 = ", 78).count()
        q7beb0 = Survey.all().filter("clas = ","BE-B").filter("q7 = ", 70).count()
        if(total_beb != 0):
            q7beb = round(float((q7beb2*2 + q7beb4*4 + q7beb6*6 + q7beb8*8 + q7beb0*10))/float(total_beb), 2)
        else:
            q7beb = 0.0
        
        #QUESTION 8
        
        q8sea2 = Survey.all().filter("clas = ","SE-A").filter("q8 = ", 82).count()
        q8sea4 = Survey.all().filter("clas = ","SE-A").filter("q8 = ", 84).count()
        q8sea6 = Survey.all().filter("clas = ","SE-A").filter("q8 = ", 86).count()
        q8sea8 = Survey.all().filter("clas = ","SE-A").filter("q8 = ", 88).count()
        q8sea0 = Survey.all().filter("clas = ","SE-A").filter("q8 = ", 80).count()
        if(total_sea != 0):
            q8sea = round(float((q8sea2*2 + q8sea4*4 + q8sea6*6 + q8sea8*8 + q8sea0*10))/float(total_sea), 2)
        else:
            q8sea = 0.0
        
        q8seb2 = Survey.all().filter("clas = ","SE-B").filter("q8 = ", 82).count()
        q8seb4 = Survey.all().filter("clas = ","SE-B").filter("q8 = ", 84).count()
        q8seb6 = Survey.all().filter("clas = ","SE-B").filter("q8 = ", 86).count()
        q8seb8 = Survey.all().filter("clas = ","SE-B").filter("q8 = ", 88).count()
        q8seb0 = Survey.all().filter("clas = ","SE-B").filter("q8 = ", 80).count()
        if(total_seb != 0):
            q8seb = round(float((q8seb2*2 + q8seb4*4 + q8seb6*6 + q8seb8*8 + q8seb0*10))/float(total_seb), 2)
        else:
            q8seb = 0.0
        
        q8tea2 = Survey.all().filter("clas = ","TE-A").filter("q8 = ", 82).count()
        q8tea4 = Survey.all().filter("clas = ","TE-A").filter("q8 = ", 84).count()
        q8tea6 = Survey.all().filter("clas = ","TE-A").filter("q8 = ", 86).count()
        q8tea8 = Survey.all().filter("clas = ","TE-A").filter("q8 = ", 88).count()
        q8tea0 = Survey.all().filter("clas = ","TE-A").filter("q8 = ", 80).count()
        if(total_tea != 0):
            q8tea = round(float((q8tea2*2 + q8tea4*4 + q8tea6*6 + q8tea8*8 + q8tea0*10))/float(total_tea), 2)
        else:
            q8tea = 0.0
        
        q8teb2 = Survey.all().filter("clas = ","TE-B").filter("q8 = ", 82).count()
        q8teb4 = Survey.all().filter("clas = ","TE-B").filter("q8 = ", 84).count()
        q8teb6 = Survey.all().filter("clas = ","TE-B").filter("q8 = ", 86).count()
        q8teb8 = Survey.all().filter("clas = ","TE-B").filter("q8 = ", 88).count()
        q8teb0 = Survey.all().filter("clas = ","TE-B").filter("q8 = ", 80).count()
        if(total_teb != 0):
            q8teb = round(float((q8teb2*2 + q8teb4*4 + q8teb6*6 + q8teb8*8 + q8teb0*10))/float(total_teb), 2)
        else:
            q8teb = 0.0
        
        q8bea2 = Survey.all().filter("clas = ","BE-A").filter("q8 = ", 82).count()
        q8bea4 = Survey.all().filter("clas = ","BE-A").filter("q8 = ", 84).count()
        q8bea6 = Survey.all().filter("clas = ","BE-A").filter("q8 = ", 86).count()
        q8bea8 = Survey.all().filter("clas = ","BE-A").filter("q8 = ", 88).count()
        q8bea0 = Survey.all().filter("clas = ","BE-A").filter("q8 = ", 80).count()
        if(total_bea != 0):
            q8bea = round(float((q8bea2*2 + q8bea4*4 + q8bea6*6 + q8bea8*8 + q8bea0*10))/float(total_bea), 2)
        else:
            q8bea = 0.0
        
        q8beb2 = Survey.all().filter("clas = ","BE-B").filter("q8 = ", 82).count()
        q8beb4 = Survey.all().filter("clas = ","BE-B").filter("q8 = ", 84).count()
        q8beb6 = Survey.all().filter("clas = ","BE-B").filter("q8 = ", 86).count()
        q8beb8 = Survey.all().filter("clas = ","BE-B").filter("q8 = ", 88).count()
        q8beb0 = Survey.all().filter("clas = ","BE-B").filter("q8 = ", 80).count()
        if(total_beb != 0):
            q8beb = round(float((q8beb2*2 + q8beb4*4 + q8beb6*6 + q8beb8*8 + q8beb0*10))/float(total_beb), 2)
        else:
            q8beb = 0.0
        
        #QUESTION 9
        
        q9sea2 = Survey.all().filter("clas = ","SE-A").filter("q9 = ", 92).count()
        q9sea4 = Survey.all().filter("clas = ","SE-A").filter("q9 = ", 94).count()
        q9sea6 = Survey.all().filter("clas = ","SE-A").filter("q9 = ", 96).count()
        q9sea8 = Survey.all().filter("clas = ","SE-A").filter("q9 = ", 98).count()
        q9sea0 = Survey.all().filter("clas = ","SE-A").filter("q9 = ", 90).count()
        if(total_sea != 0):
            q9sea = round(float((q9sea2*2 + q9sea4*4 + q9sea6*6 + q9sea8*8 + q9sea0*10))/float(total_sea), 2)
        else:
            q9sea = 0.0
        
        q9seb2 = Survey.all().filter("clas = ","SE-B").filter("q9 = ", 92).count()
        q9seb4 = Survey.all().filter("clas = ","SE-B").filter("q9 = ", 94).count()
        q9seb6 = Survey.all().filter("clas = ","SE-B").filter("q9 = ", 96).count()
        q9seb8 = Survey.all().filter("clas = ","SE-B").filter("q9 = ", 98).count()
        q9seb0 = Survey.all().filter("clas = ","SE-B").filter("q9 = ", 90).count()
        if(total_seb != 0):
            q9seb = round(float((q9seb2*2 + q9seb4*4 + q9seb6*6 + q9seb8*8 + q9seb0*10))/float(total_seb), 2)
        else:
            q9seb = 0.0
        
        q9tea2 = Survey.all().filter("clas = ","TE-A").filter("q9 = ", 92).count()
        q9tea4 = Survey.all().filter("clas = ","TE-A").filter("q9 = ", 94).count()
        q9tea6 = Survey.all().filter("clas = ","TE-A").filter("q9 = ", 96).count()
        q9tea8 = Survey.all().filter("clas = ","TE-A").filter("q9 = ", 98).count()
        q9tea0 = Survey.all().filter("clas = ","TE-A").filter("q9 = ", 90).count()
        if(total_tea != 0):
            q9tea = round(float((q9tea2*2 + q9tea4*4 + q9tea6*6 + q9tea8*8 + q9tea0*10))/float(total_tea), 2)
        else:
            q9tea = 0.0
        
        q9teb2 = Survey.all().filter("clas = ","TE-B").filter("q9 = ", 92).count()
        q9teb4 = Survey.all().filter("clas = ","TE-B").filter("q9 = ", 94).count()
        q9teb6 = Survey.all().filter("clas = ","TE-B").filter("q9 = ", 96).count()
        q9teb8 = Survey.all().filter("clas = ","TE-B").filter("q9 = ", 98).count()
        q9teb0 = Survey.all().filter("clas = ","TE-B").filter("q9 = ", 90).count()
        if(total_teb != 0):
            q9teb = round(float((q9teb2*2 + q9teb4*4 + q9teb6*6 + q9teb8*8 + q9teb0*10))/float(total_teb), 2)
        else:
            q9teb = 0.0
        
        q9bea2 = Survey.all().filter("clas = ","BE-A").filter("q9 = ", 92).count()
        q9bea4 = Survey.all().filter("clas = ","BE-A").filter("q9 = ", 94).count()
        q9bea6 = Survey.all().filter("clas = ","BE-A").filter("q9 = ", 96).count()
        q9bea8 = Survey.all().filter("clas = ","BE-A").filter("q9 = ", 98).count()
        q9bea0 = Survey.all().filter("clas = ","BE-A").filter("q9 = ", 90).count()
        if(total_bea != 0):
            q9bea = round(float((q9bea2*2 + q9bea4*4 + q9bea6*6 + q9bea8*8 + q9bea0*10))/float(total_bea), 2)
        else:
            q9bea = 0.0
        
        q9beb2 = Survey.all().filter("clas = ","BE-B").filter("q9 = ", 92).count()
        q9beb4 = Survey.all().filter("clas = ","BE-B").filter("q9 = ", 94).count()
        q9beb6 = Survey.all().filter("clas = ","BE-B").filter("q9 = ", 96).count()
        q9beb8 = Survey.all().filter("clas = ","BE-B").filter("q9 = ", 98).count()
        q9beb0 = Survey.all().filter("clas = ","BE-B").filter("q9 = ", 90).count()
        if(total_beb != 0):
            q9beb = round(float((q9beb2*2 + q9beb4*4 + q9beb6*6 + q9beb8*8 + q9beb0*10))/float(total_beb), 2)
        else:
            q9beb = 0.0
            
        sea = round((q1sea+q2sea+q3sea+q4sea+q5sea+q6sea+q7sea+q8sea+q9sea),2)    
        seb = round((q1seb+q2seb+q3seb+q4seb+q5seb+q6seb+q7seb+q8seb+q9seb),2)    
        tea = round((q1tea+q2tea+q3tea+q4tea+q5tea+q6tea+q7tea+q8tea+q9tea),2)    
        teb = round((q1teb+q2teb+q3teb+q4teb+q5teb+q6teb+q7teb+q8teb+q9teb),2)    
        bea = round((q1bea+q2bea+q3bea+q4bea+q5bea+q6bea+q7bea+q8bea+q9bea),2)    
        beb = round((q1beb+q2beb+q3beb+q4beb+q5beb+q6beb+q7beb+q8beb+q9beb),2)    
        
        psea = round((sea/9.0)*10,2)
        pseb = round((seb/9.0)*10,2)
        ptea = round((tea/9.0)*10,2)
        pteb = round((teb/9.0)*10,2)
        pbea = round((bea/9.0)*10,2)
        pbeb = round((beb/9.0)*10,2)
        
        a = Survey(vam_id = vam_id, name = name, clas = clas,
                roll_no = roll_no, semester = semester,
                q1 = q1, q2 = q2, q3 = q3, q4 = q4, q5 = q5, q6 = q6,
                q7 = q7, q8 = q8, q9 = q9)
        a.put()
        
        b = Latest(vam_id = vam_id, name = name, clas = clas,
                roll_no = roll_no, semester = semester,
                q1sea = q1sea, q1seb = q1seb, q1tea = q1tea, q1teb = q1teb,
                q1bea = q1bea, q1beb = q1beb,
                q2sea = q2sea, q2seb = q2seb, q2tea = q2tea, q2teb = q2teb,
                q2bea = q2bea, q2beb = q2beb,
                q3sea = q3sea, q3seb = q3seb, q3tea = q3tea, q3teb = q3teb,
                q3bea = q3bea, q3beb = q3beb,
                q4sea = q4sea, q4seb = q4seb, q4tea = q4tea, q4teb = q4teb,
                q4bea = q4bea, q4beb = q4beb,
                q5sea = q5sea, q5seb = q5seb, q5tea = q5tea, q5teb = q5teb,
                q5bea = q5bea, q5beb = q5beb,
                q6sea = q6sea, q6seb = q6seb, q6tea = q6tea, q6teb = q6teb,
                q6bea = q6bea, q6beb = q6beb,
                q7sea = q7sea, q7seb = q7seb, q7tea = q7tea, q7teb = q7teb,
                q7bea = q7bea, q7beb = q7beb,
                q8sea = q8sea, q8seb = q8seb, q8tea = q8tea, q8teb = q8teb,
                q8bea = q8bea, q8beb = q8beb,
                q9sea = q9sea, q9seb = q9seb, q9tea = q9tea, q9teb = q9teb,
                q9bea = q9bea, q9beb = q9beb,
                sea = sea, seb = seb, tea = tea, teb = teb, bea = bea, beb = beb,
                psea = psea, pseb = pseb, ptea = ptea, pteb = pteb, pbea = pbea, pbeb = pbeb)
                
        b.put()
        
        self.render("thanx.html")       
                
class ThankYou(Handler):
    def get(self):
        self.render("thanx.html")
		
class AdminPage(MainPage):
    def get(self):
        p = Latest.all().order('-datey').get()
        self.render("admin1.html", p = p)
        
               
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/admin', AdminPage),
                               ('/thanks', ThankYou),], debug=True)