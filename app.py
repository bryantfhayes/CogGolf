import coggolf, os, copy
from flask import Flask, request, redirect, url_for, render_template, Response, send_from_directory, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
cg = coggolf.CogGolf()

def _view_scores(request):
    # Get a copy of the submission data for displaying
    challenge = request.form["challenge"]
    submissions = copy.deepcopy(cg.get_submissions_for_challenge(challenge))
    submissions = sorted(submissions, key=lambda d: int(d["count"]))
    
    # Determine HIGH SCORE and hide all that match it
    if len(submissions) > 0:
        topscore = int(submissions[0]["count"])
        for sub in submissions:
            if sub["count"] <= topscore:
                sub["src_file"] = "HIDDEN"

    return challenge, submissions

def _upload(request):
    if 'file' not in request.files or request.files['file'].filename == "":
        return "MISSING FILE", 400

    if "challenge" not in request.form or request.form["challenge"] == "":
        return "MISSING CHALLENGE", 400

    if 'name' not in request.form or request.form['name'] == "":
        return "MISSING NAME", 400

    file = request.files['file']
    name = request.form['name']
    challenge = request.form['challenge']

    # If tmp doesnt exist, make it
    if not os.path.isdir("tmp"):
        os.mkdir("tmp")

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join("tmp", filename))
        submission = cg.new_submission(name, os.path.join("tmp", filename), challenge)
        return jsonify(submission.getData()), 200

    return "UNKNOWN ERROR", 400

@app.route('/viewscores', methods=['POST'])
def view_scores():
    ''' Redirect to view_scores page for non-api users '''
    if "challenge" not in request.form or request.form["challenge"] == "":
        return "MISSING CHALLENGE", 400

    challenge, submissions = _view_scores(request)
    print(submissions)
    return Response(render_template('viewscores.html', submissions=submissions, challenge=challenge, mimetype='text/html'))

@app.route('/api/viewscores', methods=['POST'])
def api_view_scores():
    ''' Get scores and return JSON object for API calls '''
    if "challenge" not in request.form or request.form["challenge"] == "":
        return "MISSING CHALLENGE", 400

    challenge, submissions = _view_scores(request)
    return jsonify(submissions)

@app.route('/api/upload', methods=['POST'])
def api_upload_file():
    return _upload(request)

@app.route('/upload', methods=['POST'])
def upload_file():
    return _upload(request)

@app.route('/viewsource', methods=['POST'])
def view_source():
    if request.form['path'] == "HIDDEN":
        return "UNAUTHORIZED", 400
    return send_from_directory(os.path.dirname(request.form['path']), os.path.basename(request.form["path"]))

#
# Show main home page, where users can access submission forms 
#
@app.route('/', methods=['GET'])
def index():
    return Response(render_template('index.html', challenges=cg.challenges.keys(), mimetype='text/html'))

def main():
    cg = coggolf.CogGolf()
    cg.new_submission("LocalTest", "submit.c", coggolf.HELLO_WORLD_CHALLENGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0")