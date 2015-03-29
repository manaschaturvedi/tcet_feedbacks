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
    q11 = db.IntegerProperty()
    q12 = db.IntegerProperty()
    q13 = db.IntegerProperty()
    q14 = db.IntegerProperty()
    q15 = db.IntegerProperty()
    q21 = db.IntegerProperty()
    q22 = db.IntegerProperty()
    q23 = db.IntegerProperty()
    q24 = db.IntegerProperty()
    q25 = db.IntegerProperty()
    q31 = db.IntegerProperty()
    q32 = db.IntegerProperty()
    q33 = db.IntegerProperty()
    q34 = db.IntegerProperty()
    q35 = db.IntegerProperty()
    q41 = db.IntegerProperty()
    q42 = db.IntegerProperty()
    q43 = db.IntegerProperty()
    q44 = db.IntegerProperty()
    q45 = db.IntegerProperty()
    q51 = db.IntegerProperty()
    q52 = db.IntegerProperty()
    q53 = db.IntegerProperty()
    q54 = db.IntegerProperty()
    q55 = db.IntegerProperty()
    q61 = db.IntegerProperty()
    q62 = db.IntegerProperty()
    q63 = db.IntegerProperty()
    q64 = db.IntegerProperty()
    q65 = db.IntegerProperty()
    q71 = db.IntegerProperty()
    q72 = db.IntegerProperty()
    q73 = db.IntegerProperty()
    q74 = db.IntegerProperty()
    q75 = db.IntegerProperty()
    q77 = db.IntegerProperty()
    q81 = db.IntegerProperty()
    q82 = db.IntegerProperty()
    q83 = db.IntegerProperty()
    q87 = db.IntegerProperty()
    q91 = db.IntegerProperty()
    q92 = db.IntegerProperty()
    q93 = db.IntegerProperty()
    q96 = db.IntegerProperty()
    q97 = db.IntegerProperty()
    total_q1 = db.IntegerProperty()
    total_q2 = db.IntegerProperty()
    total_q3 = db.IntegerProperty()
    total_q4 = db.IntegerProperty()
    total_q5 = db.IntegerProperty()
    total_q6 = db.IntegerProperty()
    total_q7 = db.IntegerProperty()
    total_q8 = db.IntegerProperty()
    total_q9 = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    
"""a = Survey(vam_id = "01", name = "Manas", clas = "SE-A", roll_no = 12, semester = 7,
    q11 = 5, q12 = 5, q13 = 7, q14 = 8, q15 = 9, q16 = 4, q17 = 10,
    q21 = 5, q22 = 5, q23 = 7, q24 = 8, q25 = 9, q26 = 4, q27 = 10,
    q31 = 5, q32 = 5, q33 = 7, q34 = 8, q35 = 9, q36 = 4, q37 = 10,
    q41 = 5, q42 = 5, q43 = 7, q44 = 8, q45 = 9, q46 = 4, q47 = 10,
    q51 = 5, q52 = 5, q53 = 7, q54 = 8, q55 = 9, q56 = 4, q57 = 10,
    q61 = 5, q62 = 5, q63 = 7, q64 = 8, q65 = 9, q66 = 4, q67 = 10,
    q71 = 5, q72 = 5, q73 = 7, q74 = 8, q75 = 9, q76 = 4, q77 = 10,
    q81 = 5, q82 = 5, q83 = 7, q84 = 8, q85 = 9, q86 = 4, q87 = 10,
    q91 = 5, q92 = 5, q93 = 7, q94 = 8, q95 = 9, q96 = 4, q97 = 10,
    total_q1 = 12, total_q2 = 34, total_q3 = 57, 
    total_q4 = 102, total_q5 = 44, total_q6 = 27,
    total_q7 = 45, total_q8 = 98, total_q9 = 63)
a.put()    """
        
#end of database        

class MainPage(Handler):
    def get(self):
        self.render("indexab.html")
    def post(self):
        vam_id = str(randint(1, 5000)) 
        name = self.request.get("name")
        clas = self.request.get("clas")
        roll_no = self.request.get("roll_no")
        semester = self.request.get("semester")
        q11 = self.request.get("q11")
        q12 = self.request.get("q12")
        q13 = self.request.get("q13")
        q14 = self.request.get("q14")
        q15 = self.request.get("q15")
        q21 = self.request.get("q21")
        q22 = self.request.get("q22")
        q23 = self.request.get("q23")
        q24 = self.request.get("q24")
        q25 = self.request.get("q25")
        q31 = self.request.get("q31")
        q32 = self.request.get("q32")
        q33 = self.request.get("q33")
        q34 = self.request.get("q34")
        q35 = self.request.get("q35")
        q41 = self.request.get("q41")
        q42 = self.request.get("q42")
        q43 = self.request.get("q43")
        q44 = self.request.get("q44")
        q45 = self.request.get("q45")
        q51 = self.request.get("q51")
        q52 = self.request.get("q52")
        q53 = self.request.get("q53")
        q54 = self.request.get("q54")
        q55 = self.request.get("q55")
        q61 = self.request.get("q61")
        q62 = self.request.get("q62")
        q63 = self.request.get("q63")
        q64 = self.request.get("q64")
        q65 = self.request.get("q65")
        q71 = self.request.get("q71")
        q72 = self.request.get("q72")
        q73 = self.request.get("q73")
        q74 = self.request.get("q74")
        q75 = self.request.get("q75")
        q77 = self.request.get("q77")
        q81 = self.request.get("q81")
        q82 = self.request.get("q82")
        q83 = self.request.get("q83")
        q87 = self.request.get("q87")
        q91 = self.request.get("q91")
        q92 = self.request.get("q92")
        q93 = self.request.get("q93")
        q96 = self.request.get("q96")
        q97 = self.request.get("q97")
        if(name and clas and roll_no and semester
           and q11 and q12 and q13 and q14 and q15
           and q21 and q22 and q23 and q24 and q25
           and q31 and q32 and q33 and q34 and q35
           and q41 and q42 and q43 and q44 and q45
           and q51 and q52 and q53 and q54 and q55
           and q61 and q62 and q63 and q64 and q65
           and q71 and q72 and q73 and q74 and q75 and q77
           and q81 and q82 and q83 and q87
           and q51 and q52 and q53 and q54 and q55
           and q91 and q92 and q93 and q96 and q97):
            roll_no = int(roll_no)
            semester = int(semester)
            q11 = int(q11)
            q12 = int(q12)
            q13 = int(q13)
            q14 = int(q14)
            q15 = int(q15)
            q21 = int(q21)
            q22 = int(q22)
            q23 = int(q23)
            q24 = int(q24)
            q25 = int(q25)
            q31 = int(q31)
            q32 = int(q32)
            q33 = int(q33)
            q34 = int(q34)
            q35 = int(q35)
            q41 = int(q41)
            q42 = int(q42)
            q43 = int(q43)
            q44 = int(q44)
            q45 = int(q45)
            q51 = int(q51)
            q52 = int(q52)
            q53 = int(q53)
            q54 = int(q54)
            q55 = int(q55)
            q61 = int(q61)
            q62 = int(q62)
            q63 = int(q63)
            q64 = int(q64)
            q65 = int(q65)
            q71 = int(q71)
            q72 = int(q72)
            q73 = int(q73)
            q74 = int(q74)
            q75 = int(q75)
            q77 = int(q77)
            q81 = int(q81)
            q82 = int(q82)
            q83 = int(q83)
            q87 = int(q87)
            q91 = int(q91)
            q92 = int(q92)
            q93 = int(q93)
            q96 = int(q96)
            q97 = int(q97)
            total_q1 = q11 + q12 + q13 + q14 + q15
            total_q2 = q21 + q22 + q23 + q24 + q25
            total_q3 = q31 + q32 + q33 + q34 + q35
            total_q4 = q41 + q42 + q43 + q44 + q45
            total_q5 = q51 + q52 + q53 + q54 + q55
            total_q6 = q61 + q62 + q63 + q64 + q65
            total_q7 = q71 + q72 + q73 + q74 + q75 + q77
            total_q8 = q81 + q82 + q83 + q87
            total_q9 = q91 + q92 + q93 + q96 + q97
            s = Survey(vam_id = vam_id, name = name, roll_no = roll_no, clas = clas,
            semester = semester,
            q11 = q11, q12 = q12, q13 = q13, q14 = q14, q15 = q15,
            q21 = q21, q22 = q22, q23 = q23, q24 = q24, q25 = q25,
            q31 = q31, q32 = q32, q33 = q33, q34 = q34, q35 = q35,
            q41 = q41, q42 = q42, q43 = q43, q44 = q44, q45 = q45,
            q51 = q51, q52 = q52, q53 = q53, q54 = q54, q55 = q55,
            q61 = q61, q62 = q62, q63 = q63, q64 = q64, q65 = q65,
            q71 = q71, q72 = q72, q73 = q73, q74 = q74, q75 = q75, q77 = q77,
            q81 = q81, q82 = q82, q83 = q83, q87 = q87,
            q91 = q91, q92 = q92, q93 = q93, q96 = q96, q97 = q97,
            total_q1 = total_q1, total_q2 = total_q2, total_q3 = total_q3,
            total_q4 = total_q4, total_q5 = total_q5, total_q6 = total_q6,
            total_q7 = total_q7, total_q8 = total_q8, total_q9 = total_q9)
            s.put()
            self.redirect("/thanks")
        else:
            params = dict(name = name, roll_no = roll_no, clas = clas,
            semester = semester,
            q11 = q11, q12 = q12, q13 = q13, q14 = q14, q15 = q15,
            q21 = q21, q22 = q22, q23 = q23, q24 = q24, q25 = q25,
            q31 = q31, q32 = q32, q33 = q33, q34 = q34, q35 = q35,
            q41 = q41, q42 = q42, q43 = q43, q44 = q44, q45 = q45,
            q51 = q51, q52 = q52, q53 = q53, q54 = q54, q55 = q55,
            q61 = q61, q62 = q62, q63 = q63, q64 = q64, q65 = q65,
            q71 = q71, q72 = q72, q73 = q73, q74 = q74, q75 = q75, q77 = q77,
            q81 = q81, q82 = q82, q83 = q83, q87 = q87,
            q91 = q91, q92 = q92, q93 = q93, q96 = q96, q97 = q97)
            params['error_form'] = '"PLEASE FILL ALL THE ENTRIES BEFORE SUBMITTING"'
            self.render('indexab.html',**params)
        
class ThankYou(Handler):
    def get(self):
        self.render("thanx.html")

class AdminPage(Handler):
    def get(self):
        self.render("admin.html")
        
