from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

# ----------------------------To convert capital letter------------------------------------------------
@app.route('/capitalize')
def capitalize_template():
    return render_template('capitalize.html')
    

@app.route('/capitalize',methods=['POST','GET'])
def capital():
    result1=''
    string=request.form['string']  
    result1=string.capitalize()
    result2=string.upper()
    return render_template('capitalize.html',**locals())

#-----------------------------------------For concatenate strings----------------------------------------------------------------

@app.route('/concatenate')
def concatenate_template():
    return render_template('concatenate.html')

@app.route('/concatenate',methods=['post','get'])
def concatenate():
    string1=request.form['constr']
    string2=request.form['constr1']
    concate_strings=string1+" "+string2
    return render_template('concatenate.html',concate_strings=concate_strings)

#--------------------------------------------Uppercase Conversion----------------------------------------------------------------
@app.route('/uppercase')
def uppercase_template():
    return render_template('uppercase.html')

@app.route('/uppercase',methods=['POST'])
def upper_case():
    string=request.form['upper']
    string_upper=string.upper()
    return render_template('uppercase.html',string_upper=string_upper)
#---------------------------------------------Lowercase Conversion------------------------------------------------------------------------------------------

@app.route('/lowercase')
def lowercase_template():
    return render_template('lowercase.html')

@app.route('/lowercase',methods=['POST'])
def lowercase():
    string=request.form['lower']
    string_lower=string.lower()
    return render_template('lowercase.html',string_lower=string_lower)

#----------------------------------------------Replace string/character-----------------------------------------------------------------------

@app.route('/replace')
def replace_template():
    return render_template('replace.html')

@app.route('/replace',methods=['POST'])
def replace():
    string=request.form['str_replace']
    r_str1=request.form['str_replace1']
    r_str2=request.form['str_replace2']
    replaced_string=string.replace(r_str1,r_str2)
    return render_template('replace.html',replaced_string=replaced_string)

#----------------------------------------compare two strings----------------------------------------------------------------------------------------

@app.route('/compare')
def compare_template():
    return render_template('compare.html')

@app.route('/compare',methods=['POST'])
def compare():
    str1=request.form['str1']
    str2=request.form['str2']
    str3=str1.lower()
    str4=str2.lower()
    if str1==str2 and str3==str4:
             return render_template('compare.html',letter_wise='Strings are equal',meaning_wise="Strings are equal")
    elif str1!=str2 and str3==str4:
           return render_template('compare.html',letter_wise="Strings are not equal",meaning_wise="Strings are equal")
    elif str1!=str2 and str3!=str4:
            return render_template('compare.html',letter_wise="Strings are not equal",meaning_wise="Strings are not equal")

#----------------------------------------------------------Remove spaces-----------------------------------------------------------------------------    
@app.route('/spaces')
def spaces_template():
    return render_template('removespaces.html')

@app.route('/spaces',methods=['post'])
def spaces():
    str1=request.form['str']
    spaces1=str1.strip()
    spaces2=str1.replace(" ","")
    return render_template('removespaces.html',spaces1=spaces1,spaces2=spaces2)

#----------------------------------------------Length operations------------------------------------------------------------------------------------------------
@app.route('/length')
def length_template():
    return render_template('length.html')

@app.route('/length',methods=['post'])
def length():
    string=request.form['str1']
    length1=len(string)
    length2=len([i for i in string if i.isalpha()])
    length3=len(string.strip().split(" "))
    length4=len([i for i in string if i.isnumeric()])
    return render_template('length.html',length1=length1,length2=length2,length3=length3,length4=length4)

#-------------------------------------Reverse operation------------------------------------------------------------------------------------------------------
@app.route('/reverse')
def reverse_template():
    return render_template('reverse.html')

@app.route('/reverse',methods=['post'])
def reverse():
    str=request.form['str']
    result1=str[::-1]
    result2=str.split()[::-1]
    result2=" ".join(result2)
    return render_template('reverse.html',result1=result1,result2=result2)

#----------------------------------------Slicing operations-------------------------------------------------------------------------------------------------------------------------

@app.route('/slicing')
def slicing_template():
    return render_template('slicing.html')

@app.route('/slicing',methods=['post'])
def slicing():
    str=request.form['str']
    start=int(request.form['start'])
    end=int(request.form['end'])
    steps=int(request.form['steps'])
    sliced_str=str[start:end:steps]
    print(str)
    print(start)
    return render_template('slicing.html',sliced_str=sliced_str)

#----------------------------------------------About----------------------------------------------------------------------------------------
@app.route('/about')
def about():
    return render_template("about.html")

























































































if __name__=="__main__":
    app.run(debug=True)