from flask import Flask, Response, render_template, request
from flask import jsonify
from flask import json
from collect_jobs import get_job_from_empoyment
from flask_cache import Cache
from werkzeug.contrib.cache import SimpleCache


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cache = SimpleCache()


def get_jobs_from_cache():
    jobs = cache.get('jobs')
    if jobs is None:
        jobs = get_job_from_empoyment()
        cache.set('jobs', jobs, timeout=86400)
    return jobs 


@app.route('/', methods=['GET'])
def get_api():
    jobs = get_jobs_from_cache()
    return Response(json.dumps(jobs,indent=4),
                    content_type='application/json; charset=utf-8')





   

if __name__ == "__main__":
    app.run(debug=True)