class SecondYear(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_clarit = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_clarity = q1_clarit
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_utility = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_guidance = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_process = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        gadq151=Survey.all().filter("semester = ",sem).filter("q15 = ", 4).count()
        gadq152=Survey.all().filter("semester = ",sem).filter("q15 = ", 5).count()
        gadq153=Survey.all().filter("semester = ",sem).filter("q15 = ", 6).count()
        gadq154=Survey.all().filter("semester = ",sem).filter("q15 = ", 7).count()
        gadq155=Survey.all().filter("semester = ",sem).filter("q15 = ", 8).count()
        gadq156=Survey.all().filter("semester = ",sem).filter("q15 = ", 9).count()
        gadq157=Survey.all().filter("semester = ",sem).filter("q15 = ", 10).count()
        
        q1_resource = 4*gadq151 + 5*gadq152 + 6*gadq153 + 7*gadq154 + 8*gadq155 + 9*gadq156 + 10*gadq157

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_clarit = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_clarity = q2_clarit
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_utility = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_guidance = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_process = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_resource = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_clarit = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_clarity = q3_clarit
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_utility = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_guidance = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_process = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_resource = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_clarit = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_clarity = q4_clarit
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_utility = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_guidance = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_process = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_resource = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_clarit = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_clarity = q5_clarit
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_utility = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_guidance = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_process = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_resource = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157      

        oorav111=Survey.all().filter("semester = ",sem).filter("q61 = ", 4).count()
        oorav112=Survey.all().filter("semester = ",sem).filter("q61 = ", 5).count()
        oorav113=Survey.all().filter("semester = ",sem).filter("q61 = ", 6).count()
        oorav114=Survey.all().filter("semester = ",sem).filter("q61 = ", 7).count()
        oorav115=Survey.all().filter("semester = ",sem).filter("q61 = ", 8).count()
        oorav116=Survey.all().filter("semester = ",sem).filter("q61 = ", 9).count()
        oorav117=Survey.all().filter("semester = ",sem).filter("q61 = ", 10).count()
        
        q6_clarit = 4*oorav111 + 5*oorav112 + 6*oorav113 + 7*oorav114 + 8*oorav115 + 9*oorav116 + 10*oorav117
        q6_clarity = q6_clarit
        
        oorav121=Survey.all().filter("semester = ",sem).filter("q62 = ", 4).count()
        oorav122=Survey.all().filter("semester = ",sem).filter("q62 = ", 5).count()
        oorav123=Survey.all().filter("semester = ",sem).filter("q62 = ", 6).count()
        oorav124=Survey.all().filter("semester = ",sem).filter("q62 = ", 7).count()
        oorav125=Survey.all().filter("semester = ",sem).filter("q62 = ", 8).count()
        oorav126=Survey.all().filter("semester = ",sem).filter("q62 = ", 9).count()
        oorav127=Survey.all().filter("semester = ",sem).filter("q62 = ", 10).count()
        
        q6_utility = 4*oorav121 + 5*oorav122 + 6*oorav123 + 7*oorav124 + 8*oorav125 + 9*oorav126 + 10*oorav127
        
        oorav131=Survey.all().filter("semester = ",sem).filter("q63 = ", 4).count()
        oorav132=Survey.all().filter("semester = ",sem).filter("q63 = ", 5).count()
        oorav133=Survey.all().filter("semester = ",sem).filter("q63 = ", 6).count()
        oorav134=Survey.all().filter("semester = ",sem).filter("q63 = ", 7).count()
        oorav135=Survey.all().filter("semester = ",sem).filter("q63 = ", 8).count()
        oorav136=Survey.all().filter("semester = ",sem).filter("q63 = ", 9).count()
        oorav137=Survey.all().filter("semester = ",sem).filter("q63 = ", 10).count()
        
        q6_guidance = 4*oorav131 + 5*oorav132 + 6*oorav133 + 7*oorav134 + 8*oorav135 + 9*oorav136 + 10*oorav137 
        
        oorav141=Survey.all().filter("semester = ",sem).filter("q64 = ", 4).count()
        oorav142=Survey.all().filter("semester = ",sem).filter("q64 = ", 5).count()
        oorav143=Survey.all().filter("semester = ",sem).filter("q64 = ", 6).count()
        oorav144=Survey.all().filter("semester = ",sem).filter("q64 = ", 7).count()
        oorav145=Survey.all().filter("semester = ",sem).filter("q64 = ", 8).count()
        oorav146=Survey.all().filter("semester = ",sem).filter("q64 = ", 9).count()
        oorav147=Survey.all().filter("semester = ",sem).filter("q64 = ", 10).count()
        
        q6_process = 4*oorav141 + 5*oorav142 + 6*oorav143 + 7*oorav144 + 8*oorav145 + 9*oorav146 + 10*oorav147 
        
        oorav151=Survey.all().filter("semester = ",sem).filter("q65 = ", 4).count()
        oorav152=Survey.all().filter("semester = ",sem).filter("q65 = ", 5).count()
        oorav153=Survey.all().filter("semester = ",sem).filter("q65 = ", 6).count()
        oorav154=Survey.all().filter("semester = ",sem).filter("q65 = ", 7).count()
        oorav155=Survey.all().filter("semester = ",sem).filter("q65 = ", 8).count()
        oorav156=Survey.all().filter("semester = ",sem).filter("q65 = ", 9).count()
        oorav157=Survey.all().filter("semester = ",sem).filter("q65 = ", 10).count()
        
        q6_resource = 4*oorav151 + 5*oorav152 + 6*oorav153 + 7*oorav154 + 8*oorav155 + 9*oorav156 + 10*oorav157      

        oorad111=Survey.all().filter("semester = ",sem).filter("q71 = ", 4).count()
        oorad112=Survey.all().filter("semester = ",sem).filter("q71 = ", 5).count()
        oorad113=Survey.all().filter("semester = ",sem).filter("q71 = ", 6).count()
        oorad114=Survey.all().filter("semester = ",sem).filter("q71 = ", 7).count()
        oorad115=Survey.all().filter("semester = ",sem).filter("q71 = ", 8).count()
        oorad116=Survey.all().filter("semester = ",sem).filter("q71 = ", 9).count()
        oorad117=Survey.all().filter("semester = ",sem).filter("q71 = ", 10).count()
        
        q7_clarit = 4*oorad111 + 5*oorad112 + 6*oorad113 + 7*oorad114 + 8*oorad115 + 9*oorad116 + 10*oorad117
        q7_clarity = q7_clarit
        
        oorad121=Survey.all().filter("semester = ",sem).filter("q72 = ", 4).count()
        oorad122=Survey.all().filter("semester = ",sem).filter("q72 = ", 5).count()
        oorad123=Survey.all().filter("semester = ",sem).filter("q72 = ", 6).count()
        oorad124=Survey.all().filter("semester = ",sem).filter("q72 = ", 7).count()
        oorad125=Survey.all().filter("semester = ",sem).filter("q72 = ", 8).count()
        oorad126=Survey.all().filter("semester = ",sem).filter("q72 = ", 9).count()
        oorad127=Survey.all().filter("semester = ",sem).filter("q72 = ", 10).count()
        
        q7_utility = 4*oorad121 + 5*oorad122 + 6*oorad123 + 7*oorad124 + 8*oorad125 + 9*oorad126 + 10*oorad127
        
        oorad131=Survey.all().filter("semester = ",sem).filter("q73 = ", 4).count()
        oorad132=Survey.all().filter("semester = ",sem).filter("q73 = ", 5).count()
        oorad133=Survey.all().filter("semester = ",sem).filter("q73 = ", 6).count()
        oorad134=Survey.all().filter("semester = ",sem).filter("q73 = ", 7).count()
        oorad135=Survey.all().filter("semester = ",sem).filter("q73 = ", 8).count()
        oorad136=Survey.all().filter("semester = ",sem).filter("q73 = ", 9).count()
        oorad137=Survey.all().filter("semester = ",sem).filter("q73 = ", 10).count()
        
        q7_guidance = 4*oorad131 + 5*oorad132 + 6*oorad133 + 7*oorad134 + 8*oorad135 + 9*oorad136 + 10*oorad137 
        
        oorad141=Survey.all().filter("semester = ",sem).filter("q74 = ", 4).count()
        oorad142=Survey.all().filter("semester = ",sem).filter("q74 = ", 5).count()
        oorad143=Survey.all().filter("semester = ",sem).filter("q74 = ", 6).count()
        oorad144=Survey.all().filter("semester = ",sem).filter("q74 = ", 7).count()
        oorad145=Survey.all().filter("semester = ",sem).filter("q74 = ", 8).count()
        oorad146=Survey.all().filter("semester = ",sem).filter("q74 = ", 9).count()
        oorad147=Survey.all().filter("semester = ",sem).filter("q74 = ", 10).count()
        
        q7_process = 4*oorad141 + 5*oorad142 + 6*oorad143 + 7*oorad144 + 8*oorad145 + 9*oorad146 + 10*oorad147 
        
        oorad151=Survey.all().filter("semester = ",sem).filter("q75 = ", 4).count()
        oorad152=Survey.all().filter("semester = ",sem).filter("q75 = ", 5).count()
        oorad153=Survey.all().filter("semester = ",sem).filter("q75 = ", 6).count()
        oorad154=Survey.all().filter("semester = ",sem).filter("q75 = ", 7).count()
        oorad155=Survey.all().filter("semester = ",sem).filter("q75 = ", 8).count()
        oorad156=Survey.all().filter("semester = ",sem).filter("q75 = ", 9).count()
        oorad157=Survey.all().filter("semester = ",sem).filter("q75 = ", 10).count()
        
        q7_resource = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157
        
        oorad171=Survey.all().filter("semester = ",sem).filter("q77 = ", 4).count()
        oorad172=Survey.all().filter("semester = ",sem).filter("q77 = ", 5).count()
        oorad173=Survey.all().filter("semester = ",sem).filter("q77 = ", 6).count()
        oorad174=Survey.all().filter("semester = ",sem).filter("q77 = ", 7).count()
        oorad175=Survey.all().filter("semester = ",sem).filter("q77 = ", 8).count()
        oorad176=Survey.all().filter("semester = ",sem).filter("q77 = ", 9).count()
        oorad177=Survey.all().filter("semester = ",sem).filter("q77 = ", 10).count()
        
        q7_domain = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157

        cico111=Survey.all().filter("semester = ",sem).filter("q81 = ", 4).count()
        cico112=Survey.all().filter("semester = ",sem).filter("q81 = ", 5).count()
        cico113=Survey.all().filter("semester = ",sem).filter("q81 = ", 6).count()
        cico114=Survey.all().filter("semester = ",sem).filter("q81 = ", 7).count()
        cico115=Survey.all().filter("semester = ",sem).filter("q81 = ", 8).count()
        cico116=Survey.all().filter("semester = ",sem).filter("q81 = ", 9).count()
        cico117=Survey.all().filter("semester = ",sem).filter("q81 = ", 10).count()
        
        q8_clarit = 4*cico111 + 5*cico112 + 6*cico113 + 7*cico114 + 8*cico115 + 9*cico116 + 10*cico117
        q8_clarity = q8_clarit
        
        cico121=Survey.all().filter("semester = ",sem).filter("q82 = ", 4).count()
        cico122=Survey.all().filter("semester = ",sem).filter("q82 = ", 5).count()
        cico123=Survey.all().filter("semester = ",sem).filter("q82 = ", 6).count()
        cico124=Survey.all().filter("semester = ",sem).filter("q82 = ", 7).count()
        cico125=Survey.all().filter("semester = ",sem).filter("q82 = ", 8).count()
        cico126=Survey.all().filter("semester = ",sem).filter("q82 = ", 9).count()
        cico127=Survey.all().filter("semester = ",sem).filter("q82 = ", 10).count()
        
        q8_utility = 4*cico121 + 5*cico122 + 6*cico123 + 7*cico124 + 8*cico125 + 9*cico126 + 10*cico127
        
        cico131=Survey.all().filter("semester = ",sem).filter("q83 = ", 4).count()
        cico132=Survey.all().filter("semester = ",sem).filter("q83 = ", 5).count()
        cico133=Survey.all().filter("semester = ",sem).filter("q83 = ", 6).count()
        cico134=Survey.all().filter("semester = ",sem).filter("q83 = ", 7).count()
        cico135=Survey.all().filter("semester = ",sem).filter("q83 = ", 8).count()
        cico136=Survey.all().filter("semester = ",sem).filter("q83 = ", 9).count()
        cico137=Survey.all().filter("semester = ",sem).filter("q83 = ", 10).count()
        
        q8_guidance = 4*cico131 + 5*cico132 + 6*cico133 + 7*cico134 + 8*cico135 + 9*cico136 + 10*cico137 
        
        cico141=Survey.all().filter("semester = ",sem).filter("q87 = ", 4).count()
        cico142=Survey.all().filter("semester = ",sem).filter("q87 = ", 5).count()
        cico143=Survey.all().filter("semester = ",sem).filter("q87 = ", 6).count()
        cico144=Survey.all().filter("semester = ",sem).filter("q87 = ", 7).count()
        cico145=Survey.all().filter("semester = ",sem).filter("q87 = ", 8).count()
        cico146=Survey.all().filter("semester = ",sem).filter("q87 = ", 9).count()
        cico147=Survey.all().filter("semester = ",sem).filter("q87 = ", 10).count()
        
        q8_domain = 4*cico141 + 5*cico142 + 6*cico143 + 7*cico144 + 8*cico145 + 9*cico146 + 10*cico147

        so111=Survey.all().filter("semester = ",sem).filter("q91 = ", 4).count()
        so112=Survey.all().filter("semester = ",sem).filter("q91 = ", 5).count()
        so113=Survey.all().filter("semester = ",sem).filter("q91 = ", 6).count()
        so114=Survey.all().filter("semester = ",sem).filter("q91 = ", 7).count()
        so115=Survey.all().filter("semester = ",sem).filter("q91 = ", 8).count()
        so116=Survey.all().filter("semester = ",sem).filter("q91 = ", 9).count()
        so117=Survey.all().filter("semester = ",sem).filter("q91 = ", 10).count()
        
        q9_clarit = 4*so111 + 5*so112 + 6*so113 + 7*so114 + 8*so115 + 9*so116 + 10*so117
        q9_clarity = q9_clarit
        
        so121=Survey.all().filter("semester = ",sem).filter("q92 = ", 4).count()
        so122=Survey.all().filter("semester = ",sem).filter("q92 = ", 5).count()
        so123=Survey.all().filter("semester = ",sem).filter("q92 = ", 6).count()
        so124=Survey.all().filter("semester = ",sem).filter("q92 = ", 7).count()
        so125=Survey.all().filter("semester = ",sem).filter("q92 = ", 8).count()
        so126=Survey.all().filter("semester = ",sem).filter("q92 = ", 9).count()
        so127=Survey.all().filter("semester = ",sem).filter("q92 = ", 10).count()
        
        q9_utility = 4*so121 + 5*so122 + 6*so123 + 7*so124 + 8*so125 + 9*so126 + 10*so127
        
        so131=Survey.all().filter("semester = ",sem).filter("q93 = ", 4).count()
        so132=Survey.all().filter("semester = ",sem).filter("q93 = ", 5).count()
        so133=Survey.all().filter("semester = ",sem).filter("q93 = ", 6).count()
        so134=Survey.all().filter("semester = ",sem).filter("q93 = ", 7).count()
        so135=Survey.all().filter("semester = ",sem).filter("q93 = ", 8).count()
        so136=Survey.all().filter("semester = ",sem).filter("q93 = ", 9).count()
        so137=Survey.all().filter("semester = ",sem).filter("q93 = ", 10).count()
        
        q9_guidance = 4*so131 + 5*so132 + 6*so133 + 7*so134 + 8*so135 + 9*so136 + 10*so137 
        
        so141=Survey.all().filter("semester = ",sem).filter("q96 = ", 4).count()
        so142=Survey.all().filter("semester = ",sem).filter("q96 = ", 5).count()
        so143=Survey.all().filter("semester = ",sem).filter("q96 = ", 6).count()
        so144=Survey.all().filter("semester = ",sem).filter("q96 = ", 7).count()
        so145=Survey.all().filter("semester = ",sem).filter("q96 = ", 8).count()
        so146=Survey.all().filter("semester = ",sem).filter("q96 = ", 9).count()
        so147=Survey.all().filter("semester = ",sem).filter("q96 = ", 10).count()
        
        q9_activity = 4*so141 + 5*so142 + 6*so143 + 7*so144 + 8*so145 + 9*so146 + 10*so147 
        
        so151=Survey.all().filter("semester = ",sem).filter("q97 = ", 4).count()
        so152=Survey.all().filter("semester = ",sem).filter("q97 = ", 5).count()
        so153=Survey.all().filter("semester = ",sem).filter("q97 = ", 6).count()
        so154=Survey.all().filter("semester = ",sem).filter("q97 = ", 7).count()
        so155=Survey.all().filter("semester = ",sem).filter("q97 = ", 8).count()
        so156=Survey.all().filter("semester = ",sem).filter("q97 = ", 9).count()
        so157=Survey.all().filter("semester = ",sem).filter("q97 = ", 10).count() 

        q9_domain = 4*so151 + 5*so152 + 6*so153 + 7*so154 + 8*so155 + 9*so156 + 10*so157 
        
        self.render("secondyear.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                       'gadq151':gadq151,'gadq152':gadq152,'gadq153':gadq153,'gadq154':gadq154,'gadq155':gadq155,'gadq156':gadq156,'gadq157':gadq157,
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'obmd111':obmd111,'obmd112':obmd112,'obmd113':obmd113,'obmd114':obmd114,'obmd115':obmd115,'obmd116':obmd116,'obmd117':obmd117,
                                       'obmd121':obmd121,'obmd122':obmd122,'obmd123':obmd123,'obmd124':obmd124,'obmd125':obmd125,'obmd126':obmd126,'obmd127':obmd127,
                                       'obmd131':obmd131,'obmd132':obmd132,'obmd133':obmd133,'obmd134':obmd134,'obmd135':obmd135,'obmd136':obmd136,'obmd137':obmd137,
                                       'obmd141':obmd141,'obmd142':obmd142,'obmd143':obmd143,'obmd144':obmd144,'obmd145':obmd145,'obmd146':obmd146,'obmd147':obmd147,
                                       'obmd151':obmd151,'obmd152':obmd152,'obmd153':obmd153,'obmd154':obmd154,'obmd155':obmd155,'obmd156':obmd156,'obmd157':obmd157,
                                       'obhod111':obhod111,'obhod112':obhod112,'obhod113':obhod113,'obhod114':obhod114,'obhod115':obhod115,'obhod116':obhod116,'obhod117':obhod117,
                                       'obhod121':obhod121,'obhod122':obhod122,'obhod123':obhod123,'obhod124':obhod124,'obhod125':obhod125,'obhod126':obhod126,'obhod127':obhod127,
                                       'obhod131':obhod131,'obhod132':obhod132,'obhod133':obhod133,'obhod134':obhod134,'obhod135':obhod135,'obhod136':obhod136,'obhod137':obhod137,
                                       'obhod141':obhod141,'obhod142':obhod142,'obhod143':obhod143,'obhod144':obhod144,'obhod145':obhod145,'obhod146':obhod146,'obhod147':obhod147,
                                       'obhod151':obhod151,'obhod152':obhod152,'obhod153':obhod153,'obhod154':obhod154,'obhod155':obhod155,'obhod156':obhod156,'obhod157':obhod157,
                                       'oorav111':oorav111,'oorav112':oorav112,'oorav113':oorav113,'oorav114':oorav114,'oorav115':oorav115,'oorav116':oorav116,'oorav117':oorav117,
                                       'oorav121':oorav121,'oorav122':oorav122,'oorav123':oorav123,'oorav124':oorav124,'oorav125':oorav125,'oorav126':oorav126,'oorav127':oorav127,
                                       'oorav131':oorav131,'oorav132':oorav132,'oorav133':oorav133,'oorav134':oorav134,'oorav135':oorav135,'oorav136':oorav136,'oorav137':oorav137,
                                       'oorav141':oorav141,'oorav142':oorav142,'oorav143':oorav143,'oorav144':oorav144,'oorav145':oorav145,'oorav146':oorav146,'oorav147':oorav147,
                                       'oorav151':oorav151,'oorav152':oorav152,'oorav153':oorav153,'oorav154':oorav154,'oorav155':oorav155,'oorav156':oorav156,'oorav157':oorav157,
                                       'oorad111':oorad111,'oorad112':oorad112,'oorad113':oorad113,'oorad114':oorad114,'oorad115':oorad115,'oorad116':oorad116,'oorad117':oorad117,
                                       'oorad121':oorad121,'oorad122':oorad122,'oorad123':oorad123,'oorad124':oorad124,'oorad125':oorad125,'oorad126':oorad126,'oorad127':oorad127,
                                       'oorad131':oorad131,'oorad132':oorad132,'oorad133':oorad133,'oorad134':oorad134,'oorad135':oorad135,'oorad136':oorad136,'oorad137':oorad137,
                                       'oorad141':oorad141,'oorad142':oorad142,'oorad143':oorad143,'oorad144':oorad144,'oorad145':oorad145,'oorad146':oorad146,'oorad147':oorad147,
                                       'oorad151':oorad151,'oorad152':oorad152,'oorad153':oorad153,'oorad154':oorad154,'oorad155':oorad155,'oorad156':oorad156,'oorad157':oorad157,
                                       'oorad171':oorad171,'oorad172':oorad172,'oorad173':oorad173,'oorad174':oorad174,'oorad175':oorad175,'oorad176':oorad176,'oorad177':oorad177,
                                       'cico111':cico111,'cico112':cico112,'cico113':cico113,'cico114':cico114,'cico115':cico115,'cico116':cico116,'cico117':cico117,
                                       'cico121':cico121,'cico122':cico122,'cico123':cico123,'cico124':cico124,'cico125':cico125,'cico126':cico126,'cico127':cico127,
                                       'cico131':cico131,'cico132':cico132,'cico133':cico133,'cico134':cico134,'cico135':cico135,'cico136':cico136,'cico137':cico137,
                                       'cico141':cico141,'cico142':cico142,'cico143':cico143,'cico144':cico144,'cico145':cico145,'cico146':cico146,'cico147':cico147,
                                       'so111':so111,'so112':so112,'so113':so113,'so114':so114,'so115':so115,'so116':so116,'so117':so117,
                                       'so121':so121,'so122':so122,'so123':so123,'so124':so124,'so125':so125,'so126':so126,'so127':so127,
                                       'so131':so131,'so132':so132,'so133':so133,'so134':so134,'so135':so135,'so136v':so136,'so137':so137,
                                       'so141':so141,'so142':so142,'so143':so143,'so144':so144,'so145':so145,'so146':so146,'so147':so147,
                                       'so151':so151,'so152':so152,'so153':so153,'so154':so154,'so155':so155,'so156':so156,'so157':so157,
                                       'q1_clarity':q1_clarity,'q1_guidance':q1_guidance,'q1_process':q1_process,
                                       'q1_utility':q1_utility,'q1_resource':q1_resource,'q2_clarity':q2_clarity,'q2_guidance':q2_guidance,'q2_process':q2_process,
                                       'q2_utility':q2_utility,'q2_resource':q2_resource,
                                       'q3_clarity':q3_clarity,'q3_guidance':q3_guidance,'q3_process':q3_process,
                                       'q3_utility':q3_utility,'q3_resource':q3_resource,
                                       'q4_clarity':q4_clarity,'q4_guidance':q4_guidance,'q4_process':q4_process,
                                       'q4_utility':q4_utility,'q4_resource':q4_resource,
                                       'q5_clarity':q5_clarity,'q5_guidance':q5_guidance,'q5_process':q5_process,
                                       'q5_utility':q5_utility,'q5_resource':q5_resource,
                                       'q6_clarity':q6_clarity,'q6_guidance':q6_guidance,'q6_process':q6_process,
                                       'q6_utility':q6_utility,'q6_resource':q6_resource,
                                       'q7_clarity':q7_clarity,'q7_guidance':q7_guidance,'q7_process':q7_process,
                                       'q7_utility':q7_utility,'q7_resource':q7_resource,'q7_domain':q7_domain,
                                       'q8_clarity':q8_clarity,'q8_utility':q8_utility,'q8_guidance':q8_guidance,
                                       'q8_domain':q8_domain,
                                       'q9_clarity':q9_clarity,'q9_utility':q9_utility,'q9_guidance':q9_guidance,
                                       'q9_domain':q9_domain,'q9_activity':q9_activity})                                     
                                       
        
