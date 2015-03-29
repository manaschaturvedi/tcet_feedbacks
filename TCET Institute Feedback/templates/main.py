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

    q21 = db.IntegerProperty()
    q22 = db.IntegerProperty()
    q23 = db.IntegerProperty()
    q24 = db.IntegerProperty()
    q25 = db.IntegerProperty()
    q26 = db.IntegerProperty()
    
    q31 = db.IntegerProperty()
    q32 = db.IntegerProperty()
    q33 = db.IntegerProperty()
    q34 = db.IntegerProperty()
    q35 = db.IntegerProperty()
    q36 = db.IntegerProperty()
    q37 = db.IntegerProperty()
    
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
    q56 = db.IntegerProperty()
    q57 = db.IntegerProperty()
    q58 = db.IntegerProperty()
   
    total_q1 = db.IntegerProperty()
    total_q2 = db.IntegerProperty()
    total_q3 = db.IntegerProperty()
    total_q4 = db.IntegerProperty()
    total_q5 = db.IntegerProperty()
  
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
       
        q21 = self.request.get("q21")
        q22 = self.request.get("q22")
        q23 = self.request.get("q23")
        q24 = self.request.get("q24")
        q25 = self.request.get("q25")
        q26 = self.request.get("q26")
        
        q31 = self.request.get("q31")
        q32 = self.request.get("q32")
        q33 = self.request.get("q33")
        q34 = self.request.get("q34")
        q35 = self.request.get("q35")
        q36 = self.request.get("q36")
        q37 = self.request.get("q37")
        
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
        q56 = self.request.get("q56")
        q57 = self.request.get("q57")
        q58 = self.request.get("q58")
       
        if(name and clas and roll_no and semester
           and q11 and q12 and q13 and q14
           and q21 and q22 and q23 and q24 and q25 and q26
           and q31 and q32 and q33 and q34 and q35 and q36 and q37
           and q41 and q42 and q43 and q44 and q45
           and q51 and q52 and q53 and q54 and q55 and q56 and q57 and q58):
            roll_no = int(roll_no)
            semester = int(semester)
            q11 = int(q11)
            q12 = int(q12)
            q13 = int(q13)
            q14 = int(q14)
           
            q21 = int(q21)
            q22 = int(q22)
            q23 = int(q23)
            q24 = int(q24)
            q25 = int(q25)
            q26 = int(q26)
            
            q31 = int(q31)
            q32 = int(q32)
            q33 = int(q33)
            q34 = int(q34)
            q35 = int(q35)
            q36 = int(q36)
            q37 = int(q37)
            
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
            q56 = int(q56)
            q57 = int(q57)
            q58 = int(q58)
            
            total_q1 = q11 + q12 + q13 + q14 + q21 + q22 + q23 + q24 + q25 + q26 + q31 + q32 + q33 + q34 + q35 + q36 + q37+ q41 + q42 + q43 + q44 + q45 + q51 + q52 + q53 + q54 + q55 + q56 + q57 + q58
            
             
            s = Survey(vam_id = vam_id, name = name, roll_no = roll_no, clas = clas,
            semester = semester,
            q11 = q11, q12 = q12, q13 = q13, q14 = q14, 
            q21 = q21, q22 = q22, q23 = q23, q24 = q24, q25 = q25, q26 = q26,
            q31 = q31, q32 = q32, q33 = q33, q34 = q34, q35 = q35, q36 = q36, q37 = q37,
            q41 = q41, q42 = q42, q43 = q43, q44 = q44, q45 = q45,
            q51 = q51, q52 = q52, q53 = q53, q54 = q54, q55 = q55, q56 = q56, q57 = q57, q58 = q58,
            total_q1 = total_q1)
            s.put()
            self.redirect("/thanks")
        else:
            params = dict(name = name, roll_no = roll_no, clas = clas,
            semester = semester,
            q11 = q11, q12 = q12, q13 = q13, q14 = q14, 
            q21 = q21, q22 = q22, q23 = q23, q24 = q24, q25 = q25, q26 = q26,
            q31 = q31, q32 = q32, q33 = q33, q34 = q34, q35 = q35, q36 = q36, q37 = q37,
            q41 = q41, q42 = q42, q43 = q43, q44 = q44, q45 = q45,
            q51 = q51, q52 = q52, q53 = q53, q54 = q54, q55 = q55, q56 = q56, q57 = q57, q58 = q58)
            params['error_form'] = '"PLEASE FILL ALL THE ENTRIES BEFORE SUBMITTING"'
            self.render('indexab.html',**params)
        
