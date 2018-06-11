from flask import Flask, render_template, request
import sort1

sample_data = ['sodium chloride','bismuth','phosphoric acid','ferric chloride','1,3-Dimethylamylamine', 'acetic acid'
     'alpha-galactosidase','erythro-dibromide','erythomycin', 'trans-2\'-Bromostyrene',
     'threo-2 3-dibromo-3-phenylpropanoic acid','2,3-Dibromo-3-phenylpropanoic acid']

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    unsorted_items = None
    sorted_items = "none"
    if request.method == "POST":
        unsorted_items = request.form.get('unsorted_items')
        mylist = unsorted_items.split('\n')
        sort1.bubbleSort(mylist)
        sorted_items = '\n'.join(mylist)
    
    
    if unsorted_items is None:
        unsorted_items = '\n'.join(sample_data)
        
    return render_template('index.html', unsorted_items=unsorted_items, sorted_items=sorted_items)

if __name__ == '__main__':
    app.run()