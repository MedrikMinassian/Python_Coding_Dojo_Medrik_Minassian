from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')          

def index():
    return render_templates ('index.html')

if __name__== "__main__":       
    app.run(debug=True, port=5001)

if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