class ThirdYear(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_clarit = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_clarity = q1_clarit
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_utility = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_guidance = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_process = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        gadq151=Survey.all().filter("semester = ",sem).filter("q15 = ", 4).count()
        gadq152=Survey.all().filter("semester = ",sem).filter("q15 = ", 5).count()
        gadq153=Survey.all().filter("semester = ",sem).filter("q15 = ", 6).count()
        gadq154=Survey.all().filter("semester = ",sem).filter("q15 = ", 7).count()
        gadq155=Survey.all().filter("semester = ",sem).filter("q15 = ", 8).count()
        gadq156=Survey.all().filter("semester = ",sem).filter("q15 = ", 9).count()
        gadq157=Survey.all().filter("semester = ",sem).filter("q15 = ", 10).count()
        
        q1_resource = 4*gadq151 + 5*gadq152 + 6*gadq153 + 7*gadq154 + 8*gadq155 + 9*gadq156 + 10*gadq157

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_clarit = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_clarity = q2_clarit
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_utility = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_guidance = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_process = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_resource = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_clarit = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_clarity = q3_clarit
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_utility = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_guidance = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_process = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_resource = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_clarit = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_clarity = q4_clarit
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_utility = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_guidance = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_process = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_resource = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_clarit = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_clarity = q5_clarit
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_utility = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_guidance = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_process = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_resource = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157      

        oorav111=Survey.all().filter("semester = ",sem).filter("q61 = ", 4).count()
        oorav112=Survey.all().filter("semester = ",sem).filter("q61 = ", 5).count()
        oorav113=Survey.all().filter("semester = ",sem).filter("q61 = ", 6).count()
        oorav114=Survey.all().filter("semester = ",sem).filter("q61 = ", 7).count()
        oorav115=Survey.all().filter("semester = ",sem).filter("q61 = ", 8).count()
        oorav116=Survey.all().filter("semester = ",sem).filter("q61 = ", 9).count()
        oorav117=Survey.all().filter("semester = ",sem).filter("q61 = ", 10).count()
        
        q6_clarit = 4*oorav111 + 5*oorav112 + 6*oorav113 + 7*oorav114 + 8*oorav115 + 9*oorav116 + 10*oorav117
        q6_clarity = q6_clarit
        
        oorav121=Survey.all().filter("semester = ",sem).filter("q62 = ", 4).count()
        oorav122=Survey.all().filter("semester = ",sem).filter("q62 = ", 5).count()
        oorav123=Survey.all().filter("semester = ",sem).filter("q62 = ", 6).count()
        oorav124=Survey.all().filter("semester = ",sem).filter("q62 = ", 7).count()
        oorav125=Survey.all().filter("semester = ",sem).filter("q62 = ", 8).count()
        oorav126=Survey.all().filter("semester = ",sem).filter("q62 = ", 9).count()
        oorav127=Survey.all().filter("semester = ",sem).filter("q62 = ", 10).count()
        
        q6_utility = 4*oorav121 + 5*oorav122 + 6*oorav123 + 7*oorav124 + 8*oorav125 + 9*oorav126 + 10*oorav127
        
        oorav131=Survey.all().filter("semester = ",sem).filter("q63 = ", 4).count()
        oorav132=Survey.all().filter("semester = ",sem).filter("q63 = ", 5).count()
        oorav133=Survey.all().filter("semester = ",sem).filter("q63 = ", 6).count()
        oorav134=Survey.all().filter("semester = ",sem).filter("q63 = ", 7).count()
        oorav135=Survey.all().filter("semester = ",sem).filter("q63 = ", 8).count()
        oorav136=Survey.all().filter("semester = ",sem).filter("q63 = ", 9).count()
        oorav137=Survey.all().filter("semester = ",sem).filter("q63 = ", 10).count()
        
        q6_guidance = 4*oorav131 + 5*oorav132 + 6*oorav133 + 7*oorav134 + 8*oorav135 + 9*oorav136 + 10*oorav137 
        
        oorav141=Survey.all().filter("semester = ",sem).filter("q64 = ", 4).count()
        oorav142=Survey.all().filter("semester = ",sem).filter("q64 = ", 5).count()
        oorav143=Survey.all().filter("semester = ",sem).filter("q64 = ", 6).count()
        oorav144=Survey.all().filter("semester = ",sem).filter("q64 = ", 7).count()
        oorav145=Survey.all().filter("semester = ",sem).filter("q64 = ", 8).count()
        oorav146=Survey.all().filter("semester = ",sem).filter("q64 = ", 9).count()
        oorav147=Survey.all().filter("semester = ",sem).filter("q64 = ", 10).count()
        
        q6_process = 4*oorav141 + 5*oorav142 + 6*oorav143 + 7*oorav144 + 8*oorav145 + 9*oorav146 + 10*oorav147 
        
        oorav151=Survey.all().filter("semester = ",sem).filter("q65 = ", 4).count()
        oorav152=Survey.all().filter("semester = ",sem).filter("q65 = ", 5).count()
        oorav153=Survey.all().filter("semester = ",sem).filter("q65 = ", 6).count()
        oorav154=Survey.all().filter("semester = ",sem).filter("q65 = ", 7).count()
        oorav155=Survey.all().filter("semester = ",sem).filter("q65 = ", 8).count()
        oorav156=Survey.all().filter("semester = ",sem).filter("q65 = ", 9).count()
        oorav157=Survey.all().filter("semester = ",sem).filter("q65 = ", 10).count()
        
        q6_resource = 4*oorav151 + 5*oorav152 + 6*oorav153 + 7*oorav154 + 8*oorav155 + 9*oorav156 + 10*oorav157      

        oorad111=Survey.all().filter("semester = ",sem).filter("q71 = ", 4).count()
        oorad112=Survey.all().filter("semester = ",sem).filter("q71 = ", 5).count()
        oorad113=Survey.all().filter("semester = ",sem).filter("q71 = ", 6).count()
        oorad114=Survey.all().filter("semester = ",sem).filter("q71 = ", 7).count()
        oorad115=Survey.all().filter("semester = ",sem).filter("q71 = ", 8).count()
        oorad116=Survey.all().filter("semester = ",sem).filter("q71 = ", 9).count()
        oorad117=Survey.all().filter("semester = ",sem).filter("q71 = ", 10).count()
        
        q7_clarit = 4*oorad111 + 5*oorad112 + 6*oorad113 + 7*oorad114 + 8*oorad115 + 9*oorad116 + 10*oorad117
        q7_clarity = q7_clarit
        
        oorad121=Survey.all().filter("semester = ",sem).filter("q72 = ", 4).count()
        oorad122=Survey.all().filter("semester = ",sem).filter("q72 = ", 5).count()
        oorad123=Survey.all().filter("semester = ",sem).filter("q72 = ", 6).count()
        oorad124=Survey.all().filter("semester = ",sem).filter("q72 = ", 7).count()
        oorad125=Survey.all().filter("semester = ",sem).filter("q72 = ", 8).count()
        oorad126=Survey.all().filter("semester = ",sem).filter("q72 = ", 9).count()
        oorad127=Survey.all().filter("semester = ",sem).filter("q72 = ", 10).count()
        
        q7_utility = 4*oorad121 + 5*oorad122 + 6*oorad123 + 7*oorad124 + 8*oorad125 + 9*oorad126 + 10*oorad127
        
        oorad131=Survey.all().filter("semester = ",sem).filter("q73 = ", 4).count()
        oorad132=Survey.all().filter("semester = ",sem).filter("q73 = ", 5).count()
        oorad133=Survey.all().filter("semester = ",sem).filter("q73 = ", 6).count()
        oorad134=Survey.all().filter("semester = ",sem).filter("q73 = ", 7).count()
        oorad135=Survey.all().filter("semester = ",sem).filter("q73 = ", 8).count()
        oorad136=Survey.all().filter("semester = ",sem).filter("q73 = ", 9).count()
        oorad137=Survey.all().filter("semester = ",sem).filter("q73 = ", 10).count()
        
        q7_guidance = 4*oorad131 + 5*oorad132 + 6*oorad133 + 7*oorad134 + 8*oorad135 + 9*oorad136 + 10*oorad137 
        
        oorad141=Survey.all().filter("semester = ",sem).filter("q74 = ", 4).count()
        oorad142=Survey.all().filter("semester = ",sem).filter("q74 = ", 5).count()
        oorad143=Survey.all().filter("semester = ",sem).filter("q74 = ", 6).count()
        oorad144=Survey.all().filter("semester = ",sem).filter("q74 = ", 7).count()
        oorad145=Survey.all().filter("semester = ",sem).filter("q74 = ", 8).count()
        oorad146=Survey.all().filter("semester = ",sem).filter("q74 = ", 9).count()
        oorad147=Survey.all().filter("semester = ",sem).filter("q74 = ", 10).count()
        
        q7_process = 4*oorad141 + 5*oorad142 + 6*oorad143 + 7*oorad144 + 8*oorad145 + 9*oorad146 + 10*oorad147 
        
        oorad151=Survey.all().filter("semester = ",sem).filter("q75 = ", 4).count()
        oorad152=Survey.all().filter("semester = ",sem).filter("q75 = ", 5).count()
        oorad153=Survey.all().filter("semester = ",sem).filter("q75 = ", 6).count()
        oorad154=Survey.all().filter("semester = ",sem).filter("q75 = ", 7).count()
        oorad155=Survey.all().filter("semester = ",sem).filter("q75 = ", 8).count()
        oorad156=Survey.all().filter("semester = ",sem).filter("q75 = ", 9).count()
        oorad157=Survey.all().filter("semester = ",sem).filter("q75 = ", 10).count()
        
        q7_resource = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157
        
        oorad171=Survey.all().filter("semester = ",sem).filter("q77 = ", 4).count()
        oorad172=Survey.all().filter("semester = ",sem).filter("q77 = ", 5).count()
        oorad173=Survey.all().filter("semester = ",sem).filter("q77 = ", 6).count()
        oorad174=Survey.all().filter("semester = ",sem).filter("q77 = ", 7).count()
        oorad175=Survey.all().filter("semester = ",sem).filter("q77 = ", 8).count()
        oorad176=Survey.all().filter("semester = ",sem).filter("q77 = ", 9).count()
        oorad177=Survey.all().filter("semester = ",sem).filter("q77 = ", 10).count()
        
        q7_domain = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157

        cico111=Survey.all().filter("semester = ",sem).filter("q81 = ", 4).count()
        cico112=Survey.all().filter("semester = ",sem).filter("q81 = ", 5).count()
        cico113=Survey.all().filter("semester = ",sem).filter("q81 = ", 6).count()
        cico114=Survey.all().filter("semester = ",sem).filter("q81 = ", 7).count()
        cico115=Survey.all().filter("semester = ",sem).filter("q81 = ", 8).count()
        cico116=Survey.all().filter("semester = ",sem).filter("q81 = ", 9).count()
        cico117=Survey.all().filter("semester = ",sem).filter("q81 = ", 10).count()
        
        q8_clarit = 4*cico111 + 5*cico112 + 6*cico113 + 7*cico114 + 8*cico115 + 9*cico116 + 10*cico117
        q8_clarity = q8_clarit
        
        cico121=Survey.all().filter("semester = ",sem).filter("q82 = ", 4).count()
        cico122=Survey.all().filter("semester = ",sem).filter("q82 = ", 5).count()
        cico123=Survey.all().filter("semester = ",sem).filter("q82 = ", 6).count()
        cico124=Survey.all().filter("semester = ",sem).filter("q82 = ", 7).count()
        cico125=Survey.all().filter("semester = ",sem).filter("q82 = ", 8).count()
        cico126=Survey.all().filter("semester = ",sem).filter("q82 = ", 9).count()
        cico127=Survey.all().filter("semester = ",sem).filter("q82 = ", 10).count()
        
        q8_utility = 4*cico121 + 5*cico122 + 6*cico123 + 7*cico124 + 8*cico125 + 9*cico126 + 10*cico127
        
        cico131=Survey.all().filter("semester = ",sem).filter("q83 = ", 4).count()
        cico132=Survey.all().filter("semester = ",sem).filter("q83 = ", 5).count()
        cico133=Survey.all().filter("semester = ",sem).filter("q83 = ", 6).count()
        cico134=Survey.all().filter("semester = ",sem).filter("q83 = ", 7).count()
        cico135=Survey.all().filter("semester = ",sem).filter("q83 = ", 8).count()
        cico136=Survey.all().filter("semester = ",sem).filter("q83 = ", 9).count()
        cico137=Survey.all().filter("semester = ",sem).filter("q83 = ", 10).count()
        
        q8_guidance = 4*cico131 + 5*cico132 + 6*cico133 + 7*cico134 + 8*cico135 + 9*cico136 + 10*cico137 
        
        cico141=Survey.all().filter("semester = ",sem).filter("q87 = ", 4).count()
        cico142=Survey.all().filter("semester = ",sem).filter("q87 = ", 5).count()
        cico143=Survey.all().filter("semester = ",sem).filter("q87 = ", 6).count()
        cico144=Survey.all().filter("semester = ",sem).filter("q87 = ", 7).count()
        cico145=Survey.all().filter("semester = ",sem).filter("q87 = ", 8).count()
        cico146=Survey.all().filter("semester = ",sem).filter("q87 = ", 9).count()
        cico147=Survey.all().filter("semester = ",sem).filter("q87 = ", 10).count()
        
        q8_domain = 4*cico141 + 5*cico142 + 6*cico143 + 7*cico144 + 8*cico145 + 9*cico146 + 10*cico147

        so111=Survey.all().filter("semester = ",sem).filter("q91 = ", 4).count()
        so112=Survey.all().filter("semester = ",sem).filter("q91 = ", 5).count()
        so113=Survey.all().filter("semester = ",sem).filter("q91 = ", 6).count()
        so114=Survey.all().filter("semester = ",sem).filter("q91 = ", 7).count()
        so115=Survey.all().filter("semester = ",sem).filter("q91 = ", 8).count()
        so116=Survey.all().filter("semester = ",sem).filter("q91 = ", 9).count()
        so117=Survey.all().filter("semester = ",sem).filter("q91 = ", 10).count()
        
        q9_clarit = 4*so111 + 5*so112 + 6*so113 + 7*so114 + 8*so115 + 9*so116 + 10*so117
        q9_clarity = q9_clarit
        
        so121=Survey.all().filter("semester = ",sem).filter("q92 = ", 4).count()
        so122=Survey.all().filter("semester = ",sem).filter("q92 = ", 5).count()
        so123=Survey.all().filter("semester = ",sem).filter("q92 = ", 6).count()
        so124=Survey.all().filter("semester = ",sem).filter("q92 = ", 7).count()
        so125=Survey.all().filter("semester = ",sem).filter("q92 = ", 8).count()
        so126=Survey.all().filter("semester = ",sem).filter("q92 = ", 9).count()
        so127=Survey.all().filter("semester = ",sem).filter("q92 = ", 10).count()
        
        q9_utility = 4*so121 + 5*so122 + 6*so123 + 7*so124 + 8*so125 + 9*so126 + 10*so127
        
        so131=Survey.all().filter("semester = ",sem).filter("q93 = ", 4).count()
        so132=Survey.all().filter("semester = ",sem).filter("q93 = ", 5).count()
        so133=Survey.all().filter("semester = ",sem).filter("q93 = ", 6).count()
        so134=Survey.all().filter("semester = ",sem).filter("q93 = ", 7).count()
        so135=Survey.all().filter("semester = ",sem).filter("q93 = ", 8).count()
        so136=Survey.all().filter("semester = ",sem).filter("q93 = ", 9).count()
        so137=Survey.all().filter("semester = ",sem).filter("q93 = ", 10).count()
        
        q9_guidance = 4*so131 + 5*so132 + 6*so133 + 7*so134 + 8*so135 + 9*so136 + 10*so137 
        
        so141=Survey.all().filter("semester = ",sem).filter("q96 = ", 4).count()
        so142=Survey.all().filter("semester = ",sem).filter("q96 = ", 5).count()
        so143=Survey.all().filter("semester = ",sem).filter("q96 = ", 6).count()
        so144=Survey.all().filter("semester = ",sem).filter("q96 = ", 7).count()
        so145=Survey.all().filter("semester = ",sem).filter("q96 = ", 8).count()
        so146=Survey.all().filter("semester = ",sem).filter("q96 = ", 9).count()
        so147=Survey.all().filter("semester = ",sem).filter("q96 = ", 10).count()
        
        q9_activity = 4*so141 + 5*so142 + 6*so143 + 7*so144 + 8*so145 + 9*so146 + 10*so147 
        
        so151=Survey.all().filter("semester = ",sem).filter("q97 = ", 4).count()
        so152=Survey.all().filter("semester = ",sem).filter("q97 = ", 5).count()
        so153=Survey.all().filter("semester = ",sem).filter("q97 = ", 6).count()
        so154=Survey.all().filter("semester = ",sem).filter("q97 = ", 7).count()
        so155=Survey.all().filter("semester = ",sem).filter("q97 = ", 8).count()
        so156=Survey.all().filter("semester = ",sem).filter("q97 = ", 9).count()
        so157=Survey.all().filter("semester = ",sem).filter("q97 = ", 10).count() 

        q9_domain = 4*so151 + 5*so152 + 6*so153 + 7*so154 + 8*so155 + 9*so156 + 10*so157 
        
        self.render("thirdyear.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                       'gadq151':gadq151,'gadq152':gadq152,'gadq153':gadq153,'gadq154':gadq154,'gadq155':gadq155,'gadq156':gadq156,'gadq157':gadq157,
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'obmd111':obmd111,'obmd112':obmd112,'obmd113':obmd113,'obmd114':obmd114,'obmd115':obmd115,'obmd116':obmd116,'obmd117':obmd117,
                                       'obmd121':obmd121,'obmd122':obmd122,'obmd123':obmd123,'obmd124':obmd124,'obmd125':obmd125,'obmd126':obmd126,'obmd127':obmd127,
                                       'obmd131':obmd131,'obmd132':obmd132,'obmd133':obmd133,'obmd134':obmd134,'obmd135':obmd135,'obmd136':obmd136,'obmd137':obmd137,
                                       'obmd141':obmd141,'obmd142':obmd142,'obmd143':obmd143,'obmd144':obmd144,'obmd145':obmd145,'obmd146':obmd146,'obmd147':obmd147,
                                       'obmd151':obmd151,'obmd152':obmd152,'obmd153':obmd153,'obmd154':obmd154,'obmd155':obmd155,'obmd156':obmd156,'obmd157':obmd157,
                                       'obhod111':obhod111,'obhod112':obhod112,'obhod113':obhod113,'obhod114':obhod114,'obhod115':obhod115,'obhod116':obhod116,'obhod117':obhod117,
                                       'obhod121':obhod121,'obhod122':obhod122,'obhod123':obhod123,'obhod124':obhod124,'obhod125':obhod125,'obhod126':obhod126,'obhod127':obhod127,
                                       'obhod131':obhod131,'obhod132':obhod132,'obhod133':obhod133,'obhod134':obhod134,'obhod135':obhod135,'obhod136':obhod136,'obhod137':obhod137,
                                       'obhod141':obhod141,'obhod142':obhod142,'obhod143':obhod143,'obhod144':obhod144,'obhod145':obhod145,'obhod146':obhod146,'obhod147':obhod147,
                                       'obhod151':obhod151,'obhod152':obhod152,'obhod153':obhod153,'obhod154':obhod154,'obhod155':obhod155,'obhod156':obhod156,'obhod157':obhod157,
                                       'oorav111':oorav111,'oorav112':oorav112,'oorav113':oorav113,'oorav114':oorav114,'oorav115':oorav115,'oorav116':oorav116,'oorav117':oorav117,
                                       'oorav121':oorav121,'oorav122':oorav122,'oorav123':oorav123,'oorav124':oorav124,'oorav125':oorav125,'oorav126':oorav126,'oorav127':oorav127,
                                       'oorav131':oorav131,'oorav132':oorav132,'oorav133':oorav133,'oorav134':oorav134,'oorav135':oorav135,'oorav136':oorav136,'oorav137':oorav137,
                                       'oorav141':oorav141,'oorav142':oorav142,'oorav143':oorav143,'oorav144':oorav144,'oorav145':oorav145,'oorav146':oorav146,'oorav147':oorav147,
                                       'oorav151':oorav151,'oorav152':oorav152,'oorav153':oorav153,'oorav154':oorav154,'oorav155':oorav155,'oorav156':oorav156,'oorav157':oorav157,
                                       'oorad111':oorad111,'oorad112':oorad112,'oorad113':oorad113,'oorad114':oorad114,'oorad115':oorad115,'oorad116':oorad116,'oorad117':oorad117,
                                       'oorad121':oorad121,'oorad122':oorad122,'oorad123':oorad123,'oorad124':oorad124,'oorad125':oorad125,'oorad126':oorad126,'oorad127':oorad127,
                                       'oorad131':oorad131,'oorad132':oorad132,'oorad133':oorad133,'oorad134':oorad134,'oorad135':oorad135,'oorad136':oorad136,'oorad137':oorad137,
                                       'oorad141':oorad141,'oorad142':oorad142,'oorad143':oorad143,'oorad144':oorad144,'oorad145':oorad145,'oorad146':oorad146,'oorad147':oorad147,
                                       'oorad151':oorad151,'oorad152':oorad152,'oorad153':oorad153,'oorad154':oorad154,'oorad155':oorad155,'oorad156':oorad156,'oorad157':oorad157,
                                       'oorad171':oorad171,'oorad172':oorad172,'oorad173':oorad173,'oorad174':oorad174,'oorad175':oorad175,'oorad176':oorad176,'oorad177':oorad177,
                                       'cico111':cico111,'cico112':cico112,'cico113':cico113,'cico114':cico114,'cico115':cico115,'cico116':cico116,'cico117':cico117,
                                       'cico121':cico121,'cico122':cico122,'cico123':cico123,'cico124':cico124,'cico125':cico125,'cico126':cico126,'cico127':cico127,
                                       'cico131':cico131,'cico132':cico132,'cico133':cico133,'cico134':cico134,'cico135':cico135,'cico136':cico136,'cico137':cico137,
                                       'cico141':cico141,'cico142':cico142,'cico143':cico143,'cico144':cico144,'cico145':cico145,'cico146':cico146,'cico147':cico147,
                                       'so111':so111,'so112':so112,'so113':so113,'so114':so114,'so115':so115,'so116':so116,'so117':so117,
                                       'so121':so121,'so122':so122,'so123':so123,'so124':so124,'so125':so125,'so126':so126,'so127':so127,
                                       'so131':so131,'so132':so132,'so133':so133,'so134':so134,'so135':so135,'so136v':so136,'so137':so137,
                                       'so141':so141,'so142':so142,'so143':so143,'so144':so144,'so145':so145,'so146':so146,'so147':so147,
                                       'so151':so151,'so152':so152,'so153':so153,'so154':so154,'so155':so155,'so156':so156,'so157':so157,
                                       'q1_clarity':q1_clarity,'q1_guidance':q1_guidance,'q1_process':q1_process,
                                       'q1_utility':q1_utility,'q1_resource':q1_resource,'q2_clarity':q2_clarity,'q2_guidance':q2_guidance,'q2_process':q2_process,
                                       'q2_utility':q2_utility,'q2_resource':q2_resource,
                                       'q3_clarity':q3_clarity,'q3_guidance':q3_guidance,'q3_process':q3_process,
                                       'q3_utility':q3_utility,'q3_resource':q3_resource,
                                       'q4_clarity':q4_clarity,'q4_guidance':q4_guidance,'q4_process':q4_process,
                                       'q4_utility':q4_utility,'q4_resource':q4_resource,
                                       'q5_clarity':q5_clarity,'q5_guidance':q5_guidance,'q5_process':q5_process,
                                       'q5_utility':q5_utility,'q5_resource':q5_resource,
                                       'q6_clarity':q6_clarity,'q6_guidance':q6_guidance,'q6_process':q6_process,
                                       'q6_utility':q6_utility,'q6_resource':q6_resource,
                                       'q7_clarity':q7_clarity,'q7_guidance':q7_guidance,'q7_process':q7_process,
                                       'q7_utility':q7_utility,'q7_resource':q7_resource,'q7_domain':q7_domain,
                                       'q8_clarity':q8_clarity,'q8_utility':q8_utility,'q8_guidance':q8_guidance,
                                       'q8_domain':q8_domain,
                                       'q9_clarity':q9_clarity,'q9_utility':q9_utility,'q9_guidance':q9_guidance,
                                       'q9_domain':q9_domain,'q9_activity':q9_activity}) 
        
