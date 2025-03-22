import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_utilization  = psutil.cpu_percent()
    memory_utilization  =  psutil.virtual_memory().percent
    Message  =  None
    if cpu_utilization > 80 or memory_utilization >80:
        Message = "Memory or Cpu Utilization is higher please scale up"
    return render_template("index.html",cpu_metric=cpu_utilization,mem_metric= memory_utilization,message =Message)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')