class ThankYou(Handler):
    def get(self):
        self.render("thanx.html")

class AdminPage(Handler):
    def get(self):
        #self.render("admin.html")
        
        clsea = "SE-A"
        sea=Survey.all().filter("clas = ",clsea).count()
        
        gadq111=Survey.all().filter("clas = ",clsea).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("clas = ",clsea).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("clas = ",clsea).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("clas = ",clsea).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("clas = ",clsea).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("clas = ",clsea).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("clas = ",clsea).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond/float(sea)
        
        gadq121=Survey.all().filter("clas = ",clsea).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("clas = ",clsea).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("clas = ",clsea).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("clas = ",clsea).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("clas = ",clsea).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("clas = ",clsea).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("clas = ",clsea).filter("q12 = ", 10).count()
        
        q1_ligh = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        q1_light = q1_ligh/float(sea)
        
        gadq131=Survey.all().filter("clas = ",clsea).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("clas = ",clsea).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("clas = ",clsea).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("clas = ",clsea).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("clas = ",clsea).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("clas = ",clsea).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("clas = ",clsea).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("clas = ",clsea).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("clas = ",clsea).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("clas = ",clsea).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("clas = ",clsea).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("clas = ",clsea).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("clas = ",clsea).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("clas = ",clsea).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("clas = ",clsea).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("secondyeara.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })

class SecondYearB(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_light = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("secondyearb.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })                                     
                                       
                                       
        
class ThirdYearA(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_light = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("thirdyeara.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })

class ThirdYearB(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_light = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("thirdyearb.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })
        
class FourthYearA(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_light = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("fourthyeara.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })        

class FourthYearB(Handler):
    def get(self):
        sem = int(self.request.get("semester"))
        gadq111=Survey.all().filter("semester = ",sem).filter("q11 = ", 4).count()
        gadq112=Survey.all().filter("semester = ",sem).filter("q11 = ", 5).count()
        gadq113=Survey.all().filter("semester = ",sem).filter("q11 = ", 6).count()
        gadq114=Survey.all().filter("semester = ",sem).filter("q11 = ", 7).count()
        gadq115=Survey.all().filter("semester = ",sem).filter("q11 = ", 8).count()
        gadq116=Survey.all().filter("semester = ",sem).filter("q11 = ", 9).count()
        gadq117=Survey.all().filter("semester = ",sem).filter("q11 = ", 10).count()
        
        q1_cond = 4*gadq111 + 5*gadq112 + 6*gadq113 + 7*gadq114 + 8*gadq115 + 9*gadq116 + 10*gadq117
        q1_condff = q1_cond
        
        gadq121=Survey.all().filter("semester = ",sem).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("semester = ",sem).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("semester = ",sem).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("semester = ",sem).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("semester = ",sem).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("semester = ",sem).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("semester = ",sem).filter("q12 = ", 10).count()
        
        q1_light = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        
        gadq131=Survey.all().filter("semester = ",sem).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("semester = ",sem).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("semester = ",sem).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("semester = ",sem).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("semester = ",sem).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("semester = ",sem).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("semester = ",sem).filter("q13 = ", 10).count()
        
        q1_ac = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        
        gadq141=Survey.all().filter("semester = ",sem).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("semester = ",sem).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("semester = ",sem).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("semester = ",sem).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("semester = ",sem).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("semester = ",sem).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("semester = ",sem).filter("q14 = ", 10).count()
        
        q1_clean = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        
        
        

        nbaq111=Survey.all().filter("semester = ",sem).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("semester = ",sem).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("semester = ",sem).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("semester = ",sem).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("semester = ",sem).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("semester = ",sem).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("semester = ",sem).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = q2_ea
        
        nbaq121=Survey.all().filter("semester = ",sem).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("semester = ",sem).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("semester = ",sem).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("semester = ",sem).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("semester = ",sem).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("semester = ",sem).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("semester = ",sem).filter("q22 = ", 10).count()
        
        q2_s_a = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        
        nbaq131=Survey.all().filter("semester = ",sem).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("semester = ",sem).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("semester = ",sem).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("semester = ",sem).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("semester = ",sem).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("semester = ",sem).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("semester = ",sem).filter("q23 = ", 10).count()
        
        q2_c_a = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        
        nbaq141=Survey.all().filter("semester = ",sem).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("semester = ",sem).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("semester = ",sem).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("semester = ",sem).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("semester = ",sem).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("semester = ",sem).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("semester = ",sem).filter("q24 = ", 10).count()
        
        q2_l_m = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        
        nbaq151=Survey.all().filter("semester = ",sem).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("semester = ",sem).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("semester = ",sem).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("semester = ",sem).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("semester = ",sem).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("semester = ",sem).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("semester = ",sem).filter("q25 = ", 10).count()
        
        q2_i_c = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157

        nbaq161=Survey.all().filter("semester = ",sem).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("semester = ",sem).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("semester = ",sem).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("semester = ",sem).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("semester = ",sem).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("semester = ",sem).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("semester = ",sem).filter("q26 = ", 10).count()
        
        q2_b_s = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167


        soeie111=Survey.all().filter("semester = ",sem).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("semester = ",sem).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("semester = ",sem).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("semester = ",sem).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("semester = ",sem).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("semester = ",sem).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("semester = ",sem).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = q3_li
        
        soeie121=Survey.all().filter("semester = ",sem).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("semester = ",sem).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("semester = ",sem).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("semester = ",sem).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("semester = ",sem).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("semester = ",sem).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("semester = ",sem).filter("q32 = ", 10).count()
        
        q3_i_s = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        
        soeie131=Survey.all().filter("semester = ",sem).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("semester = ",sem).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("semester = ",sem).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("semester = ",sem).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("semester = ",sem).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("semester = ",sem).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("semester = ",sem).filter("q33 = ", 10).count()
        
        q3_con_bo = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        
        soeie141=Survey.all().filter("semester = ",sem).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("semester = ",sem).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("semester = ",sem).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("semester = ",sem).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("semester = ",sem).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("semester = ",sem).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("semester = ",sem).filter("q34 = ", 10).count()
        
        q3_av_ne_ver = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        
        soeie151=Survey.all().filter("semester = ",sem).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("semester = ",sem).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("semester = ",sem).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("semester = ",sem).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("semester = ",sem).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("semester = ",sem).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("semester = ",sem).filter("q35 = ", 10).count()
        
        q3_re_ro = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157

        soeie161=Survey.all().filter("semester = ",sem).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("semester = ",sem).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("semester = ",sem).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("semester = ",sem).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("semester = ",sem).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("semester = ",sem).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("semester = ",sem).filter("q36 = ", 10).count()
        
        q3_j_m = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167

        soeie171=Survey.all().filter("semester = ",sem).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("semester = ",sem).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("semester = ",sem).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("semester = ",sem).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("semester = ",sem).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("semester = ",sem).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("semester = ",sem).filter("q37 = ", 10).count()
        
        q3_sta = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
  

        obmd111=Survey.all().filter("semester = ",sem).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("semester = ",sem).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("semester = ",sem).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("semester = ",sem).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("semester = ",sem).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("semester = ",sem).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("semester = ",sem).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = q4_h
        
        obmd121=Survey.all().filter("semester = ",sem).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("semester = ",sem).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("semester = ",sem).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("semester = ",sem).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("semester = ",sem).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("semester = ",sem).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("semester = ",sem).filter("q42 = ", 10).count()
        
        q4_men = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        
        obmd131=Survey.all().filter("semester = ",sem).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("semester = ",sem).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("semester = ",sem).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("semester = ",sem).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("semester = ",sem).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("semester = ",sem).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("semester = ",sem).filter("q43 = ", 10).count()
        
        q4_pri = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137 
        
        obmd141=Survey.all().filter("semester = ",sem).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("semester = ",sem).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("semester = ",sem).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("semester = ",sem).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("semester = ",sem).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("semester = ",sem).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("semester = ",sem).filter("q44 = ", 10).count()
        
        q4_tim_del = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147 
        
        obmd151=Survey.all().filter("semester = ",sem).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("semester = ",sem).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("semester = ",sem).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("semester = ",sem).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("semester = ",sem).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("semester = ",sem).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("semester = ",sem).filter("q45 = ", 10).count()
        
        q4_ser_qua = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157

        obhod111=Survey.all().filter("semester = ",sem).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("semester = ",sem).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("semester = ",sem).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("semester = ",sem).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("semester = ",sem).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("semester = ",sem).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("semester = ",sem).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = q5_re
        
        obhod121=Survey.all().filter("semester = ",sem).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("semester = ",sem).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("semester = ",sem).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("semester = ",sem).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("semester = ",sem).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("semester = ",sem).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("semester = ",sem).filter("q52 = ", 10).count()
        
        q5_aud = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        
        obhod131=Survey.all().filter("semester = ",sem).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("semester = ",sem).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("semester = ",sem).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("semester = ",sem).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("semester = ",sem).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("semester = ",sem).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("semester = ",sem).filter("q53 = ", 10).count()
        
        q5_gam = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        
        obhod141=Survey.all().filter("semester = ",sem).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("semester = ",sem).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("semester = ",sem).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("semester = ",sem).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("semester = ",sem).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("semester = ",sem).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("semester = ",sem).filter("q54 = ", 10).count()
        
        q5_info = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        
        obhod151=Survey.all().filter("semester = ",sem).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("semester = ",sem).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("semester = ",sem).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("semester = ",sem).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("semester = ",sem).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("semester = ",sem).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("semester = ",sem).filter("q55 = ", 10).count()
        
        q5_dr = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157

        obhod161=Survey.all().filter("semester = ",sem).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("semester = ",sem).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("semester = ",sem).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("semester = ",sem).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("semester = ",sem).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("semester = ",sem).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("semester = ",sem).filter("q56 = ", 10).count()
        
        q5_toi = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167

        obhod171=Survey.all().filter("semester = ",sem).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("semester = ",sem).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("semester = ",sem).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("semester = ",sem).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("semester = ",sem).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("semester = ",sem).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("semester = ",sem).filter("q57 = ", 10).count()
        
        q5_clean = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177

        obhod181=Survey.all().filter("semester = ",sem).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("semester = ",sem).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("semester = ",sem).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("semester = ",sem).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("semester = ",sem).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("semester = ",sem).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("semester = ",sem).filter("q58 = ", 10).count()
        
        q5_mai = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187

        
        
        self.render("fourthyearb.html" ,**{'gadq111': gadq111,'gadq112':gadq112,'gadq113':gadq113,'gadq114':gadq114,'gadq115':gadq115,'gadq116':gadq116,'gadq117':gadq117,
                                       'gadq121':gadq121,'gadq122':gadq122,'gadq123':gadq123,'gadq124':gadq124,'gadq125':gadq125,'gadq126':gadq126,'gadq127':gadq127,
                                       'gadq131':gadq131,'gadq132':gadq132,'gadq133':gadq133,'gadq134':gadq134,'gadq135':gadq135,'gadq136':gadq136,'gadq137':gadq137,
                                       'gadq141':gadq141,'gadq142':gadq142,'gadq143':gadq143,'gadq144':gadq144,'gadq145':gadq145,'gadq146':gadq146,'gadq147':gadq147,
                                      
                                       'nbaq111':nbaq111,'nbaq112':nbaq112,'nbaq113':nbaq113,'nbaq114':nbaq114,'nbaq115':nbaq115,'nbaq116':nbaq116,'nbaq117':nbaq117,
                                       'nbaq121':nbaq121,'nbaq122':nbaq122,'nbaq123':nbaq123,'nbaq124':nbaq124,'nbaq125':nbaq125,'nbaq126':nbaq126,'nbaq127':nbaq127,
                                       'nbaq131':nbaq131,'nbaq132':nbaq132,'nbaq133':nbaq133,'nbaq134':nbaq134,'nbaq135':nbaq135,'nbaq136':nbaq136,'nbaq137':nbaq137,
                                       'nbaq141':nbaq141,'nbaq142':nbaq142,'nbaq143':nbaq143,'nbaq144':nbaq144,'nbaq145':nbaq145,'nbaq146':nbaq146,'nbaq147':nbaq147,
                                       'nbaq151':nbaq151,'nbaq152':nbaq152,'nbaq153':nbaq153,'nbaq154':nbaq154,'nbaq155':nbaq155,'nbaq156':nbaq156,'nbaq157':nbaq157,
                                       'nbaq161':nbaq161,'nbaq162':nbaq162,'nbaq163':nbaq163,'nbaq164':nbaq164,'nbaq165':nbaq165,'nbaq166':nbaq166,'nbaq167':nbaq167,
                                          
                                       'soeie111':soeie111,'soeie112':soeie112,'soeie113':soeie113,'soeie114':soeie114,'soeie115':soeie115,'soeie116':soeie116,'soeie117':soeie117,
                                       'soeie121':soeie121,'soeie122':soeie122,'soeie123':soeie123,'soeie124':soeie124,'soeie125':soeie125,'soeie126':soeie126,'soeie127':soeie127,
                                       'soeie131':soeie131,'soeie132':soeie132,'soeie133':soeie133,'soeie134':soeie134,'soeie135':soeie135,'soeie136':soeie136,'soeie137':soeie137,
                                       'soeie141':soeie141,'soeie142':soeie142,'soeie143':soeie143,'soeie144':soeie144,'soeie145':soeie145,'soeie146':soeie146,'soeie147':soeie147,
                                       'soeie151':soeie151,'soeie152':soeie152,'soeie153':soeie153,'soeie154':soeie154,'soeie155':soeie155,'soeie156':soeie156,'soeie157':soeie157,
                                       'soeie161':soeie161,'soeie162':soeie162,'soeie163':soeie163,'soeie164':soeie164,'soeie165':soeie165,'soeie166':soeie166,'soeie167':soeie167,
                                       'soeie171':soeie171,'soeie172':soeie172,'soeie173':soeie173,'soeie174':soeie174,'soeie175':soeie175,'soeie176':soeie176,'soeie177':soeie177,
                                          
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
                                       'obhod161':obhod161,'obhod162':obhod162,'obhod163':obhod163,'obhod164':obhod164,'obhod165':obhod165,'obhod166':obhod166,'obhod167':obhod167,
                                       'obhod171':obhod171,'obhod172':obhod172,'obhod173':obhod173,'obhod174':obhod174,'obhod175':obhod175,'obhod176':obhod176,'obhod177':obhod177,
                                       'obhod181':obhod181,'obhod182':obhod182,'obhod183':obhod183,'obhod184':obhod184,'obhod185':obhod185,'obhod186':obhod186,'obhod187':obhod187,
                                          
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai
                                      })        

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/admin', AdminPage),
                               ('/secondyeara', SecondYearA),
                               ('/secondyearb', SecondYearB),
                               ('/thirdyeara', ThirdYearA),
                               ('/thirdyearb', ThirdYearB),
                               ('/fourthyeara', FourthYearA),
                               ('/fourthyearb', FourthYearB),
                               ('/thanks', ThankYou),], debug=True)