class FourthYear(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_clarit = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_clarity = q1_clarit
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_utility = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_guidance = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_process = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        gadq151=Survey.all().filter("semester = ",sem).filter("q15 = ", 4).count()
        gadq152=Survey.all().filter("semester = ",sem).filter("q15 = ", 5).count()
        gadq153=Survey.all().filter("semester = ",sem).filter("q15 = ", 6).count()
        gadq154=Survey.all().filter("semester = ",sem).filter("q15 = ", 7).count()
        gadq155=Survey.all().filter("semester = ",sem).filter("q15 = ", 8).count()
        gadq156=Survey.all().filter("semester = ",sem).filter("q15 = ", 9).count()
        gadq157=Survey.all().filter("semester = ",sem).filter("q15 = ", 10).count()
        
        q1_resource = 4*gadq151 + 5*gadq152 + 6*gadq153 + 7*gadq154 + 8*gadq155 + 9*gadq156 + 10*gadq157

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_clarit = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_clarity = q2_clarit
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_utility = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_guidance = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_process = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_resource = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_clarit = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_clarity = q3_clarit
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_utility = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_guidance = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_process = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_resource = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_clarit = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_clarity = q4_clarit
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_utility = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_guidance = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_process = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_resource = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_clarit = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_clarity = q5_clarit
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_utility = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_guidance = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_process = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_resource = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157      

        oorav111=Survey.all().filter("semester = ",sem).filter("q61 = ", 4).count()
        oorav112=Survey.all().filter("semester = ",sem).filter("q61 = ", 5).count()
        oorav113=Survey.all().filter("semester = ",sem).filter("q61 = ", 6).count()
        oorav114=Survey.all().filter("semester = ",sem).filter("q61 = ", 7).count()
        oorav115=Survey.all().filter("semester = ",sem).filter("q61 = ", 8).count()
        oorav116=Survey.all().filter("semester = ",sem).filter("q61 = ", 9).count()
        oorav117=Survey.all().filter("semester = ",sem).filter("q61 = ", 10).count()
        
        q6_clarit = 4*oorav111 + 5*oorav112 + 6*oorav113 + 7*oorav114 + 8*oorav115 + 9*oorav116 + 10*oorav117
        q6_clarity = q6_clarit
        
        oorav121=Survey.all().filter("semester = ",sem).filter("q62 = ", 4).count()
        oorav122=Survey.all().filter("semester = ",sem).filter("q62 = ", 5).count()
        oorav123=Survey.all().filter("semester = ",sem).filter("q62 = ", 6).count()
        oorav124=Survey.all().filter("semester = ",sem).filter("q62 = ", 7).count()
        oorav125=Survey.all().filter("semester = ",sem).filter("q62 = ", 8).count()
        oorav126=Survey.all().filter("semester = ",sem).filter("q62 = ", 9).count()
        oorav127=Survey.all().filter("semester = ",sem).filter("q62 = ", 10).count()
        
        q6_utility = 4*oorav121 + 5*oorav122 + 6*oorav123 + 7*oorav124 + 8*oorav125 + 9*oorav126 + 10*oorav127
        
        oorav131=Survey.all().filter("semester = ",sem).filter("q63 = ", 4).count()
        oorav132=Survey.all().filter("semester = ",sem).filter("q63 = ", 5).count()
        oorav133=Survey.all().filter("semester = ",sem).filter("q63 = ", 6).count()
        oorav134=Survey.all().filter("semester = ",sem).filter("q63 = ", 7).count()
        oorav135=Survey.all().filter("semester = ",sem).filter("q63 = ", 8).count()
        oorav136=Survey.all().filter("semester = ",sem).filter("q63 = ", 9).count()
        oorav137=Survey.all().filter("semester = ",sem).filter("q63 = ", 10).count()
        
        q6_guidance = 4*oorav131 + 5*oorav132 + 6*oorav133 + 7*oorav134 + 8*oorav135 + 9*oorav136 + 10*oorav137 
        
        oorav141=Survey.all().filter("semester = ",sem).filter("q64 = ", 4).count()
        oorav142=Survey.all().filter("semester = ",sem).filter("q64 = ", 5).count()
        oorav143=Survey.all().filter("semester = ",sem).filter("q64 = ", 6).count()
        oorav144=Survey.all().filter("semester = ",sem).filter("q64 = ", 7).count()
        oorav145=Survey.all().filter("semester = ",sem).filter("q64 = ", 8).count()
        oorav146=Survey.all().filter("semester = ",sem).filter("q64 = ", 9).count()
        oorav147=Survey.all().filter("semester = ",sem).filter("q64 = ", 10).count()
        
        q6_process = 4*oorav141 + 5*oorav142 + 6*oorav143 + 7*oorav144 + 8*oorav145 + 9*oorav146 + 10*oorav147 
        
        oorav151=Survey.all().filter("semester = ",sem).filter("q65 = ", 4).count()
        oorav152=Survey.all().filter("semester = ",sem).filter("q65 = ", 5).count()
        oorav153=Survey.all().filter("semester = ",sem).filter("q65 = ", 6).count()
        oorav154=Survey.all().filter("semester = ",sem).filter("q65 = ", 7).count()
        oorav155=Survey.all().filter("semester = ",sem).filter("q65 = ", 8).count()
        oorav156=Survey.all().filter("semester = ",sem).filter("q65 = ", 9).count()
        oorav157=Survey.all().filter("semester = ",sem).filter("q65 = ", 10).count()
        
        q6_resource = 4*oorav151 + 5*oorav152 + 6*oorav153 + 7*oorav154 + 8*oorav155 + 9*oorav156 + 10*oorav157      

        oorad111=Survey.all().filter("semester = ",sem).filter("q71 = ", 4).count()
        oorad112=Survey.all().filter("semester = ",sem).filter("q71 = ", 5).count()
        oorad113=Survey.all().filter("semester = ",sem).filter("q71 = ", 6).count()
        oorad114=Survey.all().filter("semester = ",sem).filter("q71 = ", 7).count()
        oorad115=Survey.all().filter("semester = ",sem).filter("q71 = ", 8).count()
        oorad116=Survey.all().filter("semester = ",sem).filter("q71 = ", 9).count()
        oorad117=Survey.all().filter("semester = ",sem).filter("q71 = ", 10).count()
        
        q7_clarit = 4*oorad111 + 5*oorad112 + 6*oorad113 + 7*oorad114 + 8*oorad115 + 9*oorad116 + 10*oorad117
        q7_clarity = q7_clarit
        
        oorad121=Survey.all().filter("semester = ",sem).filter("q72 = ", 4).count()
        oorad122=Survey.all().filter("semester = ",sem).filter("q72 = ", 5).count()
        oorad123=Survey.all().filter("semester = ",sem).filter("q72 = ", 6).count()
        oorad124=Survey.all().filter("semester = ",sem).filter("q72 = ", 7).count()
        oorad125=Survey.all().filter("semester = ",sem).filter("q72 = ", 8).count()
        oorad126=Survey.all().filter("semester = ",sem).filter("q72 = ", 9).count()
        oorad127=Survey.all().filter("semester = ",sem).filter("q72 = ", 10).count()
        
        q7_utility = 4*oorad121 + 5*oorad122 + 6*oorad123 + 7*oorad124 + 8*oorad125 + 9*oorad126 + 10*oorad127
        
        oorad131=Survey.all().filter("semester = ",sem).filter("q73 = ", 4).count()
        oorad132=Survey.all().filter("semester = ",sem).filter("q73 = ", 5).count()
        oorad133=Survey.all().filter("semester = ",sem).filter("q73 = ", 6).count()
        oorad134=Survey.all().filter("semester = ",sem).filter("q73 = ", 7).count()
        oorad135=Survey.all().filter("semester = ",sem).filter("q73 = ", 8).count()
        oorad136=Survey.all().filter("semester = ",sem).filter("q73 = ", 9).count()
        oorad137=Survey.all().filter("semester = ",sem).filter("q73 = ", 10).count()
        
        q7_guidance = 4*oorad131 + 5*oorad132 + 6*oorad133 + 7*oorad134 + 8*oorad135 + 9*oorad136 + 10*oorad137 
        
        oorad141=Survey.all().filter("semester = ",sem).filter("q74 = ", 4).count()
        oorad142=Survey.all().filter("semester = ",sem).filter("q74 = ", 5).count()
        oorad143=Survey.all().filter("semester = ",sem).filter("q74 = ", 6).count()
        oorad144=Survey.all().filter("semester = ",sem).filter("q74 = ", 7).count()
        oorad145=Survey.all().filter("semester = ",sem).filter("q74 = ", 8).count()
        oorad146=Survey.all().filter("semester = ",sem).filter("q74 = ", 9).count()
        oorad147=Survey.all().filter("semester = ",sem).filter("q74 = ", 10).count()
        
        q7_process = 4*oorad141 + 5*oorad142 + 6*oorad143 + 7*oorad144 + 8*oorad145 + 9*oorad146 + 10*oorad147 
        
        oorad151=Survey.all().filter("semester = ",sem).filter("q75 = ", 4).count()
        oorad152=Survey.all().filter("semester = ",sem).filter("q75 = ", 5).count()
        oorad153=Survey.all().filter("semester = ",sem).filter("q75 = ", 6).count()
        oorad154=Survey.all().filter("semester = ",sem).filter("q75 = ", 7).count()
        oorad155=Survey.all().filter("semester = ",sem).filter("q75 = ", 8).count()
        oorad156=Survey.all().filter("semester = ",sem).filter("q75 = ", 9).count()
        oorad157=Survey.all().filter("semester = ",sem).filter("q75 = ", 10).count()
        
        q7_resource = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157
        
        oorad171=Survey.all().filter("semester = ",sem).filter("q77 = ", 4).count()
        oorad172=Survey.all().filter("semester = ",sem).filter("q77 = ", 5).count()
        oorad173=Survey.all().filter("semester = ",sem).filter("q77 = ", 6).count()
        oorad174=Survey.all().filter("semester = ",sem).filter("q77 = ", 7).count()
        oorad175=Survey.all().filter("semester = ",sem).filter("q77 = ", 8).count()
        oorad176=Survey.all().filter("semester = ",sem).filter("q77 = ", 9).count()
        oorad177=Survey.all().filter("semester = ",sem).filter("q77 = ", 10).count()
        
        q7_domain = 4*oorad151 + 5*oorad152 + 6*oorad153 + 7*oorad154 + 8*oorad155 + 9*oorad156 + 10*oorad157

        cico111=Survey.all().filter("semester = ",sem).filter("q81 = ", 4).count()
        cico112=Survey.all().filter("semester = ",sem).filter("q81 = ", 5).count()
        cico113=Survey.all().filter("semester = ",sem).filter("q81 = ", 6).count()
        cico114=Survey.all().filter("semester = ",sem).filter("q81 = ", 7).count()
        cico115=Survey.all().filter("semester = ",sem).filter("q81 = ", 8).count()
        cico116=Survey.all().filter("semester = ",sem).filter("q81 = ", 9).count()
        cico117=Survey.all().filter("semester = ",sem).filter("q81 = ", 10).count()
        
        q8_clarit = 4*cico111 + 5*cico112 + 6*cico113 + 7*cico114 + 8*cico115 + 9*cico116 + 10*cico117
        q8_clarity = q8_clarit
        
        cico121=Survey.all().filter("semester = ",sem).filter("q82 = ", 4).count()
        cico122=Survey.all().filter("semester = ",sem).filter("q82 = ", 5).count()
        cico123=Survey.all().filter("semester = ",sem).filter("q82 = ", 6).count()
        cico124=Survey.all().filter("semester = ",sem).filter("q82 = ", 7).count()
        cico125=Survey.all().filter("semester = ",sem).filter("q82 = ", 8).count()
        cico126=Survey.all().filter("semester = ",sem).filter("q82 = ", 9).count()
        cico127=Survey.all().filter("semester = ",sem).filter("q82 = ", 10).count()
        
        q8_utility = 4*cico121 + 5*cico122 + 6*cico123 + 7*cico124 + 8*cico125 + 9*cico126 + 10*cico127
        
        cico131=Survey.all().filter("semester = ",sem).filter("q83 = ", 4).count()
        cico132=Survey.all().filter("semester = ",sem).filter("q83 = ", 5).count()
        cico133=Survey.all().filter("semester = ",sem).filter("q83 = ", 6).count()
        cico134=Survey.all().filter("semester = ",sem).filter("q83 = ", 7).count()
        cico135=Survey.all().filter("semester = ",sem).filter("q83 = ", 8).count()
        cico136=Survey.all().filter("semester = ",sem).filter("q83 = ", 9).count()
        cico137=Survey.all().filter("semester = ",sem).filter("q83 = ", 10).count()
        
        q8_guidance = 4*cico131 + 5*cico132 + 6*cico133 + 7*cico134 + 8*cico135 + 9*cico136 + 10*cico137 
        
        cico141=Survey.all().filter("semester = ",sem).filter("q87 = ", 4).count()
        cico142=Survey.all().filter("semester = ",sem).filter("q87 = ", 5).count()
        cico143=Survey.all().filter("semester = ",sem).filter("q87 = ", 6).count()
        cico144=Survey.all().filter("semester = ",sem).filter("q87 = ", 7).count()
        cico145=Survey.all().filter("semester = ",sem).filter("q87 = ", 8).count()
        cico146=Survey.all().filter("semester = ",sem).filter("q87 = ", 9).count()
        cico147=Survey.all().filter("semester = ",sem).filter("q87 = ", 10).count()
        
        q8_domain = 4*cico141 + 5*cico142 + 6*cico143 + 7*cico144 + 8*cico145 + 9*cico146 + 10*cico147

        so111=Survey.all().filter("semester = ",sem).filter("q91 = ", 4).count()
        so112=Survey.all().filter("semester = ",sem).filter("q91 = ", 5).count()
        so113=Survey.all().filter("semester = ",sem).filter("q91 = ", 6).count()
        so114=Survey.all().filter("semester = ",sem).filter("q91 = ", 7).count()
        so115=Survey.all().filter("semester = ",sem).filter("q91 = ", 8).count()
        so116=Survey.all().filter("semester = ",sem).filter("q91 = ", 9).count()
        so117=Survey.all().filter("semester = ",sem).filter("q91 = ", 10).count()
        
        q9_clarit = 4*so111 + 5*so112 + 6*so113 + 7*so114 + 8*so115 + 9*so116 + 10*so117
        q9_clarity = q9_clarit
        
        so121=Survey.all().filter("semester = ",sem).filter("q92 = ", 4).count()
        so122=Survey.all().filter("semester = ",sem).filter("q92 = ", 5).count()
        so123=Survey.all().filter("semester = ",sem).filter("q92 = ", 6).count()
        so124=Survey.all().filter("semester = ",sem).filter("q92 = ", 7).count()
        so125=Survey.all().filter("semester = ",sem).filter("q92 = ", 8).count()
        so126=Survey.all().filter("semester = ",sem).filter("q92 = ", 9).count()
        so127=Survey.all().filter("semester = ",sem).filter("q92 = ", 10).count()
        
        q9_utility = 4*so121 + 5*so122 + 6*so123 + 7*so124 + 8*so125 + 9*so126 + 10*so127
        
        so131=Survey.all().filter("semester = ",sem).filter("q93 = ", 4).count()
        so132=Survey.all().filter("semester = ",sem).filter("q93 = ", 5).count()
        so133=Survey.all().filter("semester = ",sem).filter("q93 = ", 6).count()
        so134=Survey.all().filter("semester = ",sem).filter("q93 = ", 7).count()
        so135=Survey.all().filter("semester = ",sem).filter("q93 = ", 8).count()
        so136=Survey.all().filter("semester = ",sem).filter("q93 = ", 9).count()
        so137=Survey.all().filter("semester = ",sem).filter("q93 = ", 10).count()
        
        q9_guidance = 4*so131 + 5*so132 + 6*so133 + 7*so134 + 8*so135 + 9*so136 + 10*so137 
        
        so141=Survey.all().filter("semester = ",sem).filter("q96 = ", 4).count()
        so142=Survey.all().filter("semester = ",sem).filter("q96 = ", 5).count()
        so143=Survey.all().filter("semester = ",sem).filter("q96 = ", 6).count()
        so144=Survey.all().filter("semester = ",sem).filter("q96 = ", 7).count()
        so145=Survey.all().filter("semester = ",sem).filter("q96 = ", 8).count()
        so146=Survey.all().filter("semester = ",sem).filter("q96 = ", 9).count()
        so147=Survey.all().filter("semester = ",sem).filter("q96 = ", 10).count()
        
        q9_activity = 4*so141 + 5*so142 + 6*so143 + 7*so144 + 8*so145 + 9*so146 + 10*so147 
        
        so151=Survey.all().filter("semester = ",sem).filter("q97 = ", 4).count()
        so152=Survey.all().filter("semester = ",sem).filter("q97 = ", 5).count()
        so153=Survey.all().filter("semester = ",sem).filter("q97 = ", 6).count()
        so154=Survey.all().filter("semester = ",sem).filter("q97 = ", 7).count()
        so155=Survey.all().filter("semester = ",sem).filter("q97 = ", 8).count()
        so156=Survey.all().filter("semester = ",sem).filter("q97 = ", 9).count()
        so157=Survey.all().filter("semester = ",sem).filter("q97 = ", 10).count() 

        q9_domain = 4*so151 + 5*so152 + 6*so153 + 7*so154 + 8*so155 + 9*so156 + 10*so157 
        
        self.render("fourthyear.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                       'gadq151':gadq151,'gadq152':gadq152,'gadq153':gadq153,'gadq154':gadq154,'gadq155':gadq155,'gadq156':gadq156,'gadq157':gadq157,
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'obmd111':obmd111,'obmd112':obmd112,'obmd113':obmd113,'obmd114':obmd114,'obmd115':obmd115,'obmd116':obmd116,'obmd117':obmd117,
                                       'obmd121':obmd121,'obmd122':obmd122,'obmd123':obmd123,'obmd124':obmd124,'obmd125':obmd125,'obmd126':obmd126,'obmd127':obmd127,
                                       'obmd131':obmd131,'obmd132':obmd132,'obmd133':obmd133,'obmd134':obmd134,'obmd135':obmd135,'obmd136':obmd136,'obmd137':obmd137,
                                       'obmd141':obmd141,'obmd142':obmd142,'obmd143':obmd143,'obmd144':obmd144,'obmd145':obmd145,'obmd146':obmd146,'obmd147':obmd147,
                                       'obmd151':obmd151,'obmd152':obmd152,'obmd153':obmd153,'obmd154':obmd154,'obmd155':obmd155,'obmd156':obmd156,'obmd157':obmd157,
                                       'obhod111':obhod111,'obhod112':obhod112,'obhod113':obhod113,'obhod114':obhod114,'obhod115':obhod115,'obhod116':obhod116,'obhod117':obhod117,
                                       'obhod121':obhod121,'obhod122':obhod122,'obhod123':obhod123,'obhod124':obhod124,'obhod125':obhod125,'obhod126':obhod126,'obhod127':obhod127,
                                       'obhod131':obhod131,'obhod132':obhod132,'obhod133':obhod133,'obhod134':obhod134,'obhod135':obhod135,'obhod136':obhod136,'obhod137':obhod137,
                                       'obhod141':obhod141,'obhod142':obhod142,'obhod143':obhod143,'obhod144':obhod144,'obhod145':obhod145,'obhod146':obhod146,'obhod147':obhod147,
                                       'obhod151':obhod151,'obhod152':obhod152,'obhod153':obhod153,'obhod154':obhod154,'obhod155':obhod155,'obhod156':obhod156,'obhod157':obhod157,
                                       'oorav111':oorav111,'oorav112':oorav112,'oorav113':oorav113,'oorav114':oorav114,'oorav115':oorav115,'oorav116':oorav116,'oorav117':oorav117,
                                       'oorav121':oorav121,'oorav122':oorav122,'oorav123':oorav123,'oorav124':oorav124,'oorav125':oorav125,'oorav126':oorav126,'oorav127':oorav127,
                                       'oorav131':oorav131,'oorav132':oorav132,'oorav133':oorav133,'oorav134':oorav134,'oorav135':oorav135,'oorav136':oorav136,'oorav137':oorav137,
                                       'oorav141':oorav141,'oorav142':oorav142,'oorav143':oorav143,'oorav144':oorav144,'oorav145':oorav145,'oorav146':oorav146,'oorav147':oorav147,
                                       'oorav151':oorav151,'oorav152':oorav152,'oorav153':oorav153,'oorav154':oorav154,'oorav155':oorav155,'oorav156':oorav156,'oorav157':oorav157,
                                       'oorad111':oorad111,'oorad112':oorad112,'oorad113':oorad113,'oorad114':oorad114,'oorad115':oorad115,'oorad116':oorad116,'oorad117':oorad117,
                                       'oorad121':oorad121,'oorad122':oorad122,'oorad123':oorad123,'oorad124':oorad124,'oorad125':oorad125,'oorad126':oorad126,'oorad127':oorad127,
                                       'oorad131':oorad131,'oorad132':oorad132,'oorad133':oorad133,'oorad134':oorad134,'oorad135':oorad135,'oorad136':oorad136,'oorad137':oorad137,
                                       'oorad141':oorad141,'oorad142':oorad142,'oorad143':oorad143,'oorad144':oorad144,'oorad145':oorad145,'oorad146':oorad146,'oorad147':oorad147,
                                       'oorad151':oorad151,'oorad152':oorad152,'oorad153':oorad153,'oorad154':oorad154,'oorad155':oorad155,'oorad156':oorad156,'oorad157':oorad157,
                                       'oorad171':oorad171,'oorad172':oorad172,'oorad173':oorad173,'oorad174':oorad174,'oorad175':oorad175,'oorad176':oorad176,'oorad177':oorad177,
                                       'cico111':cico111,'cico112':cico112,'cico113':cico113,'cico114':cico114,'cico115':cico115,'cico116':cico116,'cico117':cico117,
                                       'cico121':cico121,'cico122':cico122,'cico123':cico123,'cico124':cico124,'cico125':cico125,'cico126':cico126,'cico127':cico127,
                                       'cico131':cico131,'cico132':cico132,'cico133':cico133,'cico134':cico134,'cico135':cico135,'cico136':cico136,'cico137':cico137,
                                       'cico141':cico141,'cico142':cico142,'cico143':cico143,'cico144':cico144,'cico145':cico145,'cico146':cico146,'cico147':cico147,
                                       'so111':so111,'so112':so112,'so113':so113,'so114':so114,'so115':so115,'so116':so116,'so117':so117,
                                       'so121':so121,'so122':so122,'so123':so123,'so124':so124,'so125':so125,'so126':so126,'so127':so127,
                                       'so131':so131,'so132':so132,'so133':so133,'so134':so134,'so135':so135,'so136v':so136,'so137':so137,
                                       'so141':so141,'so142':so142,'so143':so143,'so144':so144,'so145':so145,'so146':so146,'so147':so147,
                                       'so151':so151,'so152':so152,'so153':so153,'so154':so154,'so155':so155,'so156':so156,'so157':so157,
                                       'q1_clarity':q1_clarity,'q1_guidance':q1_guidance,'q1_process':q1_process,
                                       'q1_utility':q1_utility,'q1_resource':q1_resource,'q2_clarity':q2_clarity,'q2_guidance':q2_guidance,'q2_process':q2_process,
                                       'q2_utility':q2_utility,'q2_resource':q2_resource,
                                       'q3_clarity':q3_clarity,'q3_guidance':q3_guidance,'q3_process':q3_process,
                                       'q3_utility':q3_utility,'q3_resource':q3_resource,
                                       'q4_clarity':q4_clarity,'q4_guidance':q4_guidance,'q4_process':q4_process,
                                       'q4_utility':q4_utility,'q4_resource':q4_resource,
                                       'q5_clarity':q5_clarity,'q5_guidance':q5_guidance,'q5_process':q5_process,
                                       'q5_utility':q5_utility,'q5_resource':q5_resource,
                                       'q6_clarity':q6_clarity,'q6_guidance':q6_guidance,'q6_process':q6_process,
                                       'q6_utility':q6_utility,'q6_resource':q6_resource,
                                       'q7_clarity':q7_clarity,'q7_guidance':q7_guidance,'q7_process':q7_process,
                                       'q7_utility':q7_utility,'q7_resource':q7_resource,'q7_domain':q7_domain,
                                       'q8_clarity':q8_clarity,'q8_utility':q8_utility,'q8_guidance':q8_guidance,
                                       'q8_domain':q8_domain,
                                       'q9_clarity':q9_clarity,'q9_utility':q9_utility,'q9_guidance':q9_guidance,
                                       'q9_domain':q9_domain,'q9_activity':q9_activity})        
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/admin', AdminPage),
                               ('/secondyear', SecondYear),
                               ('/thirdyear', ThirdYear),
                               ('/fourthyear', FourthYear),
                               ('/thanks', ThankYou),], debug=True)