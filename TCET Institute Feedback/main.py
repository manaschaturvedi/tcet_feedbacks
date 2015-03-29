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
   
    total_sea = db.FloatProperty()
    total_seb = db.IntegerProperty()
    total_tea= db.IntegerProperty()
    total_teb= db.IntegerProperty()
    total_bea= db.IntegerProperty()
    total_beb= db.IntegerProperty()
  
    created = db.DateTimeProperty(auto_now_add = True)

        
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
            
            
            
             
            s = Survey(vam_id = vam_id, name = name, roll_no = roll_no, clas = clas,
            semester = semester,
            q11 = q11, q12 = q12, q13 = q13, q14 = q14, 
            q21 = q21, q22 = q22, q23 = q23, q24 = q24, q25 = q25, q26 = q26,
            q31 = q31, q32 = q32, q33 = q33, q34 = q34, q35 = q35, q36 = q36, q37 = q37,
            q41 = q41, q42 = q42, q43 = q43, q44 = q44, q45 = q45,
            q51 = q51, q52 = q52, q53 = q53, q54 = q54, q55 = q55, q56 = q56, q57 = q57, q58 = q58)
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
        #SE-A
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
        q1_condff = round(q1_cond/float(sea),2)
        
        gadq121=Survey.all().filter("clas = ",clsea).filter("q12 = ", 4).count()
        gadq122=Survey.all().filter("clas = ",clsea).filter("q12 = ", 5).count()
        gadq123=Survey.all().filter("clas = ",clsea).filter("q12 = ", 6).count()
        gadq124=Survey.all().filter("clas = ",clsea).filter("q12 = ", 7).count()
        gadq125=Survey.all().filter("clas = ",clsea).filter("q12 = ", 8).count()
        gadq126=Survey.all().filter("clas = ",clsea).filter("q12 = ", 9).count()
        gadq127=Survey.all().filter("clas = ",clsea).filter("q12 = ", 10).count()
        
        q1_ligh = 4*gadq121 + 5*gadq122 + 6*gadq123 + 7*gadq124 + 8*gadq125 + 9*gadq126 + 10*gadq127
        q1_light = round(q1_ligh/float(sea),2)
        
        gadq131=Survey.all().filter("clas = ",clsea).filter("q13 = ", 4).count()
        gadq132=Survey.all().filter("clas = ",clsea).filter("q13 = ", 5).count()
        gadq133=Survey.all().filter("clas = ",clsea).filter("q13 = ", 6).count()
        gadq134=Survey.all().filter("clas = ",clsea).filter("q13 = ", 7).count()
        gadq135=Survey.all().filter("clas = ",clsea).filter("q13 = ", 8).count()
        gadq136=Survey.all().filter("clas = ",clsea).filter("q13 = ", 9).count()
        gadq137=Survey.all().filter("clas = ",clsea).filter("q13 = ", 10).count()
        
        q1_ac1 = 4*gadq131 + 5*gadq132 + 6*gadq133 + 7*gadq134 + 8*gadq135 + 9*gadq136 + 10*gadq137
        q1_ac = round(q1_ac1/float(sea),2)
        
        gadq141=Survey.all().filter("clas = ",clsea).filter("q14 = ", 4).count()
        gadq142=Survey.all().filter("clas = ",clsea).filter("q14 = ", 5).count()
        gadq143=Survey.all().filter("clas = ",clsea).filter("q14 = ", 6).count()
        gadq144=Survey.all().filter("clas = ",clsea).filter("q14 = ", 7).count()
        gadq145=Survey.all().filter("clas = ",clsea).filter("q14 = ", 8).count()
        gadq146=Survey.all().filter("clas = ",clsea).filter("q14 = ", 9).count()
        gadq147=Survey.all().filter("clas = ",clsea).filter("q14 = ", 10).count()
        
        q1_clean1 = 4*gadq141 + 5*gadq142 + 6*gadq143 + 7*gadq144 + 8*gadq145 + 9*gadq146 + 10*gadq147
        q1_clean = round(q1_clean1/float(sea),2)
        
        

        nbaq111=Survey.all().filter("clas = ",clsea).filter("q21 = ", 4).count()
        nbaq112=Survey.all().filter("clas = ",clsea).filter("q21 = ", 5).count()
        nbaq113=Survey.all().filter("clas = ",clsea).filter("q21 = ", 6).count()
        nbaq114=Survey.all().filter("clas = ",clsea).filter("q21 = ", 7).count()
        nbaq115=Survey.all().filter("clas = ",clsea).filter("q21 = ", 8).count()
        nbaq116=Survey.all().filter("clas = ",clsea).filter("q21 = ", 9).count()
        nbaq117=Survey.all().filter("clas = ",clsea).filter("q21 = ", 10).count()
        
        q2_ea = 4*nbaq111 + 5*nbaq112 + 6*nbaq113 + 7*nbaq114 + 8*nbaq115 + 9*nbaq116 + 10*nbaq117
        q2_eq_av = round(q2_ea/float(sea),2)
        
        nbaq121=Survey.all().filter("clas = ",clsea).filter("q22 = ", 4).count()
        nbaq122=Survey.all().filter("clas = ",clsea).filter("q22 = ", 5).count()
        nbaq123=Survey.all().filter("clas = ",clsea).filter("q22 = ", 6).count()
        nbaq124=Survey.all().filter("clas = ",clsea).filter("q22 = ", 7).count()
        nbaq125=Survey.all().filter("clas = ",clsea).filter("q22 = ", 8).count()
        nbaq126=Survey.all().filter("clas = ",clsea).filter("q22 = ", 9).count()
        nbaq127=Survey.all().filter("clas = ",clsea).filter("q22 = ", 10).count()
        
        q2_s_a1 = 4*nbaq121 + 5*nbaq122 + 6*nbaq123 + 7*nbaq124 + 8*nbaq125 + 9*nbaq126 + 10*nbaq127
        q2_s_a = round(q2_s_a1/float(sea),2)
        
        nbaq131=Survey.all().filter("clas = ",clsea).filter("q23 = ", 4).count()
        nbaq132=Survey.all().filter("clas = ",clsea).filter("q23 = ", 5).count()
        nbaq133=Survey.all().filter("clas = ",clsea).filter("q23 = ", 6).count()
        nbaq134=Survey.all().filter("clas = ",clsea).filter("q23 = ", 7).count()
        nbaq135=Survey.all().filter("clas = ",clsea).filter("q23 = ", 8).count()
        nbaq136=Survey.all().filter("clas = ",clsea).filter("q23 = ", 9).count()
        nbaq137=Survey.all().filter("clas = ",clsea).filter("q23 = ", 10).count()
        
        q2_c_a1 = 4*nbaq131 + 5*nbaq132 + 6*nbaq133 + 7*nbaq134 + 8*nbaq135 + 9*nbaq136 + 10*nbaq137 
        q2_c_a = round(q2_c_a1/float(sea),2)
        
        nbaq141=Survey.all().filter("clas = ",clsea).filter("q24 = ", 4).count()
        nbaq142=Survey.all().filter("clas = ",clsea).filter("q24 = ", 5).count()
        nbaq143=Survey.all().filter("clas = ",clsea).filter("q24 = ", 6).count()
        nbaq144=Survey.all().filter("clas = ",clsea).filter("q24 = ", 7).count()
        nbaq145=Survey.all().filter("clas = ",clsea).filter("q24 = ", 8).count()
        nbaq146=Survey.all().filter("clas = ",clsea).filter("q24 = ", 9).count()
        nbaq147=Survey.all().filter("clas = ",clsea).filter("q24 = ", 10).count()
        
        q2_l_m1 = 4*nbaq141 + 5*nbaq142 + 6*nbaq143 + 7*nbaq144 + 8*nbaq145 + 9*nbaq146 + 10*nbaq147 
        q2_l_m = round(q2_l_m1/float(sea),2)
        
        nbaq151=Survey.all().filter("clas = ",clsea).filter("q25 = ", 4).count()
        nbaq152=Survey.all().filter("clas = ",clsea).filter("q25 = ", 5).count()
        nbaq153=Survey.all().filter("clas = ",clsea).filter("q25 = ", 6).count()
        nbaq154=Survey.all().filter("clas = ",clsea).filter("q25 = ", 7).count()
        nbaq155=Survey.all().filter("clas = ",clsea).filter("q25 = ", 8).count()
        nbaq156=Survey.all().filter("clas = ",clsea).filter("q25 = ", 9).count()
        nbaq157=Survey.all().filter("clas = ",clsea).filter("q25 = ", 10).count()
        
        q2_i_c1 = 4*nbaq151 + 5*nbaq152 + 6*nbaq153 + 7*nbaq154 + 8*nbaq155 + 9*nbaq156 + 10*nbaq157
        q2_i_c = round(q2_i_c1/float(sea),2) 
            
        nbaq161=Survey.all().filter("clas = ",clsea).filter("q26 = ", 4).count()
        nbaq162=Survey.all().filter("clas = ",clsea).filter("q26 = ", 5).count()
        nbaq163=Survey.all().filter("clas = ",clsea).filter("q26 = ", 6).count()
        nbaq164=Survey.all().filter("clas = ",clsea).filter("q26 = ", 7).count()
        nbaq165=Survey.all().filter("clas = ",clsea).filter("q26 = ", 8).count()
        nbaq166=Survey.all().filter("clas = ",clsea).filter("q26 = ", 9).count()
        nbaq167=Survey.all().filter("clas = ",clsea).filter("q26 = ", 10).count()
        
        q2_b_s1 = 4*nbaq161 + 5*nbaq162 + 6*nbaq163 + 7*nbaq164 + 8*nbaq165 + 9*nbaq166 + 10*nbaq167
        q2_b_s = round(q2_b_s1/float(sea),2)

        soeie111=Survey.all().filter("clas = ",clsea).filter("q31 = ", 4).count()
        soeie112=Survey.all().filter("clas = ",clsea).filter("q31 = ", 5).count()
        soeie113=Survey.all().filter("clas = ",clsea).filter("q31 = ", 6).count()
        soeie114=Survey.all().filter("clas = ",clsea).filter("q31 = ", 7).count()
        soeie115=Survey.all().filter("clas = ",clsea).filter("q31 = ", 8).count()
        soeie116=Survey.all().filter("clas = ",clsea).filter("q31 = ", 9).count()
        soeie117=Survey.all().filter("clas = ",clsea).filter("q31 = ", 10).count()
        
        q3_li = 4*soeie111 + 5*soeie112 + 6*soeie113 + 7*soeie114 + 8*soeie115 + 9*soeie116 + 10*soeie117
        q3_lib = round(q3_li/float(sea),2)
        
        soeie121=Survey.all().filter("clas = ",clsea).filter("q32 = ", 4).count()
        soeie122=Survey.all().filter("clas = ",clsea).filter("q32 = ", 5).count()
        soeie123=Survey.all().filter("clas = ",clsea).filter("q32 = ", 6).count()
        soeie124=Survey.all().filter("clas = ",clsea).filter("q32 = ", 7).count()
        soeie125=Survey.all().filter("clas = ",clsea).filter("q32 = ", 8).count()
        soeie126=Survey.all().filter("clas = ",clsea).filter("q32 = ", 9).count()
        soeie127=Survey.all().filter("clas = ",clsea).filter("q32 = ", 10).count()
        
        q3_i_s1 = 4*soeie121 + 5*soeie122 + 6*soeie123 + 7*soeie124 + 8*soeie125 + 9*soeie126 + 10*soeie127
        q3_i_s = round(q3_i_s1/float(sea),2)
        
        soeie131=Survey.all().filter("clas = ",clsea).filter("q33 = ", 4).count()
        soeie132=Survey.all().filter("clas = ",clsea).filter("q33 = ", 5).count()
        soeie133=Survey.all().filter("clas = ",clsea).filter("q33 = ", 6).count()
        soeie134=Survey.all().filter("clas = ",clsea).filter("q33 = ", 7).count()
        soeie135=Survey.all().filter("clas = ",clsea).filter("q33 = ", 8).count()
        soeie136=Survey.all().filter("clas = ",clsea).filter("q33 = ", 9).count()
        soeie137=Survey.all().filter("clas = ",clsea).filter("q33 = ", 10).count()
        
        q3_con_bo1 = 4*soeie131 + 5*soeie132 + 6*soeie133 + 7*soeie134 + 8*soeie135 + 9*soeie136 + 10*soeie137 
        q3_con_bo = round(q3_con_bo1/float(sea),2)
        
        soeie141=Survey.all().filter("clas = ",clsea).filter("q34 = ", 4).count()
        soeie142=Survey.all().filter("clas = ",clsea).filter("q34 = ", 5).count()
        soeie143=Survey.all().filter("clas = ",clsea).filter("q34 = ", 6).count()
        soeie144=Survey.all().filter("clas = ",clsea).filter("q34 = ", 7).count()
        soeie145=Survey.all().filter("clas = ",clsea).filter("q34 = ", 8).count()
        soeie146=Survey.all().filter("clas = ",clsea).filter("q34 = ", 9).count()
        soeie147=Survey.all().filter("clas = ",clsea).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1 = 4*soeie141 + 5*soeie142 + 6*soeie143 + 7*soeie144 + 8*soeie145 + 9*soeie146 + 10*soeie147 
        q3_av_ne_ver = round(q3_av_ne_ver1/float(sea),2)
        
        soeie151=Survey.all().filter("clas = ",clsea).filter("q35 = ", 4).count()
        soeie152=Survey.all().filter("clas = ",clsea).filter("q35 = ", 5).count()
        soeie153=Survey.all().filter("clas = ",clsea).filter("q35 = ", 6).count()
        soeie154=Survey.all().filter("clas = ",clsea).filter("q35 = ", 7).count()
        soeie155=Survey.all().filter("clas = ",clsea).filter("q35 = ", 8).count()
        soeie156=Survey.all().filter("clas = ",clsea).filter("q35 = ", 9).count()
        soeie157=Survey.all().filter("clas = ",clsea).filter("q35 = ", 10).count()
        
        q3_re_ro1 = 4*soeie151 + 5*soeie152 + 6*soeie153 + 7*soeie154 + 8*soeie155 + 9*soeie156 + 10*soeie157
        q3_re_ro = round(q3_re_ro1/float(sea),2)
            
        soeie161=Survey.all().filter("clas = ",clsea).filter("q36 = ", 4).count()
        soeie162=Survey.all().filter("clas = ",clsea).filter("q36 = ", 5).count()
        soeie163=Survey.all().filter("clas = ",clsea).filter("q36 = ", 6).count()
        soeie164=Survey.all().filter("clas = ",clsea).filter("q36 = ", 7).count()
        soeie165=Survey.all().filter("clas = ",clsea).filter("q36 = ", 8).count()
        soeie166=Survey.all().filter("clas = ",clsea).filter("q36 = ", 9).count()
        soeie167=Survey.all().filter("clas = ",clsea).filter("q36 = ", 10).count()
        
        q3_j_m1 = 4*soeie161 + 5*soeie162 + 6*soeie163 + 7*soeie164 + 8*soeie165 + 9*soeie166 + 10*soeie167
        q3_j_m = round(q3_j_m1/float(sea),2)
            
        soeie171=Survey.all().filter("clas = ",clsea).filter("q37 = ", 4).count()
        soeie172=Survey.all().filter("clas = ",clsea).filter("q37 = ", 5).count()
        soeie173=Survey.all().filter("clas = ",clsea).filter("q37 = ", 6).count()
        soeie174=Survey.all().filter("clas = ",clsea).filter("q37 = ", 7).count()
        soeie175=Survey.all().filter("clas = ",clsea).filter("q37 = ", 8).count()
        soeie176=Survey.all().filter("clas = ",clsea).filter("q37 = ", 9).count()
        soeie177=Survey.all().filter("clas = ",clsea).filter("q37 = ", 10).count()
        
        q3_sta1 = 4*soeie171 + 5*soeie172 + 6*soeie173 + 7*soeie174 + 8*soeie175 + 9*soeie176 + 10*soeie177
        q3_sta = round(q3_sta1/float(sea),2)

        obmd111=Survey.all().filter("clas = ",clsea).filter("q41 = ", 4).count()
        obmd112=Survey.all().filter("clas = ",clsea).filter("q41 = ", 5).count()
        obmd113=Survey.all().filter("clas = ",clsea).filter("q41 = ", 6).count()
        obmd114=Survey.all().filter("clas = ",clsea).filter("q41 = ", 7).count()
        obmd115=Survey.all().filter("clas = ",clsea).filter("q41 = ", 8).count()
        obmd116=Survey.all().filter("clas = ",clsea).filter("q41 = ", 9).count()
        obmd117=Survey.all().filter("clas = ",clsea).filter("q41 = ", 10).count()
        
        q4_h = 4*obmd111 + 5*obmd112 + 6*obmd113 + 7*obmd114 + 8*obmd115 + 9*obmd116 + 10*obmd117
        q4_hy_cl = round(q4_h/float(sea),2)
        
        obmd121=Survey.all().filter("clas = ",clsea).filter("q42 = ", 4).count()
        obmd122=Survey.all().filter("clas = ",clsea).filter("q42 = ", 5).count()
        obmd123=Survey.all().filter("clas = ",clsea).filter("q42 = ", 6).count()
        obmd124=Survey.all().filter("clas = ",clsea).filter("q42 = ", 7).count()
        obmd125=Survey.all().filter("clas = ",clsea).filter("q42 = ", 8).count()
        obmd126=Survey.all().filter("clas = ",clsea).filter("q42 = ", 9).count()
        obmd127=Survey.all().filter("clas = ",clsea).filter("q42 = ", 10).count()
        
        q4_men1 = 4*obmd121 + 5*obmd122 + 6*obmd123 + 7*obmd124 + 8*obmd125 + 9*obmd126 + 10*obmd127
        q4_men = round(q4_men1/float(sea),2)
        
        obmd131=Survey.all().filter("clas = ",clsea).filter("q43 = ", 4).count()
        obmd132=Survey.all().filter("clas = ",clsea).filter("q43 = ", 5).count()
        obmd133=Survey.all().filter("clas = ",clsea).filter("q43 = ", 6).count()
        obmd134=Survey.all().filter("clas = ",clsea).filter("q43 = ", 7).count()
        obmd135=Survey.all().filter("clas = ",clsea).filter("q43 = ", 8).count()
        obmd136=Survey.all().filter("clas = ",clsea).filter("q43 = ", 9).count()
        obmd137=Survey.all().filter("clas = ",clsea).filter("q43 = ", 10).count()
        
        q4_pri1 = 4*obmd131 + 5*obmd132 + 6*obmd133 + 7*obmd134 + 8*obmd135 + 9*obmd136 + 10*obmd137
        q4_pri = round(q4_pri1/float(sea),2)
        
        obmd141=Survey.all().filter("clas = ",clsea).filter("q44 = ", 4).count()
        obmd142=Survey.all().filter("clas = ",clsea).filter("q44 = ", 5).count()
        obmd143=Survey.all().filter("clas = ",clsea).filter("q44 = ", 6).count()
        obmd144=Survey.all().filter("clas = ",clsea).filter("q44 = ", 7).count()
        obmd145=Survey.all().filter("clas = ",clsea).filter("q44 = ", 8).count()
        obmd146=Survey.all().filter("clas = ",clsea).filter("q44 = ", 9).count()
        obmd147=Survey.all().filter("clas = ",clsea).filter("q44 = ", 10).count()
        
        q4_tim_del1 = 4*obmd141 + 5*obmd142 + 6*obmd143 + 7*obmd144 + 8*obmd145 + 9*obmd146 + 10*obmd147
        q4_tim_del = round(q4_tim_del1/float(sea),2)
        
        obmd151=Survey.all().filter("clas = ",clsea).filter("q45 = ", 4).count()
        obmd152=Survey.all().filter("clas = ",clsea).filter("q45 = ", 5).count()
        obmd153=Survey.all().filter("clas = ",clsea).filter("q45 = ", 6).count()
        obmd154=Survey.all().filter("clas = ",clsea).filter("q45 = ", 7).count()
        obmd155=Survey.all().filter("clas = ",clsea).filter("q45 = ", 8).count()
        obmd156=Survey.all().filter("clas = ",clsea).filter("q45 = ", 9).count()
        obmd157=Survey.all().filter("clas = ",clsea).filter("q45 = ", 10).count()
        
        q4_ser_qua1 = 4*obmd151 + 5*obmd152 + 6*obmd153 + 7*obmd154 + 8*obmd155 + 9*obmd156 + 10*obmd157
        q4_ser_qua = round(q4_ser_qua1/float(sea),2)

        obhod111=Survey.all().filter("clas = ",clsea).filter("q51 = ", 4).count()
        obhod112=Survey.all().filter("clas = ",clsea).filter("q51 = ", 5).count()
        obhod113=Survey.all().filter("clas = ",clsea).filter("q51 = ", 6).count()
        obhod114=Survey.all().filter("clas = ",clsea).filter("q51 = ", 7).count()
        obhod115=Survey.all().filter("clas = ",clsea).filter("q51 = ", 8).count()
        obhod116=Survey.all().filter("clas = ",clsea).filter("q51 = ", 9).count()
        obhod117=Survey.all().filter("clas = ",clsea).filter("q51 = ", 10).count()
        
        q5_re = 4*obhod111 + 5*obhod112 + 6*obhod113 + 7*obhod114 + 8*obhod115 + 9*obhod116 + 10*obhod117
        q5_res_ad = round(q5_re/float(sea),2)
        
        obhod121=Survey.all().filter("clas = ",clsea).filter("q52 = ", 4).count()
        obhod122=Survey.all().filter("clas = ",clsea).filter("q52 = ", 5).count()
        obhod123=Survey.all().filter("clas = ",clsea).filter("q52 = ", 6).count()
        obhod124=Survey.all().filter("clas = ",clsea).filter("q52 = ", 7).count()
        obhod125=Survey.all().filter("clas = ",clsea).filter("q52 = ", 8).count()
        obhod126=Survey.all().filter("clas = ",clsea).filter("q52 = ", 9).count()
        obhod127=Survey.all().filter("clas = ",clsea).filter("q52 = ", 10).count()
        
        q5_aud1 = 4*obhod121 + 5*obhod122 + 6*obhod123 + 7*obhod124 + 8*obhod125 + 9*obhod126 + 10*obhod127
        q5_aud = round(q5_aud1/float(sea),2)
        
        obhod131=Survey.all().filter("clas = ",clsea).filter("q53 = ", 4).count()
        obhod132=Survey.all().filter("clas = ",clsea).filter("q53 = ", 5).count()
        obhod133=Survey.all().filter("clas = ",clsea).filter("q53 = ", 6).count()
        obhod134=Survey.all().filter("clas = ",clsea).filter("q53 = ", 7).count()
        obhod135=Survey.all().filter("clas = ",clsea).filter("q53 = ", 8).count()
        obhod136=Survey.all().filter("clas = ",clsea).filter("q53 = ", 9).count()
        obhod137=Survey.all().filter("clas = ",clsea).filter("q53 = ", 10).count()
        
        q5_gam1 = 4*obhod131 + 5*obhod132 + 6*obhod133 + 7*obhod134 + 8*obhod135 + 9*obhod136 + 10*obhod137 
        q5_gam = round(q5_gam1/float(sea),2)
        
        obhod141=Survey.all().filter("clas = ",clsea).filter("q54 = ", 4).count()
        obhod142=Survey.all().filter("clas = ",clsea).filter("q54 = ", 5).count()
        obhod143=Survey.all().filter("clas = ",clsea).filter("q54 = ", 6).count()
        obhod144=Survey.all().filter("clas = ",clsea).filter("q54 = ", 7).count()
        obhod145=Survey.all().filter("clas = ",clsea).filter("q54 = ", 8).count()
        obhod146=Survey.all().filter("clas = ",clsea).filter("q54 = ", 9).count()
        obhod147=Survey.all().filter("clas = ",clsea).filter("q54 = ", 10).count()
        
        q5_info1 = 4*obhod141 + 5*obhod142 + 6*obhod143 + 7*obhod144 + 8*obhod145 + 9*obhod146 + 10*obhod147 
        q5_info = round(q5_info1/float(sea),2)
        
        obhod151=Survey.all().filter("clas = ",clsea).filter("q55 = ", 4).count()
        obhod152=Survey.all().filter("clas = ",clsea).filter("q55 = ", 5).count()
        obhod153=Survey.all().filter("clas = ",clsea).filter("q55 = ", 6).count()
        obhod154=Survey.all().filter("clas = ",clsea).filter("q55 = ", 7).count()
        obhod155=Survey.all().filter("clas = ",clsea).filter("q55 = ", 8).count()
        obhod156=Survey.all().filter("clas = ",clsea).filter("q55 = ", 9).count()
        obhod157=Survey.all().filter("clas = ",clsea).filter("q55 = ", 10).count()
        
        q5_dr1 = 4*obhod151 + 5*obhod152 + 6*obhod153 + 7*obhod154 + 8*obhod155 + 9*obhod156 + 10*obhod157
        q5_dr = round(q5_dr1/float(sea),2)

        obhod161=Survey.all().filter("clas = ",clsea).filter("q56 = ", 4).count()
        obhod162=Survey.all().filter("clas = ",clsea).filter("q56 = ", 5).count()
        obhod163=Survey.all().filter("clas = ",clsea).filter("q56 = ", 6).count()
        obhod164=Survey.all().filter("clas = ",clsea).filter("q56 = ", 7).count()
        obhod165=Survey.all().filter("clas = ",clsea).filter("q56 = ", 8).count()
        obhod166=Survey.all().filter("clas = ",clsea).filter("q56 = ", 9).count()
        obhod167=Survey.all().filter("clas = ",clsea).filter("q56 = ", 10).count()
        
        q5_toi1 = 4*obhod161 + 5*obhod162 + 6*obhod163 + 7*obhod164 + 8*obhod165 + 9*obhod166 + 10*obhod167
        q5_toi = round(q5_toi1/float(sea),2)
        
        obhod171=Survey.all().filter("clas = ",clsea).filter("q57 = ", 4).count()
        obhod172=Survey.all().filter("clas = ",clsea).filter("q57 = ", 5).count()
        obhod173=Survey.all().filter("clas = ",clsea).filter("q57 = ", 6).count()
        obhod174=Survey.all().filter("clas = ",clsea).filter("q57 = ", 7).count()
        obhod175=Survey.all().filter("clas = ",clsea).filter("q57 = ", 8).count()
        obhod176=Survey.all().filter("clas = ",clsea).filter("q57 = ", 9).count()
        obhod177=Survey.all().filter("clas = ",clsea).filter("q57 = ", 10).count()
        
        q5_clean1 = 4*obhod171 + 5*obhod172 + 6*obhod173 + 7*obhod174 + 8*obhod175 + 9*obhod176 + 10*obhod177
        q5_clean = round(q5_clean1/float(sea),2)
        
        obhod181=Survey.all().filter("clas = ",clsea).filter("q58 = ", 4).count()
        obhod182=Survey.all().filter("clas = ",clsea).filter("q58 = ", 5).count()
        obhod183=Survey.all().filter("clas = ",clsea).filter("q58 = ", 6).count()
        obhod184=Survey.all().filter("clas = ",clsea).filter("q58 = ", 7).count()
        obhod185=Survey.all().filter("clas = ",clsea).filter("q58 = ", 8).count()
        obhod186=Survey.all().filter("clas = ",clsea).filter("q58 = ", 9).count()
        obhod187=Survey.all().filter("clas = ",clsea).filter("q58 = ", 10).count()
        
        q5_mai1 = 4*obhod181 + 5*obhod182 + 6*obhod183 + 7*obhod184 + 8*obhod185 + 9*obhod186 + 10*obhod187
        q5_mai = round(q5_mai1/float(sea),2)


        total_se = q5_mai + q5_clean + q5_toi + q5_dr + q5_info + q5_gam + q5_aud + q1_condff + q1_light + q1_ac + q1_clean + q2_eq_av + q2_s_a + q2_c_a + q2_l_m + q2_i_c + q2_b_s + q3_lib + q3_i_s + q3_con_bo + q3_av_ne_ver + q3_re_ro + q3_j_m + q3_sta + q4_hy_cl + q4_men + q4_pri + q4_tim_del + q4_ser_qua + q5_res_ad      
        total_sea = round(total_se,2)
        per_sea = round(10*total_sea/float(30.0),2)

        #SE-B

        clseb = "SE-B"
        seb=Survey.all().filter("clas = ",clseb).count()
        
        gadqseb111=Survey.all().filter("clas = ",clseb).filter("q11 = ", 4).count()
        gadqseb112=Survey.all().filter("clas = ",clseb).filter("q11 = ", 5).count()
        gadqseb113=Survey.all().filter("clas = ",clseb).filter("q11 = ", 6).count()
        gadqseb114=Survey.all().filter("clas = ",clseb).filter("q11 = ", 7).count()
        gadqseb115=Survey.all().filter("clas = ",clseb).filter("q11 = ", 8).count()
        gadqseb116=Survey.all().filter("clas = ",clseb).filter("q11 = ", 9).count()
        gadqseb117=Survey.all().filter("clas = ",clseb).filter("q11 = ", 10).count()
        
        q1_condse = 4*gadqseb111 + 5*gadqseb112 + 6*gadqseb113 + 7*gadqseb114 + 8*gadqseb115 + 9*gadqseb116 + 10*gadqseb117
        q1_condffseb = round(q1_condse/float(seb),2)
        
        gadqseb121=Survey.all().filter("clas = ",clseb).filter("q12 = ", 4).count()
        gadqseb122=Survey.all().filter("clas = ",clseb).filter("q12 = ", 5).count()
        gadqseb123=Survey.all().filter("clas = ",clseb).filter("q12 = ", 6).count()
        gadqseb124=Survey.all().filter("clas = ",clseb).filter("q12 = ", 7).count()
        gadqseb125=Survey.all().filter("clas = ",clseb).filter("q12 = ", 8).count()
        gadqseb126=Survey.all().filter("clas = ",clseb).filter("q12 = ", 9).count()
        gadqseb127=Survey.all().filter("clas = ",clseb).filter("q12 = ", 10).count()
        
        q1_lighse = 4*gadqseb121 + 5*gadqseb122 + 6*gadqseb123 + 7*gadqseb124 + 8*gadqseb125 + 9*gadqseb126 + 10*gadqseb127
        q1_lightseb = round(q1_lighse/float(seb),2)
        
        gadqseb131=Survey.all().filter("clas = ",clseb).filter("q13 = ", 4).count()
        gadqseb132=Survey.all().filter("clas = ",clseb).filter("q13 = ", 5).count()
        gadqseb133=Survey.all().filter("clas = ",clseb).filter("q13 = ", 6).count()
        gadqseb134=Survey.all().filter("clas = ",clseb).filter("q13 = ", 7).count()
        gadqseb135=Survey.all().filter("clas = ",clseb).filter("q13 = ", 8).count()
        gadqseb136=Survey.all().filter("clas = ",clseb).filter("q13 = ", 9).count()
        gadqseb137=Survey.all().filter("clas = ",clseb).filter("q13 = ", 10).count()
        
        q1_ac1se = 4*gadqseb131 + 5*gadqseb132 + 6*gadqseb133 + 7*gadqseb134 + 8*gadqseb135 + 9*gadqseb136 + 10*gadqseb137
        q1_acseb = round(q1_ac1se/float(seb),2)
        
        gadqseb141=Survey.all().filter("clas = ",clseb).filter("q14 = ", 4).count()
        gadqseb142=Survey.all().filter("clas = ",clseb).filter("q14 = ", 5).count()
        gadqseb143=Survey.all().filter("clas = ",clseb).filter("q14 = ", 6).count()
        gadqseb144=Survey.all().filter("clas = ",clseb).filter("q14 = ", 7).count()
        gadqseb145=Survey.all().filter("clas = ",clseb).filter("q14 = ", 8).count()
        gadqseb146=Survey.all().filter("clas = ",clseb).filter("q14 = ", 9).count()
        gadqseb147=Survey.all().filter("clas = ",clseb).filter("q14 = ", 10).count()
        
        q1_clean1se = 4*gadqseb141 + 5*gadqseb142 + 6*gadqseb143 + 7*gadqseb144 + 8*gadqseb145 + 9*gadqseb146 + 10*gadqseb147
        q1_cleanseb = round(q1_clean1se/float(seb),2)
        
        

        nbaqseb111=Survey.all().filter("clas = ",clseb).filter("q21 = ", 4).count()
        nbaqseb112=Survey.all().filter("clas = ",clseb).filter("q21 = ", 5).count()
        nbaqseb113=Survey.all().filter("clas = ",clseb).filter("q21 = ", 6).count()
        nbaqseb114=Survey.all().filter("clas = ",clseb).filter("q21 = ", 7).count()
        nbaqseb115=Survey.all().filter("clas = ",clseb).filter("q21 = ", 8).count()
        nbaqseb116=Survey.all().filter("clas = ",clseb).filter("q21 = ", 9).count()
        nbaqseb117=Survey.all().filter("clas = ",clseb).filter("q21 = ", 10).count()
        
        q2_ease = 4*nbaqseb111 + 5*nbaqseb112 + 6*nbaqseb113 + 7*nbaqseb114 + 8*nbaqseb115 + 9*nbaqseb116 + 10*nbaqseb117
        q2_eq_avseb = round(q2_ease/float(seb),2)
        
        nbaqseb121=Survey.all().filter("clas = ",clseb).filter("q22 = ", 4).count()
        nbaqseb122=Survey.all().filter("clas = ",clseb).filter("q22 = ", 5).count()
        nbaqseb123=Survey.all().filter("clas = ",clseb).filter("q22 = ", 6).count()
        nbaqseb124=Survey.all().filter("clas = ",clseb).filter("q22 = ", 7).count()
        nbaqseb125=Survey.all().filter("clas = ",clseb).filter("q22 = ", 8).count()
        nbaqseb126=Survey.all().filter("clas = ",clseb).filter("q22 = ", 9).count()
        nbaqseb127=Survey.all().filter("clas = ",clseb).filter("q22 = ", 10).count()
        
        q2_s_a1se = 4*nbaqseb121 + 5*nbaqseb122 + 6*nbaqseb123 + 7*nbaqseb124 + 8*nbaqseb125 + 9*nbaqseb126 + 10*nbaqseb127
        q2_s_aseb = round(q2_s_a1se/float(seb),2)
        
        nbaqseb131=Survey.all().filter("clas = ",clseb).filter("q23 = ", 4).count()
        nbaqseb132=Survey.all().filter("clas = ",clseb).filter("q23 = ", 5).count()
        nbaqseb133=Survey.all().filter("clas = ",clseb).filter("q23 = ", 6).count()
        nbaqseb134=Survey.all().filter("clas = ",clseb).filter("q23 = ", 7).count()
        nbaqseb135=Survey.all().filter("clas = ",clseb).filter("q23 = ", 8).count()
        nbaqseb136=Survey.all().filter("clas = ",clseb).filter("q23 = ", 9).count()
        nbaqseb137=Survey.all().filter("clas = ",clseb).filter("q23 = ", 10).count()
        
        q2_c_a1se = 4*nbaqseb131 + 5*nbaqseb132 + 6*nbaqseb133 + 7*nbaqseb134 + 8*nbaqseb135 + 9*nbaqseb136 + 10*nbaqseb137 
        q2_c_aseb = round(q2_c_a1se/float(seb),2)
        
        nbaqseb141=Survey.all().filter("clas = ",clseb).filter("q24 = ", 4).count()
        nbaqseb142=Survey.all().filter("clas = ",clseb).filter("q24 = ", 5).count()
        nbaqseb143=Survey.all().filter("clas = ",clseb).filter("q24 = ", 6).count()
        nbaqseb144=Survey.all().filter("clas = ",clseb).filter("q24 = ", 7).count()
        nbaqseb145=Survey.all().filter("clas = ",clseb).filter("q24 = ", 8).count()
        nbaqseb146=Survey.all().filter("clas = ",clseb).filter("q24 = ", 9).count()
        nbaqseb147=Survey.all().filter("clas = ",clseb).filter("q24 = ", 10).count()
        
        q2_l_m1se = 4*nbaqseb141 + 5*nbaqseb142 + 6*nbaqseb143 + 7*nbaqseb144 + 8*nbaqseb145 + 9*nbaqseb146 + 10*nbaqseb147 
        q2_l_mseb = round(q2_l_m1se/float(seb),2)
        
        nbaqseb151=Survey.all().filter("clas = ",clseb).filter("q25 = ", 4).count()
        nbaqseb152=Survey.all().filter("clas = ",clseb).filter("q25 = ", 5).count()
        nbaqseb153=Survey.all().filter("clas = ",clseb).filter("q25 = ", 6).count()
        nbaqseb154=Survey.all().filter("clas = ",clseb).filter("q25 = ", 7).count()
        nbaqseb155=Survey.all().filter("clas = ",clseb).filter("q25 = ", 8).count()
        nbaqseb156=Survey.all().filter("clas = ",clseb).filter("q25 = ", 9).count()
        nbaqseb157=Survey.all().filter("clas = ",clseb).filter("q25 = ", 10).count()
        
        q2_i_c1se = 4*nbaqseb151 + 5*nbaqseb152 + 6*nbaqseb153 + 7*nbaqseb154 + 8*nbaqseb155 + 9*nbaqseb156 + 10*nbaqseb157
        q2_i_cseb = round(q2_i_c1se/float(seb),2) 
            
        nbaqseb161=Survey.all().filter("clas = ",clseb).filter("q26 = ", 4).count()
        nbaqseb162=Survey.all().filter("clas = ",clseb).filter("q26 = ", 5).count()
        nbaqseb163=Survey.all().filter("clas = ",clseb).filter("q26 = ", 6).count()
        nbaqseb164=Survey.all().filter("clas = ",clseb).filter("q26 = ", 7).count()
        nbaqseb165=Survey.all().filter("clas = ",clseb).filter("q26 = ", 8).count()
        nbaqseb166=Survey.all().filter("clas = ",clseb).filter("q26 = ", 9).count()
        nbaqseb167=Survey.all().filter("clas = ",clseb).filter("q26 = ", 10).count()
        
        q2_b_s1se = 4*nbaqseb161 + 5*nbaqseb162 + 6*nbaqseb163 + 7*nbaqseb164 + 8*nbaqseb165 + 9*nbaqseb166 + 10*nbaqseb167
        q2_b_sseb = round(q2_b_s1se/float(seb),2)

        soeieseb111=Survey.all().filter("clas = ",clseb).filter("q31 = ", 4).count()
        soeieseb112=Survey.all().filter("clas = ",clseb).filter("q31 = ", 5).count()
        soeieseb113=Survey.all().filter("clas = ",clseb).filter("q31 = ", 6).count()
        soeieseb114=Survey.all().filter("clas = ",clseb).filter("q31 = ", 7).count()
        soeieseb115=Survey.all().filter("clas = ",clseb).filter("q31 = ", 8).count()
        soeieseb116=Survey.all().filter("clas = ",clseb).filter("q31 = ", 9).count()
        soeieseb117=Survey.all().filter("clas = ",clseb).filter("q31 = ", 10).count()
        
        q3_lise = 4*soeieseb111 + 5*soeieseb112 + 6*soeieseb113 + 7*soeieseb114 + 8*soeieseb115 + 9*soeieseb116 + 10*soeieseb117
        q3_libseb = round(q3_lise/float(seb),2)
        
        soeieseb121=Survey.all().filter("clas = ",clseb).filter("q32 = ", 4).count()
        soeieseb122=Survey.all().filter("clas = ",clseb).filter("q32 = ", 5).count()
        soeieseb123=Survey.all().filter("clas = ",clseb).filter("q32 = ", 6).count()
        soeieseb124=Survey.all().filter("clas = ",clseb).filter("q32 = ", 7).count()
        soeieseb125=Survey.all().filter("clas = ",clseb).filter("q32 = ", 8).count()
        soeieseb126=Survey.all().filter("clas = ",clseb).filter("q32 = ", 9).count()
        soeieseb127=Survey.all().filter("clas = ",clseb).filter("q32 = ", 10).count()
        
        q3_i_s1se = 4*soeieseb121 + 5*soeieseb122 + 6*soeieseb123 + 7*soeieseb124 + 8*soeieseb125 + 9*soeieseb126 + 10*soeieseb127
        q3_i_sseb = round(q3_i_s1se/float(seb),2)
        
        soeieseb131=Survey.all().filter("clas = ",clseb).filter("q33 = ", 4).count()
        soeieseb132=Survey.all().filter("clas = ",clseb).filter("q33 = ", 5).count()
        soeieseb133=Survey.all().filter("clas = ",clseb).filter("q33 = ", 6).count()
        soeieseb134=Survey.all().filter("clas = ",clseb).filter("q33 = ", 7).count()
        soeieseb135=Survey.all().filter("clas = ",clseb).filter("q33 = ", 8).count()
        soeieseb136=Survey.all().filter("clas = ",clseb).filter("q33 = ", 9).count()
        soeieseb137=Survey.all().filter("clas = ",clseb).filter("q33 = ", 10).count()
        
        q3_con_bo1se = 4*soeieseb131 + 5*soeieseb132 + 6*soeieseb133 + 7*soeieseb134 + 8*soeieseb135 + 9*soeieseb136 + 10*soeieseb137 
        q3_con_boseb = round(q3_con_bo1se/float(seb),2)
        
        soeieseb141=Survey.all().filter("clas = ",clseb).filter("q34 = ", 4).count()
        soeieseb142=Survey.all().filter("clas = ",clseb).filter("q34 = ", 5).count()
        soeieseb143=Survey.all().filter("clas = ",clseb).filter("q34 = ", 6).count()
        soeieseb144=Survey.all().filter("clas = ",clseb).filter("q34 = ", 7).count()
        soeieseb145=Survey.all().filter("clas = ",clseb).filter("q34 = ", 8).count()
        soeieseb146=Survey.all().filter("clas = ",clseb).filter("q34 = ", 9).count()
        soeieseb147=Survey.all().filter("clas = ",clseb).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1se = 4*soeieseb141 + 5*soeieseb142 + 6*soeieseb143 + 7*soeieseb144 + 8*soeieseb145 + 9*soeieseb146 + 10*soeieseb147 
        q3_av_ne_verseb =round(q3_av_ne_ver1se/float(seb),2)
        
        soeieseb151=Survey.all().filter("clas = ",clseb).filter("q35 = ", 4).count()
        soeieseb152=Survey.all().filter("clas = ",clseb).filter("q35 = ", 5).count()
        soeieseb153=Survey.all().filter("clas = ",clseb).filter("q35 = ", 6).count()
        soeieseb154=Survey.all().filter("clas = ",clseb).filter("q35 = ", 7).count()
        soeieseb155=Survey.all().filter("clas = ",clseb).filter("q35 = ", 8).count()
        soeieseb156=Survey.all().filter("clas = ",clseb).filter("q35 = ", 9).count()
        soeieseb157=Survey.all().filter("clas = ",clseb).filter("q35 = ", 10).count()
        
        q3_re_ro1se = 4*soeieseb151 + 5*soeieseb152 + 6*soeieseb153 + 7*soeieseb154 + 8*soeieseb155 + 9*soeieseb156 + 10*soeieseb157
        q3_re_roseb = round(q3_re_ro1se/float(seb),2)
            
        soeieseb161=Survey.all().filter("clas = ",clseb).filter("q36 = ", 4).count()
        soeieseb162=Survey.all().filter("clas = ",clseb).filter("q36 = ", 5).count()
        soeieseb163=Survey.all().filter("clas = ",clseb).filter("q36 = ", 6).count()
        soeieseb164=Survey.all().filter("clas = ",clseb).filter("q36 = ", 7).count()
        soeieseb165=Survey.all().filter("clas = ",clseb).filter("q36 = ", 8).count()
        soeieseb166=Survey.all().filter("clas = ",clseb).filter("q36 = ", 9).count()
        soeieseb167=Survey.all().filter("clas = ",clseb).filter("q36 = ", 10).count()
        
        q3_j_m1se = 4*soeieseb161 + 5*soeieseb162 + 6*soeieseb163 + 7*soeieseb164 + 8*soeieseb165 + 9*soeieseb166 + 10*soeieseb167
        q3_j_mseb = round(q3_j_m1se/float(seb),2)
            
        soeieseb171=Survey.all().filter("clas = ",clseb).filter("q37 = ", 4).count()
        soeieseb172=Survey.all().filter("clas = ",clseb).filter("q37 = ", 5).count()
        soeieseb173=Survey.all().filter("clas = ",clseb).filter("q37 = ", 6).count()
        soeieseb174=Survey.all().filter("clas = ",clseb).filter("q37 = ", 7).count()
        soeieseb175=Survey.all().filter("clas = ",clseb).filter("q37 = ", 8).count()
        soeieseb176=Survey.all().filter("clas = ",clseb).filter("q37 = ", 9).count()
        soeieseb177=Survey.all().filter("clas = ",clseb).filter("q37 = ", 10).count()
        
        q3_sta1se = 4*soeieseb171 + 5*soeieseb172 + 6*soeieseb173 + 7*soeieseb174 + 8*soeieseb175 + 9*soeieseb176 + 10*soeieseb177
        q3_staseb = round(q3_sta1se/float(seb),2)

        obmdseb111=Survey.all().filter("clas = ",clseb).filter("q41 = ", 4).count()
        obmdseb112=Survey.all().filter("clas = ",clseb).filter("q41 = ", 5).count()
        obmdseb113=Survey.all().filter("clas = ",clseb).filter("q41 = ", 6).count()
        obmdseb114=Survey.all().filter("clas = ",clseb).filter("q41 = ", 7).count()
        obmdseb115=Survey.all().filter("clas = ",clseb).filter("q41 = ", 8).count()
        obmdseb116=Survey.all().filter("clas = ",clseb).filter("q41 = ", 9).count()
        obmdseb117=Survey.all().filter("clas = ",clseb).filter("q41 = ", 10).count()
        
        q4_hse = 4*obmdseb111 + 5*obmdseb112 + 6*obmdseb113 + 7*obmdseb114 + 8*obmdseb115 + 9*obmdseb116 + 10*obmdseb117
        q4_hy_clseb = round(q4_hse/float(seb),2)
        
        obmdseb121=Survey.all().filter("clas = ",clseb).filter("q42 = ", 4).count()
        obmdseb122=Survey.all().filter("clas = ",clseb).filter("q42 = ", 5).count()
        obmdseb123=Survey.all().filter("clas = ",clseb).filter("q42 = ", 6).count()
        obmdseb124=Survey.all().filter("clas = ",clseb).filter("q42 = ", 7).count()
        obmdseb125=Survey.all().filter("clas = ",clseb).filter("q42 = ", 8).count()
        obmdseb126=Survey.all().filter("clas = ",clseb).filter("q42 = ", 9).count()
        obmdseb127=Survey.all().filter("clas = ",clseb).filter("q42 = ", 10).count()
        
        q4_men1se = 4*obmdseb121 + 5*obmdseb122 + 6*obmdseb123 + 7*obmdseb124 + 8*obmdseb125 + 9*obmdseb126 + 10*obmdseb127
        q4_menseb = round(q4_men1se/float(seb),2)
        
        obmdseb131=Survey.all().filter("clas = ",clseb).filter("q43 = ", 4).count()
        obmdseb132=Survey.all().filter("clas = ",clseb).filter("q43 = ", 5).count()
        obmdseb133=Survey.all().filter("clas = ",clseb).filter("q43 = ", 6).count()
        obmdseb134=Survey.all().filter("clas = ",clseb).filter("q43 = ", 7).count()
        obmdseb135=Survey.all().filter("clas = ",clseb).filter("q43 = ", 8).count()
        obmdseb136=Survey.all().filter("clas = ",clseb).filter("q43 = ", 9).count()
        obmdseb137=Survey.all().filter("clas = ",clseb).filter("q43 = ", 10).count()
        
        q4_pri1se = 4*obmdseb131 + 5*obmdseb132 + 6*obmdseb133 + 7*obmdseb134 + 8*obmdseb135 + 9*obmdseb136 + 10*obmdseb137
        q4_priseb = round(q4_pri1se/float(seb),2)
        
        obmdseb141=Survey.all().filter("clas = ",clseb).filter("q44 = ", 4).count()
        obmdseb142=Survey.all().filter("clas = ",clseb).filter("q44 = ", 5).count()
        obmdseb143=Survey.all().filter("clas = ",clseb).filter("q44 = ", 6).count()
        obmdseb144=Survey.all().filter("clas = ",clseb).filter("q44 = ", 7).count()
        obmdseb145=Survey.all().filter("clas = ",clseb).filter("q44 = ", 8).count()
        obmdseb146=Survey.all().filter("clas = ",clseb).filter("q44 = ", 9).count()
        obmdseb147=Survey.all().filter("clas = ",clseb).filter("q44 = ", 10).count()
        
        q4_tim_del1se = 4*obmdseb141 + 5*obmdseb142 + 6*obmdseb143 + 7*obmdseb144 + 8*obmdseb145 + 9*obmdseb146 + 10*obmdseb147
        q4_tim_delseb = round(q4_tim_del1se/float(seb),2)
        
        obmdseb151=Survey.all().filter("clas = ",clseb).filter("q45 = ", 4).count()
        obmdseb152=Survey.all().filter("clas = ",clseb).filter("q45 = ", 5).count()
        obmdseb153=Survey.all().filter("clas = ",clseb).filter("q45 = ", 6).count()
        obmdseb154=Survey.all().filter("clas = ",clseb).filter("q45 = ", 7).count()
        obmdseb155=Survey.all().filter("clas = ",clseb).filter("q45 = ", 8).count()
        obmdseb156=Survey.all().filter("clas = ",clseb).filter("q45 = ", 9).count()
        obmdseb157=Survey.all().filter("clas = ",clseb).filter("q45 = ", 10).count()
        
        q4_ser_qua1se = 4*obmdseb151 + 5*obmdseb152 + 6*obmdseb153 + 7*obmdseb154 + 8*obmdseb155 + 9*obmdseb156 + 10*obmdseb157
        q4_ser_quaseb = round(q4_ser_qua1se/float(seb),2)

        obhodseb111=Survey.all().filter("clas = ",clseb).filter("q51 = ", 4).count()
        obhodseb112=Survey.all().filter("clas = ",clseb).filter("q51 = ", 5).count()
        obhodseb113=Survey.all().filter("clas = ",clseb).filter("q51 = ", 6).count()
        obhodseb114=Survey.all().filter("clas = ",clseb).filter("q51 = ", 7).count()
        obhodseb115=Survey.all().filter("clas = ",clseb).filter("q51 = ", 8).count()
        obhodseb116=Survey.all().filter("clas = ",clseb).filter("q51 = ", 9).count()
        obhodseb117=Survey.all().filter("clas = ",clseb).filter("q51 = ", 10).count()
        
        q5_rese = 4*obhodseb111 + 5*obhodseb112 + 6*obhodseb113 + 7*obhodseb114 + 8*obhodseb115 + 9*obhodseb116 + 10*obhodseb117
        q5_res_adseb = round(q5_rese/float(seb),2)
        
        obhodseb121=Survey.all().filter("clas = ",clseb).filter("q52 = ", 4).count()
        obhodseb122=Survey.all().filter("clas = ",clseb).filter("q52 = ", 5).count()
        obhodseb123=Survey.all().filter("clas = ",clseb).filter("q52 = ", 6).count()
        obhodseb124=Survey.all().filter("clas = ",clseb).filter("q52 = ", 7).count()
        obhodseb125=Survey.all().filter("clas = ",clseb).filter("q52 = ", 8).count()
        obhodseb126=Survey.all().filter("clas = ",clseb).filter("q52 = ", 9).count()
        obhodseb127=Survey.all().filter("clas = ",clseb).filter("q52 = ", 10).count()
        
        q5_aud1se = 4*obhodseb121 + 5*obhodseb122 + 6*obhodseb123 + 7*obhodseb124 + 8*obhodseb125 + 9*obhodseb126 + 10*obhodseb127
        q5_audseb = round(q5_aud1se/float(seb),2)
        
        obhodseb131=Survey.all().filter("clas = ",clseb).filter("q53 = ", 4).count()
        obhodseb132=Survey.all().filter("clas = ",clseb).filter("q53 = ", 5).count()
        obhodseb133=Survey.all().filter("clas = ",clseb).filter("q53 = ", 6).count()
        obhodseb134=Survey.all().filter("clas = ",clseb).filter("q53 = ", 7).count()
        obhodseb135=Survey.all().filter("clas = ",clseb).filter("q53 = ", 8).count()
        obhodseb136=Survey.all().filter("clas = ",clseb).filter("q53 = ", 9).count()
        obhodseb137=Survey.all().filter("clas = ",clseb).filter("q53 = ", 10).count()
        
        q5_gam1se = 4*obhodseb131 + 5*obhodseb132 + 6*obhodseb133 + 7*obhodseb134 + 8*obhodseb135 + 9*obhodseb136 + 10*obhodseb137 
        q5_gamseb = round(q5_gam1se/float(seb),2)
        
        obhodseb141=Survey.all().filter("clas = ",clseb).filter("q54 = ", 4).count()
        obhodseb142=Survey.all().filter("clas = ",clseb).filter("q54 = ", 5).count()
        obhodseb143=Survey.all().filter("clas = ",clseb).filter("q54 = ", 6).count()
        obhodseb144=Survey.all().filter("clas = ",clseb).filter("q54 = ", 7).count()
        obhodseb145=Survey.all().filter("clas = ",clseb).filter("q54 = ", 8).count()
        obhodseb146=Survey.all().filter("clas = ",clseb).filter("q54 = ", 9).count()
        obhodseb147=Survey.all().filter("clas = ",clseb).filter("q54 = ", 10).count()
        
        q5_info1se = 4*obhodseb141 + 5*obhodseb142 + 6*obhodseb143 + 7*obhodseb144 + 8*obhodseb145 + 9*obhodseb146 + 10*obhodseb147 
        q5_infoseb = round(q5_info1se/float(seb),2)
        
        obhodseb151=Survey.all().filter("clas = ",clseb).filter("q55 = ", 4).count()
        obhodseb152=Survey.all().filter("clas = ",clseb).filter("q55 = ", 5).count()
        obhodseb153=Survey.all().filter("clas = ",clseb).filter("q55 = ", 6).count()
        obhodseb154=Survey.all().filter("clas = ",clseb).filter("q55 = ", 7).count()
        obhodseb155=Survey.all().filter("clas = ",clseb).filter("q55 = ", 8).count()
        obhodseb156=Survey.all().filter("clas = ",clseb).filter("q55 = ", 9).count()
        obhodseb157=Survey.all().filter("clas = ",clseb).filter("q55 = ", 10).count()
        
        q5_dr1se = 4*obhodseb151 + 5*obhodseb152 + 6*obhodseb153 + 7*obhodseb154 + 8*obhodseb155 + 9*obhodseb156 + 10*obhodseb157
        q5_drseb = round(q5_dr1se/float(seb),2)

        obhodseb161=Survey.all().filter("clas = ",clseb).filter("q56 = ", 4).count()
        obhodseb162=Survey.all().filter("clas = ",clseb).filter("q56 = ", 5).count()
        obhodseb163=Survey.all().filter("clas = ",clseb).filter("q56 = ", 6).count()
        obhodseb164=Survey.all().filter("clas = ",clseb).filter("q56 = ", 7).count()
        obhodseb165=Survey.all().filter("clas = ",clseb).filter("q56 = ", 8).count()
        obhodseb166=Survey.all().filter("clas = ",clseb).filter("q56 = ", 9).count()
        obhodseb167=Survey.all().filter("clas = ",clseb).filter("q56 = ", 10).count()
        
        q5_toi1se = 4*obhodseb161 + 5*obhodseb162 + 6*obhodseb163 + 7*obhodseb164 + 8*obhodseb165 + 9*obhodseb166 + 10*obhodseb167
        q5_toiseb =round(q5_toi1se/float(seb),2)
        
        obhodseb171=Survey.all().filter("clas = ",clseb).filter("q57 = ", 4).count()
        obhodseb172=Survey.all().filter("clas = ",clseb).filter("q57 = ", 5).count()
        obhodseb173=Survey.all().filter("clas = ",clseb).filter("q57 = ", 6).count()
        obhodseb174=Survey.all().filter("clas = ",clseb).filter("q57 = ", 7).count()
        obhodseb175=Survey.all().filter("clas = ",clseb).filter("q57 = ", 8).count()
        obhodseb176=Survey.all().filter("clas = ",clseb).filter("q57 = ", 9).count()
        obhodseb177=Survey.all().filter("clas = ",clseb).filter("q57 = ", 10).count()
        
        q5_clean1se = 4*obhodseb171 + 5*obhodseb172 + 6*obhodseb173 + 7*obhodseb174 + 8*obhodseb175 + 9*obhodseb176 + 10*obhodseb177
        q5_cleanseb = round(q5_clean1se/float(seb),2)
        
        obhodseb181=Survey.all().filter("clas = ",clseb).filter("q58 = ", 4).count()
        obhodseb182=Survey.all().filter("clas = ",clseb).filter("q58 = ", 5).count()
        obhodseb183=Survey.all().filter("clas = ",clseb).filter("q58 = ", 6).count()
        obhodseb184=Survey.all().filter("clas = ",clseb).filter("q58 = ", 7).count()
        obhodseb185=Survey.all().filter("clas = ",clseb).filter("q58 = ", 8).count()
        obhodseb186=Survey.all().filter("clas = ",clseb).filter("q58 = ", 9).count()
        obhodseb187=Survey.all().filter("clas = ",clseb).filter("q58 = ", 10).count()
        
        q5_mai1se = 4*obhodseb181 + 5*obhodseb182 + 6*obhodseb183 + 7*obhodseb184 + 8*obhodseb185 + 9*obhodseb186 + 10*obhodseb187
        q5_maiseb = round(q5_mai1se/float(seb),2)


        total_se1 = q5_maiseb + q5_cleanseb + q5_toiseb + q5_drseb + q5_infoseb + q5_gamseb + q5_audseb + q1_condffseb + q1_lightseb + q1_acseb + q1_cleanseb + q2_eq_avseb + q2_s_aseb + q2_c_aseb + q2_l_mseb + q2_i_cseb + q2_b_sseb + q3_libseb + q3_i_sseb + q3_con_boseb + q3_av_ne_verseb + q3_re_roseb + q3_j_mseb + q3_staseb + q4_hy_clseb + q4_menseb + q4_priseb + q4_tim_delseb + q4_ser_quaseb + q5_res_adseb      
        total_seb = round(total_se1,2)
        per_seb = round(10*total_seb/float(30.0),2)

        #TE-A
        cltea = "TE-A"
        tea=Survey.all().filter("clas = ",cltea).count()
        
        gadqtea111=Survey.all().filter("clas = ",cltea).filter("q11 = ", 4).count()
        gadqtea112=Survey.all().filter("clas = ",cltea).filter("q11 = ", 5).count()
        gadqtea113=Survey.all().filter("clas = ",cltea).filter("q11 = ", 6).count()
        gadqtea114=Survey.all().filter("clas = ",cltea).filter("q11 = ", 7).count()
        gadqtea115=Survey.all().filter("clas = ",cltea).filter("q11 = ", 8).count()
        gadqtea116=Survey.all().filter("clas = ",cltea).filter("q11 = ", 9).count()
        gadqtea117=Survey.all().filter("clas = ",cltea).filter("q11 = ", 10).count()
        
        q1_condte = 4*gadqtea111 + 5*gadqtea112 + 6*gadqtea113 + 7*gadqtea114 + 8*gadqtea115 + 9*gadqtea116 + 10*gadqtea117
        q1_condfftea = round(q1_condte/float(tea),2)
        
        gadqtea121=Survey.all().filter("clas = ",cltea).filter("q12 = ", 4).count()
        gadqtea122=Survey.all().filter("clas = ",cltea).filter("q12 = ", 5).count()
        gadqtea123=Survey.all().filter("clas = ",cltea).filter("q12 = ", 6).count()
        gadqtea124=Survey.all().filter("clas = ",cltea).filter("q12 = ", 7).count()
        gadqtea125=Survey.all().filter("clas = ",cltea).filter("q12 = ", 8).count()
        gadqtea126=Survey.all().filter("clas = ",cltea).filter("q12 = ", 9).count()
        gadqtea127=Survey.all().filter("clas = ",cltea).filter("q12 = ", 10).count()
        
        q1_lighte = 4*gadqtea121 + 5*gadqtea122 + 6*gadqtea123 + 7*gadqtea124 + 8*gadqtea125 + 9*gadqtea126 + 10*gadqtea127
        q1_lighttea = round(q1_lighte/float(tea),2)
        
        gadqtea131=Survey.all().filter("clas = ",cltea).filter("q13 = ", 4).count()
        gadqtea132=Survey.all().filter("clas = ",cltea).filter("q13 = ", 5).count()
        gadqtea133=Survey.all().filter("clas = ",cltea).filter("q13 = ", 6).count()
        gadqtea134=Survey.all().filter("clas = ",cltea).filter("q13 = ", 7).count()
        gadqtea135=Survey.all().filter("clas = ",cltea).filter("q13 = ", 8).count()
        gadqtea136=Survey.all().filter("clas = ",cltea).filter("q13 = ", 9).count()
        gadqtea137=Survey.all().filter("clas = ",cltea).filter("q13 = ", 10).count()
        
        q1_ac1te = 4*gadqtea131 + 5*gadqtea132 + 6*gadqtea133 + 7*gadqtea134 + 8*gadqtea135 + 9*gadqtea136 + 10*gadqtea137
        q1_actea = round(q1_ac1te/float(tea),2)
        
        gadqtea141=Survey.all().filter("clas = ",cltea).filter("q14 = ", 4).count()
        gadqtea142=Survey.all().filter("clas = ",cltea).filter("q14 = ", 5).count()
        gadqtea143=Survey.all().filter("clas = ",cltea).filter("q14 = ", 6).count()
        gadqtea144=Survey.all().filter("clas = ",cltea).filter("q14 = ", 7).count()
        gadqtea145=Survey.all().filter("clas = ",cltea).filter("q14 = ", 8).count()
        gadqtea146=Survey.all().filter("clas = ",cltea).filter("q14 = ", 9).count()
        gadqtea147=Survey.all().filter("clas = ",cltea).filter("q14 = ", 10).count()
        
        q1_clean1te = 4*gadqtea141 + 5*gadqtea142 + 6*gadqtea143 + 7*gadqtea144 + 8*gadqtea145 + 9*gadqtea146 + 10*gadqtea147
        q1_cleantea = round(q1_clean1te/float(tea),2)
        
        

        nbaqtea111=Survey.all().filter("clas = ",cltea).filter("q21 = ", 4).count()
        nbaqtea112=Survey.all().filter("clas = ",cltea).filter("q21 = ", 5).count()
        nbaqtea113=Survey.all().filter("clas = ",cltea).filter("q21 = ", 6).count()
        nbaqtea114=Survey.all().filter("clas = ",cltea).filter("q21 = ", 7).count()
        nbaqtea115=Survey.all().filter("clas = ",cltea).filter("q21 = ", 8).count()
        nbaqtea116=Survey.all().filter("clas = ",cltea).filter("q21 = ", 9).count()
        nbaqtea117=Survey.all().filter("clas = ",cltea).filter("q21 = ", 10).count()
        
        q2_eate = 4*nbaqtea111 + 5*nbaqtea112 + 6*nbaqtea113 + 7*nbaqtea114 + 8*nbaqtea115 + 9*nbaqtea116 + 10*nbaqtea117
        q2_eq_avtea = round(q2_eate/float(tea),2)
        
        nbaqtea121=Survey.all().filter("clas = ",cltea).filter("q22 = ", 4).count()
        nbaqtea122=Survey.all().filter("clas = ",cltea).filter("q22 = ", 5).count()
        nbaqtea123=Survey.all().filter("clas = ",cltea).filter("q22 = ", 6).count()
        nbaqtea124=Survey.all().filter("clas = ",cltea).filter("q22 = ", 7).count()
        nbaqtea125=Survey.all().filter("clas = ",cltea).filter("q22 = ", 8).count()
        nbaqtea126=Survey.all().filter("clas = ",cltea).filter("q22 = ", 9).count()
        nbaqtea127=Survey.all().filter("clas = ",cltea).filter("q22 = ", 10).count()
        
        q2_s_a1te = 4*nbaqtea121 + 5*nbaqtea122 + 6*nbaqtea123 + 7*nbaqtea124 + 8*nbaqtea125 + 9*nbaqtea126 + 10*nbaqtea127
        q2_s_atea = round(q2_s_a1te/float(tea),2)
        
        nbaqtea131=Survey.all().filter("clas = ",cltea).filter("q23 = ", 4).count()
        nbaqtea132=Survey.all().filter("clas = ",cltea).filter("q23 = ", 5).count()
        nbaqtea133=Survey.all().filter("clas = ",cltea).filter("q23 = ", 6).count()
        nbaqtea134=Survey.all().filter("clas = ",cltea).filter("q23 = ", 7).count()
        nbaqtea135=Survey.all().filter("clas = ",cltea).filter("q23 = ", 8).count()
        nbaqtea136=Survey.all().filter("clas = ",cltea).filter("q23 = ", 9).count()
        nbaqtea137=Survey.all().filter("clas = ",cltea).filter("q23 = ", 10).count()
        
        q2_c_a1te = 4*nbaqtea131 + 5*nbaqtea132 + 6*nbaqtea133 + 7*nbaqtea134 + 8*nbaqtea135 + 9*nbaqtea136 + 10*nbaqtea137 
        q2_c_atea = round(q2_c_a1te/float(tea),2)
        
        nbaqtea141=Survey.all().filter("clas = ",cltea).filter("q24 = ", 4).count()
        nbaqtea142=Survey.all().filter("clas = ",cltea).filter("q24 = ", 5).count()
        nbaqtea143=Survey.all().filter("clas = ",cltea).filter("q24 = ", 6).count()
        nbaqtea144=Survey.all().filter("clas = ",cltea).filter("q24 = ", 7).count()
        nbaqtea145=Survey.all().filter("clas = ",cltea).filter("q24 = ", 8).count()
        nbaqtea146=Survey.all().filter("clas = ",cltea).filter("q24 = ", 9).count()
        nbaqtea147=Survey.all().filter("clas = ",cltea).filter("q24 = ", 10).count()
        
        q2_l_m1te = 4*nbaqtea141 + 5*nbaqtea142 + 6*nbaqtea143 + 7*nbaqtea144 + 8*nbaqtea145 + 9*nbaqtea146 + 10*nbaqtea147 
        q2_l_mtea = round(q2_l_m1te/float(tea),2)
        
        nbaqtea151=Survey.all().filter("clas = ",cltea).filter("q25 = ", 4).count()
        nbaqtea152=Survey.all().filter("clas = ",cltea).filter("q25 = ", 5).count()
        nbaqtea153=Survey.all().filter("clas = ",cltea).filter("q25 = ", 6).count()
        nbaqtea154=Survey.all().filter("clas = ",cltea).filter("q25 = ", 7).count()
        nbaqtea155=Survey.all().filter("clas = ",cltea).filter("q25 = ", 8).count()
        nbaqtea156=Survey.all().filter("clas = ",cltea).filter("q25 = ", 9).count()
        nbaqtea157=Survey.all().filter("clas = ",cltea).filter("q25 = ", 10).count()
        
        q2_i_c1te = 4*nbaqtea151 + 5*nbaqtea152 + 6*nbaqtea153 + 7*nbaqtea154 + 8*nbaqtea155 + 9*nbaqtea156 + 10*nbaqtea157
        q2_i_ctea = round(q2_i_c1te/float(tea),2) 
            
        nbaqtea161=Survey.all().filter("clas = ",cltea).filter("q26 = ", 4).count()
        nbaqtea162=Survey.all().filter("clas = ",cltea).filter("q26 = ", 5).count()
        nbaqtea163=Survey.all().filter("clas = ",cltea).filter("q26 = ", 6).count()
        nbaqtea164=Survey.all().filter("clas = ",cltea).filter("q26 = ", 7).count()
        nbaqtea165=Survey.all().filter("clas = ",cltea).filter("q26 = ", 8).count()
        nbaqtea166=Survey.all().filter("clas = ",cltea).filter("q26 = ", 9).count()
        nbaqtea167=Survey.all().filter("clas = ",cltea).filter("q26 = ", 10).count()
        
        q2_b_s1te = 4*nbaqtea161 + 5*nbaqtea162 + 6*nbaqtea163 + 7*nbaqtea164 + 8*nbaqtea165 + 9*nbaqtea166 + 10*nbaqtea167
        q2_b_stea = round(q2_b_s1te/float(tea),2)

        soeietea111=Survey.all().filter("clas = ",cltea).filter("q31 = ", 4).count()
        soeietea112=Survey.all().filter("clas = ",cltea).filter("q31 = ", 5).count()
        soeietea113=Survey.all().filter("clas = ",cltea).filter("q31 = ", 6).count()
        soeietea114=Survey.all().filter("clas = ",cltea).filter("q31 = ", 7).count()
        soeietea115=Survey.all().filter("clas = ",cltea).filter("q31 = ", 8).count()
        soeietea116=Survey.all().filter("clas = ",cltea).filter("q31 = ", 9).count()
        soeietea117=Survey.all().filter("clas = ",cltea).filter("q31 = ", 10).count()
        
        q3_lite = 4*soeietea111 + 5*soeietea112 + 6*soeietea113 + 7*soeietea114 + 8*soeietea115 + 9*soeietea116 + 10*soeietea117
        q3_libtea = round(q3_lite/float(tea),2)
        
        soeietea121=Survey.all().filter("clas = ",cltea).filter("q32 = ", 4).count()
        soeietea122=Survey.all().filter("clas = ",cltea).filter("q32 = ", 5).count()
        soeietea123=Survey.all().filter("clas = ",cltea).filter("q32 = ", 6).count()
        soeietea124=Survey.all().filter("clas = ",cltea).filter("q32 = ", 7).count()
        soeietea125=Survey.all().filter("clas = ",cltea).filter("q32 = ", 8).count()
        soeietea126=Survey.all().filter("clas = ",cltea).filter("q32 = ", 9).count()
        soeietea127=Survey.all().filter("clas = ",cltea).filter("q32 = ", 10).count()
        
        q3_i_s1te = 4*soeietea121 + 5*soeietea122 + 6*soeietea123 + 7*soeietea124 + 8*soeietea125 + 9*soeietea126 + 10*soeietea127
        q3_i_stea = round(q3_i_s1te/float(tea),2)
        
        soeietea131=Survey.all().filter("clas = ",cltea).filter("q33 = ", 4).count()
        soeietea132=Survey.all().filter("clas = ",cltea).filter("q33 = ", 5).count()
        soeietea133=Survey.all().filter("clas = ",cltea).filter("q33 = ", 6).count()
        soeietea134=Survey.all().filter("clas = ",cltea).filter("q33 = ", 7).count()
        soeietea135=Survey.all().filter("clas = ",cltea).filter("q33 = ", 8).count()
        soeietea136=Survey.all().filter("clas = ",cltea).filter("q33 = ", 9).count()
        soeietea137=Survey.all().filter("clas = ",cltea).filter("q33 = ", 10).count()
        
        q3_con_bo1te = 4*soeietea131 + 5*soeietea132 + 6*soeietea133 + 7*soeietea134 + 8*soeietea135 + 9*soeietea136 + 10*soeietea137 
        q3_con_botea = round(q3_con_bo1te/float(tea),2)
        
        soeietea141=Survey.all().filter("clas = ",cltea).filter("q34 = ", 4).count()
        soeietea142=Survey.all().filter("clas = ",cltea).filter("q34 = ", 5).count()
        soeietea143=Survey.all().filter("clas = ",cltea).filter("q34 = ", 6).count()
        soeietea144=Survey.all().filter("clas = ",cltea).filter("q34 = ", 7).count()
        soeietea145=Survey.all().filter("clas = ",cltea).filter("q34 = ", 8).count()
        soeietea146=Survey.all().filter("clas = ",cltea).filter("q34 = ", 9).count()
        soeietea147=Survey.all().filter("clas = ",cltea).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1te = 4*soeietea141 + 5*soeietea142 + 6*soeietea143 + 7*soeietea144 + 8*soeietea145 + 9*soeietea146 + 10*soeietea147 
        q3_av_ne_vertea =round(q3_av_ne_ver1te/float(tea),2)
        
        soeietea151=Survey.all().filter("clas = ",cltea).filter("q35 = ", 4).count()
        soeietea152=Survey.all().filter("clas = ",cltea).filter("q35 = ", 5).count()
        soeietea153=Survey.all().filter("clas = ",cltea).filter("q35 = ", 6).count()
        soeietea154=Survey.all().filter("clas = ",cltea).filter("q35 = ", 7).count()
        soeietea155=Survey.all().filter("clas = ",cltea).filter("q35 = ", 8).count()
        soeietea156=Survey.all().filter("clas = ",cltea).filter("q35 = ", 9).count()
        soeietea157=Survey.all().filter("clas = ",cltea).filter("q35 = ", 10).count()
        
        q3_re_ro1te = 4*soeietea151 + 5*soeietea152 + 6*soeietea153 + 7*soeietea154 + 8*soeietea155 + 9*soeietea156 + 10*soeietea157
        q3_re_rotea = round(q3_re_ro1te/float(tea),2)
            
        soeietea161=Survey.all().filter("clas = ",cltea).filter("q36 = ", 4).count()
        soeietea162=Survey.all().filter("clas = ",cltea).filter("q36 = ", 5).count()
        soeietea163=Survey.all().filter("clas = ",cltea).filter("q36 = ", 6).count()
        soeietea164=Survey.all().filter("clas = ",cltea).filter("q36 = ", 7).count()
        soeietea165=Survey.all().filter("clas = ",cltea).filter("q36 = ", 8).count()
        soeietea166=Survey.all().filter("clas = ",cltea).filter("q36 = ", 9).count()
        soeietea167=Survey.all().filter("clas = ",cltea).filter("q36 = ", 10).count()
        
        q3_j_m1te = 4*soeietea161 + 5*soeietea162 + 6*soeietea163 + 7*soeietea164 + 8*soeietea165 + 9*soeietea166 + 10*soeietea167
        q3_j_mtea = round(q3_j_m1te/float(tea),2)
            
        soeietea171=Survey.all().filter("clas = ",cltea).filter("q37 = ", 4).count()
        soeietea172=Survey.all().filter("clas = ",cltea).filter("q37 = ", 5).count()
        soeietea173=Survey.all().filter("clas = ",cltea).filter("q37 = ", 6).count()
        soeietea174=Survey.all().filter("clas = ",cltea).filter("q37 = ", 7).count()
        soeietea175=Survey.all().filter("clas = ",cltea).filter("q37 = ", 8).count()
        soeietea176=Survey.all().filter("clas = ",cltea).filter("q37 = ", 9).count()
        soeietea177=Survey.all().filter("clas = ",cltea).filter("q37 = ", 10).count()
        
        q3_sta1te = 4*soeietea171 + 5*soeietea172 + 6*soeietea173 + 7*soeietea174 + 8*soeietea175 + 9*soeietea176 + 10*soeietea177
        q3_statea = round(q3_sta1te/float(tea),2)

        obmdtea111=Survey.all().filter("clas = ",cltea).filter("q41 = ", 4).count()
        obmdtea112=Survey.all().filter("clas = ",cltea).filter("q41 = ", 5).count()
        obmdtea113=Survey.all().filter("clas = ",cltea).filter("q41 = ", 6).count()
        obmdtea114=Survey.all().filter("clas = ",cltea).filter("q41 = ", 7).count()
        obmdtea115=Survey.all().filter("clas = ",cltea).filter("q41 = ", 8).count()
        obmdtea116=Survey.all().filter("clas = ",cltea).filter("q41 = ", 9).count()
        obmdtea117=Survey.all().filter("clas = ",cltea).filter("q41 = ", 10).count()
        
        q4_hte = 4*obmdtea111 + 5*obmdtea112 + 6*obmdtea113 + 7*obmdtea114 + 8*obmdtea115 + 9*obmdtea116 + 10*obmdtea117
        q4_hy_cltea = round(q4_hte/float(tea),2)
        
        obmdtea121=Survey.all().filter("clas = ",cltea).filter("q42 = ", 4).count()
        obmdtea122=Survey.all().filter("clas = ",cltea).filter("q42 = ", 5).count()
        obmdtea123=Survey.all().filter("clas = ",cltea).filter("q42 = ", 6).count()
        obmdtea124=Survey.all().filter("clas = ",cltea).filter("q42 = ", 7).count()
        obmdtea125=Survey.all().filter("clas = ",cltea).filter("q42 = ", 8).count()
        obmdtea126=Survey.all().filter("clas = ",cltea).filter("q42 = ", 9).count()
        obmdtea127=Survey.all().filter("clas = ",cltea).filter("q42 = ", 10).count()
        
        q4_men1te = 4*obmdtea121 + 5*obmdtea122 + 6*obmdtea123 + 7*obmdtea124 + 8*obmdtea125 + 9*obmdtea126 + 10*obmdtea127
        q4_mentea = round(q4_men1te/float(tea),2)
        
        obmdtea131=Survey.all().filter("clas = ",cltea).filter("q43 = ", 4).count()
        obmdtea132=Survey.all().filter("clas = ",cltea).filter("q43 = ", 5).count()
        obmdtea133=Survey.all().filter("clas = ",cltea).filter("q43 = ", 6).count()
        obmdtea134=Survey.all().filter("clas = ",cltea).filter("q43 = ", 7).count()
        obmdtea135=Survey.all().filter("clas = ",cltea).filter("q43 = ", 8).count()
        obmdtea136=Survey.all().filter("clas = ",cltea).filter("q43 = ", 9).count()
        obmdtea137=Survey.all().filter("clas = ",cltea).filter("q43 = ", 10).count()
        
        q4_pri1te = 4*obmdtea131 + 5*obmdtea132 + 6*obmdtea133 + 7*obmdtea134 + 8*obmdtea135 + 9*obmdtea136 + 10*obmdtea137
        q4_pritea = round(q4_pri1te/float(tea),2)
        
        obmdtea141=Survey.all().filter("clas = ",cltea).filter("q44 = ", 4).count()
        obmdtea142=Survey.all().filter("clas = ",cltea).filter("q44 = ", 5).count()
        obmdtea143=Survey.all().filter("clas = ",cltea).filter("q44 = ", 6).count()
        obmdtea144=Survey.all().filter("clas = ",cltea).filter("q44 = ", 7).count()
        obmdtea145=Survey.all().filter("clas = ",cltea).filter("q44 = ", 8).count()
        obmdtea146=Survey.all().filter("clas = ",cltea).filter("q44 = ", 9).count()
        obmdtea147=Survey.all().filter("clas = ",cltea).filter("q44 = ", 10).count()
        
        q4_tim_del1te = 4*obmdtea141 + 5*obmdtea142 + 6*obmdtea143 + 7*obmdtea144 + 8*obmdtea145 + 9*obmdtea146 + 10*obmdtea147
        q4_tim_deltea = round(q4_tim_del1te/float(tea),2)
        
        obmdtea151=Survey.all().filter("clas = ",cltea).filter("q45 = ", 4).count()
        obmdtea152=Survey.all().filter("clas = ",cltea).filter("q45 = ", 5).count()
        obmdtea153=Survey.all().filter("clas = ",cltea).filter("q45 = ", 6).count()
        obmdtea154=Survey.all().filter("clas = ",cltea).filter("q45 = ", 7).count()
        obmdtea155=Survey.all().filter("clas = ",cltea).filter("q45 = ", 8).count()
        obmdtea156=Survey.all().filter("clas = ",cltea).filter("q45 = ", 9).count()
        obmdtea157=Survey.all().filter("clas = ",cltea).filter("q45 = ", 10).count()
        
        q4_ser_qua1te = 4*obmdtea151 + 5*obmdtea152 + 6*obmdtea153 + 7*obmdtea154 + 8*obmdtea155 + 9*obmdtea156 + 10*obmdtea157
        q4_ser_quatea = round(q4_ser_qua1te/float(tea),2)

        obhodtea111=Survey.all().filter("clas = ",cltea).filter("q51 = ", 4).count()
        obhodtea112=Survey.all().filter("clas = ",cltea).filter("q51 = ", 5).count()
        obhodtea113=Survey.all().filter("clas = ",cltea).filter("q51 = ", 6).count()
        obhodtea114=Survey.all().filter("clas = ",cltea).filter("q51 = ", 7).count()
        obhodtea115=Survey.all().filter("clas = ",cltea).filter("q51 = ", 8).count()
        obhodtea116=Survey.all().filter("clas = ",cltea).filter("q51 = ", 9).count()
        obhodtea117=Survey.all().filter("clas = ",cltea).filter("q51 = ", 10).count()
        
        q5_rete = 4*obhodtea111 + 5*obhodtea112 + 6*obhodtea113 + 7*obhodtea114 + 8*obhodtea115 + 9*obhodtea116 + 10*obhodtea117
        q5_res_adtea = round(q5_rete/float(tea),2)
        
        obhodtea121=Survey.all().filter("clas = ",cltea).filter("q52 = ", 4).count()
        obhodtea122=Survey.all().filter("clas = ",cltea).filter("q52 = ", 5).count()
        obhodtea123=Survey.all().filter("clas = ",cltea).filter("q52 = ", 6).count()
        obhodtea124=Survey.all().filter("clas = ",cltea).filter("q52 = ", 7).count()
        obhodtea125=Survey.all().filter("clas = ",cltea).filter("q52 = ", 8).count()
        obhodtea126=Survey.all().filter("clas = ",cltea).filter("q52 = ", 9).count()
        obhodtea127=Survey.all().filter("clas = ",cltea).filter("q52 = ", 10).count()
        
        q5_aud1te = 4*obhodtea121 + 5*obhodtea122 + 6*obhodtea123 + 7*obhodtea124 + 8*obhodtea125 + 9*obhodtea126 + 10*obhodtea127
        q5_audtea = round(q5_aud1te/float(tea),2)
        
        obhodtea131=Survey.all().filter("clas = ",cltea).filter("q53 = ", 4).count()
        obhodtea132=Survey.all().filter("clas = ",cltea).filter("q53 = ", 5).count()
        obhodtea133=Survey.all().filter("clas = ",cltea).filter("q53 = ", 6).count()
        obhodtea134=Survey.all().filter("clas = ",cltea).filter("q53 = ", 7).count()
        obhodtea135=Survey.all().filter("clas = ",cltea).filter("q53 = ", 8).count()
        obhodtea136=Survey.all().filter("clas = ",cltea).filter("q53 = ", 9).count()
        obhodtea137=Survey.all().filter("clas = ",cltea).filter("q53 = ", 10).count()
        
        q5_gam1te = 4*obhodtea131 + 5*obhodtea132 + 6*obhodtea133 + 7*obhodtea134 + 8*obhodtea135 + 9*obhodtea136 + 10*obhodtea137 
        q5_gamtea = round(q5_gam1te/float(tea),2)
        
        obhodtea141=Survey.all().filter("clas = ",cltea).filter("q54 = ", 4).count()
        obhodtea142=Survey.all().filter("clas = ",cltea).filter("q54 = ", 5).count()
        obhodtea143=Survey.all().filter("clas = ",cltea).filter("q54 = ", 6).count()
        obhodtea144=Survey.all().filter("clas = ",cltea).filter("q54 = ", 7).count()
        obhodtea145=Survey.all().filter("clas = ",cltea).filter("q54 = ", 8).count()
        obhodtea146=Survey.all().filter("clas = ",cltea).filter("q54 = ", 9).count()
        obhodtea147=Survey.all().filter("clas = ",cltea).filter("q54 = ", 10).count()
        
        q5_info1te = 4*obhodtea141 + 5*obhodtea142 + 6*obhodtea143 + 7*obhodtea144 + 8*obhodtea145 + 9*obhodtea146 + 10*obhodtea147 
        q5_infotea = round(q5_info1te/float(tea),2)
        
        obhodtea151=Survey.all().filter("clas = ",cltea).filter("q55 = ", 4).count()
        obhodtea152=Survey.all().filter("clas = ",cltea).filter("q55 = ", 5).count()
        obhodtea153=Survey.all().filter("clas = ",cltea).filter("q55 = ", 6).count()
        obhodtea154=Survey.all().filter("clas = ",cltea).filter("q55 = ", 7).count()
        obhodtea155=Survey.all().filter("clas = ",cltea).filter("q55 = ", 8).count()
        obhodtea156=Survey.all().filter("clas = ",cltea).filter("q55 = ", 9).count()
        obhodtea157=Survey.all().filter("clas = ",cltea).filter("q55 = ", 10).count()
        
        q5_dr1te = 4*obhodtea151 + 5*obhodtea152 + 6*obhodtea153 + 7*obhodtea154 + 8*obhodtea155 + 9*obhodtea156 + 10*obhodtea157
        q5_drtea = round(q5_dr1te/float(tea),2)

        obhodtea161=Survey.all().filter("clas = ",cltea).filter("q56 = ", 4).count()
        obhodtea162=Survey.all().filter("clas = ",cltea).filter("q56 = ", 5).count()
        obhodtea163=Survey.all().filter("clas = ",cltea).filter("q56 = ", 6).count()
        obhodtea164=Survey.all().filter("clas = ",cltea).filter("q56 = ", 7).count()
        obhodtea165=Survey.all().filter("clas = ",cltea).filter("q56 = ", 8).count()
        obhodtea166=Survey.all().filter("clas = ",cltea).filter("q56 = ", 9).count()
        obhodtea167=Survey.all().filter("clas = ",cltea).filter("q56 = ", 10).count()
        
        q5_toi1te = 4*obhodtea161 + 5*obhodtea162 + 6*obhodtea163 + 7*obhodtea164 + 8*obhodtea165 + 9*obhodtea166 + 10*obhodtea167
        q5_toitea =round(q5_toi1te/float(tea),2)
        
        obhodtea171=Survey.all().filter("clas = ",cltea).filter("q57 = ", 4).count()
        obhodtea172=Survey.all().filter("clas = ",cltea).filter("q57 = ", 5).count()
        obhodtea173=Survey.all().filter("clas = ",cltea).filter("q57 = ", 6).count()
        obhodtea174=Survey.all().filter("clas = ",cltea).filter("q57 = ", 7).count()
        obhodtea175=Survey.all().filter("clas = ",cltea).filter("q57 = ", 8).count()
        obhodtea176=Survey.all().filter("clas = ",cltea).filter("q57 = ", 9).count()
        obhodtea177=Survey.all().filter("clas = ",cltea).filter("q57 = ", 10).count()
        
        q5_clean1te = 4*obhodtea171 + 5*obhodtea172 + 6*obhodtea173 + 7*obhodtea174 + 8*obhodtea175 + 9*obhodtea176 + 10*obhodtea177
        q5_cleantea = round(q5_clean1te/float(tea),2)
        
        obhodtea181=Survey.all().filter("clas = ",cltea).filter("q58 = ", 4).count()
        obhodtea182=Survey.all().filter("clas = ",cltea).filter("q58 = ", 5).count()
        obhodtea183=Survey.all().filter("clas = ",cltea).filter("q58 = ", 6).count()
        obhodtea184=Survey.all().filter("clas = ",cltea).filter("q58 = ", 7).count()
        obhodtea185=Survey.all().filter("clas = ",cltea).filter("q58 = ", 8).count()
        obhodtea186=Survey.all().filter("clas = ",cltea).filter("q58 = ", 9).count()
        obhodtea187=Survey.all().filter("clas = ",cltea).filter("q58 = ", 10).count()
        
        q5_mai1te = 4*obhodtea181 + 5*obhodtea182 + 6*obhodtea183 + 7*obhodtea184 + 8*obhodtea185 + 9*obhodtea186 + 10*obhodtea187
        q5_maitea = round(q5_mai1te/float(tea),2)


        total_te = q5_maitea + q5_cleantea + q5_toitea + q5_drtea + q5_infotea + q5_gamtea + q5_audtea + q1_condfftea + q1_lighttea + q1_actea + q1_cleantea + q2_eq_avtea + q2_s_atea + q2_c_atea + q2_l_mtea + q2_i_ctea + q2_b_stea + q3_libtea + q3_i_stea + q3_con_botea + q3_av_ne_vertea + q3_re_rotea + q3_j_mtea + q3_statea + q4_hy_cltea + q4_mentea + q4_pritea + q4_tim_deltea + q4_ser_quatea + q5_res_adtea      
        total_tea = round(total_te,2)
        per_tea = round(10*total_tea/float(30.0),2)

        #TE-B

        clteb = "TE-B"
        teb=Survey.all().filter("clas = ",clteb).count()
        
        gadqteb111=Survey.all().filter("clas = ",clteb).filter("q11 = ", 4).count()
        gadqteb112=Survey.all().filter("clas = ",clteb).filter("q11 = ", 5).count()
        gadqteb113=Survey.all().filter("clas = ",clteb).filter("q11 = ", 6).count()
        gadqteb114=Survey.all().filter("clas = ",clteb).filter("q11 = ", 7).count()
        gadqteb115=Survey.all().filter("clas = ",clteb).filter("q11 = ", 8).count()
        gadqteb116=Survey.all().filter("clas = ",clteb).filter("q11 = ", 9).count()
        gadqteb117=Survey.all().filter("clas = ",clteb).filter("q11 = ", 10).count()
        
        q1_condte1 = 4*gadqteb111 + 5*gadqteb112 + 6*gadqteb113 + 7*gadqteb114 + 8*gadqteb115 + 9*gadqteb116 + 10*gadqteb117
        q1_condffteb = round(q1_condte1/float(teb),2)
        
        gadqteb121=Survey.all().filter("clas = ",clteb).filter("q12 = ", 4).count()
        gadqteb122=Survey.all().filter("clas = ",clteb).filter("q12 = ", 5).count()
        gadqteb123=Survey.all().filter("clas = ",clteb).filter("q12 = ", 6).count()
        gadqteb124=Survey.all().filter("clas = ",clteb).filter("q12 = ", 7).count()
        gadqteb125=Survey.all().filter("clas = ",clteb).filter("q12 = ", 8).count()
        gadqteb126=Survey.all().filter("clas = ",clteb).filter("q12 = ", 9).count()
        gadqteb127=Survey.all().filter("clas = ",clteb).filter("q12 = ", 10).count()
        
        q1_lighte1 = 4*gadqteb121 + 5*gadqteb122 + 6*gadqteb123 + 7*gadqteb124 + 8*gadqteb125 + 9*gadqteb126 + 10*gadqteb127
        q1_lightteb = round(q1_lighte1/float(teb),2)
        
        gadqteb131=Survey.all().filter("clas = ",clteb).filter("q13 = ", 4).count()
        gadqteb132=Survey.all().filter("clas = ",clteb).filter("q13 = ", 5).count()
        gadqteb133=Survey.all().filter("clas = ",clteb).filter("q13 = ", 6).count()
        gadqteb134=Survey.all().filter("clas = ",clteb).filter("q13 = ", 7).count()
        gadqteb135=Survey.all().filter("clas = ",clteb).filter("q13 = ", 8).count()
        gadqteb136=Survey.all().filter("clas = ",clteb).filter("q13 = ", 9).count()
        gadqteb137=Survey.all().filter("clas = ",clteb).filter("q13 = ", 10).count()
        
        q1_ac1te1 = 4*gadqteb131 + 5*gadqteb132 + 6*gadqteb133 + 7*gadqteb134 + 8*gadqteb135 + 9*gadqteb136 + 10*gadqteb137
        q1_acteb = round(q1_ac1te1/float(teb),2)
        
        gadqteb141=Survey.all().filter("clas = ",clteb).filter("q14 = ", 4).count()
        gadqteb142=Survey.all().filter("clas = ",clteb).filter("q14 = ", 5).count()
        gadqteb143=Survey.all().filter("clas = ",clteb).filter("q14 = ", 6).count()
        gadqteb144=Survey.all().filter("clas = ",clteb).filter("q14 = ", 7).count()
        gadqteb145=Survey.all().filter("clas = ",clteb).filter("q14 = ", 8).count()
        gadqteb146=Survey.all().filter("clas = ",clteb).filter("q14 = ", 9).count()
        gadqteb147=Survey.all().filter("clas = ",clteb).filter("q14 = ", 10).count()
        
        q1_clean1te1 = 4*gadqteb141 + 5*gadqteb142 + 6*gadqteb143 + 7*gadqteb144 + 8*gadqteb145 + 9*gadqteb146 + 10*gadqteb147
        q1_cleanteb = round(q1_clean1te1/float(teb),2)
        
        

        nbaqteb111=Survey.all().filter("clas = ",clteb).filter("q21 = ", 4).count()
        nbaqteb112=Survey.all().filter("clas = ",clteb).filter("q21 = ", 5).count()
        nbaqteb113=Survey.all().filter("clas = ",clteb).filter("q21 = ", 6).count()
        nbaqteb114=Survey.all().filter("clas = ",clteb).filter("q21 = ", 7).count()
        nbaqteb115=Survey.all().filter("clas = ",clteb).filter("q21 = ", 8).count()
        nbaqteb116=Survey.all().filter("clas = ",clteb).filter("q21 = ", 9).count()
        nbaqteb117=Survey.all().filter("clas = ",clteb).filter("q21 = ", 10).count()
        
        q2_eate1 = 4*nbaqteb111 + 5*nbaqteb112 + 6*nbaqteb113 + 7*nbaqteb114 + 8*nbaqteb115 + 9*nbaqteb116 + 10*nbaqteb117
        q2_eq_avteb = round(q2_eate1/float(teb),2)
        
        nbaqteb121=Survey.all().filter("clas = ",clteb).filter("q22 = ", 4).count()
        nbaqteb122=Survey.all().filter("clas = ",clteb).filter("q22 = ", 5).count()
        nbaqteb123=Survey.all().filter("clas = ",clteb).filter("q22 = ", 6).count()
        nbaqteb124=Survey.all().filter("clas = ",clteb).filter("q22 = ", 7).count()
        nbaqteb125=Survey.all().filter("clas = ",clteb).filter("q22 = ", 8).count()
        nbaqteb126=Survey.all().filter("clas = ",clteb).filter("q22 = ", 9).count()
        nbaqteb127=Survey.all().filter("clas = ",clteb).filter("q22 = ", 10).count()
        
        q2_s_a1te1 = 4*nbaqteb121 + 5*nbaqteb122 + 6*nbaqteb123 + 7*nbaqteb124 + 8*nbaqteb125 + 9*nbaqteb126 + 10*nbaqteb127
        q2_s_ateb = round(q2_s_a1te1/float(teb),2)
        
        nbaqteb131=Survey.all().filter("clas = ",clteb).filter("q23 = ", 4).count()
        nbaqteb132=Survey.all().filter("clas = ",clteb).filter("q23 = ", 5).count()
        nbaqteb133=Survey.all().filter("clas = ",clteb).filter("q23 = ", 6).count()
        nbaqteb134=Survey.all().filter("clas = ",clteb).filter("q23 = ", 7).count()
        nbaqteb135=Survey.all().filter("clas = ",clteb).filter("q23 = ", 8).count()
        nbaqteb136=Survey.all().filter("clas = ",clteb).filter("q23 = ", 9).count()
        nbaqteb137=Survey.all().filter("clas = ",clteb).filter("q23 = ", 10).count()
        
        q2_c_a1te1 = 4*nbaqteb131 + 5*nbaqteb132 + 6*nbaqteb133 + 7*nbaqteb134 + 8*nbaqteb135 + 9*nbaqteb136 + 10*nbaqteb137 
        q2_c_ateb = round(q2_c_a1te1/float(teb),2)
        
        nbaqteb141=Survey.all().filter("clas = ",clteb).filter("q24 = ", 4).count()
        nbaqteb142=Survey.all().filter("clas = ",clteb).filter("q24 = ", 5).count()
        nbaqteb143=Survey.all().filter("clas = ",clteb).filter("q24 = ", 6).count()
        nbaqteb144=Survey.all().filter("clas = ",clteb).filter("q24 = ", 7).count()
        nbaqteb145=Survey.all().filter("clas = ",clteb).filter("q24 = ", 8).count()
        nbaqteb146=Survey.all().filter("clas = ",clteb).filter("q24 = ", 9).count()
        nbaqteb147=Survey.all().filter("clas = ",clteb).filter("q24 = ", 10).count()
        
        q2_l_m1te1 = 4*nbaqteb141 + 5*nbaqteb142 + 6*nbaqteb143 + 7*nbaqteb144 + 8*nbaqteb145 + 9*nbaqteb146 + 10*nbaqteb147 
        q2_l_mteb = round(q2_l_m1te1/float(teb),2)
        
        nbaqteb151=Survey.all().filter("clas = ",clteb).filter("q25 = ", 4).count()
        nbaqteb152=Survey.all().filter("clas = ",clteb).filter("q25 = ", 5).count()
        nbaqteb153=Survey.all().filter("clas = ",clteb).filter("q25 = ", 6).count()
        nbaqteb154=Survey.all().filter("clas = ",clteb).filter("q25 = ", 7).count()
        nbaqteb155=Survey.all().filter("clas = ",clteb).filter("q25 = ", 8).count()
        nbaqteb156=Survey.all().filter("clas = ",clteb).filter("q25 = ", 9).count()
        nbaqteb157=Survey.all().filter("clas = ",clteb).filter("q25 = ", 10).count()
        
        q2_i_c1te1 = 4*nbaqteb151 + 5*nbaqteb152 + 6*nbaqteb153 + 7*nbaqteb154 + 8*nbaqteb155 + 9*nbaqteb156 + 10*nbaqteb157
        q2_i_cteb = round(q2_i_c1te1/float(teb),2) 
            
        nbaqteb161=Survey.all().filter("clas = ",clteb).filter("q26 = ", 4).count()
        nbaqteb162=Survey.all().filter("clas = ",clteb).filter("q26 = ", 5).count()
        nbaqteb163=Survey.all().filter("clas = ",clteb).filter("q26 = ", 6).count()
        nbaqteb164=Survey.all().filter("clas = ",clteb).filter("q26 = ", 7).count()
        nbaqteb165=Survey.all().filter("clas = ",clteb).filter("q26 = ", 8).count()
        nbaqteb166=Survey.all().filter("clas = ",clteb).filter("q26 = ", 9).count()
        nbaqteb167=Survey.all().filter("clas = ",clteb).filter("q26 = ", 10).count()
        
        q2_b_s1te1 = 4*nbaqteb161 + 5*nbaqteb162 + 6*nbaqteb163 + 7*nbaqteb164 + 8*nbaqteb165 + 9*nbaqteb166 + 10*nbaqteb167
        q2_b_steb = round(q2_b_s1te1/float(teb),2)

        soeieteb111=Survey.all().filter("clas = ",clteb).filter("q31 = ", 4).count()
        soeieteb112=Survey.all().filter("clas = ",clteb).filter("q31 = ", 5).count()
        soeieteb113=Survey.all().filter("clas = ",clteb).filter("q31 = ", 6).count()
        soeieteb114=Survey.all().filter("clas = ",clteb).filter("q31 = ", 7).count()
        soeieteb115=Survey.all().filter("clas = ",clteb).filter("q31 = ", 8).count()
        soeieteb116=Survey.all().filter("clas = ",clteb).filter("q31 = ", 9).count()
        soeieteb117=Survey.all().filter("clas = ",clteb).filter("q31 = ", 10).count()
        
        q3_lite1 = 4*soeieteb111 + 5*soeieteb112 + 6*soeieteb113 + 7*soeieteb114 + 8*soeieteb115 + 9*soeieteb116 + 10*soeieteb117
        q3_libteb = round(q3_lite1/float(teb),2)
        
        soeieteb121=Survey.all().filter("clas = ",clteb).filter("q32 = ", 4).count()
        soeieteb122=Survey.all().filter("clas = ",clteb).filter("q32 = ", 5).count()
        soeieteb123=Survey.all().filter("clas = ",clteb).filter("q32 = ", 6).count()
        soeieteb124=Survey.all().filter("clas = ",clteb).filter("q32 = ", 7).count()
        soeieteb125=Survey.all().filter("clas = ",clteb).filter("q32 = ", 8).count()
        soeieteb126=Survey.all().filter("clas = ",clteb).filter("q32 = ", 9).count()
        soeieteb127=Survey.all().filter("clas = ",clteb).filter("q32 = ", 10).count()
        
        q3_i_s1te1 = 4*soeieteb121 + 5*soeieteb122 + 6*soeieteb123 + 7*soeieteb124 + 8*soeieteb125 + 9*soeieteb126 + 10*soeieteb127
        q3_i_steb = round(q3_i_s1te1/float(teb),2)
        
        soeieteb131=Survey.all().filter("clas = ",clteb).filter("q33 = ", 4).count()
        soeieteb132=Survey.all().filter("clas = ",clteb).filter("q33 = ", 5).count()
        soeieteb133=Survey.all().filter("clas = ",clteb).filter("q33 = ", 6).count()
        soeieteb134=Survey.all().filter("clas = ",clteb).filter("q33 = ", 7).count()
        soeieteb135=Survey.all().filter("clas = ",clteb).filter("q33 = ", 8).count()
        soeieteb136=Survey.all().filter("clas = ",clteb).filter("q33 = ", 9).count()
        soeieteb137=Survey.all().filter("clas = ",clteb).filter("q33 = ", 10).count()
        
        q3_con_bo1te1 = 4*soeieteb131 + 5*soeieteb132 + 6*soeieteb133 + 7*soeieteb134 + 8*soeieteb135 + 9*soeieteb136 + 10*soeieteb137 
        q3_con_boteb = round(q3_con_bo1te1/float(teb),2)
        
        soeieteb141=Survey.all().filter("clas = ",clteb).filter("q34 = ", 4).count()
        soeieteb142=Survey.all().filter("clas = ",clteb).filter("q34 = ", 5).count()
        soeieteb143=Survey.all().filter("clas = ",clteb).filter("q34 = ", 6).count()
        soeieteb144=Survey.all().filter("clas = ",clteb).filter("q34 = ", 7).count()
        soeieteb145=Survey.all().filter("clas = ",clteb).filter("q34 = ", 8).count()
        soeieteb146=Survey.all().filter("clas = ",clteb).filter("q34 = ", 9).count()
        soeieteb147=Survey.all().filter("clas = ",clteb).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1te1 = 4*soeieteb141 + 5*soeieteb142 + 6*soeieteb143 + 7*soeieteb144 + 8*soeieteb145 + 9*soeieteb146 + 10*soeieteb147 
        q3_av_ne_verteb =round(q3_av_ne_ver1te1/float(teb),2)
        
        soeieteb151=Survey.all().filter("clas = ",clteb).filter("q35 = ", 4).count()
        soeieteb152=Survey.all().filter("clas = ",clteb).filter("q35 = ", 5).count()
        soeieteb153=Survey.all().filter("clas = ",clteb).filter("q35 = ", 6).count()
        soeieteb154=Survey.all().filter("clas = ",clteb).filter("q35 = ", 7).count()
        soeieteb155=Survey.all().filter("clas = ",clteb).filter("q35 = ", 8).count()
        soeieteb156=Survey.all().filter("clas = ",clteb).filter("q35 = ", 9).count()
        soeieteb157=Survey.all().filter("clas = ",clteb).filter("q35 = ", 10).count()
        
        q3_re_ro1te1 = 4*soeieteb151 + 5*soeieteb152 + 6*soeieteb153 + 7*soeieteb154 + 8*soeieteb155 + 9*soeieteb156 + 10*soeieteb157
        q3_re_roteb = round(q3_re_ro1te1/float(teb),2)
            
        soeieteb161=Survey.all().filter("clas = ",clteb).filter("q36 = ", 4).count()
        soeieteb162=Survey.all().filter("clas = ",clteb).filter("q36 = ", 5).count()
        soeieteb163=Survey.all().filter("clas = ",clteb).filter("q36 = ", 6).count()
        soeieteb164=Survey.all().filter("clas = ",clteb).filter("q36 = ", 7).count()
        soeieteb165=Survey.all().filter("clas = ",clteb).filter("q36 = ", 8).count()
        soeieteb166=Survey.all().filter("clas = ",clteb).filter("q36 = ", 9).count()
        soeieteb167=Survey.all().filter("clas = ",clteb).filter("q36 = ", 10).count()
        
        q3_j_m1te1 = 4*soeieteb161 + 5*soeieteb162 + 6*soeieteb163 + 7*soeieteb164 + 8*soeieteb165 + 9*soeieteb166 + 10*soeieteb167
        q3_j_mteb = round(q3_j_m1te1/float(teb),2)
            
        soeieteb171=Survey.all().filter("clas = ",clteb).filter("q37 = ", 4).count()
        soeieteb172=Survey.all().filter("clas = ",clteb).filter("q37 = ", 5).count()
        soeieteb173=Survey.all().filter("clas = ",clteb).filter("q37 = ", 6).count()
        soeieteb174=Survey.all().filter("clas = ",clteb).filter("q37 = ", 7).count()
        soeieteb175=Survey.all().filter("clas = ",clteb).filter("q37 = ", 8).count()
        soeieteb176=Survey.all().filter("clas = ",clteb).filter("q37 = ", 9).count()
        soeieteb177=Survey.all().filter("clas = ",clteb).filter("q37 = ", 10).count()
        
        q3_sta1te1 = 4*soeieteb171 + 5*soeieteb172 + 6*soeieteb173 + 7*soeieteb174 + 8*soeieteb175 + 9*soeieteb176 + 10*soeieteb177
        q3_stateb = round(q3_sta1te1/float(teb),2)

        obmdteb111=Survey.all().filter("clas = ",clteb).filter("q41 = ", 4).count()
        obmdteb112=Survey.all().filter("clas = ",clteb).filter("q41 = ", 5).count()
        obmdteb113=Survey.all().filter("clas = ",clteb).filter("q41 = ", 6).count()
        obmdteb114=Survey.all().filter("clas = ",clteb).filter("q41 = ", 7).count()
        obmdteb115=Survey.all().filter("clas = ",clteb).filter("q41 = ", 8).count()
        obmdteb116=Survey.all().filter("clas = ",clteb).filter("q41 = ", 9).count()
        obmdteb117=Survey.all().filter("clas = ",clteb).filter("q41 = ", 10).count()
        
        q4_hte1 = 4*obmdteb111 + 5*obmdteb112 + 6*obmdteb113 + 7*obmdteb114 + 8*obmdteb115 + 9*obmdteb116 + 10*obmdteb117
        q4_hy_clteb = round(q4_hte1/float(teb),2)
        
        obmdteb121=Survey.all().filter("clas = ",clteb).filter("q42 = ", 4).count()
        obmdteb122=Survey.all().filter("clas = ",clteb).filter("q42 = ", 5).count()
        obmdteb123=Survey.all().filter("clas = ",clteb).filter("q42 = ", 6).count()
        obmdteb124=Survey.all().filter("clas = ",clteb).filter("q42 = ", 7).count()
        obmdteb125=Survey.all().filter("clas = ",clteb).filter("q42 = ", 8).count()
        obmdteb126=Survey.all().filter("clas = ",clteb).filter("q42 = ", 9).count()
        obmdteb127=Survey.all().filter("clas = ",clteb).filter("q42 = ", 10).count()
        
        q4_men1te1 = 4*obmdteb121 + 5*obmdteb122 + 6*obmdteb123 + 7*obmdteb124 + 8*obmdteb125 + 9*obmdteb126 + 10*obmdteb127
        q4_menteb = round(q4_men1te1/float(teb),2)
        
        obmdteb131=Survey.all().filter("clas = ",clteb).filter("q43 = ", 4).count()
        obmdteb132=Survey.all().filter("clas = ",clteb).filter("q43 = ", 5).count()
        obmdteb133=Survey.all().filter("clas = ",clteb).filter("q43 = ", 6).count()
        obmdteb134=Survey.all().filter("clas = ",clteb).filter("q43 = ", 7).count()
        obmdteb135=Survey.all().filter("clas = ",clteb).filter("q43 = ", 8).count()
        obmdteb136=Survey.all().filter("clas = ",clteb).filter("q43 = ", 9).count()
        obmdteb137=Survey.all().filter("clas = ",clteb).filter("q43 = ", 10).count()
        
        q4_pri1te1 = 4*obmdteb131 + 5*obmdteb132 + 6*obmdteb133 + 7*obmdteb134 + 8*obmdteb135 + 9*obmdteb136 + 10*obmdteb137
        q4_priteb = round(q4_pri1te1/float(teb),2)
        
        obmdteb141=Survey.all().filter("clas = ",clteb).filter("q44 = ", 4).count()
        obmdteb142=Survey.all().filter("clas = ",clteb).filter("q44 = ", 5).count()
        obmdteb143=Survey.all().filter("clas = ",clteb).filter("q44 = ", 6).count()
        obmdteb144=Survey.all().filter("clas = ",clteb).filter("q44 = ", 7).count()
        obmdteb145=Survey.all().filter("clas = ",clteb).filter("q44 = ", 8).count()
        obmdteb146=Survey.all().filter("clas = ",clteb).filter("q44 = ", 9).count()
        obmdteb147=Survey.all().filter("clas = ",clteb).filter("q44 = ", 10).count()
        
        q4_tim_del1te1 = 4*obmdteb141 + 5*obmdteb142 + 6*obmdteb143 + 7*obmdteb144 + 8*obmdteb145 + 9*obmdteb146 + 10*obmdteb147
        q4_tim_delteb = round(q4_tim_del1te1/float(teb),2)
        
        obmdteb151=Survey.all().filter("clas = ",clteb).filter("q45 = ", 4).count()
        obmdteb152=Survey.all().filter("clas = ",clteb).filter("q45 = ", 5).count()
        obmdteb153=Survey.all().filter("clas = ",clteb).filter("q45 = ", 6).count()
        obmdteb154=Survey.all().filter("clas = ",clteb).filter("q45 = ", 7).count()
        obmdteb155=Survey.all().filter("clas = ",clteb).filter("q45 = ", 8).count()
        obmdteb156=Survey.all().filter("clas = ",clteb).filter("q45 = ", 9).count()
        obmdteb157=Survey.all().filter("clas = ",clteb).filter("q45 = ", 10).count()
        
        q4_ser_qua1te1 = 4*obmdteb151 + 5*obmdteb152 + 6*obmdteb153 + 7*obmdteb154 + 8*obmdteb155 + 9*obmdteb156 + 10*obmdteb157
        q4_ser_quateb = round(q4_ser_qua1te1/float(teb),2)

        obhodteb111=Survey.all().filter("clas = ",clteb).filter("q51 = ", 4).count()
        obhodteb112=Survey.all().filter("clas = ",clteb).filter("q51 = ", 5).count()
        obhodteb113=Survey.all().filter("clas = ",clteb).filter("q51 = ", 6).count()
        obhodteb114=Survey.all().filter("clas = ",clteb).filter("q51 = ", 7).count()
        obhodteb115=Survey.all().filter("clas = ",clteb).filter("q51 = ", 8).count()
        obhodteb116=Survey.all().filter("clas = ",clteb).filter("q51 = ", 9).count()
        obhodteb117=Survey.all().filter("clas = ",clteb).filter("q51 = ", 10).count()
        
        q5_rete1 = 4*obhodteb111 + 5*obhodteb112 + 6*obhodteb113 + 7*obhodteb114 + 8*obhodteb115 + 9*obhodteb116 + 10*obhodteb117
        q5_res_adteb = round(q5_rete1/float(teb),2)
        
        obhodteb121=Survey.all().filter("clas = ",clteb).filter("q52 = ", 4).count()
        obhodteb122=Survey.all().filter("clas = ",clteb).filter("q52 = ", 5).count()
        obhodteb123=Survey.all().filter("clas = ",clteb).filter("q52 = ", 6).count()
        obhodteb124=Survey.all().filter("clas = ",clteb).filter("q52 = ", 7).count()
        obhodteb125=Survey.all().filter("clas = ",clteb).filter("q52 = ", 8).count()
        obhodteb126=Survey.all().filter("clas = ",clteb).filter("q52 = ", 9).count()
        obhodteb127=Survey.all().filter("clas = ",clteb).filter("q52 = ", 10).count()
        
        q5_aud1te1 = 4*obhodteb121 + 5*obhodteb122 + 6*obhodteb123 + 7*obhodteb124 + 8*obhodteb125 + 9*obhodteb126 + 10*obhodteb127
        q5_audteb = round(q5_aud1te1/float(teb),2)
        
        obhodteb131=Survey.all().filter("clas = ",clteb).filter("q53 = ", 4).count()
        obhodteb132=Survey.all().filter("clas = ",clteb).filter("q53 = ", 5).count()
        obhodteb133=Survey.all().filter("clas = ",clteb).filter("q53 = ", 6).count()
        obhodteb134=Survey.all().filter("clas = ",clteb).filter("q53 = ", 7).count()
        obhodteb135=Survey.all().filter("clas = ",clteb).filter("q53 = ", 8).count()
        obhodteb136=Survey.all().filter("clas = ",clteb).filter("q53 = ", 9).count()
        obhodteb137=Survey.all().filter("clas = ",clteb).filter("q53 = ", 10).count()
        
        q5_gam1te1 = 4*obhodteb131 + 5*obhodteb132 + 6*obhodteb133 + 7*obhodteb134 + 8*obhodteb135 + 9*obhodteb136 + 10*obhodteb137 
        q5_gamteb = round(q5_gam1te1/float(teb),2)
        
        obhodteb141=Survey.all().filter("clas = ",clteb).filter("q54 = ", 4).count()
        obhodteb142=Survey.all().filter("clas = ",clteb).filter("q54 = ", 5).count()
        obhodteb143=Survey.all().filter("clas = ",clteb).filter("q54 = ", 6).count()
        obhodteb144=Survey.all().filter("clas = ",clteb).filter("q54 = ", 7).count()
        obhodteb145=Survey.all().filter("clas = ",clteb).filter("q54 = ", 8).count()
        obhodteb146=Survey.all().filter("clas = ",clteb).filter("q54 = ", 9).count()
        obhodteb147=Survey.all().filter("clas = ",clteb).filter("q54 = ", 10).count()
        
        q5_info1te1 = 4*obhodteb141 + 5*obhodteb142 + 6*obhodteb143 + 7*obhodteb144 + 8*obhodteb145 + 9*obhodteb146 + 10*obhodteb147 
        q5_infoteb = round(q5_info1te1/float(teb),2)
        
        obhodteb151=Survey.all().filter("clas = ",clteb).filter("q55 = ", 4).count()
        obhodteb152=Survey.all().filter("clas = ",clteb).filter("q55 = ", 5).count()
        obhodteb153=Survey.all().filter("clas = ",clteb).filter("q55 = ", 6).count()
        obhodteb154=Survey.all().filter("clas = ",clteb).filter("q55 = ", 7).count()
        obhodteb155=Survey.all().filter("clas = ",clteb).filter("q55 = ", 8).count()
        obhodteb156=Survey.all().filter("clas = ",clteb).filter("q55 = ", 9).count()
        obhodteb157=Survey.all().filter("clas = ",clteb).filter("q55 = ", 10).count()
        
        q5_dr1te1 = 4*obhodteb151 + 5*obhodteb152 + 6*obhodteb153 + 7*obhodteb154 + 8*obhodteb155 + 9*obhodteb156 + 10*obhodteb157
        q5_drteb = round(q5_dr1te1/float(teb),2)

        obhodteb161=Survey.all().filter("clas = ",clteb).filter("q56 = ", 4).count()
        obhodteb162=Survey.all().filter("clas = ",clteb).filter("q56 = ", 5).count()
        obhodteb163=Survey.all().filter("clas = ",clteb).filter("q56 = ", 6).count()
        obhodteb164=Survey.all().filter("clas = ",clteb).filter("q56 = ", 7).count()
        obhodteb165=Survey.all().filter("clas = ",clteb).filter("q56 = ", 8).count()
        obhodteb166=Survey.all().filter("clas = ",clteb).filter("q56 = ", 9).count()
        obhodteb167=Survey.all().filter("clas = ",clteb).filter("q56 = ", 10).count()
        
        q5_toi1te1 = 4*obhodteb161 + 5*obhodteb162 + 6*obhodteb163 + 7*obhodteb164 + 8*obhodteb165 + 9*obhodteb166 + 10*obhodteb167
        q5_toiteb =round(q5_toi1te1/float(teb),2)
        
        obhodteb171=Survey.all().filter("clas = ",clteb).filter("q57 = ", 4).count()
        obhodteb172=Survey.all().filter("clas = ",clteb).filter("q57 = ", 5).count()
        obhodteb173=Survey.all().filter("clas = ",clteb).filter("q57 = ", 6).count()
        obhodteb174=Survey.all().filter("clas = ",clteb).filter("q57 = ", 7).count()
        obhodteb175=Survey.all().filter("clas = ",clteb).filter("q57 = ", 8).count()
        obhodteb176=Survey.all().filter("clas = ",clteb).filter("q57 = ", 9).count()
        obhodteb177=Survey.all().filter("clas = ",clteb).filter("q57 = ", 10).count()
        
        q5_clean1te1 = 4*obhodteb171 + 5*obhodteb172 + 6*obhodteb173 + 7*obhodteb174 + 8*obhodteb175 + 9*obhodteb176 + 10*obhodteb177
        q5_cleanteb = round(q5_clean1te1/float(teb),2)
        
        obhodteb181=Survey.all().filter("clas = ",clteb).filter("q58 = ", 4).count()
        obhodteb182=Survey.all().filter("clas = ",clteb).filter("q58 = ", 5).count()
        obhodteb183=Survey.all().filter("clas = ",clteb).filter("q58 = ", 6).count()
        obhodteb184=Survey.all().filter("clas = ",clteb).filter("q58 = ", 7).count()
        obhodteb185=Survey.all().filter("clas = ",clteb).filter("q58 = ", 8).count()
        obhodteb186=Survey.all().filter("clas = ",clteb).filter("q58 = ", 9).count()
        obhodteb187=Survey.all().filter("clas = ",clteb).filter("q58 = ", 10).count()
        
        q5_mai1te1 = 4*obhodteb181 + 5*obhodteb182 + 6*obhodteb183 + 7*obhodteb184 + 8*obhodteb185 + 9*obhodteb186 + 10*obhodteb187
        q5_maiteb = round(q5_mai1te1/float(teb),2)


        total_te1 = q5_maiteb + q5_cleanteb + q5_toiteb + q5_drteb + q5_infoteb + q5_gamteb + q5_audteb + q1_condffteb + q1_lightteb + q1_acteb + q1_cleanteb + q2_eq_avteb + q2_s_ateb + q2_c_ateb + q2_l_mteb + q2_i_cteb + q2_b_steb + q3_libteb + q3_i_steb + q3_con_boteb + q3_av_ne_verteb + q3_re_roteb + q3_j_mteb + q3_stateb + q4_hy_clteb + q4_menteb + q4_priteb + q4_tim_delteb + q4_ser_quateb + q5_res_adteb      
        total_teb = round(total_te1,2)
        per_teb = round(10*total_teb/float(30.0),2)

        #BE-A

        clbea = "BE-A"
        bea=Survey.all().filter("clas = ",clbea).count()
        
        gadqbea111=Survey.all().filter("clas = ",clbea).filter("q11 = ", 4).count()
        gadqbea112=Survey.all().filter("clas = ",clbea).filter("q11 = ", 5).count()
        gadqbea113=Survey.all().filter("clas = ",clbea).filter("q11 = ", 6).count()
        gadqbea114=Survey.all().filter("clas = ",clbea).filter("q11 = ", 7).count()
        gadqbea115=Survey.all().filter("clas = ",clbea).filter("q11 = ", 8).count()
        gadqbea116=Survey.all().filter("clas = ",clbea).filter("q11 = ", 9).count()
        gadqbea117=Survey.all().filter("clas = ",clbea).filter("q11 = ", 10).count()
        
        q1_condte1 = 4*gadqbea111 + 5*gadqbea112 + 6*gadqbea113 + 7*gadqbea114 + 8*gadqbea115 + 9*gadqbea116 + 10*gadqbea117
        q1_condffbea = round(q1_condte1/float(bea),2)
        
        gadqbea121=Survey.all().filter("clas = ",clbea).filter("q12 = ", 4).count()
        gadqbea122=Survey.all().filter("clas = ",clbea).filter("q12 = ", 5).count()
        gadqbea123=Survey.all().filter("clas = ",clbea).filter("q12 = ", 6).count()
        gadqbea124=Survey.all().filter("clas = ",clbea).filter("q12 = ", 7).count()
        gadqbea125=Survey.all().filter("clas = ",clbea).filter("q12 = ", 8).count()
        gadqbea126=Survey.all().filter("clas = ",clbea).filter("q12 = ", 9).count()
        gadqbea127=Survey.all().filter("clas = ",clbea).filter("q12 = ", 10).count()
        
        q1_lighte1 = 4*gadqbea121 + 5*gadqbea122 + 6*gadqbea123 + 7*gadqbea124 + 8*gadqbea125 + 9*gadqbea126 + 10*gadqbea127
        q1_lightbea = round(q1_lighte1/float(bea),2)
        
        gadqbea131=Survey.all().filter("clas = ",clbea).filter("q13 = ", 4).count()
        gadqbea132=Survey.all().filter("clas = ",clbea).filter("q13 = ", 5).count()
        gadqbea133=Survey.all().filter("clas = ",clbea).filter("q13 = ", 6).count()
        gadqbea134=Survey.all().filter("clas = ",clbea).filter("q13 = ", 7).count()
        gadqbea135=Survey.all().filter("clas = ",clbea).filter("q13 = ", 8).count()
        gadqbea136=Survey.all().filter("clas = ",clbea).filter("q13 = ", 9).count()
        gadqbea137=Survey.all().filter("clas = ",clbea).filter("q13 = ", 10).count()
        
        q1_ac1te1 = 4*gadqbea131 + 5*gadqbea132 + 6*gadqbea133 + 7*gadqbea134 + 8*gadqbea135 + 9*gadqbea136 + 10*gadqbea137
        q1_acbea = round(q1_ac1te1/float(bea),2)
        
        gadqbea141=Survey.all().filter("clas = ",clbea).filter("q14 = ", 4).count()
        gadqbea142=Survey.all().filter("clas = ",clbea).filter("q14 = ", 5).count()
        gadqbea143=Survey.all().filter("clas = ",clbea).filter("q14 = ", 6).count()
        gadqbea144=Survey.all().filter("clas = ",clbea).filter("q14 = ", 7).count()
        gadqbea145=Survey.all().filter("clas = ",clbea).filter("q14 = ", 8).count()
        gadqbea146=Survey.all().filter("clas = ",clbea).filter("q14 = ", 9).count()
        gadqbea147=Survey.all().filter("clas = ",clbea).filter("q14 = ", 10).count()
        
        q1_clean1te1 = 4*gadqbea141 + 5*gadqbea142 + 6*gadqbea143 + 7*gadqbea144 + 8*gadqbea145 + 9*gadqbea146 + 10*gadqbea147
        q1_cleanbea = round(q1_clean1te1/float(bea),2)
        
        

        nbaqbea111=Survey.all().filter("clas = ",clbea).filter("q21 = ", 4).count()
        nbaqbea112=Survey.all().filter("clas = ",clbea).filter("q21 = ", 5).count()
        nbaqbea113=Survey.all().filter("clas = ",clbea).filter("q21 = ", 6).count()
        nbaqbea114=Survey.all().filter("clas = ",clbea).filter("q21 = ", 7).count()
        nbaqbea115=Survey.all().filter("clas = ",clbea).filter("q21 = ", 8).count()
        nbaqbea116=Survey.all().filter("clas = ",clbea).filter("q21 = ", 9).count()
        nbaqbea117=Survey.all().filter("clas = ",clbea).filter("q21 = ", 10).count()
        
        q2_eate1 = 4*nbaqbea111 + 5*nbaqbea112 + 6*nbaqbea113 + 7*nbaqbea114 + 8*nbaqbea115 + 9*nbaqbea116 + 10*nbaqbea117
        q2_eq_avbea = round(q2_eate1/float(bea),2)
        
        nbaqbea121=Survey.all().filter("clas = ",clbea).filter("q22 = ", 4).count()
        nbaqbea122=Survey.all().filter("clas = ",clbea).filter("q22 = ", 5).count()
        nbaqbea123=Survey.all().filter("clas = ",clbea).filter("q22 = ", 6).count()
        nbaqbea124=Survey.all().filter("clas = ",clbea).filter("q22 = ", 7).count()
        nbaqbea125=Survey.all().filter("clas = ",clbea).filter("q22 = ", 8).count()
        nbaqbea126=Survey.all().filter("clas = ",clbea).filter("q22 = ", 9).count()
        nbaqbea127=Survey.all().filter("clas = ",clbea).filter("q22 = ", 10).count()
        
        q2_s_a1te1 = 4*nbaqbea121 + 5*nbaqbea122 + 6*nbaqbea123 + 7*nbaqbea124 + 8*nbaqbea125 + 9*nbaqbea126 + 10*nbaqbea127
        q2_s_abea = round(q2_s_a1te1/float(bea),2)
        
        nbaqbea131=Survey.all().filter("clas = ",clbea).filter("q23 = ", 4).count()
        nbaqbea132=Survey.all().filter("clas = ",clbea).filter("q23 = ", 5).count()
        nbaqbea133=Survey.all().filter("clas = ",clbea).filter("q23 = ", 6).count()
        nbaqbea134=Survey.all().filter("clas = ",clbea).filter("q23 = ", 7).count()
        nbaqbea135=Survey.all().filter("clas = ",clbea).filter("q23 = ", 8).count()
        nbaqbea136=Survey.all().filter("clas = ",clbea).filter("q23 = ", 9).count()
        nbaqbea137=Survey.all().filter("clas = ",clbea).filter("q23 = ", 10).count()
        
        q2_c_a1te1 = 4*nbaqbea131 + 5*nbaqbea132 + 6*nbaqbea133 + 7*nbaqbea134 + 8*nbaqbea135 + 9*nbaqbea136 + 10*nbaqbea137 
        q2_c_abea = round(q2_c_a1te1/float(bea),2)
        
        nbaqbea141=Survey.all().filter("clas = ",clbea).filter("q24 = ", 4).count()
        nbaqbea142=Survey.all().filter("clas = ",clbea).filter("q24 = ", 5).count()
        nbaqbea143=Survey.all().filter("clas = ",clbea).filter("q24 = ", 6).count()
        nbaqbea144=Survey.all().filter("clas = ",clbea).filter("q24 = ", 7).count()
        nbaqbea145=Survey.all().filter("clas = ",clbea).filter("q24 = ", 8).count()
        nbaqbea146=Survey.all().filter("clas = ",clbea).filter("q24 = ", 9).count()
        nbaqbea147=Survey.all().filter("clas = ",clbea).filter("q24 = ", 10).count()
        
        q2_l_m1te1 = 4*nbaqbea141 + 5*nbaqbea142 + 6*nbaqbea143 + 7*nbaqbea144 + 8*nbaqbea145 + 9*nbaqbea146 + 10*nbaqbea147 
        q2_l_mbea = round(q2_l_m1te1/float(bea),2)
        
        nbaqbea151=Survey.all().filter("clas = ",clbea).filter("q25 = ", 4).count()
        nbaqbea152=Survey.all().filter("clas = ",clbea).filter("q25 = ", 5).count()
        nbaqbea153=Survey.all().filter("clas = ",clbea).filter("q25 = ", 6).count()
        nbaqbea154=Survey.all().filter("clas = ",clbea).filter("q25 = ", 7).count()
        nbaqbea155=Survey.all().filter("clas = ",clbea).filter("q25 = ", 8).count()
        nbaqbea156=Survey.all().filter("clas = ",clbea).filter("q25 = ", 9).count()
        nbaqbea157=Survey.all().filter("clas = ",clbea).filter("q25 = ", 10).count()
        
        q2_i_c1te1 = 4*nbaqbea151 + 5*nbaqbea152 + 6*nbaqbea153 + 7*nbaqbea154 + 8*nbaqbea155 + 9*nbaqbea156 + 10*nbaqbea157
        q2_i_cbea = round(q2_i_c1te1/float(bea),2) 
            
        nbaqbea161=Survey.all().filter("clas = ",clbea).filter("q26 = ", 4).count()
        nbaqbea162=Survey.all().filter("clas = ",clbea).filter("q26 = ", 5).count()
        nbaqbea163=Survey.all().filter("clas = ",clbea).filter("q26 = ", 6).count()
        nbaqbea164=Survey.all().filter("clas = ",clbea).filter("q26 = ", 7).count()
        nbaqbea165=Survey.all().filter("clas = ",clbea).filter("q26 = ", 8).count()
        nbaqbea166=Survey.all().filter("clas = ",clbea).filter("q26 = ", 9).count()
        nbaqbea167=Survey.all().filter("clas = ",clbea).filter("q26 = ", 10).count()
        
        q2_b_s1te1 = 4*nbaqbea161 + 5*nbaqbea162 + 6*nbaqbea163 + 7*nbaqbea164 + 8*nbaqbea165 + 9*nbaqbea166 + 10*nbaqbea167
        q2_b_sbea = round(q2_b_s1te1/float(bea),2)

        soeiebea111=Survey.all().filter("clas = ",clbea).filter("q31 = ", 4).count()
        soeiebea112=Survey.all().filter("clas = ",clbea).filter("q31 = ", 5).count()
        soeiebea113=Survey.all().filter("clas = ",clbea).filter("q31 = ", 6).count()
        soeiebea114=Survey.all().filter("clas = ",clbea).filter("q31 = ", 7).count()
        soeiebea115=Survey.all().filter("clas = ",clbea).filter("q31 = ", 8).count()
        soeiebea116=Survey.all().filter("clas = ",clbea).filter("q31 = ", 9).count()
        soeiebea117=Survey.all().filter("clas = ",clbea).filter("q31 = ", 10).count()
        
        q3_lite1 = 4*soeiebea111 + 5*soeiebea112 + 6*soeiebea113 + 7*soeiebea114 + 8*soeiebea115 + 9*soeiebea116 + 10*soeiebea117
        q3_libbea = round(q3_lite1/float(bea),2)
        
        soeiebea121=Survey.all().filter("clas = ",clbea).filter("q32 = ", 4).count()
        soeiebea122=Survey.all().filter("clas = ",clbea).filter("q32 = ", 5).count()
        soeiebea123=Survey.all().filter("clas = ",clbea).filter("q32 = ", 6).count()
        soeiebea124=Survey.all().filter("clas = ",clbea).filter("q32 = ", 7).count()
        soeiebea125=Survey.all().filter("clas = ",clbea).filter("q32 = ", 8).count()
        soeiebea126=Survey.all().filter("clas = ",clbea).filter("q32 = ", 9).count()
        soeiebea127=Survey.all().filter("clas = ",clbea).filter("q32 = ", 10).count()
        
        q3_i_s1te1 = 4*soeiebea121 + 5*soeiebea122 + 6*soeiebea123 + 7*soeiebea124 + 8*soeiebea125 + 9*soeiebea126 + 10*soeiebea127
        q3_i_sbea = round(q3_i_s1te1/float(bea),2)
        
        soeiebea131=Survey.all().filter("clas = ",clbea).filter("q33 = ", 4).count()
        soeiebea132=Survey.all().filter("clas = ",clbea).filter("q33 = ", 5).count()
        soeiebea133=Survey.all().filter("clas = ",clbea).filter("q33 = ", 6).count()
        soeiebea134=Survey.all().filter("clas = ",clbea).filter("q33 = ", 7).count()
        soeiebea135=Survey.all().filter("clas = ",clbea).filter("q33 = ", 8).count()
        soeiebea136=Survey.all().filter("clas = ",clbea).filter("q33 = ", 9).count()
        soeiebea137=Survey.all().filter("clas = ",clbea).filter("q33 = ", 10).count()
        
        q3_con_bo1te1 = 4*soeiebea131 + 5*soeiebea132 + 6*soeiebea133 + 7*soeiebea134 + 8*soeiebea135 + 9*soeiebea136 + 10*soeiebea137 
        q3_con_bobea = round(q3_con_bo1te1/float(bea),2)
        
        soeiebea141=Survey.all().filter("clas = ",clbea).filter("q34 = ", 4).count()
        soeiebea142=Survey.all().filter("clas = ",clbea).filter("q34 = ", 5).count()
        soeiebea143=Survey.all().filter("clas = ",clbea).filter("q34 = ", 6).count()
        soeiebea144=Survey.all().filter("clas = ",clbea).filter("q34 = ", 7).count()
        soeiebea145=Survey.all().filter("clas = ",clbea).filter("q34 = ", 8).count()
        soeiebea146=Survey.all().filter("clas = ",clbea).filter("q34 = ", 9).count()
        soeiebea147=Survey.all().filter("clas = ",clbea).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1te1 = 4*soeiebea141 + 5*soeiebea142 + 6*soeiebea143 + 7*soeiebea144 + 8*soeiebea145 + 9*soeiebea146 + 10*soeiebea147 
        q3_av_ne_verbea =round(q3_av_ne_ver1te1/float(bea),2)
        
        soeiebea151=Survey.all().filter("clas = ",clbea).filter("q35 = ", 4).count()
        soeiebea152=Survey.all().filter("clas = ",clbea).filter("q35 = ", 5).count()
        soeiebea153=Survey.all().filter("clas = ",clbea).filter("q35 = ", 6).count()
        soeiebea154=Survey.all().filter("clas = ",clbea).filter("q35 = ", 7).count()
        soeiebea155=Survey.all().filter("clas = ",clbea).filter("q35 = ", 8).count()
        soeiebea156=Survey.all().filter("clas = ",clbea).filter("q35 = ", 9).count()
        soeiebea157=Survey.all().filter("clas = ",clbea).filter("q35 = ", 10).count()
        
        q3_re_ro1te1 = 4*soeiebea151 + 5*soeiebea152 + 6*soeiebea153 + 7*soeiebea154 + 8*soeiebea155 + 9*soeiebea156 + 10*soeiebea157
        q3_re_robea = round(q3_re_ro1te1/float(bea),2)
            
        soeiebea161=Survey.all().filter("clas = ",clbea).filter("q36 = ", 4).count()
        soeiebea162=Survey.all().filter("clas = ",clbea).filter("q36 = ", 5).count()
        soeiebea163=Survey.all().filter("clas = ",clbea).filter("q36 = ", 6).count()
        soeiebea164=Survey.all().filter("clas = ",clbea).filter("q36 = ", 7).count()
        soeiebea165=Survey.all().filter("clas = ",clbea).filter("q36 = ", 8).count()
        soeiebea166=Survey.all().filter("clas = ",clbea).filter("q36 = ", 9).count()
        soeiebea167=Survey.all().filter("clas = ",clbea).filter("q36 = ", 10).count()
        
        q3_j_m1te1 = 4*soeiebea161 + 5*soeiebea162 + 6*soeiebea163 + 7*soeiebea164 + 8*soeiebea165 + 9*soeiebea166 + 10*soeiebea167
        q3_j_mbea = round(q3_j_m1te1/float(bea),2)
            
        soeiebea171=Survey.all().filter("clas = ",clbea).filter("q37 = ", 4).count()
        soeiebea172=Survey.all().filter("clas = ",clbea).filter("q37 = ", 5).count()
        soeiebea173=Survey.all().filter("clas = ",clbea).filter("q37 = ", 6).count()
        soeiebea174=Survey.all().filter("clas = ",clbea).filter("q37 = ", 7).count()
        soeiebea175=Survey.all().filter("clas = ",clbea).filter("q37 = ", 8).count()
        soeiebea176=Survey.all().filter("clas = ",clbea).filter("q37 = ", 9).count()
        soeiebea177=Survey.all().filter("clas = ",clbea).filter("q37 = ", 10).count()
        
        q3_sta1te1 = 4*soeiebea171 + 5*soeiebea172 + 6*soeiebea173 + 7*soeiebea174 + 8*soeiebea175 + 9*soeiebea176 + 10*soeiebea177
        q3_stabea = round(q3_sta1te1/float(bea),2)

        obmdbea111=Survey.all().filter("clas = ",clbea).filter("q41 = ", 4).count()
        obmdbea112=Survey.all().filter("clas = ",clbea).filter("q41 = ", 5).count()
        obmdbea113=Survey.all().filter("clas = ",clbea).filter("q41 = ", 6).count()
        obmdbea114=Survey.all().filter("clas = ",clbea).filter("q41 = ", 7).count()
        obmdbea115=Survey.all().filter("clas = ",clbea).filter("q41 = ", 8).count()
        obmdbea116=Survey.all().filter("clas = ",clbea).filter("q41 = ", 9).count()
        obmdbea117=Survey.all().filter("clas = ",clbea).filter("q41 = ", 10).count()
        
        q4_hte1 = 4*obmdbea111 + 5*obmdbea112 + 6*obmdbea113 + 7*obmdbea114 + 8*obmdbea115 + 9*obmdbea116 + 10*obmdbea117
        q4_hy_clbea = round(q4_hte1/float(bea),2)
        
        obmdbea121=Survey.all().filter("clas = ",clbea).filter("q42 = ", 4).count()
        obmdbea122=Survey.all().filter("clas = ",clbea).filter("q42 = ", 5).count()
        obmdbea123=Survey.all().filter("clas = ",clbea).filter("q42 = ", 6).count()
        obmdbea124=Survey.all().filter("clas = ",clbea).filter("q42 = ", 7).count()
        obmdbea125=Survey.all().filter("clas = ",clbea).filter("q42 = ", 8).count()
        obmdbea126=Survey.all().filter("clas = ",clbea).filter("q42 = ", 9).count()
        obmdbea127=Survey.all().filter("clas = ",clbea).filter("q42 = ", 10).count()
        
        q4_men1te1 = 4*obmdbea121 + 5*obmdbea122 + 6*obmdbea123 + 7*obmdbea124 + 8*obmdbea125 + 9*obmdbea126 + 10*obmdbea127
        q4_menbea = round(q4_men1te1/float(bea),2)
        
        obmdbea131=Survey.all().filter("clas = ",clbea).filter("q43 = ", 4).count()
        obmdbea132=Survey.all().filter("clas = ",clbea).filter("q43 = ", 5).count()
        obmdbea133=Survey.all().filter("clas = ",clbea).filter("q43 = ", 6).count()
        obmdbea134=Survey.all().filter("clas = ",clbea).filter("q43 = ", 7).count()
        obmdbea135=Survey.all().filter("clas = ",clbea).filter("q43 = ", 8).count()
        obmdbea136=Survey.all().filter("clas = ",clbea).filter("q43 = ", 9).count()
        obmdbea137=Survey.all().filter("clas = ",clbea).filter("q43 = ", 10).count()
        
        q4_pri1te1 = 4*obmdbea131 + 5*obmdbea132 + 6*obmdbea133 + 7*obmdbea134 + 8*obmdbea135 + 9*obmdbea136 + 10*obmdbea137
        q4_pribea = round(q4_pri1te1/float(bea),2)
        
        obmdbea141=Survey.all().filter("clas = ",clbea).filter("q44 = ", 4).count()
        obmdbea142=Survey.all().filter("clas = ",clbea).filter("q44 = ", 5).count()
        obmdbea143=Survey.all().filter("clas = ",clbea).filter("q44 = ", 6).count()
        obmdbea144=Survey.all().filter("clas = ",clbea).filter("q44 = ", 7).count()
        obmdbea145=Survey.all().filter("clas = ",clbea).filter("q44 = ", 8).count()
        obmdbea146=Survey.all().filter("clas = ",clbea).filter("q44 = ", 9).count()
        obmdbea147=Survey.all().filter("clas = ",clbea).filter("q44 = ", 10).count()
        
        q4_tim_del1te1 = 4*obmdbea141 + 5*obmdbea142 + 6*obmdbea143 + 7*obmdbea144 + 8*obmdbea145 + 9*obmdbea146 + 10*obmdbea147
        q4_tim_delbea = round(q4_tim_del1te1/float(bea),2)
        
        obmdbea151=Survey.all().filter("clas = ",clbea).filter("q45 = ", 4).count()
        obmdbea152=Survey.all().filter("clas = ",clbea).filter("q45 = ", 5).count()
        obmdbea153=Survey.all().filter("clas = ",clbea).filter("q45 = ", 6).count()
        obmdbea154=Survey.all().filter("clas = ",clbea).filter("q45 = ", 7).count()
        obmdbea155=Survey.all().filter("clas = ",clbea).filter("q45 = ", 8).count()
        obmdbea156=Survey.all().filter("clas = ",clbea).filter("q45 = ", 9).count()
        obmdbea157=Survey.all().filter("clas = ",clbea).filter("q45 = ", 10).count()
        
        q4_ser_qua1te1 = 4*obmdbea151 + 5*obmdbea152 + 6*obmdbea153 + 7*obmdbea154 + 8*obmdbea155 + 9*obmdbea156 + 10*obmdbea157
        q4_ser_quabea = round(q4_ser_qua1te1/float(bea),2)

        obhodbea111=Survey.all().filter("clas = ",clbea).filter("q51 = ", 4).count()
        obhodbea112=Survey.all().filter("clas = ",clbea).filter("q51 = ", 5).count()
        obhodbea113=Survey.all().filter("clas = ",clbea).filter("q51 = ", 6).count()
        obhodbea114=Survey.all().filter("clas = ",clbea).filter("q51 = ", 7).count()
        obhodbea115=Survey.all().filter("clas = ",clbea).filter("q51 = ", 8).count()
        obhodbea116=Survey.all().filter("clas = ",clbea).filter("q51 = ", 9).count()
        obhodbea117=Survey.all().filter("clas = ",clbea).filter("q51 = ", 10).count()
        
        q5_rete1 = 4*obhodbea111 + 5*obhodbea112 + 6*obhodbea113 + 7*obhodbea114 + 8*obhodbea115 + 9*obhodbea116 + 10*obhodbea117
        q5_res_adbea = round(q5_rete1/float(bea),2)
        
        obhodbea121=Survey.all().filter("clas = ",clbea).filter("q52 = ", 4).count()
        obhodbea122=Survey.all().filter("clas = ",clbea).filter("q52 = ", 5).count()
        obhodbea123=Survey.all().filter("clas = ",clbea).filter("q52 = ", 6).count()
        obhodbea124=Survey.all().filter("clas = ",clbea).filter("q52 = ", 7).count()
        obhodbea125=Survey.all().filter("clas = ",clbea).filter("q52 = ", 8).count()
        obhodbea126=Survey.all().filter("clas = ",clbea).filter("q52 = ", 9).count()
        obhodbea127=Survey.all().filter("clas = ",clbea).filter("q52 = ", 10).count()
        
        q5_aud1te1 = 4*obhodbea121 + 5*obhodbea122 + 6*obhodbea123 + 7*obhodbea124 + 8*obhodbea125 + 9*obhodbea126 + 10*obhodbea127
        q5_audbea = round(q5_aud1te1/float(bea),2)
        
        obhodbea131=Survey.all().filter("clas = ",clbea).filter("q53 = ", 4).count()
        obhodbea132=Survey.all().filter("clas = ",clbea).filter("q53 = ", 5).count()
        obhodbea133=Survey.all().filter("clas = ",clbea).filter("q53 = ", 6).count()
        obhodbea134=Survey.all().filter("clas = ",clbea).filter("q53 = ", 7).count()
        obhodbea135=Survey.all().filter("clas = ",clbea).filter("q53 = ", 8).count()
        obhodbea136=Survey.all().filter("clas = ",clbea).filter("q53 = ", 9).count()
        obhodbea137=Survey.all().filter("clas = ",clbea).filter("q53 = ", 10).count()
        
        q5_gam1te1 = 4*obhodbea131 + 5*obhodbea132 + 6*obhodbea133 + 7*obhodbea134 + 8*obhodbea135 + 9*obhodbea136 + 10*obhodbea137 
        q5_gambea = round(q5_gam1te1/float(bea),2)
        
        obhodbea141=Survey.all().filter("clas = ",clbea).filter("q54 = ", 4).count()
        obhodbea142=Survey.all().filter("clas = ",clbea).filter("q54 = ", 5).count()
        obhodbea143=Survey.all().filter("clas = ",clbea).filter("q54 = ", 6).count()
        obhodbea144=Survey.all().filter("clas = ",clbea).filter("q54 = ", 7).count()
        obhodbea145=Survey.all().filter("clas = ",clbea).filter("q54 = ", 8).count()
        obhodbea146=Survey.all().filter("clas = ",clbea).filter("q54 = ", 9).count()
        obhodbea147=Survey.all().filter("clas = ",clbea).filter("q54 = ", 10).count()
        
        q5_info1te1 = 4*obhodbea141 + 5*obhodbea142 + 6*obhodbea143 + 7*obhodbea144 + 8*obhodbea145 + 9*obhodbea146 + 10*obhodbea147 
        q5_infobea = round(q5_info1te1/float(bea),2)
        
        obhodbea151=Survey.all().filter("clas = ",clbea).filter("q55 = ", 4).count()
        obhodbea152=Survey.all().filter("clas = ",clbea).filter("q55 = ", 5).count()
        obhodbea153=Survey.all().filter("clas = ",clbea).filter("q55 = ", 6).count()
        obhodbea154=Survey.all().filter("clas = ",clbea).filter("q55 = ", 7).count()
        obhodbea155=Survey.all().filter("clas = ",clbea).filter("q55 = ", 8).count()
        obhodbea156=Survey.all().filter("clas = ",clbea).filter("q55 = ", 9).count()
        obhodbea157=Survey.all().filter("clas = ",clbea).filter("q55 = ", 10).count()
        
        q5_dr1te1 = 4*obhodbea151 + 5*obhodbea152 + 6*obhodbea153 + 7*obhodbea154 + 8*obhodbea155 + 9*obhodbea156 + 10*obhodbea157
        q5_drbea = round(q5_dr1te1/float(bea),2)

        obhodbea161=Survey.all().filter("clas = ",clbea).filter("q56 = ", 4).count()
        obhodbea162=Survey.all().filter("clas = ",clbea).filter("q56 = ", 5).count()
        obhodbea163=Survey.all().filter("clas = ",clbea).filter("q56 = ", 6).count()
        obhodbea164=Survey.all().filter("clas = ",clbea).filter("q56 = ", 7).count()
        obhodbea165=Survey.all().filter("clas = ",clbea).filter("q56 = ", 8).count()
        obhodbea166=Survey.all().filter("clas = ",clbea).filter("q56 = ", 9).count()
        obhodbea167=Survey.all().filter("clas = ",clbea).filter("q56 = ", 10).count()
        
        q5_toi1te1 = 4*obhodbea161 + 5*obhodbea162 + 6*obhodbea163 + 7*obhodbea164 + 8*obhodbea165 + 9*obhodbea166 + 10*obhodbea167
        q5_toibea =round(q5_toi1te1/float(bea),2)
        
        obhodbea171=Survey.all().filter("clas = ",clbea).filter("q57 = ", 4).count()
        obhodbea172=Survey.all().filter("clas = ",clbea).filter("q57 = ", 5).count()
        obhodbea173=Survey.all().filter("clas = ",clbea).filter("q57 = ", 6).count()
        obhodbea174=Survey.all().filter("clas = ",clbea).filter("q57 = ", 7).count()
        obhodbea175=Survey.all().filter("clas = ",clbea).filter("q57 = ", 8).count()
        obhodbea176=Survey.all().filter("clas = ",clbea).filter("q57 = ", 9).count()
        obhodbea177=Survey.all().filter("clas = ",clbea).filter("q57 = ", 10).count()
        
        q5_clean1te1 = 4*obhodbea171 + 5*obhodbea172 + 6*obhodbea173 + 7*obhodbea174 + 8*obhodbea175 + 9*obhodbea176 + 10*obhodbea177
        q5_cleanbea = round(q5_clean1te1/float(bea),2)
        
        obhodbea181=Survey.all().filter("clas = ",clbea).filter("q58 = ", 4).count()
        obhodbea182=Survey.all().filter("clas = ",clbea).filter("q58 = ", 5).count()
        obhodbea183=Survey.all().filter("clas = ",clbea).filter("q58 = ", 6).count()
        obhodbea184=Survey.all().filter("clas = ",clbea).filter("q58 = ", 7).count()
        obhodbea185=Survey.all().filter("clas = ",clbea).filter("q58 = ", 8).count()
        obhodbea186=Survey.all().filter("clas = ",clbea).filter("q58 = ", 9).count()
        obhodbea187=Survey.all().filter("clas = ",clbea).filter("q58 = ", 10).count()
        
        q5_mai1te1 = 4*obhodbea181 + 5*obhodbea182 + 6*obhodbea183 + 7*obhodbea184 + 8*obhodbea185 + 9*obhodbea186 + 10*obhodbea187
        q5_maibea = round(q5_mai1te1/float(bea),2)


        total_be = q5_maibea + q5_cleanbea + q5_toibea + q5_drbea + q5_infobea + q5_gambea + q5_audbea + q1_condffbea + q1_lightbea + q1_acbea + q1_cleanbea + q2_eq_avbea + q2_s_abea + q2_c_abea + q2_l_mbea + q2_i_cbea + q2_b_sbea + q3_libbea + q3_i_sbea + q3_con_bobea + q3_av_ne_verbea + q3_re_robea + q3_j_mbea + q3_stabea + q4_hy_clbea + q4_menbea + q4_pribea + q4_tim_delbea + q4_ser_quabea + q5_res_adbea      
        total_bea = round(total_be,2)
        per_bea = round(10*total_bea/float(30.0),2)

        #BE-B

        clbeb = "BE-B"
        beb=Survey.all().filter("clas = ",clbeb).count()
        
        gadqbeb111=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 4).count()
        gadqbeb112=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 5).count()
        gadqbeb113=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 6).count()
        gadqbeb114=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 7).count()
        gadqbeb115=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 8).count()
        gadqbeb116=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 9).count()
        gadqbeb117=Survey.all().filter("clas = ",clbeb).filter("q11 = ", 10).count()
        
        q1_condbe1 = 4*gadqbeb111 + 5*gadqbeb112 + 6*gadqbeb113 + 7*gadqbeb114 + 8*gadqbeb115 + 9*gadqbeb116 + 10*gadqbeb117
        q1_condffbeb = round(q1_condbe1/float(beb),2)
        
        gadqbeb121=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 4).count()
        gadqbeb122=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 5).count()
        gadqbeb123=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 6).count()
        gadqbeb124=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 7).count()
        gadqbeb125=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 8).count()
        gadqbeb126=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 9).count()
        gadqbeb127=Survey.all().filter("clas = ",clbeb).filter("q12 = ", 10).count()
        
        q1_lighbe1 = 4*gadqbeb121 + 5*gadqbeb122 + 6*gadqbeb123 + 7*gadqbeb124 + 8*gadqbeb125 + 9*gadqbeb126 + 10*gadqbeb127
        q1_lightbeb = round(q1_lighbe1/float(beb),2)
        
        gadqbeb131=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 4).count()
        gadqbeb132=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 5).count()
        gadqbeb133=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 6).count()
        gadqbeb134=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 7).count()
        gadqbeb135=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 8).count()
        gadqbeb136=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 9).count()
        gadqbeb137=Survey.all().filter("clas = ",clbeb).filter("q13 = ", 10).count()
        
        q1_ac1be1 = 4*gadqbeb131 + 5*gadqbeb132 + 6*gadqbeb133 + 7*gadqbeb134 + 8*gadqbeb135 + 9*gadqbeb136 + 10*gadqbeb137
        q1_acbeb = round(q1_ac1be1/float(beb),2)
        
        gadqbeb141=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 4).count()
        gadqbeb142=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 5).count()
        gadqbeb143=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 6).count()
        gadqbeb144=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 7).count()
        gadqbeb145=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 8).count()
        gadqbeb146=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 9).count()
        gadqbeb147=Survey.all().filter("clas = ",clbeb).filter("q14 = ", 10).count()
        
        q1_clean1be1 = 4*gadqbeb141 + 5*gadqbeb142 + 6*gadqbeb143 + 7*gadqbeb144 + 8*gadqbeb145 + 9*gadqbeb146 + 10*gadqbeb147
        q1_cleanbeb = round(q1_clean1be1/float(beb),2)
        
        

        nbaqbeb111=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 4).count()
        nbaqbeb112=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 5).count()
        nbaqbeb113=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 6).count()
        nbaqbeb114=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 7).count()
        nbaqbeb115=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 8).count()
        nbaqbeb116=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 9).count()
        nbaqbeb117=Survey.all().filter("clas = ",clbeb).filter("q21 = ", 10).count()
        
        q2_eabe1 = 4*nbaqbeb111 + 5*nbaqbeb112 + 6*nbaqbeb113 + 7*nbaqbeb114 + 8*nbaqbeb115 + 9*nbaqbeb116 + 10*nbaqbeb117
        q2_eq_avbeb = round(q2_eabe1/float(beb),2)
        
        nbaqbeb121=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 4).count()
        nbaqbeb122=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 5).count()
        nbaqbeb123=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 6).count()
        nbaqbeb124=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 7).count()
        nbaqbeb125=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 8).count()
        nbaqbeb126=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 9).count()
        nbaqbeb127=Survey.all().filter("clas = ",clbeb).filter("q22 = ", 10).count()
        
        q2_s_a1be1 = 4*nbaqbeb121 + 5*nbaqbeb122 + 6*nbaqbeb123 + 7*nbaqbeb124 + 8*nbaqbeb125 + 9*nbaqbeb126 + 10*nbaqbeb127
        q2_s_abeb = round(q2_s_a1be1/float(beb),2)
        
        nbaqbeb131=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 4).count()
        nbaqbeb132=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 5).count()
        nbaqbeb133=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 6).count()
        nbaqbeb134=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 7).count()
        nbaqbeb135=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 8).count()
        nbaqbeb136=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 9).count()
        nbaqbeb137=Survey.all().filter("clas = ",clbeb).filter("q23 = ", 10).count()
        
        q2_c_a1be1 = 4*nbaqbeb131 + 5*nbaqbeb132 + 6*nbaqbeb133 + 7*nbaqbeb134 + 8*nbaqbeb135 + 9*nbaqbeb136 + 10*nbaqbeb137 
        q2_c_abeb = round(q2_c_a1be1/float(beb),2)
        
        nbaqbeb141=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 4).count()
        nbaqbeb142=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 5).count()
        nbaqbeb143=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 6).count()
        nbaqbeb144=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 7).count()
        nbaqbeb145=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 8).count()
        nbaqbeb146=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 9).count()
        nbaqbeb147=Survey.all().filter("clas = ",clbeb).filter("q24 = ", 10).count()
        
        q2_l_m1be1 = 4*nbaqbeb141 + 5*nbaqbeb142 + 6*nbaqbeb143 + 7*nbaqbeb144 + 8*nbaqbeb145 + 9*nbaqbeb146 + 10*nbaqbeb147 
        q2_l_mbeb = round(q2_l_m1be1/float(beb),2)
        
        nbaqbeb151=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 4).count()
        nbaqbeb152=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 5).count()
        nbaqbeb153=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 6).count()
        nbaqbeb154=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 7).count()
        nbaqbeb155=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 8).count()
        nbaqbeb156=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 9).count()
        nbaqbeb157=Survey.all().filter("clas = ",clbeb).filter("q25 = ", 10).count()
        
        q2_i_c1be1 = 4*nbaqbeb151 + 5*nbaqbeb152 + 6*nbaqbeb153 + 7*nbaqbeb154 + 8*nbaqbeb155 + 9*nbaqbeb156 + 10*nbaqbeb157
        q2_i_cbeb = round(q2_i_c1be1/float(beb),2) 
            
        nbaqbeb161=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 4).count()
        nbaqbeb162=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 5).count()
        nbaqbeb163=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 6).count()
        nbaqbeb164=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 7).count()
        nbaqbeb165=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 8).count()
        nbaqbeb166=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 9).count()
        nbaqbeb167=Survey.all().filter("clas = ",clbeb).filter("q26 = ", 10).count()
        
        q2_b_s1be1 = 4*nbaqbeb161 + 5*nbaqbeb162 + 6*nbaqbeb163 + 7*nbaqbeb164 + 8*nbaqbeb165 + 9*nbaqbeb166 + 10*nbaqbeb167
        q2_b_sbeb = round(q2_b_s1be1/float(beb),2)

        soeiebeb111=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 4).count()
        soeiebeb112=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 5).count()
        soeiebeb113=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 6).count()
        soeiebeb114=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 7).count()
        soeiebeb115=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 8).count()
        soeiebeb116=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 9).count()
        soeiebeb117=Survey.all().filter("clas = ",clbeb).filter("q31 = ", 10).count()
        
        q3_libe1 = 4*soeiebeb111 + 5*soeiebeb112 + 6*soeiebeb113 + 7*soeiebeb114 + 8*soeiebeb115 + 9*soeiebeb116 + 10*soeiebeb117
        q3_libbeb = round(q3_libe1/float(beb),2)
        
        soeiebeb121=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 4).count()
        soeiebeb122=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 5).count()
        soeiebeb123=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 6).count()
        soeiebeb124=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 7).count()
        soeiebeb125=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 8).count()
        soeiebeb126=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 9).count()
        soeiebeb127=Survey.all().filter("clas = ",clbeb).filter("q32 = ", 10).count()
        
        q3_i_s1be1 = 4*soeiebeb121 + 5*soeiebeb122 + 6*soeiebeb123 + 7*soeiebeb124 + 8*soeiebeb125 + 9*soeiebeb126 + 10*soeiebeb127
        q3_i_sbeb = round(q3_i_s1be1/float(beb),2)
        
        soeiebeb131=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 4).count()
        soeiebeb132=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 5).count()
        soeiebeb133=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 6).count()
        soeiebeb134=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 7).count()
        soeiebeb135=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 8).count()
        soeiebeb136=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 9).count()
        soeiebeb137=Survey.all().filter("clas = ",clbeb).filter("q33 = ", 10).count()
        
        q3_con_bo1be1 = 4*soeiebeb131 + 5*soeiebeb132 + 6*soeiebeb133 + 7*soeiebeb134 + 8*soeiebeb135 + 9*soeiebeb136 + 10*soeiebeb137 
        q3_con_bobeb = round(q3_con_bo1be1/float(beb),2)
        
        soeiebeb141=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 4).count()
        soeiebeb142=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 5).count()
        soeiebeb143=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 6).count()
        soeiebeb144=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 7).count()
        soeiebeb145=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 8).count()
        soeiebeb146=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 9).count()
        soeiebeb147=Survey.all().filter("clas = ",clbeb).filter("q34 = ", 10).count()
        
        q3_av_ne_ver1be1 = 4*soeiebeb141 + 5*soeiebeb142 + 6*soeiebeb143 + 7*soeiebeb144 + 8*soeiebeb145 + 9*soeiebeb146 + 10*soeiebeb147 
        q3_av_ne_verbeb =round(q3_av_ne_ver1be1/float(beb),2)
        
        soeiebeb151=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 4).count()
        soeiebeb152=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 5).count()
        soeiebeb153=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 6).count()
        soeiebeb154=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 7).count()
        soeiebeb155=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 8).count()
        soeiebeb156=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 9).count()
        soeiebeb157=Survey.all().filter("clas = ",clbeb).filter("q35 = ", 10).count()
        
        q3_re_ro1be1 = 4*soeiebeb151 + 5*soeiebeb152 + 6*soeiebeb153 + 7*soeiebeb154 + 8*soeiebeb155 + 9*soeiebeb156 + 10*soeiebeb157
        q3_re_robeb = round(q3_re_ro1be1/float(beb),2)
            
        soeiebeb161=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 4).count()
        soeiebeb162=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 5).count()
        soeiebeb163=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 6).count()
        soeiebeb164=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 7).count()
        soeiebeb165=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 8).count()
        soeiebeb166=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 9).count()
        soeiebeb167=Survey.all().filter("clas = ",clbeb).filter("q36 = ", 10).count()
        
        q3_j_m1be1 = 4*soeiebeb161 + 5*soeiebeb162 + 6*soeiebeb163 + 7*soeiebeb164 + 8*soeiebeb165 + 9*soeiebeb166 + 10*soeiebeb167
        q3_j_mbeb = round(q3_j_m1be1/float(beb),2)
            
        soeiebeb171=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 4).count()
        soeiebeb172=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 5).count()
        soeiebeb173=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 6).count()
        soeiebeb174=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 7).count()
        soeiebeb175=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 8).count()
        soeiebeb176=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 9).count()
        soeiebeb177=Survey.all().filter("clas = ",clbeb).filter("q37 = ", 10).count()
        
        q3_sta1be1 = 4*soeiebeb171 + 5*soeiebeb172 + 6*soeiebeb173 + 7*soeiebeb174 + 8*soeiebeb175 + 9*soeiebeb176 + 10*soeiebeb177
        q3_stabeb = round(q3_sta1be1/float(beb),2)

        obmdbeb111=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 4).count()
        obmdbeb112=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 5).count()
        obmdbeb113=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 6).count()
        obmdbeb114=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 7).count()
        obmdbeb115=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 8).count()
        obmdbeb116=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 9).count()
        obmdbeb117=Survey.all().filter("clas = ",clbeb).filter("q41 = ", 10).count()
        
        q4_hbe1 = 4*obmdbeb111 + 5*obmdbeb112 + 6*obmdbeb113 + 7*obmdbeb114 + 8*obmdbeb115 + 9*obmdbeb116 + 10*obmdbeb117
        q4_hy_clbeb = round(q4_hbe1/float(beb),2)
        
        obmdbeb121=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 4).count()
        obmdbeb122=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 5).count()
        obmdbeb123=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 6).count()
        obmdbeb124=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 7).count()
        obmdbeb125=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 8).count()
        obmdbeb126=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 9).count()
        obmdbeb127=Survey.all().filter("clas = ",clbeb).filter("q42 = ", 10).count()
        
        q4_men1be1 = 4*obmdbeb121 + 5*obmdbeb122 + 6*obmdbeb123 + 7*obmdbeb124 + 8*obmdbeb125 + 9*obmdbeb126 + 10*obmdbeb127
        q4_menbeb = round(q4_men1be1/float(beb),2)
        
        obmdbeb131=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 4).count()
        obmdbeb132=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 5).count()
        obmdbeb133=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 6).count()
        obmdbeb134=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 7).count()
        obmdbeb135=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 8).count()
        obmdbeb136=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 9).count()
        obmdbeb137=Survey.all().filter("clas = ",clbeb).filter("q43 = ", 10).count()
        
        q4_pri1be1 = 4*obmdbeb131 + 5*obmdbeb132 + 6*obmdbeb133 + 7*obmdbeb134 + 8*obmdbeb135 + 9*obmdbeb136 + 10*obmdbeb137
        q4_pribeb = round(q4_pri1be1/float(beb),2)
        
        obmdbeb141=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 4).count()
        obmdbeb142=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 5).count()
        obmdbeb143=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 6).count()
        obmdbeb144=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 7).count()
        obmdbeb145=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 8).count()
        obmdbeb146=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 9).count()
        obmdbeb147=Survey.all().filter("clas = ",clbeb).filter("q44 = ", 10).count()
        
        q4_tim_del1be1 = 4*obmdbeb141 + 5*obmdbeb142 + 6*obmdbeb143 + 7*obmdbeb144 + 8*obmdbeb145 + 9*obmdbeb146 + 10*obmdbeb147
        q4_tim_delbeb = round(q4_tim_del1be1/float(beb),2)
        
        obmdbeb151=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 4).count()
        obmdbeb152=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 5).count()
        obmdbeb153=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 6).count()
        obmdbeb154=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 7).count()
        obmdbeb155=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 8).count()
        obmdbeb156=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 9).count()
        obmdbeb157=Survey.all().filter("clas = ",clbeb).filter("q45 = ", 10).count()
        
        q4_ser_qua1be1 = 4*obmdbeb151 + 5*obmdbeb152 + 6*obmdbeb153 + 7*obmdbeb154 + 8*obmdbeb155 + 9*obmdbeb156 + 10*obmdbeb157
        q4_ser_quabeb = round(q4_ser_qua1be1/float(beb),2)

        obhodbeb111=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 4).count()
        obhodbeb112=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 5).count()
        obhodbeb113=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 6).count()
        obhodbeb114=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 7).count()
        obhodbeb115=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 8).count()
        obhodbeb116=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 9).count()
        obhodbeb117=Survey.all().filter("clas = ",clbeb).filter("q51 = ", 10).count()
        
        q5_rebe1 = 4*obhodbeb111 + 5*obhodbeb112 + 6*obhodbeb113 + 7*obhodbeb114 + 8*obhodbeb115 + 9*obhodbeb116 + 10*obhodbeb117
        q5_res_adbeb = round(q5_rebe1/float(beb),2)
        
        obhodbeb121=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 4).count()
        obhodbeb122=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 5).count()
        obhodbeb123=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 6).count()
        obhodbeb124=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 7).count()
        obhodbeb125=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 8).count()
        obhodbeb126=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 9).count()
        obhodbeb127=Survey.all().filter("clas = ",clbeb).filter("q52 = ", 10).count()
        
        q5_aud1be1 = 4*obhodbeb121 + 5*obhodbeb122 + 6*obhodbeb123 + 7*obhodbeb124 + 8*obhodbeb125 + 9*obhodbeb126 + 10*obhodbeb127
        q5_audbeb = round(q5_aud1be1/float(beb),2)
        
        obhodbeb131=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 4).count()
        obhodbeb132=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 5).count()
        obhodbeb133=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 6).count()
        obhodbeb134=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 7).count()
        obhodbeb135=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 8).count()
        obhodbeb136=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 9).count()
        obhodbeb137=Survey.all().filter("clas = ",clbeb).filter("q53 = ", 10).count()
        
        q5_gam1be1 = 4*obhodbeb131 + 5*obhodbeb132 + 6*obhodbeb133 + 7*obhodbeb134 + 8*obhodbeb135 + 9*obhodbeb136 + 10*obhodbeb137 
        q5_gambeb = round(q5_gam1be1/float(beb),2)
        
        obhodbeb141=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 4).count()
        obhodbeb142=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 5).count()
        obhodbeb143=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 6).count()
        obhodbeb144=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 7).count()
        obhodbeb145=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 8).count()
        obhodbeb146=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 9).count()
        obhodbeb147=Survey.all().filter("clas = ",clbeb).filter("q54 = ", 10).count()
        
        q5_info1be1 = 4*obhodbeb141 + 5*obhodbeb142 + 6*obhodbeb143 + 7*obhodbeb144 + 8*obhodbeb145 + 9*obhodbeb146 + 10*obhodbeb147 
        q5_infobeb = round(q5_info1be1/float(beb),2)
        
        obhodbeb151=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 4).count()
        obhodbeb152=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 5).count()
        obhodbeb153=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 6).count()
        obhodbeb154=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 7).count()
        obhodbeb155=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 8).count()
        obhodbeb156=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 9).count()
        obhodbeb157=Survey.all().filter("clas = ",clbeb).filter("q55 = ", 10).count()
        
        q5_dr1be1 = 4*obhodbeb151 + 5*obhodbeb152 + 6*obhodbeb153 + 7*obhodbeb154 + 8*obhodbeb155 + 9*obhodbeb156 + 10*obhodbeb157
        q5_drbeb = round(q5_dr1be1/float(beb),2)

        obhodbeb161=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 4).count()
        obhodbeb162=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 5).count()
        obhodbeb163=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 6).count()
        obhodbeb164=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 7).count()
        obhodbeb165=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 8).count()
        obhodbeb166=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 9).count()
        obhodbeb167=Survey.all().filter("clas = ",clbeb).filter("q56 = ", 10).count()
        
        q5_toi1be1 = 4*obhodbeb161 + 5*obhodbeb162 + 6*obhodbeb163 + 7*obhodbeb164 + 8*obhodbeb165 + 9*obhodbeb166 + 10*obhodbeb167
        q5_toibeb =round(q5_toi1be1/float(beb),2)
        
        obhodbeb171=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 4).count()
        obhodbeb172=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 5).count()
        obhodbeb173=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 6).count()
        obhodbeb174=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 7).count()
        obhodbeb175=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 8).count()
        obhodbeb176=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 9).count()
        obhodbeb177=Survey.all().filter("clas = ",clbeb).filter("q57 = ", 10).count()
        
        q5_clean1be1 = 4*obhodbeb171 + 5*obhodbeb172 + 6*obhodbeb173 + 7*obhodbeb174 + 8*obhodbeb175 + 9*obhodbeb176 + 10*obhodbeb177
        q5_cleanbeb = round(q5_clean1be1/float(beb),2)
        
        obhodbeb181=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 4).count()
        obhodbeb182=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 5).count()
        obhodbeb183=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 6).count()
        obhodbeb184=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 7).count()
        obhodbeb185=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 8).count()
        obhodbeb186=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 9).count()
        obhodbeb187=Survey.all().filter("clas = ",clbeb).filter("q58 = ", 10).count()
        
        q5_mai1be1 = 4*obhodbeb181 + 5*obhodbeb182 + 6*obhodbeb183 + 7*obhodbeb184 + 8*obhodbeb185 + 9*obhodbeb186 + 10*obhodbeb187
        q5_maibeb = round(q5_mai1be1/float(beb),2)


        total_be1 = q5_maibeb + q5_cleanbeb + q5_toibeb + q5_drbeb + q5_infobeb + q5_gambeb + q5_audbeb + q1_condffbeb + q1_lightbeb + q1_acbeb + q1_cleanbeb + q2_eq_avbeb + q2_s_abeb + q2_c_abeb + q2_l_mbeb + q2_i_cbeb + q2_b_sbeb + q3_libbeb + q3_i_sbeb + q3_con_bobeb + q3_av_ne_verbeb + q3_re_robeb + q3_j_mbeb + q3_stabeb + q4_hy_clbeb + q4_menbeb + q4_pribeb + q4_tim_delbeb + q4_ser_quabeb + q5_res_adbeb      
        total_beb = round(total_be1,2)
        per_beb = round(10*total_beb/float(30.0),2)




        
            
        self.render("admin.html" ,**{
                                       'total_sea':total_sea,'per_sea':per_sea,
                                        
                                       'q1_condff':q1_condff,'q1_light':q1_light,'q1_ac':q1_ac,
                                       'q1_clean':q1_clean,'q2_eq_av':q2_eq_av,'q2_s_a':q2_s_a,'q2_c_a':q2_c_a,'q2_l_m':q2_l_m ,
                                       'q2_i_c':q2_i_c,'q2_b_s':q2_b_s,
                                       'q3_lib':q3_lib,'q3_i_s':q3_i_s,'q3_con_bo':q3_con_bo,
                                       'q3_av_ne_ver':q3_av_ne_ver,'q3_re_ro':q3_re_ro,
                                       'q3_j_m':q3_j_m,'q3_sta':q3_sta,'q4_hy_cl':q4_hy_cl,
                                       'q4_men':q4_men,'q4_pri':q4_pri,
                                       'q4_tim_del':q4_tim_del,'q4_ser_qua':q4_ser_qua,'q5_res_ad':q5_res_ad,
                                       'q5_aud':q5_aud,'q5_gam':q5_gam, 'q5_info':q5_info,'q5_dr':q5_dr,'q5_toi':q5_toi,
                                       'q5_clean':q5_clean,'q5_mai':q5_mai,

                                       'total_seb':total_seb,'per_seb':per_seb,
                                        
                                       'q1_condffseb':q1_condffseb,'q1_lightseb':q1_lightseb,'q1_acseb':q1_acseb,
                                       'q1_cleanseb':q1_cleanseb,'q2_eq_avseb':q2_eq_avseb,'q2_s_aseb':q2_s_aseb,'q2_c_aseb':q2_c_aseb,'q2_l_mseb':q2_l_mseb ,
                                       'q2_i_cseb':q2_i_cseb,'q2_b_sseb':q2_b_sseb,
                                       'q3_libseb':q3_libseb,'q3_i_sseb':q3_i_sseb,'q3_con_boseb':q3_con_boseb,
                                       'q3_av_ne_verseb':q3_av_ne_verseb,'q3_re_roseb':q3_re_roseb,
                                       'q3_j_mseb':q3_j_mseb,'q3_staseb':q3_staseb,'q4_hy_clseb':q4_hy_clseb,
                                       'q4_menseb':q4_menseb,'q4_priseb':q4_priseb,
                                       'q4_tim_delseb':q4_tim_delseb,'q4_ser_quaseb':q4_ser_quaseb,'q5_res_adseb':q5_res_adseb,
                                       'q5_audseb':q5_audseb,'q5_gamseb':q5_gamseb, 'q5_infoseb':q5_infoseb,'q5_drseb':q5_drseb,'q5_toiseb':q5_toiseb,
                                       'q5_cleanseb':q5_cleanseb,'q5_maiseb':q5_maiseb,

                                       'total_tea':total_tea,'per_tea':per_tea,
                                        
                                       'q1_condfftea':q1_condfftea,'q1_lighttea':q1_lighttea,'q1_actea':q1_actea,
                                       'q1_cleantea':q1_cleantea,'q2_eq_avtea':q2_eq_avtea,'q2_s_atea':q2_s_atea,'q2_c_atea':q2_c_atea,'q2_l_mtea':q2_l_mtea ,
                                       'q2_i_ctea':q2_i_ctea,'q2_b_stea':q2_b_stea,
                                       'q3_libtea':q3_libtea,'q3_i_stea':q3_i_stea,'q3_con_botea':q3_con_botea,
                                       'q3_av_ne_vertea':q3_av_ne_vertea,'q3_re_rotea':q3_re_rotea,
                                       'q3_j_mtea':q3_j_mtea,'q3_statea':q3_statea,'q4_hy_cltea':q4_hy_cltea,
                                       'q4_mentea':q4_mentea,'q4_pritea':q4_pritea,
                                       'q4_tim_deltea':q4_tim_deltea,'q4_ser_quatea':q4_ser_quatea,'q5_res_adtea':q5_res_adtea,
                                       'q5_audtea':q5_audtea,'q5_gamtea':q5_gamtea, 'q5_infotea':q5_infotea,'q5_drtea':q5_drtea,'q5_toitea':q5_toitea,
                                       'q5_cleantea':q5_cleantea,'q5_maitea':q5_maitea,

                                       'total_teb':total_teb,'per_teb':per_teb,
                                        
                                       'q1_condffteb':q1_condffteb,'q1_lightteb':q1_lightteb,'q1_acteb':q1_acteb,
                                       'q1_cleanteb':q1_cleanteb,'q2_eq_avteb':q2_eq_avteb,'q2_s_ateb':q2_s_ateb,'q2_c_ateb':q2_c_ateb,'q2_l_mteb':q2_l_mteb ,
                                       'q2_i_cteb':q2_i_cteb,'q2_b_steb':q2_b_steb,
                                       'q3_libteb':q3_libteb,'q3_i_steb':q3_i_steb,'q3_con_boteb':q3_con_boteb,
                                       'q3_av_ne_verteb':q3_av_ne_verteb,'q3_re_roteb':q3_re_roteb,
                                       'q3_j_mteb':q3_j_mteb,'q3_stateb':q3_stateb,'q4_hy_clteb':q4_hy_clteb,
                                       'q4_menteb':q4_menteb,'q4_priteb':q4_priteb,
                                       'q4_tim_delteb':q4_tim_delteb,'q4_ser_quateb':q4_ser_quateb,'q5_res_adteb':q5_res_adteb,
                                       'q5_audteb':q5_audteb,'q5_gamteb':q5_gamteb, 'q5_infoteb':q5_infoteb,'q5_drteb':q5_drteb,'q5_toiteb':q5_toiteb,
                                       'q5_cleanteb':q5_cleanteb,'q5_maiteb':q5_maiteb,

                                       'total_bea':total_bea,'per_bea':per_bea,
                                        
                                       'q1_condffbea':q1_condffbea,'q1_lightbea':q1_lightbea,'q1_acbea':q1_acbea,
                                       'q1_cleanbea':q1_cleanbea,'q2_eq_avbea':q2_eq_avbea,'q2_s_abea':q2_s_abea,'q2_c_abea':q2_c_abea,'q2_l_mbea':q2_l_mbea ,
                                       'q2_i_cbea':q2_i_cbea,'q2_b_sbea':q2_b_sbea,
                                       'q3_libbea':q3_libbea,'q3_i_sbea':q3_i_sbea,'q3_con_bobea':q3_con_bobea,
                                       'q3_av_ne_verbea':q3_av_ne_verbea,'q3_re_robea':q3_re_robea,
                                       'q3_j_mbea':q3_j_mbea,'q3_stabea':q3_stabea,'q4_hy_clbea':q4_hy_clbea,
                                       'q4_menbea':q4_menbea,'q4_pribea':q4_pribea,
                                       'q4_tim_delbea':q4_tim_delbea,'q4_ser_quabea':q4_ser_quabea,'q5_res_adbea':q5_res_adbea,
                                       'q5_audbea':q5_audbea,'q5_gambea':q5_gambea, 'q5_infobea':q5_infobea,'q5_drbea':q5_drbea,'q5_toibea':q5_toibea,
                                       'q5_cleanbea':q5_cleanbea,'q5_maibea':q5_maibea,

                                       'total_beb':total_beb,'per_beb':per_beb,
                                        
                                       'q1_condffbeb':q1_condffbeb,'q1_lightbeb':q1_lightbeb,'q1_acbeb':q1_acbeb,
                                       'q1_cleanbeb':q1_cleanbeb,'q2_eq_avbeb':q2_eq_avbeb,'q2_s_abeb':q2_s_abeb,'q2_c_abeb':q2_c_abeb,'q2_l_mbeb':q2_l_mbeb ,
                                       'q2_i_cbeb':q2_i_cbeb,'q2_b_sbeb':q2_b_sbeb,
                                       'q3_libbeb':q3_libbeb,'q3_i_sbeb':q3_i_sbeb,'q3_con_bobeb':q3_con_bobeb,
                                       'q3_av_ne_verbeb':q3_av_ne_verbeb,'q3_re_robeb':q3_re_robeb,
                                       'q3_j_mbeb':q3_j_mbeb,'q3_stabeb':q3_stabeb,'q4_hy_clbeb':q4_hy_clbeb,
                                       'q4_menbeb':q4_menbeb,'q4_pribeb':q4_pribeb,
                                       'q4_tim_delbeb':q4_tim_delbeb,'q4_ser_quabeb':q4_ser_quabeb,'q5_res_adbeb':q5_res_adbeb,
                                       'q5_audbeb':q5_audbeb,'q5_gambeb':q5_gambeb, 'q5_infobeb':q5_infobeb,'q5_drbeb':q5_drbeb,'q5_toibeb':q5_toibeb,
                                       'q5_cleanbeb':q5_cleanbeb,'q5_maibeb':q5_maibeb
                                      })



app = webapp2.WSGIApplication([('/', MainPage),
                               ('/admin', AdminPage),
                              
                               ('/thanks', ThankYou),], debug=True)
